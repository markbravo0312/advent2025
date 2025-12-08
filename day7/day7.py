FILENAME = "input.txt" 
from collections import defaultdict

input_str = open(FILENAME, "r").read().strip().splitlines() 
COLS = len(input_str[0])
ROWS = len(input_str)

grid = [[input_str[r][c] for c in range(COLS)] for r in range(ROWS)]
sr = 0
sc = 0
for i, char in enumerate(grid[0]) :
    if char == "S": 
        sc = i 

def solve() : 
    curr_row = sr + 1
    cols = set([sc]) 
    total = 0
    p2 = {sc:1} 
    while curr_row < ROWS : 
        next_cols = set()
        next_p2 = defaultdict(int)
        for x in cols : 
            if grid[curr_row][x] == "^" :
                if x-1 >= 0 : 
                    next_cols.add(x-1)
                    next_p2[x-1] += p2[x]
                if x+1 < COLS : 
                    next_cols.add(x+1)
                    next_p2[x+1] += p2[x]
                total += 1
            else: 
                next_cols.add(x)
                next_p2[x] += p2[x]
        cols = next_cols
        #print(next_p2)
        p2 = next_p2
        curr_row += 1 

    return total, sum(next_p2.values())

if __name__ == "__main__" : 
    p1,p2 = solve() 
    print("Result to part1 is: " + str(p1) )
    print("Result to part2 is: " + str(p2 ))