#DiceRoll.py
#Name:
#Date:
#Assignment:
import random

def main():
  #Create an empty list with possible roll values
  rolls = [0,0,0,0,0,0,0,0,0,0,0,0]
  #Create two dice values ranging from 1 - 6 each
  for r in range(100):
    dice1 = random.randint(1, 6)
    dice2 = random.randint(1, 6)
    sum_dice = dice1 + dice2
    rolls[sum_dice - 1] += 1
    print(f"Roll {r+1}: Dice 1 = {dice1}, Dice 2 = {dice2}, Sum = {sum_dice}")

  #find the sum total of the two dice
  
  #print statictics for dice rolls
  dice = 1
  for count in rolls:
    print(dice, ":", count)
    dice = dice + 1

if __name__ == '__main__':
  main()
