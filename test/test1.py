import ast
from utils import Colors, fn_timer
# from memory_profiler import profile


@fn_timer
# @profile
def solution(A, K):
    n = len(A)
    # if A is empty or K is negative, return False
    if n == 0 or K < 0:
        return False

    # Check whether it matches the pattern 
    for i in range(n - 1):
        # if (A[i] + 1 < A[i + 1]):
        if A[i] != A[i + 1] and A[i] + 1 != A[i + 1]:
            return False
    # if (A[0] != 1 and A[n - 1] != K): # the first should be 1 and the last should be K
    # if A[0] != 1 or A[n - 1] != K:
    #     return False
    # else:
    #     return True
    return A[0] == 1 and A[n - 1] == K


if __name__ == "__main__":
    with open("data1.txt", 'r') as f:

        for line in f:
            case = (ast.literal_eval(line))
            print("*"*60)
            print(Colors.HEADER + "Test case: ", case, Colors.ENDC)
            print("A: ", case[0], " K: ", case[1])
            print(Colors.OKBLUE + "Result: ", solution(case[0], case[1]), Colors.ENDC)
