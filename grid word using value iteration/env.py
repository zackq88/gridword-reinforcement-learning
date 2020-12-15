'''
Env:
##giveReward->map rewards.
##isEndFunc->return Boolean if game is end.
##nxtPosition(action)->return state.
##showBoard.
'''
import numpy as np

BOARD_ROWS = 5
BOARD_COLS = 5
WIN_STATE = (0, 4)
LOSE_STATE = (1, 4)
START = (4, 0)

class State:
    def __init__(self, state=START):
        self.board = np.zeros([BOARD_ROWS, BOARD_COLS])
        self.state = state
        self.isEnd = False

    def giveReward(self):
        if self.state == WIN_STATE:
            return 10
        elif self.state == LOSE_STATE:
            return -10
        elif (self.state == (4,2)) or (self.state == (4,4)) or (self.state == (2,3)) or (self.state == (1,2)) :
            return 1
        elif (self.state == (1,3)) or (self.state == (0,1)):
            return -9
        else:
            return 0

    def isEndFunc(self):
        if (self.state == WIN_STATE) or (self.state == LOSE_STATE):
            self.isEnd = True

    def nxtPosition(self, action):
        if True:
            if action == "up":
                nxtState = (self.state[0] - 1, self.state[1])
            elif action == "down":
                nxtState = (self.state[0] + 1, self.state[1])
            elif action == "left":
                nxtState = (self.state[0], self.state[1] - 1)
            else:
                nxtState = (self.state[0], self.state[1] + 1)
            # if next state legal
            if (nxtState[0] >= 0) and (nxtState[0] <= (BOARD_ROWS -1)):
                if (nxtState[1] >= 0) and (nxtState[1] <= (BOARD_COLS -1)):
                    if (nxtState != (3, 1)) and (nxtState != (3, 2)) and (nxtState != (1, 1)) and (nxtState != (2, 0)) :
                        return nxtState
            return self.state

    def showBoard(self):
        self.board[self.state] = 1
        for i in range(0, BOARD_ROWS):
            print('-------------------------------------------------------------------------------')
            out = '| '
            for j in range(0, BOARD_COLS):
                if self.board[i, j] == 1:
                    token = '*'
                if self.board[i, j] == -1:
                    token = 'z'
                if self.board[i, j] == 0:
                    token = '0'
                out += token + ' | '
            print(out)
        print('-----------------')
