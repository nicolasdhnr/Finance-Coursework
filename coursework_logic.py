
def calculate_probability(total_cards, spades, hearts, diamonds, clubs):
    # Calculate the probability of winning the game for each suit (even if its just an approximation) with num cards / total cards
    # The probability of winning the game is the number of cards remaining in the deck of that suit / the total number of cards remaining in the deck

    return (spades / total_cards, hearts / total_cards, diamonds / total_cards, clubs / total_cards)



if __name__ == "__main__":
    print(calculate_probability(52, 13, 13, 13, 13))


