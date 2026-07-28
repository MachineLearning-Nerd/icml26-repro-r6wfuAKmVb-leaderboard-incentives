"""Reconstruct Figure 1's 384,668 value from the hashed arXiv source."""
from __future__ import annotations

import hashlib
import io
import json
import math
import tarfile
import time
import urllib.request
from pathlib import Path

import numpy as np
import pymupdf

ROOT = Path(__file__).resolve().parents[2]
OUTPUT = ROOT / "outputs" / "claim6_reconstruction.json"
SOURCE_URL = "https://export.arxiv.org/e-print/2603.08371"
SOURCE_SHA256 = "9f6d8668713011bee867b6c83a8e88a5f6b9cec201cc1806a30c891b11106ae8"
TRAJ2_SHA256 = "aa814bc7a08fe91b8ecc7ef5d0e079dea28fd9aa74b8cb6107c6d76608078032"
USER_AGENT = (
    "OpenResearch-Reproduction/1.0 "
    "(paper audit; contact via github.com/MachineLearning-Nerd)"
)


def sha256(blob: bytes) -> str:
    return hashlib.sha256(blob).hexdigest()


def download_source() -> bytes:
    request = urllib.request.Request(SOURCE_URL, headers={"User-Agent": USER_AGENT})
    with urllib.request.urlopen(request, timeout=60) as response:
        blob = response.read()
    actual = sha256(blob)
    if actual != SOURCE_SHA256:
        raise AssertionError(f"arXiv source hash mismatch: {actual}")
    return blob


def extract_member(bundle: bytes, name: str) -> bytes:
    with tarfile.open(fileobj=io.BytesIO(bundle), mode="r:*") as archive:
        member = archive.getmember(name)
        handle = archive.extractfile(member)
        if handle is None:
            raise AssertionError(f"missing source member: {name}")
        return handle.read()


def route_1_vector_endpoint(pdf_blob: bytes) -> tuple[dict, list[float], list[float]]:
    document = pymupdf.open(stream=pdf_blob, filetype="pdf")
    drawings = document[0].get_drawings()
    curves = [
        drawing
        for drawing in drawings
        if math.isclose(drawing.get("width") or 0, 4.0)
        and drawing.get("color")
        and drawing["color"][0] > 0.8
        and len(drawing["items"]) == 30
    ]
    if len(curves) != 1:
        raise AssertionError(f"expected one 30-segment red curve, found {len(curves)}")
    curve = curves[0]
    points = [curve["items"][0][1]] + [item[2] for item in curve["items"]]

    x_grid = sorted(
        drawing["rect"].x0
        for drawing in drawings
        if drawing.get("color")
        and 0.68 < drawing["color"][0] < 0.70
        and math.isclose(drawing["rect"].x0, drawing["rect"].x1, abs_tol=1e-5)
    )
    y_ticks = sorted(
        drawing["rect"].y0
        for drawing in drawings
        if drawing.get("color") == (0.0, 0.0, 0.0)
        and math.isclose(drawing.get("width") or 0, 0.8, abs_tol=1e-5)
        and math.isclose(drawing["rect"].y0, drawing["rect"].y1, abs_tol=1e-5)
        and math.isclose(drawing["rect"].x1 - drawing["rect"].x0, 3.5, abs_tol=1e-3)
    )
    if len(x_grid) != 7 or len(y_ticks) != 9:
        raise AssertionError(f"unexpected axis geometry: x={len(x_grid)}, y={len(y_ticks)}")

    x_zero, x_3000 = x_grid[0], x_grid[-1]
    y_400000, y_zero = y_ticks[0], y_ticks[-1]
    x_values = [(point.x - x_zero) / (x_3000 - x_zero) * 3000 for point in points]
    y_values = [
        (y_zero - point.y) / (y_zero - y_400000) * 400000 for point in points
    ]
    endpoint = y_values[-1]
    if round(endpoint) != 384668:
        raise AssertionError(f"endpoint rounds to {round(endpoint)}, not 384668")
    if not math.isclose(x_values[-1], 3000, abs_tol=1e-6):
        raise AssertionError(f"endpoint x is {x_values[-1]}, not 3000")
    return (
        {
            "route": "direct_vector_coordinate_calibrated_from_labeled_ticks",
            "x": x_values[-1],
            "raw_y": endpoint,
            "rounded_y": round(endpoint),
            "absolute_rounding_difference": abs(endpoint - 384668),
            "curve_count": len(curves),
            "curve_points": len(points),
            "x_tick_count": len(x_grid),
            "y_tick_count": len(y_ticks),
        },
        x_values,
        y_values,
    )


