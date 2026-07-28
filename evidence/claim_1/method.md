# Claim 1 method

Partition every nonnegative effort pair by the winner. For a higher-capability
winner, split on whether its effort is above the minimum winning boundary. For
a lower-capability winner, split at effort `e_high+3/2`. Each of the four
regions has an explicit strictly profitable deviation. Z3 proves the negation
of each arithmetic implication unsatisfiable.
