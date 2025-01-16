import random, sys
print('ROCK, PAPER, SCISSORS\n')
Wins,Losses,Ties = 0, 0, 0
while True:
    #print('%s Wins, %s Losses, %s Ties' %(Wins,Losses,Ties))
    print('{0} Wins, {1} Losses, {2} Ties'.format(Wins,Losses,Ties))
    while True:
        print('Enter your move: (r)ock (p)aper (s)cissors or (q)quit')
        playerMove=input()
        if playerMove == 'q':
            sys.exit()
        if playerMove == 'r' or playerMove == 'p' or playerMove == 's':
            break # Break out from the player input loop
        print('Type one of r, p, s, or q.')
    
    # Pick a random move from computer
    num = random.randint(1,3)
    compMove=''
    if num == 1:
        compMove = 'ROCK'
    elif num == 2:
        compMove = 'PAPER'
    else:
        compMove = 'SCISSORS'

    if playerMove == 'p' and compMove == 'PAPER':
        print("PAPER versus ...")
        print(compMove)
        print("It is a tie!")
        Ties += 1
    elif playerMove == 'p' and compMove == 'ROCK':
        print("PAPER versus ...")
        print(compMove)
        print("You Win!")
        Wins += 1
    elif playerMove == 'p' and compMove == 'SCISSORS':
        print("PAPER versus ...")
        print(compMove)
        print("You Lose!")
        Losses += 1
    elif playerMove == 'r' and compMove == 'ROCK':
        print("ROCK versus ...")
        print(compMove)
        print("It is a tie!")
        Ties += 1
    elif playerMove == 'r' and compMove == 'SCISSORS':
        print("ROCK versus ...")
        print(compMove)
        print("You Win!")
        Wins += 1
    elif playerMove == 'r' and compMove == 'PAPER':
        print("ROCK versus ...")
        print(compMove)
        print("You Lose!")
        Losses += 1
    elif playerMove == 's' and compMove == 'SCISSORS':
        print("SCISSORS versus ...")
        print(compMove)
        print("It is a tie!")
        Ties += 1
    elif playerMove == 's' and compMove == 'PAPER':
        print("SCISSORS versus ...")
        print(compMove)
        print("You Win!")
        Wins += 1
    elif playerMove == 's' and compMove == 'ROCK':
        print("SCISSORS versus ...")
        print(compMove)
        print("You Lose!")
        Losses += 1
