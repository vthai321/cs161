import re
class Land(object):
    def dfs(self, listar, i):
        # input is the matrix and the index of the starting vertex
        # implementation of dfs for purposes of island exploration
        # will mark visited tiles with 2
        n = listar[0]
        # dfs lands on a tile that isn't land or invalid
        if(i < 1 or i > n**2 or listar[i] != 1):
            return
        
        listar[i] = 2
        
        if (i+1) % n != 1:
            self.dfs(listar, i+1)
        
        if (i-1) % n != 0:
            self.dfs(listar, i-1)
        
        self.dfs(listar, i+n)
        self.dfs(listar, i-n)
 
    def eval(self, listone):
        tokensone = listone.split()
        listar = list(map(int, tokensone))
        # listar[0] has the row/column size n of the matrix,
        # listar[1], listar[2], ... denote the binary value of
        # each entry of the matrix. listar[j+(i-1)*n] denotes (i,j) entry
        # your code here, value is the answer

        # iterate through every tile
        # if a tile is unvisited and is land, call dfs on it
        # when dfs concludes, the entire island has been visited (increment island count by 1)
        value = 0
        n = listar[0]
        for i in range(1, (n**2)+1): # from 1 to n^2 inclusive
            if listar[i] == 1:
                self.dfs(listar, i)
                value += 1
        return value

if __name__ == '__main__':
    calc = Land()
    calc.eval()

