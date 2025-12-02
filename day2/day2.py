FILENAME = "input.txt" 

input = open(FILENAME, "r").read() 




def solve() : 
    count = 0
    input_as_ranges = input.split(",")
    c2 = 0

    for interval in input_as_ranges: 
        members = interval.split("-")
        start = int(members[0])
        end = int(members[1])
        
        for i in range(start, end + 1) :
        
            
            as_str = str(i) 

            
            n = len(as_str) 

            yy = as_str + as_str 

            if as_str in yy[1:-1] :
                c2 += i

            if (n % 2 != 0) or (i < 10) : 
                continue 

            j = 0 
            while j < n//2 and as_str[j] == as_str[j + n//2] :
                j += 1

            if j == n//2 :
                #print("i is : " + as_str)
                count += i

            

      

    return count, c2



if __name__ == "__main__" : 
    p1, p2 = solve()
    print("Result to part1 is : " + str(p1))
    print("Result to part2 is : " + str(p2)) 

