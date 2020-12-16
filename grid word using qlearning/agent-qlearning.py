'''
Agent:
##chooseAction->return action
##takeAction(action)->return state.
##reset.
##play : 1.chooseAction  2.takeAction  3.isEndFunc (if yes->update state values).
'''

import numpy as np
from env import State
BOARD_ROWS = 5
BOARD_COLS = 5
WIN_STATE = (0, 4)
LOSE_STATE = (1, 4)
START = (4, 0)

class Agent:
    def __init__(self):
        self.State=State()
        self.isEnd = self.State.isEnd
        self.states = []
        self.actions = ["up", "down", "left", "right"]
        self.lr = 0.05
        self.exp_rate = 0.5
        self.decay_gamma=0.9

        self.Q_values={}
        for i in range(BOARD_ROWS):
            for j in range(BOARD_COLS):
                self.Q_values[(i, j)] = {}
                for a in self.actions:
                    self.Q_values[(i,j)][a]=0

    def chooseAction(self):
        mx_nxt_reward=0
        action=""
        if np.random.uniform(0, 1) <= self.exp_rate:
            action = np.random.choice(self.actions)
        else:
            # greedy action
            for a in self.actions:
                current_position = self.State.state
                nxt_reward = self.Q_values[current_position][a]
                if nxt_reward >= mx_nxt_reward:
                    action = a
                    mx_nxt_reward = nxt_reward
        return action

    def takeAction(self,action):
        position=self.State.nxtPosition(action)
        return State(state=position)

    def reset(self):
        self.states = []
        self.State = State()
        self.isEnd = self.State.isEnd

    def play(self,rounds=10):
        i=0
        while i < rounds:
            # If End game , update all state values
            if self.State.isEnd:
                # back propagate
                reward = self.State.giveReward()
                for a in self.actions:
                    self.Q_values[self.State.state][a] = reward
                print("Game End Reward", reward)
                # update state values
                for s in reversed(self.states):
                    for a in (self.actions):
                        #print('////////////////////////////////////////////////////////////////')
                        #print(self.Q_values[s][a])
                        current_q_value = self.Q_values[s][a]
                        reward = current_q_value + self.lr * (self.decay_gamma * reward - current_q_value)
                        self.Q_values[s][a] = round(reward, 3)

                self.reset()
                i += 1
                print(
                    '***************************************************************************************************')
                print('round{}'.format(i))
                print(
                    '***************************************************************************************************')

            else:  # we start with this part
                action = self.chooseAction()
                # append trace
                self.states.append(self.State.nxtPosition(action))
                print("current position {} action {}".format(self.State.state, action))
                # next state
                self.State = self.takeAction(action)
                # test if End game
                self.State.isEndFunc()
                print("nxt state", self.State.state)
                print("-------------------------------")

    def showValues(self):
        for i in range(0, BOARD_ROWS):
            print('----------------------------------')
            out = '| '
            for j in range(0, BOARD_COLS):
                # for a in self.actions:
                out += str(self.Q_values[(i, j)]).ljust(6) + ' | '
            print(out)
        print('----------------------------------')


if __name__ == "__main__":
    ag = Agent()
    print("initial Q-values ... \n")
    print(ag.Q_values)

    ag.play(150)
    print("latest Q-values ... \n")
    print(ag.Q_values)

