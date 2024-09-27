def luhn_algorithm(card_number):
    digits = [int(digit) for digit in str(card_number)]
    digits.reverse()
    for i in range(1, len(digits), 2):
        digits[i] *= 2
        if digits[i] > 9:
            digits[i] -= 9
    total_sum = sum(digits)
    return total_sum % 10 == 0

card_number = 4532015112830366
if luhn_algorithm(card_number):
    print("Card is valid.")
else:
    print("Card is invalid.")
