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
    
    #Print Player Move
    if playerMove == 'r':
        print("ROCK versus ...")
    elif playerMove == 'p':
        print("PAPER versus ...")
    elif playerMove == 's':
        print("SCISSORS versus ...")

    # Pick a random move from computer and print Computer Move
    num = random.randint(1,3)
    compMove=''
    if num == 1:
        compMove = 'r'
        print('ROCK')
    elif num == 2:
        compMove = 'p'
        print('PAPER')
    else:
        compMove = 's'
        print('SCISSORS')

    # Record Win/Lose/Tie
    if playerMove == compMove:
        print("It is a tie!")
        Ties += 1
    elif playerMove == 'p' and compMove == 'r':
        print("You Win!")
        Wins += 1
    elif playerMove == 'p' and compMove == 's':
        print("You Lose!")
        Losses += 1
    elif playerMove == 'r' and compMove == 's':
        print("You Win!")
        Wins += 1
    elif playerMove == 'r' and compMove == 'p':
        print("You Lose!")
        Losses += 1
    elif playerMove == 's' and compMove == 'p':
        print("You Win!")
        Wins += 1
    elif playerMove == 's' and compMove == 'r':
        print("You Lose!")
        Losses += 1
