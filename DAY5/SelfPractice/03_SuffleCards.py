import random

card_point = ['A', 'K', 'Q', 'J', '2', '3', '4', '5', '6', '7', '8', '9', '10']
card_signs = ['HEART', 'CLUB', 'DIAMOND', 'SPADE']

deck = []

# Create deck
for sign in card_signs:
    for point in card_point:
        deck.append(sign + "-" + point)


# Print initial deck
print("Initial Deck:")

for position, card in enumerate(deck, start=1):
    print("Position", position, ":", card)


# Find positions of Kings
king_positions = []

for position, card in enumerate(deck, start=1):
    if card.endswith("-K"):
        king_positions.append(position)

print("\nInitial positions of all Kings:")
print(king_positions)


# Shuffle deck
random.shuffle(deck)


# Print shuffled deck
print("\nShuffled Deck:")

for position, card in enumerate(deck, start=1):
    print("Position", position, ":", card)


# Find new positions of Kings
king_positions = []

for position, card in enumerate(deck, start=1):
    if card.endswith("-K"):
        king_positions.append(position)

print("\nShuffled positions of all Kings:")
print(king_positions)