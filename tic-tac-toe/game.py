""""""


def run():
    """Run the game!"""
    print("Welcome to Tic Tac Toe")
    playingfield = [" "," "," "," "," "," "," "," "," "]
    player = "X"
    game_running = True
    print_playingfield(playingfield)
    while game_running:
        input_playingfield(playingfield, player)
        print_playingfield(playingfield)
        game_running = check_playingfield(playingfield, player, game_running)
        if player == "X":
            player = "O"
        else:
            player = "X"


def print_playingfield(playingfield):
    print("  1   2   3 ")
    print(f"A {playingfield[0]} | {playingfield[1]} | {playingfield[2]} ")
    print(f"B {playingfield[3]} | {playingfield[4]} | {playingfield[5]} ")
    print(f"C {playingfield[6]} | {playingfield[7]} | {playingfield[8]} ")


def input_playingfield(playingfield, player):
    yourturn = True
    while yourturn:
        user_input = input(f"{player}'s turn: ")
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


def check_playingfield(playingfield, player, game_running):
    if playingfield[0] == playingfield[1] == playingfield[2] == "X":
        print("X won!")
        return False
    elif playingfield[0] == playingfield[1] == playingfield[2] == "O":
        print("O won!")
        return False
    elif playingfield[3] == playingfield[4] == playingfield[5] == "X":
        print("X won!")
        return False
    elif playingfield[3] == playingfield[4] == playingfield[5] == "O":
        print("O won!")
        return False
    elif playingfield[6] == playingfield[7] == playingfield[8] == "X":
        print("X won!")
        return False
    elif playingfield[6] == playingfield[7] == playingfield[8] == "O":
        print("O won!")
        return False
    elif playingfield[0] == playingfield[4] == playingfield[8] == "X":
        print("X won!")
        return False
    elif playingfield[0] == playingfield[4] == playingfield[8] == "O":
        print("O won!")
        return False
    elif playingfield[2] == playingfield[4] == playingfield[6] == "X":
        print("X won!")
        return False
    elif playingfield[2] == playingfield[4] == playingfield[6] == "O":
        print("O won!")
        return False
    elif playingfield[0] == playingfield[3] == playingfield[6] == "X":
        print("X won!")
        return False
    elif playingfield[0] == playingfield[3] == playingfield[6] == "O":
        print("O won!")
        return False
    elif playingfield[1] == playingfield[4] == playingfield[7] == "X":
        print("X won!")
        return False
    elif playingfield[1] == playingfield[4] == playingfield[7] == "O":
        print("O won!")
        return False
    elif playingfield[2] == playingfield[5] == playingfield[8] == "X":
        print("X won!")
        return False
    elif playingfield[2] == playingfield[5] == playingfield[8] == "O":
        print("O won!")
        return False
    elif playingfield[0] != " " and playingfield[1] != " " and playingfield[2] != " " and playingfield[3] != " " and playingfield[4] != " " and playingfield[5] != " " and playingfield[6] != " " and playingfield[7] != " " and playingfield[8] != " ":
        print("it is a tie!")
        return False
    else:
        return True


if __name__ == '__main__':
    run()