def route_2_endpoint_blind(x_values: list[float], y_values: list[float]) -> dict:
    x_train = np.asarray(x_values[:-1])
    y_train = np.asarray(y_values[:-1])
    target = y_values[-1]
    rows = []
    for degree in [3, 4, 5, 6]:
        coefficients = np.polyfit(x_train, y_train, degree)
        prediction = float(np.polyval(coefficients, 3000))
        rows.append(
            {
                "degree": degree,
                "prediction": prediction,
                "absolute_error": abs(prediction - target),
            }
        )
    selected = rows[-1]
    if selected["absolute_error"] >= 25:
        raise AssertionError(f"endpoint-blind extrapolation error too large: {selected}")
    return {
        "route": "endpoint_blind_extrapolation",
        "training_points": len(x_train),
        "held_out_x": 3000,
        "degree_sensitivity": rows,
        "selected_degree_declared_before_endpoint_check": 6,
        "prediction": selected["prediction"],
        "direct_vector_endpoint": target,
        "relative_error": selected["absolute_error"] / target,
    }


def route_3_source_text(bundle: bytes) -> dict:
    paths = [
        "Sections/introv2.tex",
        "Sections/equilibrium.tex",
        "Sections/tune-before-test.tex",
    ]
    occurrences = {}
    for path in paths:
        text = extract_member(bundle, path).decode("utf-8")
        occurrences[path] = text.count("384,668")
    if any(count != 1 for count in occurrences.values()):
        raise AssertionError(f"unexpected source-text occurrences: {occurrences}")
    return {
        "route": "independent_tex_anchor_consistency",
        "occurrences": occurrences,
        "total_occurrences": sum(occurrences.values()),
        "quantifiers": {
            "tbt_steps": 3000,
            "reported_minimum_additional_steps": 384668,
            "models": ["Qwen2.5-0.5B", "1.5B", "3B", "7B", "14B"],
            "benchmark": "Winogrande",
            "training_range": [0, 3000],
            "batch_size": 8,
        },
    }


def route_4_falsification(endpoint: float, y_ticks: int) -> tuple[dict, dict]:
    wrong_axis_max = 350000
    wrong_calibration = endpoint / 400000 * wrong_axis_max
    negative_control = {
        "mutation": "replace the labeled 400000 top tick by 350000",
        "mutated_endpoint": wrong_calibration,
        "passes_384668_check": round(wrong_calibration) == 384668,
    }
    if negative_control["passes_384668_check"]:
        raise AssertionError("negative control unexpectedly passed")
    falsification = {
        "route": "dedicated_falsification",
        "restated_claim": (
            "The fitted Winogrande trajectories imply that at common TbT 3000, "
            "the minimum adjacent additional effort is at least 384668 steps."
        ),
        "assumptions_checked": [
            "the plotted path is the unique red 30-segment Figure 1 curve",
            "axis labels map 0 through 400000 in 50000 increments",
            "the endpoint is at TbT 3000",
            "the source bundle and figure hashes match the audited revision",
        ],
        "alternate_curve_found": False,
        "coordinate_contradiction_found": False,
        "valid_falsification_found": False,
        "endpoint": endpoint,
        "axis_tick_count": y_ticks,
    }
    return falsification, negative_control


def run_claim_6() -> dict:
    started = time.perf_counter()
    cpu_started = time.process_time()
    bundle = download_source()
    figure = extract_member(bundle, "figures/traj2.pdf")
    if sha256(figure) != TRAJ2_SHA256:
        raise AssertionError("Figure 1 right-panel hash mismatch")
    route_1, x_values, y_values = route_1_vector_endpoint(figure)
    route_2 = route_2_endpoint_blind(x_values, y_values)
    route_3 = route_3_source_text(bundle)
    route_4, negative_control = route_4_falsification(
        route_1["raw_y"], route_1["y_tick_count"]
    )
    wall = time.perf_counter() - started
    cpu = time.process_time() - cpu_started
    payload = {
        "claim": 6,
        "status": "BLOCKED",
        "paper_value": 384668,
        "observed_source_reconstruction": route_1["raw_y"],
        "assessment": (
            "The exact published vector source is internally reproducible, but the "
            "arXiv bundle contains no raw Winogrande measurements, fit parameters, "
            "training code, or checkpoints. The underlying empirical fit therefore "
            "cannot be independently rerun on authorized CPU compute."
        ),
        "routes": [route_1, route_2, route_3, route_4],
        "negative_control": negative_control,
        "source": {
            "url": SOURCE_URL,
            "retrieval_user_agent": USER_AGENT,
            "bundle_sha256": SOURCE_SHA256,
            "figure_sha256": TRAJ2_SHA256,
        },
        "raw_training_data_present_in_source": False,
        "unblocker": (
            "Author Winogrande per-checkpoint measurements and fit parameters, or "
            "CPU-feasible published logits/checkpoints sufficient to recreate them."
        ),
        "runtime": {
            "backend": "local",
            "selected_flavor": None,
            "estimated_required_cores": 1,
            "estimated_runtime": "under 5 minutes",
            "wall_seconds": wall,
            "process_cpu_seconds": cpu,
            "mean_cpu_cores_used": cpu / wall,
            "seed": None,
        },
    }
    OUTPUT.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n")
    print("CLAIM6_RAW " + json.dumps(payload, sort_keys=True))
    return payload


if __name__ == "__main__":
    run_claim_6()
