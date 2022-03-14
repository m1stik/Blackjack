from logo import logo
import random
from replit import clear

#Initial variables
cards = [2, 3, 4, 5, 6, 7, 8, 9, 10, "jack", "queen", "king", "ace"]
loop = True
gameover = False
player = {}
ai = {}

#Function to reset cards
def reset_cards():
    global player, ai
    player = {
        "cards": [],
        "points": 0
    }
    ai = {
        "cards": [],
        "points": 0
    }

#Function to draw a card
def draw_card(target):
  card = random.choice(cards)
  target["cards"].append(card)
  if card == "jack" or card == "queen" or card == "king":
    target["points"] += 10
  elif card == "ace" and target["points"] <= 10:
    target["points"] += 11
  elif card == "ace" and target["points"] > 10:
    target["points"] += 1
  else:
    target["points"] += card

#Function to check points and return the result
def check_points():
  result = ""
  global gameover
  if player["points"] > ai["points"]:
    result = "win"
  elif player["points"] < ai["points"]:
    result = "lose"
  elif player["points"] == ai["points"]:
    result = "draw"

  if player["points"] > 21:
    gameover = True
    result = "lose"

  return result

#Main loop for game going on
while loop:
  answer_play = input("Do you want to play Blackjack? Type 'yes' or 'no': ")
  if answer_play == "yes" or answer_play == "y":
    #Calling functions to reset data
    clear()
    reset_cards()
    gameover = False
    print(logo)
    #Initial draw
    for i in range(2):
      draw_card(player)
      draw_card(ai)
    #Play stages
    while not gameover:
      print(f"Your cards {player['cards']}, current score: {player['points']}")
      print(f"Computer's first card: {ai['cards'][0]}")
      
      #Offer one more card
      answer_take_card = input("Type 'y' to get another card, type 'n' to pass: ")
      if answer_take_card == "y" or answer_take_card == "yes":
        draw_card(player)
        if ai["points"] < 15:
          draw_card(ai)
      else:
        while ai["points"] < 15:
            draw_card(ai)
        gameover = True

    #When all stages are over, make and display the result
    print(f"Your final hand {player['cards']}, final score: {player['points']}")
    print(f"Computer's final hand {ai['cards']}, final score: {ai['points']}")

    if check_points() == "win":
      print("Congrats, you win!")
    elif check_points() == "lose":
      print("You lose :(")
    elif check_points() == "draw":
      print("Hmm, that's a draw")

  else:
    loop = False
print("Thanks for playing")