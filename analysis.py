import numpy as np

import random



rand = random.Random()



class Connect_Four():

    NUM_ROW = 6

    NUM_COLUMN = 7

    NUM_WINNER = 4

    NUM_PARTICLE = 200

    NUM_ITERATION = 5

    def __init__(self):

        self.board = np.zeros((self.NUM_ROW, self.NUM_COLUMN), dtype = int)

        self.fitness = np.array([[3, 4, 5, 7, 5, 4, 3],\

                        [4, 6, 8, 10, 8, 6, 4],\

                        [5, 8, 11, 13, 11, 8, 5],\

                        [5, 8, 11, 13, 11, 8, 5],\

                        [4, 6, 8, 10, 8, 6, 4],\

                        [3, 4, 5, 7, 5, 4, 3]], dtype = int)

        self.fitness_copy = self.fitness.copy()

        self.particle = []



    def __str__(self):

        string_board = "\n\n" + str(self.board).replace("0","_").replace("-1"," O").replace("1","X")

        string_board = string_board.replace("[", " ").replace("]", " ")

        return string_board



    def moves_available(self):

        return [m for m in range(self.NUM_COLUMN) if self.board[0][m] == 0]



    def make_move(self, move):

        if np.sum(self.board) == 0:

            player = 1

        else:

            player = -1

        j = 0

        while j+1 < self.NUM_ROW and self.board[j+1][move] == 0:

            j += 1



        self.board[j][move] = player



    def decide_winner(self):

        for i in range(self.NUM_ROW-self.NUM_WINNER+1):

            for j in range(self.NUM_COLUMN-self.NUM_WINNER+1):

                subboard = self.board[i:i+self.NUM_WINNER, j:j+self.NUM_WINNER]

                if np.max(np.abs(np.sum(subboard, 0))) == self.NUM_WINNER:

                    return True

                if np.max(np.abs(np.sum(subboard, 1))) == self.NUM_WINNER:

                    return True

                elif np.abs(sum([subboard[k, k] for k in range(self.NUM_WINNER)])) == self.NUM_WINNER:

                    return True

                elif np.abs(sum([subboard[k, self.NUM_WINNER-1-k] for k in range(self.NUM_WINNER)])) == self.NUM_WINNER:

                    return True

        return False



    def generate_random_board(self, board):

        self.board = board

    

    def fitness_eval(self, board):

        board = self.board

        for row in range(0, self.NUM_ROW):

            #print("row", row)

            for col in range(0, self.NUM_COLUMN):

                #if (board[row][col] == 0 and board[row+1][col] != 0) or (board[row][col] == 0 and row+1 > 5):

                    #print("col", col)

                    # This if statement is the "How to not lose" function. It first considers the ways any of the enemy

                    # player's pieces could win. If there are a three-string of enemy pieces in any direction, then it

                    # will allocate a supreme weight to the final fourth position, so that it will play at a place where

                    # it will ensure it won't lose that way.

                    if board[row][col] == 1:

                            #print(board[row][col])

                            if row == 0 or row == 1 or row == 2:

                                if col == 0 or col == 1 or col == 2:

                                    # if statements for when row++, col++

                                    if board[row + 1][col] == 1:

                                        if board[row + 2][col] == 1:

                                            self.fitness[row + 3][col] = 5000

                                    if board[row][col + 1] == 1:

                                        if board[row][col + 2] == 1:

                                            self.fitness[row][col + 3] = 5000

                                    if board[row + 1][col + 1] == 1:

                                        if board[row + 2][col + 2] == 1:

                                            self.fitness[row + 3][col + 3] = 5000

                                if col == 3:

                                    # if statements for when row++. col++/--

                                    if board[row + 1][col] == 1:

                                        if board[row + 2][col] == 1:

                                            self.fitness[row + 3][col] = 5000

                                    if board[row][col + 1] == 1:

                                        if board[row][col + 2] == 1:

                                            self.fitness[row][col + 3] = 5000

                                    if board[row + 1][col + 1] == 1:

                                        if board[row + 2][col + 2] == 1:

                                            self.fitness[row + 3][col + 3] = 5000

                                    if board[row + 1][col - 1] == 1:

                                        if board[row + 2][col - 2] == 1:

                                            self.fitness[row + 3][col - 3] = 5000

                                    if board[row][col - 1] == 1:

                                        if board[row][col - 2] == 1:

                                            self.fitness[row][col - 3] = 5000

                                if col == 4 or col == 5 or col == 6:

                                    # if statements for when row++, col--

                                    if board[row + 1][col] == 1:

                                        if board[row + 2][col] == 1:

                                            self.fitness[row + 3][col] = 5000

                                    if board[row + 1][col - 1] == 1:

                                        if board[row + 2][col - 2] == 1:

                                            self.fitness[row + 3][col - 3] = 5000

                                    if board[row][col - 1] == 1:

                                        if board[row][col - 2] == 1:

                                            self.fitness[row][col - 3] = 5000

                            if row == 3 or row == 4 or row == 5:

                                if col == 0 or col == 1 or col == 2:

                                    # if statements for when row--, col++

                                    if board[row - 1][col + 1] == 1:

                                        if board[row - 2][col + 2] == 1:

                                            self.fitness[row - 3][col + 3] = 5000

                                    if board[row][col + 1] == 1:

                                        if board[row][col + 2] == 1:

                                            self.fitness[row][col + 3] = 5000

                                    if board[row - 1][col] == 1:

                                        if board[row - 2][col] == 1:

                                            self.fitness[row - 3][col] = 5000

                                if col == 3:

                                    # if statements for when row--. col++/--

                                    if board[row - 1][col - 1] == 1:

                                        if board[row - 2][col - 2] == 1:

                                            self.fitness[row - 3][col - 3] = 5000

                                    if board[row - 1][col + 1] == 1:

                                        if board[row - 2][col + 2] == 1:

                                            self.fitness[row - 3][col + 3] = 5000

                                    if board[row - 1][col] == 1:

                                        if board[row - 2][col] == 1:

                                            self.fitness[row - 3][col] = 5000

                                    if board[row][col - 1] == 1:

                                        if board[row][col - 2] == 1:

                                            self.fitness[row][col - 3] = 5000

                                    if board[row][col + 1] == 1:

                                        if board[row][col + 2] == 1:

                                            self.fitness[row][col + 3] = 5000

                                if col == 4 or col == 5 or col == 6:

                                    # if statements for when row--, col--

                                    if board[row - 1][col - 1] == 1:

                                        if board[row - 2][col - 2] == 1:

                                            self.fitness[row - 3][col - 3] = 5000

                                    if board[row - 1][col] == 1:

                                        if board[row - 2][col] == 1:

                                            self.fitness[row - 3][col] = 5000

                                    if board[row][col - 1] == 1:

                                        if board[row][col - 2] == 1:

                                            self.fitness[row][col - 3] = 5000

                    # Now that it ensured it won't lose (or lose one way), it will now consider how to win. It detects

                    # its own pieces and if it has any two-strings. If it does, then it will allocate a intermediate

                    # weight to putting a third consecutive piece. If that 3rd spot is already filled by its own piece,

                    # then it will put an even bigger weight behind the 4th.

                    if board[row][col] == -1:

                        if row == 0 or row == 1 or row == 2:

                            if col == 0 or col == 1 or col == 2:

                                # if statements for when row++, col++

                                if board[row + 1][col] == -1:

                                    if self.fitness[row + 2][col] < 1000:

                                        self.fitness[row + 2][col] = 1000

                                    if board[row + 2][col] == -1 and self.fitness[row + 3][col] != 5000:

                                        self.fitness[row + 3][col] = 6000

                                if board[row][col + 1] == -1:

                                    if self.fitness[row][col + 2] < 1000:

                                        self.fitness[row][col + 2] = 1000

                                    if board[row][col + 2] == -1 and self.fitness[row][col + 3] != 5000:

                                        self.fitness[row][col + 3] = 6000

                                if board[row + 1][col + 1] == -1:

                                    if self.fitness[row + 2][col + 2] < 1000:

                                        self.fitness[row + 2][col + 2] = 1000

                                    if board[row + 2][col + 2] == -1 and self.fitness[row + 3][col + 3] != 5000:

                                        self.fitness[row + 3][col + 3] = 6000

                            if col == 3:

                                # if statements for when row++. col++/--

                                if board[row + 1][col] == -1:

                                    if self.fitness[row + 2][col] < 1000:

                                        self.fitness[row + 2][col] = 1000

                                    if board[row + 2][col] == -1 and self.fitness[row + 3][col] != 5000:

                                        self.fitness[row + 3][col] = 6000

                                if board[row][col + 1] == -1:

                                    if self.fitness[row][col + 2] < 1000:

                                        self.fitness[row][col + 2] = 1000

                                    if board[row][col + 2] == -1 and self.fitness[row][col + 3] != 5000:

                                        self.fitness[row][col + 3] = 6000

                                if board[row + 1][col + 1] == -1:

                                    if self.fitness[row + 2][col + 2] < 1000:

                                        self.fitness[row + 2][col + 2] = 1000

                                    if board[row + 2][col + 2] == -1 and self.fitness[row + 3][col + 3] != 5000:

                                        self.fitness[row + 3][col + 3] = 6000

                                if board[row + 1][col - 1] == -1:

                                    if self.fitness[row + 2][col - 2] < 1000:

                                        self.fitness[row + 2][col - 2] = 1000

                                    if board[row + 2][col - 2] == -1 and self.fitness[row + 3][col - 3] != 5000:

                                        self.fitness[row + 3][col - 3] = 6000

                                if board[row][col - 1] == -1:

                                    if self.fitness[row][col - 2] < 1000:

                                        self.fitness[row][col - 2] = 1000

                                    if board[row][col - 2] == -1 and self.fitness[row][col - 3] != 5000:

                                        self.fitness[row][col - 3] = 6000

                            if col == 4 or col == 5 or col == 6:

                                # if statements for when row++, col--

                                if board[row + 1][col] == -1:

                                    if self.fitness[row + 2][col] < 1000:

                                        self.fitness[row + 2][col] = 1000

                                    if board[row + 2][col] == -1 and self.fitness[row + 3][col] != 5000:

                                        self.fitness[row + 3][col] = 6000

                                if board[row + 1][col - 1] == -1:

                                    if self.fitness[row + 2][col - 2] < 1000:

                                        self.fitness[row + 2][col - 2] = 1000

                                    if board[row + 2][col - 2] == -1 and self.fitness[row + 3][col - 3] != 5000:

                                        self.fitness[row + 3][col - 3] = 6000

                                if board[row][col - 1] == -1:

                                    if self.fitness[row][col - 2] < 1000:

                                        self.fitness[row][col - 2] = 1000

                                    if board[row][col - 2] == -1 and self.fitness[row][col - 3] != 5000:

                                        self.fitness[row][col - 3] = 6000

                        if row == 3 or row == 4 or row == 5:

                            if col == 0 or col == 1 or col == 2:

                                # if statements for when row--, col++

                                if board[row - 1][col + 1] == -1:

                                    if self.fitness[row - 2][col + 2] < 1000:

                                        self.fitness[row - 2][col + 2] = 1000

                                    if board[row - 2][col + 2] == -1 and self.fitness[row - 3][col + 3] != 5000:

                                        self.fitness[row - 3][col + 3] = 6000

                                if board[row][col + 1] == -1:

                                    if self.fitness[row][col + 2] < 1000:

                                        self.fitness[row][col + 2] = 1000

                                    if board[row][col + 2] == -1 and self.fitness[row][col + 3] != 5000:

                                        self.fitness[row][col + 3] = 6000

                                if board[row - 1][col] == -1:

                                    if self.fitness[row - 2][col] < 1000:

                                        self.fitness[row - 2][col] = 1000

                                    if board[row - 2][col] == -1 and self.fitness[row - 3][col] != 5000:

                                        self.fitness[row - 3][col] = 6000

                            if col == 3:

                                # if statements for when row--. col++/--

                                if board[row - 1][col - 1] == -1:

                                    if self.fitness[row - 2][col - 2] < 1000:

                                        self.fitness[row - 2][col - 2] = 1000

                                    if board[row - 2][col - 2] == -1 and self.fitness[row - 3][col - 3] != 5000:

                                        self.fitness[row - 3][col - 3] = 6000

                                if board[row - 1][col + 1] == -1:

                                    if self.fitness[row - 2][col + 2] < 1000:

                                        self.fitness[row - 2][col + 2] = 1000

                                    if board[row - 2][col + 2] == -1 and self.fitness[row - 3][col + 3] != 5000:

                                        self.fitness[row - 3][col + 3] = 6000

                                if board[row - 1][col] == -1:

                                    if self.fitness[row - 2][col] < 1000:

                                        self.fitness[row - 2][col] = 1000

                                    if board[row - 2][col] == -1 and self.fitness[row - 3][col] != 5000:

                                        self.fitness[row - 3][col] = 6000

                                if board[row][col - 1] == -1:

                                    if self.fitness[row][col - 2] < 1000:

                                        self.fitness[row][col - 2] = 1000

                                    if board[row][col - 2] == -1 and self.fitness[row][col - 3] != 5000:

                                        self.fitness[row][col - 3] = 6000

                                if board[row][col + 1] == -1:

                                    if self.fitness[row][col + 2] < 1000:

                                        self.fitness[row][col + 2] = 1000

                                    if board[row][col + 2] == -1 and self.fitness[row][col + 3] != 5000:

                                        self.fitness[row][col + 3] = 6000

                            if col == 4 or col == 5 or col == 6:

                                # if statements for when row--, col--

                                if board[row - 1][col - 1] == -1:

                                    if self.fitness[row - 2][col - 2] < 1000:

                                        self.fitness[row - 2][col - 2] = 1000

                                    if board[row - 2][col - 2] == -1 and self.fitness[row - 3][col - 3] != 5000:

                                        self.fitness[row - 3][col - 3] = 6000

                                if board[row - 1][col] == -1:

                                    if self.fitness[row - 2][col] < 1000:

                                        self.fitness[row - 2][col] = 1000

                                    if board[row - 2][col] == -1 and self.fitness[row - 3][col] != 5000:

                                        self.fitness[row - 3][col] = 6000

                                if board[row][col - 1] == -1:

                                    if self.fitness[row][col - 2] < 1000:

                                        self.fitness[row][col - 2] = 1000

                                    if board[row][col - 2] == -1 and self.fitness[row][col - 3] != 5000:

                                        self.fitness[row][col - 3] = 6000

        for row in range(0, self.NUM_ROW):

            # print("row", row)

            for col in range(0, self.NUM_COLUMN):

                if board[row][col] == 0:

                    if row != 5:

                        if board[row+1][col] == 0:

                            self.fitness[row][col] = self.fitness_copy[row][col]

                    if row == 5:

                        if board[row][col] == 0:

                            self.fitness[row][col] = self.fitness_copy[row][col]

                elif board[row][col] == 1 or board[row][col] == -1:

                    self.fitness[row][col] = self.fitness_copy[row][col]



        for col in range(0, self.NUM_COLUMN):

            if board[0][col] != 0:

                for row in range(0, self.NUM_ROW):

                    self.fitness[row][col] = 0



        temp_best_val = -1

        temp_best_col = 0

        for row in range(0, self.NUM_ROW):

            for col in range(0, self.NUM_COLUMN):

                if self.fitness[row][col] > temp_best_val:

                    temp_best_val = self.fitness[row][col]

                    temp_best_col = col



        print "From evaluation: best move is ", temp_best_col







        string_fitness = "\n\n" + str(self.fitness)

        string_fitness = string_fitness.replace("[", " ").replace("]", " ")

        return [string_fitness, temp_best_col]







    def PSO(self):

        c1 = 2

        c2 = 2

        r1 = rand.random()

        r2 = rand.random()

        for i in range(0, self.NUM_PARTICLE):

            coord = [rand.choice(range(0, self.NUM_ROW)), rand.choice(range(0, self.NUM_COLUMN))]

            self.particle.append([coord, int(self.fitness[coord[0]][coord[1]]), [0, 0], coord])

        global_temp_best_val = -1

        global_temp_best_cord = 0

        for row in range(0, self.NUM_ROW):

            for col in range(0, self.NUM_COLUMN):

                if self.fitness[row][col] > global_temp_best_val:

                    global_temp_best_val = self.fitness[row][col]

                    global_temp_best_cord = [row, col]





        for i in range(0, self.NUM_ITERATION):

            for p in range(0, len(self.particle)):

                if self.fitness[self.particle[p][0][0]][self.particle[p][0][1]] > self.particle[p][1]:

                    self.particle[p][1] = int(self.fitness[self.particle[p][0][0]][self.particle[p][0][1]])

                    self.particle[p][3] = [self.particle[p][0][0], self.particle[p][0][1]]

            max_fitness = 0

            gbest = []

            for p in range(0, self.NUM_PARTICLE):

                if self.particle[p][1] > max_fitness:

                    max_fitness = self.particle[p][1]

                    gbest = self.particle[p]

            for p in range(0, self.NUM_PARTICLE):

                for x in range(0, 2):

                    self.particle[p][2][x] = int(self.particle[p][2][x] + c1*r1*(self.particle[p][3][x]-self.particle[p][0][x]) \

                                             + c2*r2*(gbest[0][x] - self.particle[p][0][x]))

                    self.particle[p][0][x] = int(self.particle[p][0][x] + self.particle[p][2][x])

                if self.particle[p][0][0] > 5:

                    self.particle[p][0][0] = 5

                if self.particle[p][0][1] > 6:

                    self.particle[p][0][1] = 6

                if self.particle[p][0][0] < 0:

                    self.particle[p][0][0] = 0

                if self.particle[p][0][1] < 0:

                    self.particle[p][0][1] = 0

        print gbest

        print "\nPSO best move: ", gbest[3][1], "\n"



        return gbest[3][1]







