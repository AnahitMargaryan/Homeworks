
#Exercise 3. Input a two-digit natural number and output the sum of its digits. You can
#assume that the input will be a two-digit number and need not check that
#programmatically.

number = 68
tens_digit = number // 10
units_digit = number % 10
digit_sum = tens_digit + units_digit
print(digit_sum)

# Integer Division (//):

# When we perform number // 10, it divides the original number by 10 and returns only the integer quotient.
# For example, if the number is 56, 56 // 10 equals 5. This gives us the tens digit.
# Modulo Operator (%):

# The modulo operator % gives us the remainder when the number is divided by 10.
# For example, if the number is 56, 56 % 10 equals 6. This gives us the units digit.