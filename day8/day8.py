

import heapq


FILENAME = "input.txt"
lines = open(FILENAME, "r").read().splitlines() 
connections = 1000


class UnionFind: 
    def __init__(self, n : int) :
        self.map = [i for i in range(n)]
        self.size = [1] * n

    def get_parent(self, x :int) :
        
        if self.map[x] != x : 
            self.map[x] = self.get_parent(self.map[x])

        return self.map[x]

    def union(self, left :int, right:int) :
        left_parent, right_parent = self.get_parent(left), self.get_parent(right) 

        if left_parent == right_parent :
            return False
        
        if self.size[left_parent] < self.size[right_parent] :
            left_parent, right_parent = right_parent, left_parent

        self.map[right_parent] = left_parent
        self.size[left_parent] += self.size[right_parent]
        

        return True

        
def dist3(a, b):
    return ((a[0]-b[0])**2 +
            (a[1]-b[1])**2 +
            (a[2]-b[2])**2)

def part1() : 
    coordinates = [
        tuple(map(int, line.strip().split(","))) 
        for line in lines
    ]

    total = 0
    
    distances = []
    uf = UnionFind(len(coordinates))


    for i in range(len(coordinates)-1) :
        for j in range(i+1, len(coordinates)) :
            distance = dist3(coordinates[i],coordinates[j])
            heapq.heappush(distances, (distance, i, j))
    
    
    for i in range(connections):
        _, left, right = heapq.heappop(distances)

        uf.union(left, right) 
        

    sizes= []
    for i in range(len(coordinates)):
        uf.get_parent(i)

    for i in range(len(coordinates)) :
        if uf.map[i] == i :
            sizes.append(uf.size[i])
            

    sizes.sort(reverse=True)  
    print(sizes[0])
    print(sizes[1])
    print(sizes[2])
    return sizes[0] * sizes[1] * sizes[2]



def part2() : 
    coordinates = [
        tuple(map(int, line.strip().split(","))) 
        for line in lines
    ]

    total = 0
    
    distances = []
    uf = UnionFind(len(coordinates))


    for i in range(len(coordinates)-1) :
        for j in range(i+1, len(coordinates)) :
            distance = dist3(coordinates[i],coordinates[j])
            heapq.heappush(distances, (distance, i, j))
    
    
    while True and distances:
        _, left, right = heapq.heappop(distances)

        uf.union(left, right) 
        if uf.size[uf.get_parent(left)] == 1000 or uf.size[uf.get_parent(right)] == 1000: 
            return coordinates[left][0] * coordinates[right][0]

    


if __name__ == "__main__" :
    p1 = part1() 
    p2 = part2() 
    print("Result to part1 is: " + str(p1))
    print("Result to part2 is: " + str(p2))