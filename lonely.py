state = "Iron Man"

while True:
    if state == "Iron Man":
        print("You are Iron Man")

        while True:
            event = input("What do you do?")
            event = event.lower()

            if event == "shield" or event == "hammer":
                if event == "shield":
                    state = "Captain America"
                else:
                    state = "Thor"
                break
            else:
                print("Invalid Input.")

    elif state == "Captain America":
        print("You are Captain America")

        while True:
            event = input("What do you do?")
            event = event.lower()

            if event == "web" or event == "armor":
                if event == "web":
                    state = "Spider-Man"
                else:
                    state = "Iron Man"
                break
            else:
                print("Invalid Input.")

    elif state == "Thor":
        print("You are Thor.")

        while True:
            event = input("What do you do?")
            event = event.lower()

            if event == "shield" or event == "web":
                if event == "shield":
                    state = "Captain America"
                else:
                    state = "Spider-Man"
                break
            else:
                print("Invalid Input.")

    elif state == "Spider-Man":
        print("You are Spider-Man.")

        while True:
            event = input("What do you do?")
            event = event.lower()

            if event == "armor" or event == "hammer":
                if event == "armor":
                    state = "Iron Man"
                else:
                    state = "Thor"
                break
            else:
                print("Invalid Input.")
