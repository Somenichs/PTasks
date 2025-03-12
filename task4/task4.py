import math
import sys

if len(sys.argv) != 2:
    print("Необходимо указать 1 аргумент коммандной строки\nВ качестве аргумента принимается путь к файлу"
          "\nExample: python task4.py path_to_file")
    exit(1)

with open(sys.argv[1], 'r') as numsFile:
    nums = list(map(int, numsFile.readlines()))
nums.sort()


def is_odd(number):
    return number % 2 == 0


def get_median(array):
    length = len(array)
    if is_odd(length):
        return (array[length // 2 - 1] + array[length // 2]) / 2
    else:
        return array[math.floor(length // 2)]


def min_steps(array):
    median = get_median(array)
    steps = 0
    for number in nums:
        steps += math.fabs(number - median)
    return int(steps)


print(min_steps(nums))
