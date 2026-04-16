""""""


def run():
    """Run the game!"""
    print("Welcome to Tic Tac Toe")
    playingfield = [" "," "," "," "," "," "," "," "," "]
    print_playingfield(playingfield)
    input_playingfield(playingfield, "X")
    print_playingfield(playingfield)


def print_playingfield(playingfield):
    print("  1   2   3 ")
    print(f"A {playingfield[0]} | {playingfield[1]} | {playingfield[2]} ")
    print(f"B {playingfield[3]} | {playingfield[4]} | {playingfield[5]} ")
    print(f"C {playingfield[6]} | {playingfield[7]} | {playingfield[8]} ")


def input_playingfield(playingfield, player):
    yourturn = True
    while yourturn:
        user_input = input("Player 1's turn: ")
        if user_input == "A1":
            if playingfield[0] == " ":
                playingfield[0] = player
                yourturn = False
            else :
                print("field blocked")
        elif user_input == "A2":
            if playingfield[1] == " ":
                playingfield[1] = player
                yourturn = False
            else :
                print("field blocked")
        elif user_input == "A3":
            if playingfield[2] == " ":
                playingfield[2] = player
                yourturn = False
            else :
                print("field blocked")
        elif user_input == "B1":
            if playingfield[3] == " ":
                playingfield[3] = player
                yourturn = False
            else :
                print("field blocked")
        elif user_input == "B2":
            if playingfield[4] == " ":
                playingfield[4] = player
                yourturn = False
            else :
                print("field blocked")
        elif user_input == "B3":
            if playingfield[5] == " ":
                playingfield[5] = player
                yourturn = False
            else :
                print("field blocked")
        elif user_input == "C1":
            if playingfield[6] == " ":
                playingfield[6] = player
                yourturn = False
            else :
                print("field blocked")
        elif user_input == "C2":
            if playingfield[7] == " ":
                playingfield[7] = player
                yourturn = False
            else :
                print("field blocked")
        elif user_input == "C3":
            if playingfield[8] == " ":
                playingfield[8] = player
                yourturn = False
            else :
                print("field blocked")
        else:
            print("invalid input")


if __name__ == '__main__':
    run()
