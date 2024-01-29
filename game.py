import random

def start():
    mat = [[0]*4 for i in range(4)]
    print("Commands are as follows : ")
    print("'W' or 'w' : Move Up")
    print("'S' or 's' : Move Down")
    print("'A' or 'a' : Move Left")
    print("'D' or 'd' : Move Right")
    add_new_two(mat)
    return mat

def add_new_two(mat):
    r = random.randint(0,3)
    c = random.randint(0,3)
    while mat[r][c] != 0:
        r = random.randint(0, 3)
        c = random.randint(0, 3)
    mat[r][c] = 2

def get_curent_state(mat):
    for i in range(4):
        for j in range(4):
            if(mat[i][j] == 2048):
                return "WON"
    for i in range(4):
        for j in range(4):
            if (mat[i][j] == 0):
                return "GAME NOT OVER"
    for i in range(3):
        for j in range(3):
            if mat[i][j] ==mat[i][j+1] or  mat[i][j] ==mat[i+1][j]:
                return "GAME NOT OVER"
    for i in range(3):
        if mat[i][3] == mat[i+1][3]:
            return "GAME NOT OVER"
    for j in range(3):
        if mat[3][j] == mat[3][j+1]:
            return "GAME NOT OVER"
    return 'Lost'

# def merge(mat):
#     for i in range(4):
#         for j in range(3):
#             if mat[i][j] == mat[i][j+1] and mat[i][j]!=0:
#                 mat[i][j] *=2
#                 mat[i][j+1] = 0
#     return mat

def move_left(mat):
    new_mat = [[0]*4 for i in range(4)]
    for i in range(4):
        pos = 0
        for j in range(4):
            if mat[i][j]!=0:
                if new_mat[i][pos] == 0:
                    new_mat[i][pos] = mat[i][j]
                elif new_mat[i][pos] == mat[i][j]:
                    new_mat[i][pos] *= 2
                    pos += 1
                else:
                    pos+=1
                    new_mat[i][pos] = mat[i][j]

    return new_mat

def transpose(mat):
    return [list(row) for row in zip(*mat)]

def display(mat):
    for row in mat:
        print('  '.join(str(cell) for cell in row))





