import re
import ast
from functools import cache
from collections import deque

FILENAME = "input.txt" 

lines = open(FILENAME, "r").read().strip().splitlines() 

configs = [] 
buttons = [] 
joltage = []

for line in lines : 
    curr = re.split(r"\s+", line)
    configs.append([])
    buttons.append([])
    for i, c in enumerate(curr[0]) :
            match c : 
                case "[" :
                    continue 
                case "." : 
                    configs[-1].append(False) 
                
                case "#" : 
                    configs[-1].append(True)

                case "]": 
                    break

                case _ : 
                    print("unexpected char")
    
    for tup in curr[1:-1] :
        val = ast.literal_eval(tup)
        if isinstance(val, int) :
            buttons[-1].append([val]) 
        else: 
            buttons[-1].append(list(val))

    joltage.append(list(map(int, curr[-1].strip("{}").split(","))))



def part1() : 
    total = 0
    for config, bts in zip(configs, buttons) : 

        target = 0 

        for i, on in enumerate(config) : 
            if on: 
                target |= (1 << i )

        button_masks = [] 

        for b in bts : 
            m = 0

            for idx in b : 
                m |= (1 << idx) 
            button_masks.append(m) 

        B = len(button_masks) 
        best = float('inf') 

        for mask in range(1 << B) : 
            state = 0

            for j in range(B) : 
                if mask & (1 << j) : 
                    state ^= button_masks[j] 

            if state == target : 
                presses = mask.bit_count() 
                best = min(presses,  best)
        
        #print("adding " + str(best))

        total += best

    return total


def part2() : 
    total = 0

    deltas = []
    for j,bts in zip(joltage, buttons) :
        case_deltas = []
        for b in bts : 
            delta = [0] * len(j)
            for idx in b: 
                delta[idx] = 1 

            case_deltas.append(delta) 
            
        case_deltas.sort(key=len, reverse=True)
        deltas.append(case_deltas) 



    ba = [tuple(delta) for delta in deltas]

            

    for j, cd in zip(joltage, deltas): 
        
        start = tuple(0 for _ in range(len(j)))
        target = tuple(j)
        visited = set([start]) 

        q = deque()
        q.append((0, start))
        best = 0

        while q : 
            count, curr = q.popleft()

            if curr == target :
                best = count 
                break
            
            visited.add(curr)

            for delta in cd: 
                curr_as_list = list(curr)
                overshoot = False

                
                for idx in range(len(j)):
                    if delta[idx]:
                        v = curr_as_list[idx] + 1
                        if v > j[idx]:
                            overshoot = True
                            break
                        curr_as_list[idx] = v

                if overshoot:
                    continue

                nxt = tuple(curr_as_list)
                if nxt not in visited:
                    q.append((count + 1, nxt))
                    

        total += best 


    return total


    
                
            

if __name__ == "__main__" : 
    print("Solution to part1 is: " + str(part1()))
    print("Solution to part2 is: " + str(part2()))