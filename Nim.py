import random #random
import time #time

def print_heading(heading_text): # optional feature
    """Prints a heading in a box of '#' characters."""
    width = 80
    print("#" * width)
    print(heading_text.center(width))
    print("#" * width)

def display_sticks(sticks_list):
    """Display the current state of sticks."""
    print("\n Generating sticks... Get Ready! \n")
    time.sleep(2)  # time delay for generating sticks - improves game flow.
    max_sticks = max(sticks_list)
    for i, sticks in enumerate(sticks_list, start=1):
        row_display = "|" * sticks
        print("Row {}: {}".format(i, row_display.center(max_sticks)))
    print("\n Okay, Let's go! \n") # one space away from left margin & using \n to add some visual separation.
    time.sleep(1) 

def print_move(current_player, row, stick_quantity): # required function
    """Print a player's move."""
    if stick_quantity == 1:
        print("\n {} takes {} stick from row {}.".format(current_player, stick_quantity, row))
        time.sleep(1) 
    else:
        print("\n {} takes {} sticks from row {}.".format(current_player, stick_quantity, row))
        time.sleep(1) 

def game_over(sticks_list):
    """Determine if the game has ended.""" # games ends when 0 sticks remain.
    return sum(sticks_list) == 0

def return_scores(player_score, nimby_score): # I might make the box fancy if there's time 
    """Returns a formatted score box.""" 
    player_score_str = "Your current score is: " + str(player_score)
    nim_score_str = "Nimby's current score is: " + str(nimby_score)
    return player_score_str + "\n" + nim_score_str

def player_move(sticks_list, player_name):
    """Handle player's move."""
    valid_move = False
    while not valid_move:
        try:
            print(" It's your turn to move... \n")
            row = int(input("Choose a row: ")) - 1
            stick_quantity = int(input("How many sticks do you want to take? "))
            if 0 <= row < len(sticks_list) and 0 < stick_quantity <= sticks_list[row]:
                sticks_list[row] -= stick_quantity
                print_move(player_name, row + 1, stick_quantity)
                valid_move = True
            else:
                print("Invalid move, try again.")
        except ValueError:
            print("Please enter valid numbers.")
    return sticks_list

def nimby_move(sticks_list):
    """Nimby's move logic."""
    print("\n Nimby is thinking... \n")
    time.sleep(3)  # shhhhh nimby is thinking <3
    rows_with_sticks = [index for index, sticks in enumerate(sticks_list) if sticks > 0]
    chosen_row = random.choice(rows_with_sticks)
    stick_quantity = random.randint(1, sticks_list[chosen_row])
    sticks_list[chosen_row] -= stick_quantity
    print_move("Nimby", chosen_row + 1, stick_quantity)
    return sticks_list

def play_nim():
    """Main game function."""
    print_heading("Welcome to Nim")
    
    player_name = input("\n My name is Nimby. What's your name? (Type 'exit' to end.): ") # initial player interaction
    if player_name.lower() == 'exit':
        print("Goodbye!")
        time.sleep(5)
        return
    print("\n Hello " + player_name + "! let's play!")
    
    sticks_list = [1, 3, 5, 7]
    player_score, nimby_score = 0, 0
    
    while True: # randomly choose first player
        current_player = player_name if random.randint(0, 1) == 0 else "Nimby"
        print("\n {}, you get to start. \n".format(current_player))

        while not game_over(sticks_list):
            display_sticks(sticks_list)
            if current_player == player_name:
                sticks_list = player_move(sticks_list, player_name)
                current_player = "Nimby" if not game_over(sticks_list) else player_name
            else:
                sticks_list = nimby_move(sticks_list)
                current_player = player_name if not game_over(sticks_list) else "Nimby"

        if current_player == player_name:
            player_score += 1
        else:
            nimby_score += 1

        print("\n Game over! \n It looks like we have a winner! \n\n W I N N E R \n\n {} gets the point!\n".format(current_player)) # announces ~W I N N E R~ 
        print(return_scores(player_score,        nimby_score))
        
        play_again = input("\n Do you want to play again? (yes/no): ").lower()
        if play_again != "yes":
            print("\n Final Scores:")
            print(return_scores(player_score, nimby_score))
            time.sleep(3)
            break
        else:
            print("Goodbye!")
            time.sleep(5)
            sticks_list = [1, 3, 5, 7]  # Resets the game

if __name__ == "__main__":
    play_nim()


# Fin
