# no argument ,no return type
def show():
    print("hello world")
    for i in  range(5):
        show()

# no arugument, no return type
def sum():
    n1 = 10
    n2 = 20
    ans = n1+n2
    print("sum is ",ans)

    sum()

#arument , no returntype
def printName(a):
    print("hello",a)

print("mahesh")       
print("chinamy")

# argument, no return type
def sum(n1,n2):
    ans = n1+n2
    print("sum is", ans)

print(10,20)

 #argument ,return type
def printName(a):
    msg = "hello" + a
    return msg
#method 1
print(printName("mahesh"))
#method 2
ans = printName("chinamy)")
print(ans)

# argument , return type
def sum(n1,n2):
    ans = n1+n2
    return ans

a1 = sum(10, 20)
print("sum is ", a1)

#sum avg
def dosum(a,b,c):
    d = a + b + c 
    return d
def calculateAvg(total):
    per = total/300*100
    return per

totalmarks = dosum(85,65,74)
print("total is",totalmarks)

getper = calculateAvg(totalmarks)
print("% is ",getper)





