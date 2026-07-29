# Input: the table rule + dealer hand + you're hand
# Output: the best move to make (hit H, stand T, double D, split P, sournded S)

from typing import Dict, List, Union


UPCARDS: List[str] = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "A"]

Row = Dict[str, str]


def _row(*actions: str) -> Row:
    assert len(actions) == len(UPCARDS), "Every row needs exactly 10 actions"
    return dict(zip(UPCARDS, actions))


# Basic Strategy Books

# Dealer Stand on all 17's
CHART_2DECK_S17: Dict[str, Dict[str, Row]] = {
    "hard": {
        "5-7": _row("H", "H", "H", "H", "H", "H", "H", "H", "H", "H"),
        "8": _row("H", "H", "H", "H", "H", "H", "H", "H", "H", "H"),
        "9": _row("D", "D", "D", "D", "D", "H", "H", "H", "H", "H"),
        "10": _row("D", "D", "D", "D", "D", "D", "D", "D", "H", "H"),
        "11": _row("D", "D", "D", "D", "D", "D", "D", "D", "D", "D"),
        "12": _row("H", "H", "S", "S", "S", "H", "H", "H", "H", "H"),
        "13": _row("S", "S", "S", "S", "S", "H", "H", "H", "H", "H"),
        "14": _row("S", "S", "S", "S", "S", "H", "H", "H", "H", "H"),
        "15": _row("S", "S", "S", "S", "S", "H", "H", "H", "R", "H"),
        "16": _row("S", "S", "S", "S", "S", "H", "H", "H", "R", "R"),
        "17": _row("S", "S", "S", "S", "S", "S", "S", "S", "S", "S"),
    },
    "soft": {
        "A,2": _row("H", "H", "H", "D", "D", "H", "H", "H", "H", "H"),
        "A,3": _row("H", "H", "H", "D", "D", "H", "H", "H", "H", "H"),
        "A,4": _row("H", "H", "D", "D", "D", "H", "H", "H", "H", "H"),
        "A,5": _row("H", "H", "D", "D", "D", "H", "H", "H", "H", "H"),
        "A,6": _row("H", "D", "D", "D", "D", "H", "H", "H", "H", "H"),
        "A,7": _row("S", "DS", "DS", "DS", "DS", "S", "S", "H", "H", "H"),
        "A,8": _row("S", "S", "S", "S", "S", "S", "S", "S", "S", "S"),
        "A,9": _row("S", "S", "S", "S", "S", "S", "S", "S", "S", "S"),
    },
}

# Dealer Hits Soft 17

CHART_1DECK_H17: Dict[str, Dict[str, Row]] = {
    "hard": {
        "5-7": _row("H", "H", "H", "H", "H", "H", "H", "H", "H", "H"),
        "8": _row("H", "H", "H", "D", "D", "H", "H", "H", "H", "H"),
        "9": _row("D", "D", "D", "D", "D", "H", "H", "H", "H", "H"),
        "10": _row("D", "D", "D", "D", "D", "D", "D", "D", "H", "H"),
        "11": _row("D", "D", "D", "D", "D", "D", "D", "D", "D", "D"),
        "12": _row("H", "H", "S", "S", "S", "H", "H", "H", "H", "H"),
        "13": _row("S", "S", "S", "S", "S", "H", "H", "H", "H", "H"),
        "14": _row("S", "S", "S", "S", "S", "H", "H", "H", "H", "H"),
        "15": _row("S", "S", "S", "S", "S", "H", "H", "H", "R", "H"),
        "16": _row("S", "S", "S", "S", "S", "H", "H", "R", "R", "R"),
        "17": _row("S", "S", "S", "S", "S", "S", "S", "S", "S", "RS"),
    },
    "soft": {
        "A,2": _row("H", "H", "D", "D", "D", "H", "H", "H", "H", "H"),
        "A,3": _row("H", "H", "D", "D", "D", "H", "H", "H", "H", "H"),
        "A,4": _row("H", "H", "D", "D", "D", "H", "H", "H", "H", "H"),
        "A,5": _row("H", "H", "D", "D", "D", "H", "H", "H", "H", "H"),
        "A,6": _row("D", "D", "D", "D", "D", "H", "H", "H", "H", "H"),
        "A,7": _row("S", "DS", "DS", "DS", "DS", "S", "S", "H", "H", "H"),
        "A,8": _row("S", "S", "S", "S", "DS", "S", "S", "S", "S", "S"),
        "A,9": _row("S", "S", "S", "S", "S", "S", "S", "S", "S", "S"),
    },
}

CHARTS: Dict[str, Dict[str, Dict[str, Row]]] = {
    "2_decks_stand_soft_17": CHART_2DECK_S17,
    "1_deck_hit_soft_17": CHART_1DECK_H17,
}

# Move
STR_MOVE = {
    "H": "Hit",
    "T": "Stand",
    "D": "Double",
    "DS": "Double if allowed otherwise stand",
    "S": "Split",
    "R": "Surrender if allowed otherwise hit",
    "RS": "Surrender if allowed otherwise stand",
    "": "NONE",
}

# Table rule
T_RULE = {"s": "Stand on all 17's", "h": "Hits soft 17"}

# helpers


def die(msg):
    print(f"Error: {msg}")
    exit(1)


# TODO: fix the dict search
def is_valid_card(card: str):
    if "A" in card:
        if not card in CHARTS["2_decks_stand_soft_17"]["soft"].items():
            return False
    elif not card in CHARTS["2_decks_stand_soft_17"]["hard"].items():
        return False

    return True


# get user hand
def get_hand():
    card = str(input(f"Enter the hand: "))
    if not is_valid_card(card):
        die(f"Error: {card} is invalid")
    return card


# lockup function
def get_action(
    chart: str, hand_type: str, player_total: str, dealer_upcard: Union[str, int]
):

    upcard = str(dealer_upcard)
    return CHARTS[chart][hand_type][player_total][upcard]


# get the move to make (string)
def make_move(p_card, d_card, t_rule):
    move = ""

    if "A" in p_card:
        hand_type = "soft"
    else:
        hand_type = "hard"

    if t_rule == "stand":
        move = get_action("2_decks_stand_soft_17", hand_type, p_card, d_card)

    # hits soft 17
    else:
        move = get_action("2_deck_hit_soft_17", hand_type, p_card, d_card)

    return STR_MOVE.get(move)


def main():
    print(
        "Repsect this card format:\nif u have a totale that is bteween 5 to 7 entre `5-7`\nif u have Aice use A,x ex: A,6"
    )

    # getting the user input
    table_rule = str(
        input("table rule (Stand on 17: stand) (Hits soft 17: hit): ").strip().lower()
    )
    if table_rule != "stand" or table_rule != "hit":
        die("Entre a valid choice")

    print("\nTable rule is: ", T_RULE.get(table_rule))

    player_hand = get_hand()

    dealer_up_card = get_hand()

    mv = make_move(player_hand, dealer_up_card, table_rule)

    while mv == "Hit":
        player_hand = get_hand()
        mv = make_move(player_hand, dealer_up_card, table_rule)

    print(f"Best move: {mv}")


if __name__ == "__main__":
    main()
