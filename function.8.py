#9.  Print Prime Numbers Function
#Write a function that prints all prime numbers up to a given limit.

# def prime_numbers(number):
#     if number <= 1:
#         return False
#     for i in range(2, (number // 2) + 1):
#         if number % i == 0:
#             return False
#     return i
# print(prime_numbers(23))

def prime_numbers(n):
    for i in range(2,(n//2)+1):
        if(n % i==0):
            return False
    return True
N = 10
for i in range(1,N+1):
  if(prime_numbers(i)):
      print(i)

    