def main():

    '''

    XO = {-1: "O", 0: "Nobody", 1: "X"}

    my_game = Connect_Four()

    moves = my_game.moves_available()

    print my_game

    player = -1

    #human_player = rand.choice([1, -1])

    human_player = -1

    while moves != []:

        if player == human_player:

            print "Available moves are: ", moves

            move = int(input("Enter move human: "))

            if move not in moves:

            	continue

        else:

            move = rand.choice(moves)

            if move not in moves:

            	continue

        my_game.make_move(move)

        print my_game

        winner = my_game.decide_winner()

        if winner:

            print XO[player], "wins!"

            break

        moves = my_game.moves_available()

        player = -player   

    '''

    board1_accurate = 0

    board2_accurate = 0

    board3_accurate = 0

    board4_accurate = 0

    board5_accurate = 0

    board6_accurate = 0

    board7_accurate = 0

    board8_accurate = 0

    board9_accurate = 0

    board10_accurate = 0

    

    for loop in range(0, 10):

        XO = {-1: "O", 0: "Nobody", 1: "X"}

        print "O is AI player, X is enemy of AI"

        my_game = Connect_Four()

        board1 = np.array([[0., 0, 0, 0, 0, 0, 0],\

                           [0, 0, 0, 0, 0, 0, 0],\

                           [0, 0, 0, 1, 0, 0, 0],\

                           [0, 1, 0, -1, 0, 0, 0],\

                           [0, 1, -1, -1, -1, 0, 0],\

                           [1, 1, 1, -1, -1, -1, 0]], dtype = int)

        my_game.generate_random_board(board1)    

        print my_game

        fitness = my_game.fitness_eval(board1)

        print fitness[0]

        best = my_game.PSO()

        print best

        if(best == fitness[1]):

            board1_accurate += 1

        

        

        my_game = Connect_Four()

        print "O is AI player, X is enemy of AI"

        board2 = np.array([[0., 0, 0, 0, 0, 0, 0],\

                           [0, 0, 0, 0, 0, 0, 0],\

                           [0, 0, 0, 0, 0, 0, 0],\

                           [0, 0, 1, -1, 0, 0, 0],\

                           [0, 0, 1, -1, 0, 0, 0],\

                           [0, 0, 1, -1, 0, 0, 0]], dtype = int)

        my_game.generate_random_board(board2)

        print my_game

        fitness = my_game.fitness_eval(board2)

        print fitness[0]

        best = my_game.PSO()

        print best

        if(best == fitness[1]):

            board2_accurate += 1

                

        my_game = Connect_Four()

        print "O is AI player, X is enemy of AI"

        board3 = np.array([[0., 0, 0, 0, 0, 0, 0],\

                           [0, 0, 0, 0, 0, 0, 0],\

                           [0, 0, 0, 0, 0, 0, 0],\

                           [0, 0, 1, -1, -1, 1, 0],\

                           [0, 0, 1, -1, 1, -1, 0],\

                           [0, 0, -1, 1, 1, -1, 0]], dtype = int)

        my_game.generate_random_board(board3)

        print my_game

        fitness = my_game.fitness_eval(board3)

        print fitness[0]

        best = my_game.PSO()

        print best

        if(best == fitness[1]):

            board3_accurate += 1

        

        my_game = Connect_Four()

        print "O is AI player, X is enemy of AI"

        board4 = np.array([[0., 0, 0, 0, 0, 0, 0],\

                           [0, 0, 0, 0, 0, 0, 0],\

                           [0, 0, 0, 0, 0, 0, 0],\

                           [0, 0, 0, 0, 0, 0, 0],\

                           [0, 0, 0, 0, 0, 0, 0],\

                           [0, 0, 0, 0, 0, 0, 0]], dtype = int)

        my_game.generate_random_board(board4)

        print my_game

        fitness = my_game.fitness_eval(board4)

        print fitness[0]

        best = my_game.PSO()

        print best

        if(best == fitness[1]):

            board4_accurate += 1

        

        my_game = Connect_Four()

        board5 = np.array([[0., 0, 0, 0, 0, 0, 0],\

                           [0, 0, 0, 0, 0, 0, 0],\

                           [0, 0, 0, 0, 0, 0, 0],\

                           [0, 0, 0, 0, 0, 0, 1],\

                           [-1, 0, 0, 0, 0, 0, 1],\

                           [-1, 0, 0, 0, 0, 0, 1]], dtype = int)

        my_game.generate_random_board(board5)

        print my_game

        fitness = my_game.fitness_eval(board5)

        print fitness[0]

        best = my_game.PSO()

        print best

        if(best == fitness[1]):

            board5_accurate += 1

        

        my_game = Connect_Four()

        print "O is AI player, X is enemy of AI"

        board6 = np.array([[0., 0, 0, 0, 0, 0, 0],\

                           [0, 0, 0, 0, 0, 0, 0],\

                           [0, 0, 0, 0, 0, 0, 0],\

                           [0, 0, 0, 0, 0, 0, 1],\

                           [-1, -1, -1, 0, 0, 0,1 ],\

                           [-1, -1, 1, 1, 0, 1, 1]], dtype = int)

        my_game.generate_random_board(board6)

        print my_game

        fitness = my_game.fitness_eval(board6)

        print fitness[0]

        best = my_game.PSO()

        print best

        if(best == fitness[1]):

            board6_accurate += 1

        

        my_game = Connect_Four()

        print "O is AI player, X is enemy of AI"

        board7 = np.array([[0., 0, 0, 0, 0, 0, 0],\

                           [0, 1, 0, 0, 0, 0, 0],\

                           [0, -1, 0, 0, 0, 0, -1],\

                           [1, 1, -1, 0, 0, -1, 1],\

                           [-1, -1, 1, -1, 1, 1, 1],\

                           [-1, -1, 1, -1, 1, -1, 1]], dtype = int)

        my_game.generate_random_board(board7)

        print my_game

        fitness = my_game.fitness_eval(board7)

        print fitness[0]

        best = my_game.PSO()

        print best

        if(best == fitness[1]):

            board7_accurate += 1

        

        my_game = Connect_Four()

        print "O is AI player, X is enemy of AI"

        board8 = np.array([[0., 0, 0, 0, 0, 0, 0],\

                           [0, 1, 0, 0, 0, 0, 0],\

                           [0, -1, -1, 1, 0, 0, -1],\

                           [1, 1, -1, 1, 0, -1, 1],\

                           [-1, -1, 1, -1, 1, 1, 1],\

                           [-1, -1, 1, -1, 1, -1, 1]], dtype = int)

        my_game.generate_random_board(board8)

        print my_game

        fitness = my_game.fitness_eval(board8)

        print fitness[0]

        best = my_game.PSO()

        print best

        if(best == fitness[1]):

            board8_accurate += 1



        my_game = Connect_Four()

        print "O is AI player, X is enemy of AI"

        board9 = np.array([[0., 0, 0, 0, 0, 0, 0],\

                           [0, 1, 1, 0, 0, 0, 0],\

                           [-1, -1, -1, 1, 0, 0, -1],\

                           [1, 1, -1, 1, 0, -1, 1],\

                           [-1, -1, 1, -1, 1, 1, 1],\

                           [-1, -1, 1, -1, 1, -1, 1]], dtype = int)

        my_game.generate_random_board(board9)

        print my_game

        fitness = my_game.fitness_eval(board9)

        print fitness[0]

        best = my_game.PSO()

        print best

        if(best == fitness[1]):

            board9_accurate += 1

        



        my_game = Connect_Four()

        print "O is AI player, X is enemy of AI"

        board10 = np.array([[0., 0, 0, 0, 0, 0, 0],\

                           [0, 1, 0, 0, 0, 0, 0],\

                           [1, -1, -1, 1, 0, 1, -1],\

                           [1, 1, -1, 1, -1, -1, 1],\

                           [-1, -1, 1, -1, 1, 1, 1],\

                           [-1, -1, 1, -1, 1, -1, 1]], dtype = int)

        my_game.generate_random_board(board10)

        print my_game

        fitness = my_game.fitness_eval(board10)

        print fitness[0]

        best = my_game.PSO()

        print best

        if(best == fitness[1]):

            board10_accurate += 1

    



    print("board 1 no of accurate", board1_accurate)

    print("board 2 no of accurate", board2_accurate)

    print("board 3 no of accurate", board3_accurate)

    print("board 4 no of accurate", board4_accurate)

    print("board 5 no of accurate", board5_accurate)

    print("board 6 no of accurate", board6_accurate)

    print("board 7 no of accurate", board7_accurate)

    print("board 8 no of accurate", board8_accurate)

    print("board 9 no of accurate", board9_accurate)

    print("board 10 no of accurate", board10_accurate)
    
    total = board1_accurate + board2_accurate + board3_accurate + board4_accurate + \
        board5_accurate + board6_accurate + board7_accurate + board8_accurate + board9_accurate + board10_accurate
    print('\n')
    print("average", total/10)
    print('\n')

if __name__ == "__main__":

    main()



    

