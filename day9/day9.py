FILENAME = "input.txt"


lines = open(FILENAME, "r").read().splitlines()



def solve() : 
    coordinates = [
        tuple(map(int, line.strip().split(",")))
        for line in lines
    ]

    max_area = 0


    for i in range(len(coordinates)-1) : 
        for j in range(i+1, len(coordinates)) :

            curr = abs(coordinates[i][0] - coordinates[j][0] + 1) * abs(coordinates[i][1] - coordinates[j][1] + 1)
            max_area = max(max_area, curr)

    return max_area


if __name__ == "__main__" : 
    p1 = solve() 
    #p2 = part2() 
    print("Result to part1 is: " + str(p1))
    #print("Result to part2 is: " + str(p2))
