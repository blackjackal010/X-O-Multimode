import os
import sys
import time

class Game():
    def __init__(self):
        self.board = [[' ' for i in range(3)] for j in range(3)]
        self.help_board = [[str(j*3+i+1) for i in range(3)] for j in range(3)]
        self.player_1 = None
        self.player_2 = None
        self.scores = [0,0]
        self.turn = 0
        self.coin = 'x'
    def clear_all(self):
        os.system('clear')
        print('')
        print(' '*12+'+------------------------------+')
        print(' '*12+'|          X O Game            |')
        print(' '*12+'+------------------------------+')
        print('')

    def show_board(self,board):
        for i in range(3):
            print(' '*12+'+-------'*3+'+')
            print(' '*12+'|       '*3+'|')
            print(' '*12,end='')
            for j in range(3):
                print('|   '+board[i][j]+"   ", end='')
            print(' '*12+'|')
            print(' '*12+'|       '*3+'|')
        print(' '*12+'+-------'*3+'+')
        print('')

    def show_menu(self,options,close = 'Back',conds={}):
        keys = list(options.keys())
        for i in range(len(keys)):
            if keys[i] in conds:
                if not conds[keys[i]]:
                    del options[keys[i]]
        options[close] = False
        keys = list(options.keys())
        while not options[close]:
            self.clear_all()
            for i in range(len(keys)):
                print(f"{i+1}) {keys[i]}")
            try:
                choice = int(input("\n\n---> "))
                for i in range(len(keys)-1):
                    if choice == i+1:
                        if type(options[keys[i]]) == dict:
                            self.show_menu(options=options[keys[i]])
                        else:
                            self.nav(options[keys[i]])
                        break
                if choice == len(keys):
                    options[close] = True
            except:
                continue

    def load_game(self):
        self.feature_coming_soon()
    def feature_coming_soon(self):
        self.clear_all()
        print('feature coming soon')
        time.sleep(1)

    def nav(self,goto):
        if goto == 'singleplay':
            self.feature_coming_soon()
        elif goto == 'localmultiplay':
            self.feature_coming_soon()
        elif goto == 'samescreen':
            self.samescreen()
        elif goto == 'loadgame':
            self.load_game()

    def singleplay(self): # single player mode with AI
        pass

    def localmultiplay(self): # Local network Multiplayer
        pass

    def samescreen(self): # Same screen Multiplayer
        self.clear_all()
        self.show_board(self.help_board)
        print('Type the number to fill the board!')
        if self.player_1 == None or self.player_2 == None:
            self.player_1 = input("Player 1 [X] Name: ")
            self.player_2 = input("Player 2 [O] Name: ")
        while True:
            try:
                self.clear_all()
                print(f'{self.player_1} Score : {self.scores[0]}')
                print(f'{self.player_2} Score : {self.scores[1]}')
                self.show_board(self.board)
                if self.turn%2 == 0:
                    self.coin = 'X'
                    print(f"{self.player_1}'s turn [X]")
                else:
                    self.coin = 'O'
                    print(f"{self.player_2}'s turn [O]")
                choice = int(input("\n\n---> "))
                if choice < 1 or choice > 9:
                    print('Please Type number between 1 to 9')
                    time.sleep(0.5)
                else:
                    i = (choice-1)//3
                    j = (choice-1)%3
                    self.board[i][j] = self.coin
                    self.turn += 1
                    self.check_board()
                    
            except:
                print('Please Type number between 1 to 9')
                time.sleep(0.5)
    
    def check_board(self):
        win = ''
        pass
        if self.turn == 9 and win == '':
            print("draw")
            self.turn = 0
            self.board = [[' ' for i in range(3)] for j in range(3)]
            self.swap()
        else:
            pass
    def swap(self):
        c = self.player_1
        self.player_1 = self.player_2
        self.player_2 = c
        self.scores = self.scores[::-1]
    def start(self):
        self.show_menu(options={
            'New Game': {
                'Single player':'singleplay',
                'Multi player': {
                    'Local Multiplayer':'localmultiplay',
                    'Same Screen':'samescreen'
                }
            },
            'Continue Game': 'loadgame'
        },
        close = 'Quit', 
        conds={'Continue Game': os.path.isfile('game.json')})
        


if __name__ == "__main__":
    g = Game()
    g.start()
