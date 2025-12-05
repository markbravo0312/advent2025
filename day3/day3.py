FILENAME = "input.txt"

banks = open(FILENAME, "r").read().splitlines() 


def part1() : 
    total = 0
    for bank in banks: 
        curr = bank[0]
        curr_index = 0
        n = len(bank)
        for index, digit in enumerate(bank[1:-1]) : 
            if int(digit) > int(curr) : 
                curr = digit
                curr_index = index + 1

            if curr == "9" :
                break 
                
        second_digit = bank[n-1]
        for index in range(n-2, curr_index, -1) : 
            if int(bank[index]) > int(second_digit) : 
                
                second_digit = bank[index]
        total += int(curr + second_digit)

    return total 



def part2() : 
    total = 0



    def recFunction(n, k, lastindex, bank) :
        remaining = n - lastindex - 1
        if remaining == k : 
            return bank[lastindex+1:]
        
        if k == 0 :
            return ""
        
        else: 
            curr = bank[lastindex+1]
            curr_index = lastindex+1

            for i in range(lastindex+1, n-k+1) :
                if int(bank[i]) > int(curr) : 
                    curr = bank[i]
                    curr_index = i

            return curr + recFunction(n, k-1,curr_index, bank)
        
    for bank in banks: 
        result = recFunction(len(bank), 12, -1, bank)
        #print(result)
        total += int(result)

    return total 




if __name__ == "__main__" : 
    print("Result to part1: " + str(part1()))
    print("Result to part2: " + str(part2())) 
