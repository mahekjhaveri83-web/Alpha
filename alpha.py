import math


def alphabeta(depth, index, isMax, myarray, max_depth, alpha, beta):

    if depth == max_depth:
        return myarray[index]

    if isMax:
        best = -math.inf

        for i in range(2):
            best = max(
                best,
                alphabeta(
                    depth + 1,
                    index * 2 + i,
                    False,
                    myarray,
                    max_depth,
                    alpha,
                    beta
                )
            )

            alpha = max(alpha, best)

            if beta <= alpha:
                print(f"Pruning at depth {depth + 1}, index of max is {index}")
                break

        return best

    else:
        best = math.inf

        for i in range(2):
            best = min(
                best,
                alphabeta(
                    depth + 1,
                    index * 2 + i,
                    True,
                    myarray,
                    max_depth,
                    alpha,
                    beta
                )
            )

            beta = min(beta, best)

            if beta <= alpha:
                print(f"Pruning at depth {depth + 1}, index of min is {index}")
                break

        return best


myarray = [3, 5, 6, 9, 1, 2, 0, -1]
max_depth = int(math.log2(len(myarray)))

alpha = -math.inf
beta = math.inf

result = alphabeta(0, 0, True, myarray, max_depth, alpha, beta)

print("Optimal value:", result)
