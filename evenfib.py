#problem 2
#By considering the terms in the Fibonacci sequence whose values do not exceed four million, find the sum of the even-valued terms

def fib(n):
   if n == 0:
      return 1
   if n == 1:
      return 2
   else:   
      return fib(n-1)+fib(n-2)

count = 2
n = 1
#n = 1 +3j will be even (odd,odd,even,odd,odd,even)
bool = True
while(bool):
   n = n+3
   j = fib(n)
   if(j>4_000_000):
      bool = False
      break
   count = count + j
   print(count)

