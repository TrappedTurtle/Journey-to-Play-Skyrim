import time

def play_game():
    print("It is November 11th, 2011. You wake up in your bed craving to play Skyrim.")
    print("You have one of the most important pitch meetings in your life in the morning pitching the idea for Bassman 4: The Gaping.")
    print("What do you do?")
    print("1. Wake up and play Skyrim.")
    print("2. Go back to sleep and wake up well-rested for work.")

    choice = input("Enter your choice (1 or 2): ")

    if choice == "1":
        play_skyrim()
    elif choice == "2":
        go_to_sleep()
    else:
        print("Invalid choice. Please try again.")
        play_game()

def go_to_sleep():
    print("You decide to go back to sleep.")
    print("Before that, you have a couple of options.")
    print("1. Drink some choccy milk before sleeping.")
    print("2. Go to sleep without any assistance.")
    print("3. Take sleep medication (RX Fake Brand Name).")

    choice = input("Enter your choice (1, 2, or 3): ")

    if choice == "1":
        print("Your stomach rumbles.")
        choccy_milk()
    elif choice == "2":
        wake_up_hostage()
    elif choice == "3":
        sleep_medication()
    else:
        print("Invalid choice. Please try again.")
        go_to_sleep()

def choccy_milk():
    print("You drink some choccy milk before sleeping.")
    print("Your stomach rumbles with the milky goodness.")
    print("You fall asleep and dream of epic adventures.")
    print("You wake up in the middle of the night.")
    print("You have two choices:")
    print("1. Go back to sleep.")
    print("2. Play Skyrim.")

    choice = input("Enter your choice (1 or 2): ")

    if choice == "1":
        wake_up_hostage()
    elif choice == "2":
        play_skyrim()
    else:
        print("Invalid choice. Please try again.")
        choccy_milk()

def sleep_medication():
    print("You take the sleep medication (RX Fake Brand Name).")
    print("You fall asleep peacefully.")
    print("When you wake up, you find yourself in your neighbor's house, covered in blood with a knife in your hand.")
    print("Written in blood on the wall is 'OJ WAS RIGHT.'")
    print("Game over.")
    play_game()

def play_skyrim():
    print("You go downstairs to play Skyrim.")
    print("You grab a cup of soda from the Mt.Dew Dispenser.")
    print("As you walk past your elegant kitchen, you hear a robber.")

    choice = input("What do you do? (1 or 2): ")

    if choice == "1":
        print("You bum rush the robber.")
        print("The robber turns around and shoots you in the face. You die.")
        russell_crowe_sequence()
        play_game()
    elif choice == "2":
        print("You run to your man cave and lock yourself behind a 5-inch thick VAULT door.")
        print("The robber rummages upstairs.")
        call_police()
    else:
        print("Invalid choice. Please try again.")
        play_skyrim()

def wake_up_hostage():
    print("You wake up in the middle of the night.")
    print("A masked man is standing over you, pressing a gun into your mouth.")
    print("The robber talks to you in a heavy Boston accent, 'You got anything valuable in this domicile?'")

    choice = input("What do you say? (1, 2, 3, or 4): ")

    if choice == "1":
        print("The robber asks you to take him to the room with the gaming PC.")
        call_police()
    elif choice == "2":
        print("The robber says, 'Hell no, that thing is gonna be showing me red rings before I even get to sell it off to some poor bastard.'")
        print("The robber asks, 'What else do you have?'")
        choice = input("What do you say? (1 or 4): ")
        if choice == "1":
            print("The robber asks you to take him to the room with the gaming PC.")
            call_police()
        elif choice == "4":
            print("The robber says, 'That guy hates a certain race that I like... I don't consume his art.'")
            print("The robber asks, 'What else do you have?'")
            choice = input("What do you say? (1 or 5): ")
            if choice == "1":
                print("The robber asks you to take him to the room with the gaming PC.")
                call_police()
            elif choice == "5":
                russell_crowe_sequence()
                play_game()
            else:
                print("Invalid choice. Please try again.")
                wake_up_hostage()
        else:
            print("Invalid choice. Please try again.")
            wake_up_hostage()
    elif choice == "3":
        print("The robber says, 'I didn't know you was Batman.'")
        print("The robber asks, 'What else do you have?'")
        choice = input("What do you say? (1 or 4): ")
        if choice == "1":
            print("The robber asks you to take him to the room with the gaming PC.")
            call_police()
        elif choice == "4":
            print("The robber says, 'That guy hates a certain race that I like... I don't consume his art.'")
            print("The robber asks, 'What else do you have?'")
            choice = input("What do you say? (1 or 5): ")
            if choice == "1":
                print("The robber asks you to take him to the room with the gaming PC.")
                call_police()
            elif choice == "5":
                russell_crowe_sequence()
                play_game()
            else:
                print("Invalid choice. Please try again.")
                wake_up_hostage()
        else:
            print("Invalid choice. Please try again.")
            wake_up_hostage()
    elif choice == "4":
        russell_crowe_sequence()
        play_game()
    else:
        print("Invalid choice. Please try again.")
        wake_up_hostage()

def russell_crowe_sequence():
    print("As you utter the words, 'Attempt Die,' everything fades away.")
    print("You have a sudden vision.")
    print("Russell Crowe appears before you in a field, dressed as Maximus from Gladiator.")
    print("He looks at you with intense eyes and says, 'Your decisions have led you to this place.'")
    print("You find yourself in a dark, fiery landscape.")
    print("Tormented souls surround you, and you can feel the heat of the flames.")
    print("You realize that you are in hell, a consequence of your actions.")
    print("The vision fades, and you find yourself back in the waking world.")
    print("Game over.")
    play_game()

def call_police():
    print("You discreetly call the police and inform them about the robbery in progress.")
    print("You provide them with your address and details about the situation.")
    print("They assure you that help is on the way and advise you to stay hidden until the police arrive.")
    print("While waiting, you hear the sound of the robber rummaging upstairs.")
    print("You decide to turn on your PC and start a new playthrough of Skyrim to distract yourself.")
    print("As the game loads, you hear the police enter your house.")
    print("There are screams and gunshots ringing out.")
    print("Your character in Skyrim is about to approach the chopping block.")
    print("Suddenly, your phone rings. It's the 911 dispatch lady.")
    print("'The intruder has injured officers and taken them hostage. Do not make noise and stay where you are until everything is clear.'")
    print("What do you do?")
    print("1. Stay hidden and wait for the situation to resolve.")
    print("2. Attempt to escape through the back door.")
    choice = input("Enter your choice (1 or 2): ")

    if choice == "1":
        print("You follow the dispatcher's instructions and stay hidden, hoping for a safe resolution.")
        print("After a tense wait, you hear the sound of sirens and the police storming your house.")
        print("The robber is apprehended, and the officers are freed.")
        print("Although the situation was terrifying, you are relieved that everyone is safe.")
        print("Congratulations! You survived the robbery.")
        play_game()
    elif choice == "2":
        print("You make a daring escape through the back door, fleeing from your own home.")
        print("While you manage to get away, you live with the constant fear and paranoia of being pursued.")
        print("Your life takes a dark turn as you become a fugitive, constantly on the run.")
        print("The story ends here, with your future uncertain and your freedom compromised.")
        print("Game over.")
        play_game()
    else:
        print("Invalid choice. Please try again.")
        call_police()

play_game()

