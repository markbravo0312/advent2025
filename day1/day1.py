FILENAME = "input.txt"

input = open(FILENAME, "r").read().splitlines()

def solution() : 
    curr = 50 
    count = 0
    c2 = 0
    for s in input : 
        dir = -1 if s[0] == "L" else 1

        total = dir * int(s[1:]) 

        # full spins
        spins = abs(total) // 100
        extra = abs(total) - (spins * 100)

        #print("at: " + str(curr) + " total is " + str(total) + "with spin factor " + str(spins) )
        if dir == 1 : 
            if curr + extra > 100 and curr != 0 :
                c2 += 1
                print("incrementing c2" )
        else : 
            if curr - extra < 0 and curr != 0:
                c2 += 1
                print("incrementing c2" )
        c2 += spins
        
        

        curr = ((curr + total) % 100 )

        if curr == 0 : 
            count += 1 

    return count, c2






if __name__ == "__main__" : 
    p1, p2 = solution() 
    print("Solution to part1: " + str(p1))
    print("Solution to part2: " + str(p2 + p1))
