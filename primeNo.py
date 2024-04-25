'''
import math

n = int(input("Enter a number: "))


for i in range(2, int(math.sqrt(n))):
    if n % i == 0:
        print(" Not prime")
        break
#leave the entire for loop and give the other condition
else:
    print("prime")
'''

