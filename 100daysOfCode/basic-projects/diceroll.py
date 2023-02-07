import random

x = random.randint(1, 6)

def startGame() :
        num = int(input('\nEnter a number between 1 to 6 : '))
        if num > 6 or num < 1:
            print('\nI said enter between 1 to 6 ')
            startGame()
        else :
            if x == num :
                print('\nIts a match ------> You Won!!')
                if x==1:
                    print('---------------')
                    print('|             |')
                    print('|             |')
                    print('|      0      |')
                    print('|             |')
                    print('|             |')
                    print('---------------')

                if x==2:
                    print('---------------')
                    print('|             |')
                    print('|             |')
                    print('|   0     0   |')
                    print('|             |')
                    print('|             |')
                    print('---------------')

                if x==3:
                    print('---------------')
                    print('|      0      |')
                    print('|             |')
                    print('|      0      |')
                    print('|             |')
                    print('|      0      |')
                    print('---------------')

                if x==4:
                    print('---------------')
                    print('|             |')
                    print('|   0     0   |')
                    print('|             |')
                    print('|   0     0   |')
                    print('|             |')
                    print('---------------')
                
                if x==5:
                    print('---------------')
                    print('|             |')
                    print('|   0     0   |')
                    print('|      0      |')
                    print('|   0     0   |')
                    print('|             |')
                    print('---------------')
                
                if x==6:
                    print('---------------')
                    print('|  0       0  |')
                    print('|             |')
                    print('|  0       0  |')
                    print('|             |')
                    print('|  0       0  |')
                    print('---------------')
                print('\n Game Ended!!')
                print('\n')
            else:
                print()
                print('Bad luck!! Try next time.')
                print()
                print('The correct number was : ',x)
                if x==1:
                    print('---------------')
                    print('|             |')
                    print('|             |')
                    print('|      0      |')
                    print('|             |')
                    print('|             |')
                    print('---------------')

                if x==2:
                    print('---------------')
                    print('|             |')
                    print('|             |')
                    print('|   0     0   |')
                    print('|             |')
                    print('|             |')
                    print('---------------')

                if x==3:
                    print('---------------')
                    print('|      0      |')
                    print('|             |')
                    print('|      0      |')
                    print('|             |')
                    print('|      0      |')
                    print('---------------')

                if x==4:
                    print('---------------')
                    print('|             |')
                    print('|   0     0   |')
                    print('|             |')
                    print('|   0     0   |')
                    print('|             |')
                    print('---------------')
                
                if x==5:
                    print('---------------')
                    print('|             |')
                    print('|   0     0   |')
                    print('|      0      |')
                    print('|   0     0   |')
                    print('|             |')
                    print('---------------')
                
                if x==6:
                    print('---------------')
                    print('|  0       0  |')
                    print('|             |')
                    print('|  0       0  |')
                    print('|             |')
                    print('|  0       0  |')
                    print('---------------')

                tryAgain = input('Do you want to try again? : ')
                if tryAgain == 'y':
                    startGame()
                else:
                    return


def enterCommand():
    print('Do you want to play Dice roll game?\n')
    command = input('Enter Y to start : ')
    if command == 'y' or command == 'Y':
        startGame()
    else:
        print('\nI said Enter y to start!!! \n')
        enterCommand()

enterCommand()