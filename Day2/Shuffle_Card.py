# Shuffle Card
# Shuffle Card : Create a deck of cards with “card_Point” List and with “card_sign” List.
# card_point = ['A','K','Q','J','2','3','4','5','6','7','8','9','10'] card_signs =['HEART','CLUB','DIAMOND','SPADE'] Cards will have names like ‘Diamond-7’, ‘Spade-Q’, …

# Check the positions of all the Kings in the deck and print the same. Shuffle the card and then check the positions again.

# Note : use shuffle function of random module to shuffle


import random

card_point = ['A', 'K', 'Q', 'J', '2', '3', '4',
              '5', '6', '7', '8', '9', '10']

card_signs = ['HEART', 'CLUB', 'DIAMOND', 'SPADE']

# Create deck
deck = [
    sign + "-" + point
    for sign in card_signs
    for point in card_point
]

# Function to print deck and find Kings
def show_deck(deck, title):
    kings = []

    print(title)

    for i, card in enumerate(deck):
        print(f"Position {i + 1}: {card}")

        if card.endswith("-K"):
            kings.append(i)

    return kings


# Initial deck
initial_kings = show_deck(deck, "Initial Deck:")

print("\nInitial positions of all Kings:")
print(initial_kings)

# Shuffle the deck
random.shuffle(deck)

# Shuffled deck
shuffled_kings = show_deck(deck, "\nShuffled Deck:")

print("\nShuffled positions of all Kings:")
print(shuffled_kings)

