FILENAME = "input.txt"
import re
from functools import reduce 
import operator

lines = open(FILENAME, "r").read().strip().splitlines() 



def prod(it) : 
    return reduce(operator.mul, it, 1)

def part1() : 
    operators = re.split('\s+', lines[-1])
    operands = lines[:-1]


    num_problems = len(operators)

    total = 0
    nums = [[int(num) for num in re.split('\s+', line.strip())] for line in operands]
    new_nums = [[nums[j][i] for j in range(len(nums))] for i in range(len(nums[0]))]
    
    for i in range(num_problems) :
        temp = sum(new_nums[i]) if operators[i] == "+" else prod(new_nums[i])
        total += temp

    return total

def part2() : 
    g = [l.rstrip("\n") for l in lines]; w = max(map(len, g), default=0); g = [l.ljust(w) for l in g]
    d, op = g[:-1], g[-1]; operators = op.split()
    blocks, s = [], None
    for c in range(w):
        if all(r[c] == " " for r in g):
            if s is not None: blocks.append((s, c)); s = None
        elif s is None: s = c
    if s is not None: blocks.append((s, w))
    cols = [[x for x in ("".join(r[c] for r in d if r[c].isdigit()) for c in range(a, b)) if x][::-1] for a, b in blocks]
    return sum((prod(map(int, col)) if operators[i] == "*" else sum(map(int, col))) for i, col in enumerate(cols))






if __name__ == "__main__" : 
    print("Solution to part 1 is: " + str(part1()))
    print("Solution to part 2 is: " + str(part2()))