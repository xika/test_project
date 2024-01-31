# try add commit pull
import game

if __name__ == '__main__':
    mat = game.start()
    game.display(mat)
    while True:
        x = input("Press the command : ")
        if x == 'A' or x == 'a':
            mat = game.move_left(mat)
            state = game.get_curent_state(mat)
            print(state)
            if (state == 'GAME NOT OVER'):
                game.add_new_two(mat)
            else:
                break

        elif x == 'D' or x == 'd':
            rev_mat = [row[::-1] for row in mat]
            rev_mat = game.move_left(rev_mat)
            mat = [row[::-1] for row in rev_mat]
            state = game.get_curent_state(mat)
            print(state)
            if (state == 'GAME NOT OVER'):
                game.add_new_two(mat)
            else:
                break
        elif x == 'W' or x == 'w':
            transpose_mat = game.transpose(mat)
            transpose_mat = game.move_left(transpose_mat)
            mat = game.transpose(transpose_mat)
            state = game.get_curent_state(mat)
            print(state)
            if (state == 'GAME NOT OVER'):
                game.add_new_two(mat)
            else:
                break

        elif x == 'S' or x == 's':
            transpose_mat = game.transpose(mat)
            transpose_rev_mat = [row[::-1] for row in transpose_mat]
            transpose_rev_mat = game.move_left(transpose_rev_mat)
            transpose_mat = [row[::-1] for row in transpose_rev_mat]
            mat = game.transpose(transpose_mat)
            state = game.get_curent_state(mat)
            print(state)
            if (state == 'GAME NOT OVER'):
                game.add_new_two(mat)
            else:
                break
        else:
            print("Invalid Key Pressed")

        game.display(mat)


