
from audioop import maxpp


def smallestNegativeBalance(debts):
    res = {}
    borrower =[]
    for debt in debts:
        print(debt)
        if debt[0] in res:
            res[debt[0]] -= int(debt[2])
        else:
            res[debt[0]] = -1* int(debt[2])
        if debt[1] in res:
            res[debt[1]] += int(debt[2])
        else:
            res[debt[1]] = 1*int(debt[2])
        print(res)

    
    minV = min(res.values())
    print(minV)
    if minV >= 0:
        borrower.append('Nobody has a negative balance')
        return borrower

    def getKeysByValue(dictOfElements, valueToFind):
        listOfKeys = list()
        listOfItems = dictOfElements.items()
        for item  in listOfItems:
            if item[1] == valueToFind:
                listOfKeys.append(item[0])
        return  listOfKeys

    borrowers = getKeysByValue(res, minV)
    borrowers.sort()
    return borrowers

#print(smallestNegativeBalance( [('A', 'B', '5'), ('B', 'A', '3'), ('Cas', 'A', '7'),('Cas','A','4'),('Cas','A','2'),('D','E',13),('F','G',13)] ))

def stringToInt(s):
    return int(s)

def listToString(l):
    return ''.join(l)

def sortAlist(alist):
    alist.sort()
    return alist

def actMaxPahSum(board1,p1,q1):
    print(board1)
    def maxpathSum(board,p,q):
        if p == 0:
            #print(board[p][q])
            return board[p][q]
        elif p == len(board)-1:
            #print(board[p][q])
            return board[p][q]
        elif q == 0:
            #print(board[p][q])
            return board[p][q]
        elif q == len(board[0])-1:
            #print(board[p][q])
            return board[p][q]
        else:
            #print(board[p][q]+"in else")
            return board[p][q] + max(maxpathSum(board,p-1,q),maxpathSum(board,p,q-1))
        #return board[p][q] + max(maxpathSum(board,0,p),maxpathSum(board,len(board)-1,q))

    res = []
    res.append(maxpathSum(board1,0,p1))
    res.append(maxpathSum(board1,len(board1)-1,q1))
    print(res)
    print(maxpathSum(board1,p1,q1))
    return max(res)

def maxPathSum(board, p, q):
    res =[]
    #board1 = board.copy()
    board1 = list(map(list, board))
    def find_max_path_w_start(mat, h,q):
        res = mat[0][0]
        M = len(mat[0])
        N = len((mat))

        for i in range(N-2,-1,-1):
            for j in range(M):
                possible_values = [mat[i+1][j]]
                if j==0:
                    possible_values.append(mat[i+1][j+1])
                elif j==M-1:
                    possible_values.append(mat[i+1][j-1])
                else:
                    possible_values.append(mat[i+1][j+1])
                    possible_values.append(mat[i+1][j-1])
                mat[i][j] += max(possible_values)
        print(mat)
        print(mat[q][h])
        return mat[0][h]
    #print(find_max_path_w_start(board,0))
    #print(find_max_path_w_start(board,1)) 
    #board = [[1,2,3],[4,5,6],[7,8,9]]
    #board1 = [[1,2,3],[4,5,6],[7,8,9]]
    #print(find_max_path_w_start(board,1))
    #print(find_max_path_w_start(board1,0))
    res.append(find_max_path_w_start(board,p,q))
    #print(res)
    print(board1)
    res.append(find_max_path_w_start(board1,q,p))
    print(res)
    return max(res)
#print(actMaxPahSum([[1,2,3],[4,5,6],[7,8,9]],1,0))
#print(maxpa)
print(maxPathSum([[1,2,3],[4,5,6],[7,8,9]],1,0))
print(maxPathSum([[9,4,7],[2,1,3],[1,4,2]],2,1))


def MaximumPath(grid):
 
    # Dimensions of grid[][]
    N = len(grid)
    M = len(grid[0])
 
    # Stores maximum sum at each cell
    # sum[i][j] from cell sum[0][0]
    sum = [[0 for i in range(M + 1)]
              for i in range(N + 1)]
 
    # Iterate to compute the maximum
    # sum path in the grid
    for i in range(1, N + 1):
        for j in range(1, M + 1):
 
            # Update the maximum path sum
            sum[i][j] = (max(sum[i - 1][j],
                             sum[i][j - 1]) +
                        grid[i - 1][j - 1])
 
    # Return the maximum sum
    print(sum)
    return sum[N][M]

print(MaximumPath([[9,4,7],[2,1,3],[1,4,2]]))