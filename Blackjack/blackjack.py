# Input: the table rule + dealer hand + you're hand
# Output: the best move to make (hit H, stand T, double D, split P, sournded S)

# basic strategy book

# stand on all 17's

stand_17 = {{}}


# hit soft 17

hits_soft_17 = {}


# Move
STR_MOVE = {"H": "Hit", "T": "Stand", "D": "Double", "P": "Split", "S": "Surrender"}

# Table rule

T_RULE = {"s": "Stand on all 17's", "h": "Hits soft 17"}


# TODO: use a msg lib
def die(msg):
    pass


# get both dealer and player hand
def get_hand():
    card = int(input(f"Enter a card: "))
    if not card in range(2, 12):
        die(f"Error: {card} is invalid")
    return card


# get the move to make (string)
def make_move(p_card, d_card, t_rule):

    move = ""

    # check if the count exceed 21
    count = 0
    for card in p_card:
        if card == 11 and count + 11 > 21:
            pass
        else:
            count += card
        if count > 21:
            return "to try again"

    # stand on all 17's
    if t_rule == "s":
        pass

    # hits soft 17
    else:
        pass

    return move


def main():
    print("Important: use 11 as the A card\n")
    player_hand = []
    dealer_up_card = 0
    table_rule = ""
    soft = False  # if there is a `A` or not

    # getting the user input
    table_rule = input("table rule (Stand on 17: s) (Hits soft 17: h):")
    if not table_rule.lower() in "s" or not table_rule.lower() in "h":
        die("Error: Entre a valid choice")

    print("Table rule is: ", T_RULE.get(table_rule))

    player_hand.append(get_hand())

    dealer_up_card = get_hand()

    player_hand.append(get_hand())

    mv = make_move(player_hand, dealer_up_card, table_rule)

    while mv == "Hit":
        player_hand.append(get_hand())
        mv = make_move(player_hand, dealer_up_card, table_rule)

    print(f"Best move is: {mv}")


if __name__ == "__main__":
    main()
