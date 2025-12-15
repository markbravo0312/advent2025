FILENAME = "input.txt" 
import re
from collections import defaultdict, deque
from functools import cache

lines = open(FILENAME, "r").read().splitlines()

outgoing = defaultdict(list)
indegree = defaultdict(int)

for line in lines: 
    line = line.split(":")
    key = line[0]
    values = re.split("\s+", line[1].strip())
    outgoing[key].extend(values)
    indegree[key] += len(values)


def part1() : 
    visited = {}
    start = "you" 

    q = deque(outgoing[start])

    while q : 
        curr = q.popleft() 

        if curr in visited: 
            visited[curr] += 1 
        else: 
            visited[curr] = 1


        for out in outgoing[curr] : 
            q.append(out) 

    return visited["out"]
        
def part2() : 
    start = "svr" 
    target = "out" 

    @cache
    def recSolve(node : str, reached_fft : bool, reached_dac) -> int :
        if node == target and reached_fft and reached_dac : 
            return 1 
        
        total = 0

        for out in outgoing[node] :
            total += recSolve(out, reached_fft or out == "fft", reached_dac or out == "dac") 


        return total
    
    return recSolve(start, False, False)
        

        
            

        

        
        
        
if __name__ == "__main__" : 
    print("Solution to part1 is: " + str(part1())) 
    print("Solution to part2 is: " + str(part2()))