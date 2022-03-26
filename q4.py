from sys import stdin


class Solution:
    def __init__(self):
        self.di = 0
        self.dj = 0
        self.sj = 0
        self.si = 0
        self.m = []

    def readMaze(self):
        """Creates the maze self.m which is a list of 10 strings;
           computes the row index self.si and column index self.sj of the source S
           and the row index self.di and column index self.dj of the destination D"""
        # Write your code here
        for line in stdin:
            self.m.append(line)

        for i in range(len(self.m)):
            for pos, char in enumerate(self.m[i]):
                # Find S position
                if char == 'S':
                    self.si = i
                    self.sj = pos
                # Find D position
                if char == 'D':
                    self.di = i
                    self.dj = pos

    def printMaze(self):
        """Prints the maze self.m"""
        for i in range(10):
            print(self.m[i], end="")
        print("\n")

    def neighbors(self, i, j):
        """Returns the list of self.m[i][j]'s neighbors index (ni, nj) where self.m[ni][nj] is a path"""
        result = []
        # Write your code here
        try:
            # get path in i
            for loop in range(i - 1, i + 2, 2):
                if self.m[loop][j] == '.' or self.m[loop][j] == 'D' and loop != -1:
                    result.append((loop, j))
        except:
            pass

        try:
            # get path in j
            for loop in range(j - 1, j + 2, 2):
                if self.m[i][loop] == '.' or self.m[i][loop] == 'D':
                    result.append((i, loop))
        except:
            pass
        return result

    def bfs(self):
        """Returns the shortest path distance from S to D using breadth-first search"""
        dist = [[None for i in range(10)] for j in range(10)]

        queue = [(self.si, self.sj)]
        dist[self.si][self.sj] = 0
        while queue:
            # Write your code here
            u = queue.pop(0)
            ni, nj = u[0], u[1]
            neighbor = self.neighbors(ni, nj)
            for i in range(len(neighbor)):
                if dist[neighbor[i][0]][neighbor[i][1]] is None:
                    dist[neighbor[i][0]][neighbor[i][1]] = dist[ni][nj] + 1
                    if neighbor[i][0] == self.di and neighbor[i][1] == self.dj:
                        return dist[neighbor[i][0]][neighbor[i][1]]
                    queue.append(neighbor[i])
        return -1


if __name__ == '__main__':
    sol = Solution()
    sol.readMaze()
    sol.printMaze()
    # print(f"The position of S is {sol.si}, {sol.sj}.")
    # print(f"The position of D is {sol.di}, {sol.dj}.")
    # print(f"Neighbors of position 1, 4 is {sol.neighbors(0, 0)}")
    print(f"The shortest path distance is {sol.bfs()}.")
