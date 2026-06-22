#add two numbers
a = 10
b = 40
print("sum =", a + b)

#evan or odd

num = int(input("enter a number:"))
if num % 2 == 0:
    print("even")
else:
  print("odd")

#largest of two number
a = int(input(" enter first number: "))
b = int(input("enter second number: "))

if a > b:
    print("largest:", a )
else:
    print("largest:", b )


 #factorial of number
n = int(input("enter a number :"))
fact = 1

for i in range(1, n + 1):
    fact  *= i

print("factorial =", fact)

 #fibonacci series
n = int(input("enter number of terms: "))
a, b = 0, 1

for i in range(n):
    print(a, end=" ")
    a, b = b, a + b

 #prime number cheak
n = int(input("enter a number: "))

if n > 1:
    for i in range(2, n):
        if n % i == 0:
            print("not prime")
            break
    else:
        print("prime")
else:
    print("not prime")




        