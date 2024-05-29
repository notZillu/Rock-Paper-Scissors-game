import random 

#Introduction to the game
intro = input("This is a rock, paper, scissors game. Press any key to continue or q to quit. ").lower()

#Checking if the player wants to continue or quit the game
if intro == 'q':
  quit()

#Setting starting points for the player and computer
player_points = 0
computer_points = 0

#A list so that the computer gets to choose from these
options = ["rock", "paper", "scissors"]

#Setting the number of attempts for the player
attempts = 5

#Using for loop for attempts
for a in range(1, attempts+1):
  
  player_input = input("Enter rock/paper/scissors: ").lower()

  #Command for computer to choose from the list givem above
  computer_input = random.choice(options)

  #Checking conditions for the player to win or lose which adds the points for the player and computer accordingly
  if player_input == 'rock' and computer_input == 'paper':
    print("Computer chose " ,computer_input)
    print("You lose.")
    computer_points = computer_points + 1
  elif player_input == 'paper' and computer_input == 'rock':
    print("Computer chose " ,computer_input)
    print("You win!")
    player_points = player_points + 1
  elif player_input == 'paper' and computer_input == 'scissors':
    print("Computer chose " ,computer_input)
    print("You lose.")
    computer_points = computer_points + 1
  elif player_input == 'scissors' and computer_input == 'paper':
    print("Computer chose " ,computer_input)
    print("You win!")
    player_points = player_points + 1
  elif player_input == 'scissors' and computer_input == 'rock':
    print("Computer chose " ,computer_input)
    print("You lose.")
    computer_points = computer_points + 1
  elif player_input == 'rock' and computer_input == 'scissors':
    print("Computer chose " ,computer_input)
    print("You win!")
    player_points = player_points + 1
  elif player_input == computer_input:
    print("Computer chose " ,computer_input)
    print("It's a draw")

#Printing the player's and computer's points
print("You have" ,player_points, "points.")
print("Computer has" ,computer_points, "points.")

#Checking who won or if it is a draw according to points
if player_points > computer_points:
  print("You won!")
elif player_points == computer_points:
  print("Its a draw.")
else:
  print("Computer won.")