ranges_string, ids = open("input.txt" , "r").read().strip().split("\n\n")




def solve() : 
    ranges = ranges_string.split("\n")
    parsed = [list(map(int, x.split("-"))) for x in ranges]
    parsed.sort(key = lambda x: x[0])

    result = []
    c2 = 0
    curr_start = parsed[0][0]
    curr_end = parsed[0][1]
    for [start,end] in parsed[1:]: 

        if start > curr_end :
            result.append([curr_start, curr_end])
            c2 += curr_end - curr_start + 1
            curr_start = start 
            curr_end = end
        else: 
            curr_end = max(curr_end, end)

    result.append([curr_start, curr_end])
    c2 += curr_end - curr_start + 1

    print(result)

    parsed_ids = list(map(int, ids.split("\n")))
    n = len(result)

    total = 0 


    for id in parsed_ids :
        left = 0
        right = n-1 
        while left <= right : 
            middle = (left + right) // 2 

            if result[middle][0] <= id <= result[middle][1] :
                total += 1
                break
            elif id < result[middle][0] :
                right = middle - 1 
            else : 
                left = middle + 1




    return total, c2

    






if __name__ == "__main__" : 
    c1, c2 = solve() 
    print("Result to part1: " + str(c1)) 
    print("Result to part2: " + str(c2))