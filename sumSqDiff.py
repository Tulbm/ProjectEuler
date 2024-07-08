#problem 6
#difference between the sum of the squares of the first one hundred natural numbers and the square of the sum

#100 x 101/2 = 5050

sum = 0
for i in range(1,101):
   sum = sum + i**2

square = 5050**2

print(sum-square)