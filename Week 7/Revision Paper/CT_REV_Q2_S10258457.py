def calculate_total_value(card1, card2, card3):
    # Convert face cards (jack, queen, king) to a value of 10
    card1 = min(card1, 10)
    card2 = min(card2, 10)
    card3 = min(card3, 10)
    
    # Calculate the total value
    total_value = card1 + card2 + card3
    
    # Check if an ace (1) should be counted as 11
    if card1 == 1 or card2 == 1 or card3 == 1:
        # If total_value + 10 does not exceed 21, count ace as 11
        if total_value + 10 <= 21:
            total_value += 10
    
    return total_value


# Prompt the user to enter three card values
card1 = int(input("Enter card 1: "))
card2 = int(input("Enter card 2: "))
card3 = int(input("Enter card 3: "))

# Calculate the total value
total_value = calculate_total_value(card1, card2, card3)

# Display the value of the three cards and the total value
print("Total value is", total_value)
