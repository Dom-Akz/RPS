"""
From a given board (full 5 card) it give u the best possible hand rank
"""

from pokerlib import HandParser
from pokerlib.enums import Rank, Suit
from itertools import combinations, product


RANK = {
    1: "HIGHCARD",
    2: "PAIR",
    3: "TOWPAIR",
    4: "THREEOFAKIND",
    5: "STRIGHT",
    6: "FLUSH",
    7: "FULLHOUSE",
    8: "FOUROFAKIND",
    9: "STRIGHTFLUSH",
    10: "ROYALFLUSH",
}

STR_RANK = {
    "2": Rank.TWO,
    "3": Rank.THREE,
    "4": Rank.FOUR,
    "5": Rank.FIVE,
    "6": Rank.SIX,
    "7": Rank.SEVEN,
    "8": Rank.EIGHT,
    "9": Rank.NINE,
    "T": Rank.TEN,
    "J": Rank.JACK,
    "Q": Rank.QUEEN,
    "K": Rank.KING,
    "A": Rank.ACE,
}

STR_SUIT = {
    "s": Suit.SPADE,
    "c": Suit.CLUB,
    "d": Suit.DIAMOND,
    "h": Suit.HEART,
}


# generate all possible combos excluding the board card
def get_all_combos(board):
    board_set = set(board)
    remaining_deck = [c for c in product(Rank, Suit) if c not in board_set]
    return tuple(combinations(remaining_deck, 2))


# return the max hand rank possible base on the board (string)
def max_rank(board):
    max = 1  # min hand rank

    combos = get_all_combos(board)

    # test each hand combo with the bord
    for cm in combos:
        hand = HandParser(list(cm) + board)
        for k, v in RANK.items():
            if hand.handenum.name == v:
                if max < k:
                    max = k
                    break

    return RANK.get(max)


# validate the input card
def _iscardvalid(card):
    rank, suit = card.split(",")
    if rank in STR_RANK and suit in STR_SUIT:
        return True
    return False


def main():
    print("Card form: rank,suit (ex 2,s or J,h), note that 10 is represent as T")
    # get the borad card (5)
    nb_card = 0
    card = ""
    board = []
    while nb_card < 5:
        card = input(f"Enter card {nb_card + 1}: ")
        if not _iscardvalid(card):
            print(f"Invalid card: {card}")
            exit(1)
        else:
            rank, suit = card.split(",")
            board.append((STR_RANK[rank], STR_SUIT[suit]))
            nb_card += 1

    print(max_rank(board))


if __name__ == "__main__":
    main()
