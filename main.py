#imports
from random import randint
from game_data import data
from art import logo, vs


play_again = True
def check(player1_followers, player2_followers, compare):
  if player1_followers > player2_followers and compare.upper() == "A":
    return False
  elif player1_followers < player2_followers and compare.upper() == "B":
    return False
  else:
    return True
def format(player):
  player_name = player["name"]
  player_desc = player["description"]
  player_country = player["country"]
  return f"{player_name}, a {player_desc}, from {player_country}"
    
    
def game():
  player1 = {}
  player1 = data[randint(0, 49)]
  score = 0
  game_is_over = False
  print(logo)
  #choosing two players to the game
  while not game_is_over:
    player2 = {}
    player2 = data[randint(0,49)]
    while player1 == player2:
      player2 = data[randint(0,49)]
    follower1 = player1["follower_count"]
    follower2 = player2["follower_count"]
  
    print(f"Compare A: {format(player1)}")
    print(vs)
    print(f"Aganist B: {format(player2)}")
    answer = input("Who has more followers? Type 'A' or 'B': ")
    game_is_over = check(follower1, follower2, answer)
    print(logo)
    if not game_is_over:
      score += 1
      print(f"\nYou got it right, Current score is : {score}")
      player1 = player2
    else:
      print(f"\nSorry, you lose. Your final score is: {score}")


while play_again:
  game()
  play = input("Do you want to play again?[y/n] ")
  if play.lower() == 'n':
    play_again = False


  
  
  
