# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   "I have not given or received any unauthorized aid on this assignment."
#
# Name:         YUAN SI
#               Andrew Oh
#               Tran Lam
# Section:      469-569
# Assignment:   final semester project (3 games)
# Date:         12/6/2021

from random import*
mm1 = input('Which game would you like to play? (Hangman? Rock Paper Scissors? Tic Tac Toe?) or enter stop:')
while mm1 != 'stop':
    if mm1 == 'Rock Paper Scissors' or mm1 == 'rock paper scissors':
        try:
            x = float(mm1)
        except:

            w = 0
            l = 0
            d = 0

            m1 = 'Welcome to a classic game of Rock Paper Scissors!'
            m2 = 'You will be battling the computer for a total of 8 rounds!'
            m3 = "However, you may exit the game by typing 'stop' before the 8 rounds conclude"
            m4 = 'May the odds be in your favor!'

            print('{a:^100}\n{b:^100}\n{c:^100}\n{d:^100}\n'.format(a=m1, b=m2, c=m3, d=m4))
            #dict for reference and just in case needs to be used
            dict = {1 : 'Rock',
                    2 : 'Paper',
                    3 : 'Scissors'
            }

            def call():
                global action
                action = input('Choose your fate: Rock, Paper, or Scissors?')

            def win(action):
                global ran
                global w
                ran = randint(1,3)
                if ran == 1 and (action == 'Paper' or action == 'paper'):
                    print('The computer chose Rock. Round won!')
                    w += 1
                if ran == 2 and (action == 'Scissors' or action == 'scissors'):
                    print('The computer chose Paper. Round won!')
                    w += 1
                if ran == 3 and (action == 'Rock' or action == 'rock'):
                    print('The computer chose Scissors. Round won!')
                    w += 1

            def lose(action):
                global l
                if ran == 1 and (action == 'Scissors' or action == 'scissors'):
                    print('The Computer chose Rock. Round lost!')
                    l += 1
                if ran == 2 and (action == 'Rock' or action == 'rock'):
                    print('The Computer chose Paper. Round lost!')
                    l += 1
                if ran == 3 and (action == 'Paper' or action == 'paper'):
                    print('The computer chose Scissors. Round lost!')
                    l += 1


            def draw(action):
                global d
                if ran == 1 and (action == 'Rock' or action == 'rock'):
                    print('The computer chose Rock too! It is a draw!')
                    d += 1
                if ran == 2 and (action == 'Paper' or action == 'paper'):
                    print('The computer chose paper, it is a draw!')
                    d += 1
                if ran == 3 and (action == 'Scissors' or action == 'scissors'):
                    print('The computer chose scissors, It is a draw!')
                    d += 1


            def game():
                record = ''
                line = 13 * '='
                global i
                i = 0
                while i < 8:
                    call()
                    win(action)
                    lose(action)
                    draw(action)
                    i += 1
                    print()
                    if action == 'Stop' or action == 'stop':
                        print('Thanks for playing this game.')
                        print('Here is your record:')
                        print()
                        break
                per = str(int((w / i) * 100)) + '%'
                print('Here is your record:')
                record += '{W:<6}{D:<6}{L:<3}\n{li:<0}\n{w:<6}{d:<6}{l:<3}'.format(W='W', D='D', L='L', li=line, w=w, d=d, l=l)
                print(record, '\nYour winning percentage is', per)

            game()
        mm1 = input('Which game would you like to play? (Hangman? Rock Paper Scissors? Tic Tac Toe?)')


    elif mm1 == 'Hangman' or mm1 == 'hangman':

        from random import randint


        # Functions with ASCII art of each level of the hangman
        def hangmanZero():
            print("                ")
            print("                ")
            print("                ")
            print("                ")
            print("                ")
            print("                ")
            print("                ")
            print("                ")


        def hangmanOne():
            print("                ")
            print("|               ")
            print("|               ")
            print("|               ")
            print("|               ")
            print("|               ")
            print("|               ")
            print("|               ")


        def hangmanTwo():
            print("________,       ")
            print("|               ")
            print("|               ")
            print("|               ")
            print("|               ")
            print("|               ")
            print("|               ")
            print("|               ")


        def hangmanThree():
            print("________,       ")
            print("|      (0)      ")
            print("|               ")
            print("|               ")
            print("|               ")
            print("|               ")
            print("|               ")
            print("|               ")


        def hangmanFour():
            print("________,       ")
            print("|      (0)      ")
            print("|       |       ")
            print("|               ")
            print("|               ")
            print("|               ")
            print("|               ")
            print("|               ")


        def hangmanFive():
            print("________,       ")
            print("|      (0)      ")
            print("|       |       ")
            print("|       |       ")
            print("|       |       ")
            print("|               ")
            print("|               ")
            print("|               ")


        def hangmanSix():
            print("________,       ")
            print("|      (0)      ")
            print("|       |       ")
            print("|  -----|       ")
            print("|       |       ")
            print("|               ")
            print("|               ")
            print("|               ")


        def hangmanSeven():
            print("________,       ")
            print("|      (0)      ")
            print("|       |       ")
            print("|  -----|-----  ")
            print("|       |       ")
            print("|               ")
            print("|               ")
            print("|               ")


        def hangmanEight():
            print("________,       ")
            print("|      (0)      ")
            print("|       |       ")
            print("|  -----|-----  ")
            print("|       |       ")
            print("|      /        ")
            print("|     /         ")
            print("|    /          ")


        def hangmanNine():
            print("________,       ")
            print("|      (0)      ")
            print("|       |       ")
            print("|  -----|-----  ")
            print("|       |       ")
            print("|      / \      ")
            print("|     /   \     ")
            print("|    /     \    ")


        wordsList = ["turtle", "napkin", "apple", "rockstar", "palace", "supreme"]
        incorrectGuesses = []
        # Chooses a random word from the wordsList
        word = wordsList[randint(1, len(wordsList)) - 1]
        # Counts the number of incorrect answers
        incorrect = 0
        # Replaces letters from random word with underscores
        guessWord = "_" * len(word)

        # print(word)
        print("Guess the word!")

        while incorrect < 9:
            # Prints the corresponding hangman ASCII art
            if incorrect == 0:
                hangmanZero()
            elif incorrect == 1:
                hangmanOne()
            elif incorrect == 2:
                hangmanTwo()
            elif incorrect == 3:
                hangmanThree()
            elif incorrect == 4:
                hangmanFour()
            elif incorrect == 5:
                hangmanFive()
            elif incorrect == 6:
                hangmanSix()
            elif incorrect == 7:
                hangmanSeven()
            elif incorrect == 8:
                hangmanEight()

            print(guessWord)
            print("Incorrect Guesses: ", end="")
            print(incorrectGuesses)
            # Prints the number of attemts left
            print("You have " + str(9 - incorrect) + " incorrect attempt(s) left!")
            # Converts the guessWord to a list in order to be mutable
            listWord = list(guessWord)
            guess = input("Guess a Letter, enter stop to be taken back to menu: ")
            if guess == 'stop':
                print('Thanks for playing Hangman!')
                print()
                break
            print()
            correctGuessCount = 0
            underscoreCount = 0
            for i in range(len(word)):
                # If the guess is in the word then replace the underscore with the guess in its same position
                if guess == word[i]:
                    listWord[i] = guess
                    correctGuessCount += 1
            # Converts the guessWord list back in a string
            guessWord = "".join(listWord)
            # If the guess was not in the word then add 1 to the number of incorrect guesses
            if correctGuessCount == 0:
                incorrect += 1
                incorrectGuesses.append(guess)

            # Checks if there are any underscores in the word that needs to be guessed
            for j in range(len(guessWord)):
                if guessWord[j] == "_":
                    underscoreCount += 1
            # If there are no underscores in the word that needs to be guessed then break out of the loop
            if underscoreCount == 0:
                break

        # If the number of incorrect attempts equals 9 then print a game over
        if incorrect == 9:
            hangmanNine()
            print("Game Over! You Lose!")
            print("The word was {}".format(word))
        # Else then the player wins
        else:
            if guess != "stop":
                print(guessWord)
                print("Congratulations! You Win!")
                print("You guessed the word with {} incorrect attempt(s)".format(incorrect))
            mm1 = input('Which game would you like to play? (Hangman? Rock Paper Scissors? Tic Tac Toe?)')


    elif mm1 == 'Tic Tac Toe' or mm1 == 'tic tac toe':
        a = 0
        b = 0


        def tictactoe(n1, n2, m):
            if (m == 'X'):
                move = 'O'
            elif (m == 'O'):
                move = 'X'
            print("                   {} ({}) - {} ({})".format(n1, a, n2, b))
            Board = [['_', '_', '_'], ['_', '_', '_'], ['_', '_', '_']]
            firstboard(Board, m, move)


        def Tictactoe(n1, n2, M):
            if (M == 'X'):
                Move = 'O'
            elif (M == 'O'):
                Move = 'X'
            print("                   {} ({}) - {} ({})".format(n1, a, n2, b))
            Board = [['_', '_', '_'], ['_', '_', '_'], ['_', '_', '_']]
            secondboard(Board, M, Move)


        def secondboard(board, Marks, m2):
            global a
            global b
            # creates loop
            two = 'true'
            while (two != 'stop'):
                print(board[0])
                print(board[1])
                print(board[2])
                # board is printed

                # 1st player's turn
                row = int(input("(1st player) Enter the row: "))
                r = row - 1
                column = int(input("(1st player) Enter the column: "))
                print()
                c = column - 1
                board[r][c] = Marks

                # If first player wins
                if (board[0][0] == Marks and board[1][0] == Marks and board[2][0] == Marks):
                    b += 1
                    print(board[0])
                    print(board[1])
                    print(board[2])
                    winner = input("First player wins!. Continue? (Yes/No) ")
                    if (winner == "Yes"):
                        mark = input("2nd player, which mark do you choose, 'X' or 'O'?: ")
                        print()
                        tictactoe(name1, name2, mark)
                        break
                    elif (winner == 'No'):
                        break
                elif (board[0][1] == Marks and board[1][1] == Marks and board[2][1] == Marks):
                    b += 1
                    print(board[0])
                    print(board[1])
                    print(board[2])
                    winner = input("First player wins!. Continue? (Yes/No) ")
                    if (winner == "Yes"):
                        mark = input("2nd player, which mark do you choose, 'X' or 'O'?: ")
                        print()
                        tictactoe(name1, name2, mark)
                        break
                    elif (winner == 'No'):
                        break
                elif (board[0][2] == Marks and board[1][2] == Marks and board[2][2] == Marks):
                    b += 1
                    print(board[0])
                    print(board[1])
                    print(board[2])
                    winner = input("First player wins!. Continue? (Yes/No) ")
                    if (winner == "Yes"):
                        mark = input("2nd player, which mark do you choose, 'X' or 'O'?: ")
                        print()
                        tictactoe(name1, name2, mark)
                        break
                    elif (winner == 'No'):
                        break
                if (board[0][0] == Marks and board[0][1] == Marks and board[0][2] == Marks):
                    b += 1
                    print(board[0])
                    print(board[1])
                    print(board[2])
                    winner = input("First player wins!. Continue? (Yes/No) ")
                    if (winner == "Yes"):
                        mark = input("2nd player, which mark do you choose, 'X' or 'O'?: ")
                        print()
                        tictactoe(name1, name2, mark)
                        break
                    elif (winner == 'No'):
                        break
                elif (board[1][0] == Marks and board[1][1] == Marks and board[1][2] == Marks):
                    b += 1
                    print(board[0])
                    print(board[1])
                    print(board[2])
                    winner = input("First player wins!. Continue? (Yes/No) ")
                    if (winner == "Yes"):
                        mark = input("2nd player, which mark do you choose, 'X' or 'O'?: ")
                        print()
                        tictactoe(name1, name2, mark)
                        break
                    elif (winner == 'No'):
                        break
                elif (board[2][0] == Marks and board[2][1] == Marks and board[2][2] == Marks):
                    b += 1
                    print(board[0])
                    print(board[1])
                    print(board[2])
                    winner = input("First player wins!. Continue? (Yes/No) ")
                    if (winner == "Yes"):
                        mark = input("2nd player, which mark do you choose, 'X' or 'O'?: ")
                        print()
                        tictactoe(name1, name2, mark)
                        break
                    elif (winner == 'No'):
                        break
                elif (board[0][0] == Marks and board[1][1] == Marks and board[2][2] == Marks):
                    b += 1
                    print(board[0])
                    print(board[1])
                    print(board[2])
                    winner = input("First player wins!. Continue? (Yes/No) ")
                    if (winner == "Yes"):
                        mark = input("2nd player, which mark do you choose, 'X' or 'O'?: ")
                        print()
                        tictactoe(name1, name2, mark)
                        break
                    elif (winner == 'No'):
                        break
                elif (board[2][0] == Marks and board[1][1] == Marks and board[0][2] == Marks):
                    b += 1
                    print(board[0])
                    print(board[1])
                    print(board[2])
                    winner = input("First player wins!. Continue? (Yes/No) ")
                    if (winner == "Yes"):
                        mark = input("2nd player, which mark do you choose, 'X' or 'O'?: ")
                        print()
                        tictactoe(name1, name2, mark)
                        break
                    elif (winner == 'No'):
                        break

                # board is printed for second player
                print(board[0])
                print(board[1])
                print(board[2])

                # 2nd player's turn
                Row = int(input("(2nd player) Enter the row: "))
                R = Row - 1
                Column = int(input("(2nd player) Enter the column: "))
                print()
                C = Column - 1

                # if the spot has already marked
                if (r == R and c == C):
                    print("Your opponent have already marked this spot. Try again")
                    print()
                    print(board[0])
                    print(board[1])
                    print(board[2])
                    Row = int(input("(2nd player) Enter the row: "))
                    R = Row - 1
                    Column = int(input("(2nd player) Enter the column: "))
                    C = Column - 1
                    if (Marks == 'X'):
                        board[R][C] = 'O'
                    elif (Marks == 'O'):
                        board[R][C] = 'X'
                else:
                    if (Marks == 'X'):
                        board[R][C] = 'O'
                    elif (Marks == 'O'):
                        board[R][C] = 'X'

                # If second player wins
                if (board[0][0] == m2 and board[1][0] == m2 and board[2][0] == m2):
                    a += 1
                    print(board[0])
                    print(board[1])
                    print(board[2])
                    winner = input("Second player wins!. Continue? (Yes/No) ")
                    if (winner == "Yes"):
                        mark = input("1st player, which mark do you choose, 'X' or 'O'?: ")
                        print()
                        Tictactoe(name1, name2, mark)
                        break
                    elif (winner == 'No'):
                        break
                elif (board[0][1] == m2 and board[1][1] == m2 and board[2][1] == m2):
                    a += 1
                    print(board[0])
                    print(board[1])
                    print(board[2])
                    winner = input("Second player wins!. Continue? (Yes/No) ")
                    if (winner == "Yes"):
                        mark = input("1st player, which mark do you choose, 'X' or 'O'?: ")
                        print()
                        Tictactoe(name1, name2, mark)
                        break
                    elif (winner == 'No'):
                        two = 'stop'
                elif (board[0][2] == m2 and board[1][2] == m2 and board[2][2] == m2):
                    a += 1
                    print(board[0])
                    print(board[1])
                    print(board[2])
                    winner = input("Second player wins!. Continue? (Yes/No) ")
                    if (winner == "Yes"):
                        mark = input("1st player, which mark do you choose, 'X' or 'O'?: ")
                        print()
                        Tictactoe(name1, name2, mark)
                        break
                    elif (winner == 'No'):
                        two = 'stop'
                elif (board[0][0] == m2 and board[0][1] == m2 and board[0][2] == m2):
                    a += 1
                    print(board[0])
                    print(board[1])
                    print(board[2])
                    winner = input("Second player wins!. Continue? (Yes/No) ")
                    if (winner == "Yes"):
                        mark = input("1st player, which mark do you choose, 'X' or 'O'?: ")
                        print()
                        Tictactoe(name1, name2, mark)
                        break
                    elif (winner == 'No'):
                        two = 'stop'
                elif (board[1][0] == m2 and board[1][1] == m2 and board[1][2] == m2):
                    a += 1
                    print(board[0])
                    print(board[1])
                    print(board[2])
                    winner = input("Second player wins!. Continue? (Yes/No) ")
                    if (winner == "Yes"):
                        mark = input("1st player, which mark do you choose, 'X' or 'O'?: ")
                        print()
                        Tictactoe(name1, name2, mark)
                        break
                    elif (winner == 'No'):
                        two = 'stop'
                elif (board[2][0] == m2 and board[2][1] == m2 and board[2][2] == m2):
                    a += 1
                    print(board[0])
                    print(board[1])
                    print(board[2])
                    winner = input("Second player wins!. Continue? (Yes/No) ")
                    if (winner == "Yes"):
                        mark = input("1st player, which mark do you choose, 'X' or 'O'?: ")
                        print()
                        Tictactoe(name1, name2, mark)
                        break
                    elif (winner == 'No'):
                        two = 'stop'
                elif (board[0][0] == m2 and board[1][1] == m2 and board[2][2] == m2):
                    a += 1
                    print(board[0])
                    print(board[1])
                    print(board[2])
                    winner = input("Second player wins!. Continue? (Yes/No) ")
                    if (winner == "Yes"):
                        mark = input("1st player, which mark do you choose, 'X' or 'O'?: ")
                        print()
                        Tictactoe(name1, name2, mark)
                        break
                    elif (winner == 'No'):
                        two = 'stop'
                elif (board[2][0] == m2 and board[1][1] == m2 and board[0][2] == m2):
                    a += 1
                    print(board[0])
                    print(board[1])
                    print(board[2])
                    winner = input("Second player wins!. Continue? (Yes/No) ")
                    if (winner == "Yes"):
                        mark = input("1st player, which mark do you choose, 'X' or 'O'?: ")
                        print()
                        Tictactoe(name1, name2, mark)
                        break
                    elif (winner == 'No'):
                        two = 'stop'


        def firstboard(board, marks, m1):
            global a
            global b
            # creates loop
            one = 'true'
            while (one != 'stop'):
                print(board[0])
                print(board[1])
                print(board[2])
                # board is printed

                # 1st player's turn
                row = int(input("(1st player) Enter the row: "))
                r = row - 1
                column = int(input("(1st player) Enter the column: "))
                print()
                c = column - 1
                board[r][c] = marks

                # If first player wins
                if (board[0][0] == marks and board[1][0] == marks and board[2][0] == marks):
                    a += 1
                    print(board[0])
                    print(board[1])
                    print(board[2])
                    winner = input("First player wins!. Continue? (Yes/No) ")
                    if (winner == "Yes"):
                        Mark = input("2nd player, which mark do you choose, 'X' or 'O'?: ")
                        print()
                        tictactoe(name1, name2, Mark)
                        break
                    elif (winner == 'No'):
                        break
                elif (board[0][1] == marks and board[1][1] == marks and board[2][1] == marks):
                    a += 1
                    print(board[0])
                    print(board[1])
                    print(board[2])
                    winner = input("First player wins!. Continue? (Yes/No) ")
                    if (winner == "Yes"):
                        Mark = input("2nd player, which mark do you choose, 'X' or 'O'?: ")
                        print()
                        tictactoe(name1, name2, Mark)
                        break
                    elif (winner == 'No'):
                        break
                elif (board[0][2] == marks and board[1][2] == marks and board[2][2] == marks):
                    a += 1
                    print(board[0])
                    print(board[1])
                    print(board[2])
                    winner = input("First player wins!. Continue? (Yes/No) ")
                    if (winner == "Yes"):
                        Mark = input("2nd player, which mark do you choose, 'X' or 'O'?: ")
                        print()
                        tictactoe(name1, name2, Mark)
                        break
                    elif (winner == 'No'):
                        break
                elif (board[0][0] == marks and board[0][1] == marks and board[0][2] == marks):
                    a += 1
                    print(board[0])
                    print(board[1])
                    print(board[2])
                    winner = input("First player wins!. Continue? (Yes/No) ")
                    if (winner == "Yes"):
                        Mark = input("2nd player, which mark do you choose, 'X' or 'O'?: ")
                        print()
                        tictactoe(name1, name2, Mark)
                        break
                    elif (winner == 'No'):
                        break
                elif (board[1][0] == marks and board[1][1] == marks and board[1][2] == marks):
                    a += 1
                    print(board[0])
                    print(board[1])
                    print(board[2])
                    winner = input("First player wins!. Continue? (Yes/No) ")
                    if (winner == "Yes"):
                        Mark = input("2nd player, which mark do you choose, 'X' or 'O'?: ")
                        print()
                        tictactoe(name1, name2, Mark)
                        break
                    elif (winner == 'No'):
                        break
                elif (board[2][0] == marks and board[2][1] == marks and board[2][2] == marks):
                    a += 1
                    print(board[0])
                    print(board[1])
                    print(board[2])
                    winner = input("First player wins!. Continue? (Yes/No) ")
                    if (winner == "Yes"):
                        Mark = input("2nd player, which mark do you choose, 'X' or 'O'?: ")
                        print()
                        tictactoe(name1, name2, Mark)
                        break
                    elif (winner == 'No'):
                        break
                elif (board[0][0] == marks and board[1][1] == marks and board[2][2] == marks):
                    a += 1
                    print(board[0])
                    print(board[1])
                    print(board[2])
                    winner = input("First player wins!. Continue? (Yes/No) ")
                    if (winner == "Yes"):
                        Mark = input("2nd player, which mark do you choose, 'X' or 'O'?: ")
                        print()
                        tictactoe(name1, name2, Mark)
                        break
                    elif (winner == 'No'):
                        break
                elif (board[2][0] == marks and board[1][1] == marks and board[0][2] == marks):
                    a += 1
                    print(board[0])
                    print(board[1])
                    print(board[2])
                    winner = input("First player wins!. Continue? (Yes/No) ")
                    if (winner == "Yes"):
                        Mark = input("2nd player, which mark do you choose, 'X' or 'O'?: ")
                        print()
                        tictactoe(name1, name2, Mark)
                        break
                    elif (winner == 'No'):
                        break

                # board is printed for second player
                print(board[0])
                print(board[1])
                print(board[2])

                # 2nd player's turn
                Row = int(input("(2nd player) Enter the row: "))
                R = Row - 1
                Column = int(input("(2nd player) Enter the column: "))
                print()
                C = Column - 1

                # if the spot has already marked
                if (r == R and c == C):
                    print("Your opponent have already marked this spot. Try again")
                    print()
                    print(board[0])
                    print(board[1])
                    print(board[2])
                    Row = int(input("(2nd player) Enter the row: "))
                    R = Row - 1
                    Column = int(input("(2nd player) Enter the column: "))
                    C = Column - 1
                    if (marks == 'X'):
                        board[R][C] = 'O'
                    elif (marks == 'O'):
                        board[R][C] = 'X'
                else:
                    if (marks == 'X'):
                        board[R][C] = 'O'
                    elif (marks == 'O'):
                        board[R][C] = 'X'

                # If second player wins
                if (board[0][0] == m1 and board[1][0] == m1 and board[2][0] == m1):
                    b += 1
                    print(board[0])
                    print(board[1])
                    print(board[2])
                    winner = input("Second player wins!. Continue? (Yes/No) ")
                    if (winner == "Yes"):
                        Mark = input("1st player, which mark do you choose, 'X' or 'O'?: ")
                        print()
                        tictactoe(name1, name2, Mark)
                        break
                    elif (winner == 'No'):
                        one = 'stop'
                elif (board[0][1] == m1 and board[1][1] == m1 and board[2][1] == m1):
                    b += 1
                    print(board[0])
                    print(board[1])
                    print(board[2])
                    winner = input("Second player wins!. Continue? (Yes/No) ")
                    if (winner == "Yes"):
                        Mark = input("1st player, which mark do you choose, 'X' or 'O'?: ")
                        print()
                        tictactoe(name1, name2, Mark)
                        break
                    elif (winner == 'No'):
                        one = 'stop'
                elif (board[0][2] == m1 and board[1][2] == m1 and board[2][2] == m1):
                    b += 1
                    print(board[0])
                    print(board[1])
                    print(board[2])
                    winner = input("Second player wins!. Continue? (Yes/No) ")
                    if (winner == "Yes"):
                        Mark = input("1st player, which mark do you choose, 'X' or 'O'?: ")
                        print()
                        tictactoe(name1, name2, Mark)
                        break
                    elif (winner == 'No'):
                        one = 'stop'
                elif (board[0][0] == m1 and board[0][1] == m1 and board[0][2] == m1):
                    b += 1
                    print(board[0])
                    print(board[1])
                    print(board[2])
                    winner = input("Second player wins!. Continue? (Yes/No) ")
                    if (winner == "Yes"):
                        Mark = input("1st player, which mark do you choose, 'X' or 'O'?: ")
                        print()
                        tictactoe(name1, name2, Mark)
                        break
                    elif (winner == 'No'):
                        one = 'stop'
                elif (board[1][0] == m1 and board[1][1] == m1 and board[1][2] == m1):
                    b += 1
                    print(board[0])
                    print(board[1])
                    print(board[2])
                    winner = input("Second player wins!. Continue? (Yes/No) ")
                    if (winner == "Yes"):
                        Mark = input("1st player, which mark do you choose, 'X' or 'O'?: ")
                        print()
                        tictactoe(name1, name2, Mark)
                        break
                    elif (winner == 'No'):
                        one = 'stop'
                elif (board[2][0] == m1 and board[2][1] == m1 and board[2][2] == m1):
                    b += 1
                    print(board[0])
                    print(board[1])
                    print(board[2])
                    winner = input("Second player wins!. Continue? (Yes/No) ")
                    if (winner == "Yes"):
                        Mark = input("1st player, which mark do you choose, 'X' or 'O'?: ")
                        print()
                        tictactoe(name1, name2, Mark)
                        break
                    elif (winner == 'No'):
                        one = 'stop'
                elif (board[0][0] == m1 and board[1][1] == m1 and board[2][2] == m1):
                    b += 1
                    print(board[0])
                    print(board[1])
                    print(board[2])
                    winner = input("Second player wins!. Continue? (Yes/No) ")
                    if (winner == "Yes"):
                        Mark = input("1st player, which mark do you choose, 'X' or 'O'?: ")
                        print()
                        tictactoe(name1, name2, Mark)
                        break
                    elif (winner == 'No'):
                        one = 'stop'
                elif (board[2][0] == m1 and board[1][1] == m1 and board[0][2] == m1):
                    b += 1
                    print(board[0])
                    print(board[1])
                    print(board[2])
                    winner = input("Second player wins!. Continue? (Yes/No) ")
                    if (winner == "Yes"):
                        Mark = input("1st player, which mark do you choose, 'X' or 'O'?: ")
                        print()
                        tictactoe(name1, name2, Mark)
                        break
                    elif (winner == 'No'):
                        one = 'stop'


        print("                                        Welcome to Tic-Tac-Toe!")
        print("                     Enter 'start' to play the game. Enter 'stop' to quit the game")
        play = input("                                            Enter here: ")

        if (play == 'start' or play == 'Start'):
            name1 = input("1st player's name: ")
            name2 = input("2nd player's name: ")
            mark = input("1st player, which mark do you choose, 'X' or 'O'?: ")
            tictactoe(name1, name2, mark)
        elif (play == 'stop' or play == 'stop'):
            print("                                              bye..........")
        elif(play == 'TikiTakiToki'):
            print("L O L")
            mm1 = input('Which game would you like to play? (Hangman? Rock Paper Scissors? Tic Tac Toe?)')
if mm1 == 'stop' or mm1 == 'Stop':
    print('Thanks for playing our games! Thank you!')

