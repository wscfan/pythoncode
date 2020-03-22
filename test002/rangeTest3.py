num = 8
is_prime = True
for i in range(2, num):
    if num % i == 0 :
        is_prime = False
        break
print(is_prime)