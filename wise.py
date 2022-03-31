def maxpathSum(board,p,q):
    if p == 0:
        return board[p][q]
    elif p == len(board)-1:
        return board[p][q]
    elif q == 0:
        return board[p][q]
    elif q == len(board[0])-1:
        return board[p][q]
    else:
        return board[p][q] + max(maxpathSum(board,p-1,q),maxpathSum(board,p,q-1))

print(maxpathSum([[1,2,3],[4,5,6],[7,8,9]],1,1))