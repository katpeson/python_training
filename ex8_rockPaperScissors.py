#http://www.practicepython.org/exercise/2014/03/26/08-rock-paper-scissors.html

# Make a two-player Rock-Paper-Scissors game. (Hint: Ask for player plays (using input), compare them, print out a message of congratulations to the winner, and ask if the players want to start a new game)
# 
# Remember the rules:
# 
# Rock beats scissors
# Scissors beats paper
# Paper beats rock

userInput1 = input('Type "rock", "paper" or "scissors" to play as user 1:' )
  while userInput1 != "rock" or "paper" or "scissors":
    userInput1 = input('Type "rock", "paper" or "scissors" to play as user 1:' )
    
userInput2 = input('Type "rock", "paper" or "scissors" to play as user 2:' )
  while userInput2 != "rock" or "paper" or "scissors":
    userInput2 = input('Type "rock", "paper" or "scissors" to play as user 2:' )
 
 