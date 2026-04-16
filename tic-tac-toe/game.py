""""""


def run():
    """Run the game!"""
    print("Welcome to Tic Tac Toe")
    print("Would you like to be X or O")
    playingfield = [" "," "," "," "," "," "," "," "," "]
    print_playingfield(playingfield)


def print_playingfield(playingfield):
    print("  1   2   3 ")
    print(f"A {playingfield[0]} | {playingfield[1]} | {playingfield[2]} ")
    print(f"B {playingfield[3]} | {playingfield[4]} | {playingfield[5]} ")
    print(f"C {playingfield[6]} | {playingfield[7]} | {playingfield[8]} ")


if __name__ == '__main__':
    run()
