import time

def play_game():
    print("It is November 11th, 2011. You wake up in your bed craving to play Skyrim.")
    print("You have one of the most important pitch meetings in your life in the morning pitching the idea for Bassman 4: The Gaping.")
    print("What do you do?")
    print("1. Wake up and play Skyrim.")
    print("2. Go back to sleep and wake up well rested for work.")

    choice = input("Enter your choice (1 or 2): ")

    if choice == "1":
        play_skyrim()
    elif choice == "2":
        rest_for_work()
    else:
        print("Invalid choice. Please try again.")
        play_game()

def play_skyrim():
    print("You go downstairs to play Skyrim.")
    print("You grab a cup of soda from the Mt.Dew Dispenser.")
    print("As you walk past your elegant kitchen, you hear a robber.")

    choice = input("What do you do? (1 or 2): ")

    if choice == "1":
        print("You bum rush the robber.")
        print("The robber turns around and shoots you in the face. You die.")
        game_over()
    elif choice == "2":
        print("You run to your man cave and lock yourself behind a 5-inch thick VAULT door.")
        print("The robber rummages upstairs.")
        call_police()

def rest_for_work():
    print("You go back to sleep to wake up well-rested for work.")
    print("You suddenly wake up with a gun being pressed into your mouth.")
    print("The robber talks to you in a heavy Boston accent: 'You got anything valuable in this domicile?'")

    choice = input("What do you say? (1, 2, 3, 4, or 5): ")

    if choice == "1":
        print("The robber asks you to take him to the room with the gaming PC.")
        call_police()
    elif choice == "2":
        print("The robber refuses the Xbox 360 and asks what else you have.")
        choice = input("What else do you say? (1, 3, 4, or 5): ")
        if choice == "1":
            print("The robber asks you to take him to the room with the gaming PC.")
            call_police()
        elif choice == "3":
            print("The robber comments on your reference to Batman and asks what else you have.")
            choice = input("What else do you say? (1, 4, or 5): ")
            if choice == "1":
                print("The robber asks you to take him to the room with the gaming PC.")
                call_police()
            elif choice == "4":
                print("The robber refuses to watch that movie and asks what else you have.")
                choice = input("What else do you say? (1 or 5): ")
                if choice == "1":
                    print("The robber asks you to take him to the room with the gaming PC.")
                    call_police()
                elif choice == "5":
                    print("The robber gets angry and shoots you. You die.")
                    game_over()
                else:
                    invalid_choice()
            else:
                invalid_choice()
        elif choice == "4":
            print("The robber refuses to watch that movie and asks what else you have.")
            choice = input("What else do you say? (1 or 5): ")
            if choice == "1":
                print("The robber asks you to take him to the room with the gaming PC.")
                call_police()
            elif choice == "5":
                print("The robber gets angry and shoots you. You die.")
                game_over()
            else:
                invalid_choice()
        else:
            invalid_choice()
    elif choice == "3":
        print("The robber comments on your choice and asks what else you have.")
        choice = input("What else do you say? (1, 2, 4, or 5): ")
        if choice == "1":
            print("The robber asks you to take him to the room with the gaming PC.")
            call_police()
        elif choice == "2":
            print("The robber refuses the Xbox 360 and asks what else you have.")
            choice = input("What else do you say? (1, 4, or 5): ")
            if choice == "1":
                print("The robber asks you to take him to the room with the gaming PC.")
                call_police()
            elif choice == "4":
                print("The robber refuses to watch that movie and asks what else you have.")
                choice = input("What else do you say? (1 or 5): ")
                if choice == "1":
                    print("The robber asks you to take him to the room with the gaming PC.")
                    call_police()
                elif choice == "5":
                    print("The robber gets angry and shoots you. You die.")
                    game_over()
                else:
                    invalid_choice()
            else:
                invalid_choice()
        elif choice == "4":
            print("The robber refuses to watch that movie and asks what else you have.")
            choice = input("What else do you say? (1 or 5): ")
            if choice == "1":
                print("The robber asks you to take him to the room with the gaming PC.")
                call_police()
            elif choice == "5":
                print("The robber gets angry and shoots you. You die.")
                game_over()
            else:
                invalid_choice()
        elif choice == "5":
            print("The robber gets angry and shoots you. You die.")
            game_over()
        else:
            invalid_choice()
    elif choice == "4":
        print("You tell the robber to kill himself.")
        print("You suddenly find yourself in a field of wheat with Russell Crowe dressed like a gladiator.")
        print("But it turns out you're actually in Hell. You died.")
        game_over()
    else:
        invalid_choice()

def call_police():
    print("You call the police and turn on your PC to start your FIRST playthrough of Skyrim.")
    print("The unnecessary cutscene on the wagon plays.")
    print("You hear the police enter your house.")

    time.sleep(2)  # Simulating some delay for dramatic effect

    print("There is screaming, and gunshots ring out.")
    print("Your phone rings. It's the 911 dispatch lady.")

    input("Press Enter to continue...")

    print("\n911 Dispatch: 'The intruder has injured officers and taken them hostage.")
    print("Do not make noise and stay where you are until everything is clear.'")

    # Continue the game here...

def invalid_choice():
    print("Invalid choice. Please try again.")
    play_game()

def game_over():
    print("Game over.")

play_game()
