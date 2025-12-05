lines = open("input.txt", "r").read().splitlines()

def part1() : 
    n = len(lines)
    k = len(lines[0])

    

    total = 0
    for i, line in enumerate(lines): 
        for j, c in enumerate(line) :
            if c == "@":
                count = 0
                for di, dj in [(0,1),(1,0),(1,1),(-1,1)] :
                    for multiplier in [-1,1] :
                        if (0 <= i + di * multiplier < n 
                            and 0 <= j + dj * multiplier < k):
                            if lines[i+di*multiplier][j+dj*multiplier] == "@" :
                                count += 1 
            

                if count < 4 : 
                    total += 1


    return total 

def part2() : 
    n = len(lines)
    k = len(lines[0])

    removed = set() 

    while True: 
        changed = False
        for i, line in enumerate(lines): 
            for j, c in enumerate(line) :
                if (i,j) in removed: 
                    continue 

                if c == "@":
                    count = 0
                    for di, dj in [(0,1),(1,0),(1,1),(-1,1)] :
                        for multiplier in [-1,1] :
                            if (0 <= i + di * multiplier < n 
                                and 0 <= j + dj * multiplier < k):
                                
                                if lines[i+di*multiplier][j+dj*multiplier] == "@" :
                                    if (i+di*multiplier, j+dj*multiplier) not in removed:
                                        count += 1 
                

                    if count < 4 : 
                        changed = True
                        removed.add((i,j))

        if not changed:
            break


    return len(removed) 




if __name__ == "__main__" : 
    print("Solution to part1: " + str(part1()))
    print("Solution to part2: " + str(part2()))