# Creating a 3 x 3 matrix with all empty strings
plane=[['','',''],['','',''],['','','']]

# var turn for find which player input player 1 odd player 2 even
turn = 0

def clicked(m,n):
    global turn
    turn += 1
    print("passing")
    if (turn%2 == 1):
        plane[m][n] = 'O'
    else:
        plane[m][n] = 'X'
    for i in plane:
        if ((len(set(i)) == 1) and (i[0] != '')):
            print ('WON1')
            break
        if (((plane[0][0] == plane[1][0] != '') and (plane[1][0] == plane[2][0] != '')) or ((plane[0][1] == plane[1][1] != '') and (plane[1][1] == plane[2][1] != '')) or ((plane[0][2] == plane[1][2] != '') and (plane[1][2] == plane[2][2] != ''))):
            print('WON2')
        elif (((plane[0][0] == plane[1][1] != '') and (plane[2][2] == plane[1][1] != '')) or ((plane[0][2] == plane[1][1] != '') and (plane[1][1] == plane[2][0] != ''))):
            print('WON3')
