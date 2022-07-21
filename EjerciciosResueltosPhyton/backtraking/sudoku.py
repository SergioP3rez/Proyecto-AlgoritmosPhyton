def find_empty(mat):
    for i in range(len(mat)):
        for j in range(len(mat[0])):
            if mat[i][j] == 0:
                return (i, j)
    return None

def solve(mat):
    find = find_empty(mat)
    if not find:
        return True
    else:
        row,col = find
    for i in range (1,10):
        if valid (mat, i, (row,col)):
            mat[row][col] = i
            if solve(mat):
                return True
            mat[row][col] = 0
    return False

def valid(mat, num, pos):
     #Comprobación fila
     for i in range(len(mat[0])):
         if mat[pos[0]][i] == num and pos[1] != i:
             return False

    #Comprobación columna
     for i in range(len(mat)):
         if mat[i][pos[1]] == num and pos[0] != i:
             return False

    #Comprobación submatriz
     boxX = pos[1] // 3
     boxY = pos[0] // 3

     for i in range(boxY * 3, boxY * 3 + 3):
         for j in range (boxX * 3, boxX * 3 + 3):
             if mat[i][j] == num and (i,j) != pos:
                 return False
     return True

def print_board(mat):
    for i in range(len(mat)):
        for j in range(len(mat[0])):
            if j == 8:
                print(mat[i][j])
            else:
                print(str(mat[i][j]) + " ", end="")

mat = []
for i in range(9):
    row = list(map(int, input().strip().split()))
    mat.append(row)

solve(mat)
print_board(mat)