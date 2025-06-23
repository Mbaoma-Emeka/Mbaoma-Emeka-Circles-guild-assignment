import random
def roll_dice(sides=6):
    return random.randint(1, sides)
def main():
    print("Dice Simulator")
    print("Press Enter to roll the dice or type 'q' to quit.")
  while True:
        user_input = input("Roll the dice? ")
        if user_input.lower() == 'q':
            print("Thanks for playing. Goodbye!")
            break
        result = roll_dice()
        print(f"You rolled a {result}!")
if __name__ == "__main__":
    main()
