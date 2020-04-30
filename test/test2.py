import ast
from utils import Colors, fn_timer
# from memory_profiler import profile


@fn_timer
# @profile
def solution(N, version='s1'):
    # write your code in Python 3.6
    def s1(num):
        # Time complexity O(n)
        return str(num).count('1')

    def s2(num):
        # Time complexity O(n)
        count = 0
        while num // 10:
            if num % 10 == 1:
                count += 1
            num //= 10
        return count + 1 if num == 1 else count

    if N < 0 or not isinstance(N, int):
        raise ValueError

    v = 11 ** N
    print("N: {}, 11**N: {}".format(N, v))

    return s1(v) if version == 's1' else s2(v)


if __name__ == "__main__":
    with open("data2.txt", 'r') as f:
        for line in f:
            case = (ast.literal_eval(line))
            print("*"*60)
            print(Colors.HEADER + "Test case: ", case, Colors.ENDC)
            # print(Colors.OKBLUE + "V1 Result: ", solution(case, version='v1'), Colors.ENDC)
            print(Colors.OKBLUE + "V2 Result: ", solution(case, version='v2'), Colors.ENDC)
