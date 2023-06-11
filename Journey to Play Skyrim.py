import curses
import random

def main(stdscr):
    # Set up the screen
    curses.curs_set(0)
    stdscr.nodelay(1)
    stdscr.timeout(100)
    stdscr.clear()
    height, width = stdscr.getmaxyx()
    center_y = height // 2
    center_x = width // 2
    output_win = curses.newwin(center_y - 1, width, 0, 0)
    input_win = curses.newwin(1, width, center_y, 0)
    input_win.keypad(1)

    # Call the existing code inside the main loop
    wake_up_play_skyrim(output_win, input_win)

    # Clean up the windows and end the game
    curses.curs_set(1)
    input_win.keypad(0)
    curses.echo()
    curses.endwin()

def wake_up_play_skyrim(output_win, input_win):
    output_win.addstr("It is November 11th, 2011. You wake up in your bed, craving to play Skyrim.\n")
    output_win.addstr("You have one of the most important pitch meetings in your life in the morning, pitching the idea for Bassman 4: The Gaping.\n")
    output_win.addstr("Do you answer your Skyrim Calling or do you rest your brain for the big day ahead?\n")
    output_win.addstr("1. Wake up and play Skyrim.\n")
    output_win.addstr("2. Go back to sleep and wake up well-rested for work.\n")
    output_win.refresh()

    choice = input_win.getstr().decode()

    if choice.lower() == "skyrim":
        play_skyrim(output_win, input_win)

    elif choice.lower() == "sleep":
        go_back_to_sleep(output_win, input_win)

    else:
        output_win.addstr("Invalid choice. Please try again.\n")
        wake_up_play_skyrim(output_win, input_win)

def play_skyrim(output_win, input_win):
    output_win.addstr("You decide to wake up and play Skyrim.\n")
    output_win.addstr("You go down the stairs of your mansion, grab a cup of soda from the Mt. Dew dispenser, and walk past your elegant kitchen.\n")
    output_win.addstr("Suddenly, you hear a robber in your house. He is facing away from you.\n")
    output_win.addstr("What do you do?\n")
    output_win.addstr("1. Run away to your man cave and lock yourself behind the 5-inch thick VAULT door.\n")
    output_win.addstr("2. Bum rush the robber.\n")
    output_win.refresh()

    choice = input_win.getstr().decode()

    if choice.lower() == "run":
        output_win.addstr("You run to your man cave and lock yourself behind the vault door.\n")
        output_win.addstr("The robber rummages upstairs while you call the police.\n")
        output_win.addstr("You turn on your PC and start a new playthrough of Skyrim.\n")
        output_win.addstr("Suddenly, your phone rings. It's the 911 dispatch lady.\n")
        output_win.addstr("'The intruder has injured officers and taken them hostage. Do not make noise and stay where you are until everything is clear,' she says.\n")
        output_win.addstr("You continue playing Skyrim, waiting for the situation to resolve.\n")
        output_win.refresh()

    elif choice.lower() == "bum rush":
        output_win.addstr("You bum rush the robber. Your flat feet slap on the ground like a duck trying to mate as you get closer.\n")
        output_win.addstr("The intruder turns around and discharges his weapon, hitting you square in the face.\n")
        output_win.refresh()
        russell_crowe_sequence(output_win, input_win)

    else:
        output_win.addstr("Invalid choice. Please try again.\n")
        play_skyrim(output_win, input_win)

def go_back_to_sleep(output_win, input_win):
    output_win.addstr("You decide to go back to sleep and wake up well-rested for work.\n")
    output_win.addstr("As you drift off to sleep, you wake up in the middle of the night.\n")
    output_win.addstr("You have two choices.\n")
    output_win.addstr("1. Wake up and play Skyrim.\n")
    output_win.addstr("2. Go back to sleep.\n")
    output_win.refresh()

    choice = input_win.getstr().decode()

    if choice.lower() == "skyrim":
        play_skyrim(output_win, input_win)

    elif choice.lower() == "sleep":
        wake_up_with_gun_in_mouth(output_win, input_win)

    else:
        output_win.addstr("Invalid choice. Please try again.\n")
        go_back_to_sleep(output_win, input_win)

def wake_up_with_gun_in_mouth(output_win, input_win):
    output_win.addstr("You wake up with a gun being pressed into your mouth.\n")
    output_win.addstr("The robber talks to you in a heavy Boston accent, 'You got anything valuable in this domicile?'\n")
    output_win.addstr("He moves the gun just enough for you to mutter.\n")
    output_win.addstr("What do you say?\n")
    output_win.addstr("1. Gaming PC\n")
    output_win.addstr("2. Xbox 360\n")
    output_win.addstr("3. Mother's pearls\n")
    output_win.addstr("4. 'Kill yourself'\n")
    output_win.addstr("5. Passion of the Christ directed by Mel Gibson on Blu-ray\n")
    output_win.refresh()

    choice = input_win.getstr().decode()

    if choice.lower() == "gaming pc":
        output_win.addstr("You tell the robber about your gaming PC.\n")
        output_win.addstr("He asks you to take him to the room that has it.\n")
        output_win.refresh()
        russell_crowe_sequence(output_win, input_win)

    elif choice.lower() == "xbox 360":
        output_win.addstr("You tell the robber about your Xbox 360.\n")
        output_win.addstr("'Hell no, that thing is gonna be showing me red rings before I even get to sell it off to some poor bastard,' he says.\n")
        output_win.addstr("He asks what else you have.\n")
        output_win.addstr("1. Mother's pearls\n")
        output_win.addstr("2. 'Kill yourself'\n")
        output_win.refresh()
        russell_crowe_sequence(output_win, input_win)

    elif choice.lower() == "pearls":
        output_win.addstr("You tell the robber about your mother's pearls.\n")
        output_win.addstr("'I didn't know you was Batman,' he exclaims.\n")
        output_win.addstr("He asks what else you have.\n")
        output_win.addstr("1. Gaming PC\n")
        output_win.addstr("2. 'Kill yourself'\n")
        output_win.refresh()
        russell_crowe_sequence(output_win, input_win)

    elif choice.lower() == "kill":
        russell_crowe_sequence(output_win, input_win)

    elif choice.lower() == "passion":
        output_win.addstr("You tell the robber about Passion of the Christ directed by Mel Gibson on Blu-ray.\n")
        output_win.addstr("'That guy hates a certain race that I like... I don't consume his art,' he says.\n")
        output_win.addstr("He asks what else you have.\n")
        output_win.addstr("1. Gaming PC\n")
        output_win.addstr("2. 'Kill yourself'\n")
        output_win.refresh()
        russell_crowe_sequence(output_win, input_win)

    else:
        output_win.addstr("Invalid choice. Please try again.\n")
        wake_up_with_gun_in_mouth(output_win, input_win)

def russell_crowe_sequence(output_win, input_win):
    output_win.addstr("The world around you begins to distort and fade away.\n")
    output_win.addstr("You find yourself standing in a beautiful field, surrounded by golden wheat.\n")
    output_win.addstr("In the distance, you spot Russell Crowe dressed like a gladiator, staring at you longingly.\n")
    output_win.addstr("As you approach him, he and all the emperors of Rome embrace you, praising your work as an alpha male, an example of stoicism, and a martyr to be remembered for generations.\n")
    output_win.addstr("But suddenly, the field transforms into a nightmarish scene of fire and brimstone.\n")
    output_win.addstr("You realize that your choices have led you to Hell.\n")
    output_win.addstr("Game over.\n")
    output_win.refresh()
    wake_up_play_skyrim(output_win, input_win)

# Call the main function to start the game
curses.wrapper(main)
