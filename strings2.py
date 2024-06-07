#Exercise 2. Count all letters, digits, and special symbols from a given string.

word = "yERevan2024@mail.ru"
chars = 0
digits = 0
symbols = 0
for x in word:
    if x.isdigit():
        digits = digits + 1
    elif ord(x) in range(97,123) or ord(x) in range(65,91):
        chars = chars + 1
mix = chars + digits 
symbols = len(word) - mix
print(f'''chars = {chars} 
digits = {digits }
symbols = {symbols}''')







