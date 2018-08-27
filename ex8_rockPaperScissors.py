#http://www.practicepython.org/exercise/2014/03/26/08-rock-paper-scissors.html

# Make a two-player Rock-Paper-Scissors game. (Hint: Ask for player plays (using input), compare them, print out a message of congratulations to the winner, and ask if the players want to start a new game)
# 
# Remember the rules:
# 
# Rock beats scissors
# Scissors beats paper
# Paper beats rock
@TODO to improve: try to use dictionary to print the actual value of weapon instead of the letter!

while True:
	print "Let's play ROCK, PAPER, SCISSORS!"
	print "RULES: Rock beats scissors beats paper beats rock"

	user1 = raw_input('Type Rock (R), Paper (P) or Scissors (S) to play:' )
	user2 = raw_input('Type Rock (R), Paper (P) or Scissors (S) to play:' )

	if user1 == user2:
		print "It's a draw!"
	elif (user1 == 'R' and user2 == 'P') or (user1 == 'P' and user2 == 'S') or (user1 == 'S' and user2 == 'R'):
		print "User2 wins with ", user2
	elif (user2 == 'R' and user1 == 'P') or (user2 == 'P' and user1 == 'S') or (user2 == 'S' and user1 == 'R'):
		print "User1 wins with ", user1
	
	newGame = raw_input ('Play again (Y)es or (N)o?')
	if newGame == N:
		break
	else:
		print "Thanks for playing, goodbye!"

#while userInput != "rock" or "paper" or "scissors":
 
#print "User 1 has chosen %s and user 2 has chosen " % userInput1, userinput2