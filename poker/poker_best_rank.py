from pokerlib import HandParser
from pokerlib.enums import Rank, Suit


RANK = {
    10: "HIGHCARD",
    9: "PAIR",
    8: "TOWPAIR",
    7: "THREEOFAKIND",
    6: "STRIGHT",
    5: "FLUSH",
    4: "FULLHOUSE",
    3: "FOUROFAKIND",
    2: "STRIGHTFLUSH",
    1: "ROYALFLUSH",
}


# return the max rank a hand can have base on the board (string)
def max_rank(board):
    pass


# validate the input card
def _iscardvalid(card):
    pass


def main():
    # get the borad card (5)
    nb_card = 0
    card = ""
    while nb_card < 5:
        card = input(f"Enter card {card}: ")
        if not _iscardvalid(card):
            print(f"Invalid card: {card}")
            exit(1)
        else:
            pass
            # add the card to the board
            nb_card += 1

    print(max_rank)


if __name__ == "__main__":
    main()
