# Ans 1
# def keyword is  use to produce function
def odd():
    return [i for i in range(1,26) if i%2 !=0]
print(odd())





# Ans 2
def use(*args):
    return [x + y for (x, y) in args]
result = use((1, 2))
print(result)





# Ans 3
# an iterator is an object that implements the iterator protocol, recall the function by next().
list=[2,4,6,8,10,12,14,16,18,20]
my_iter=iter(list)

for i in range(5):
    element = next(my_iter)
    print(element)   
 
 
 
 
 
# Ans 4
# generator=it is use to declared a function and behaver like  iterator,
# yield is store value of n ,each loop rotation value of n is change
def even(n):
    for i in range(2, n+1, 2):
        yield i
result = even(10)
for num in result:
    print(num)
    
    
    
    
    
    
# Ans5
def numbers():
    primes = []
    num = 2
    while True:
        if all(num % p != 0 for p in primes):
            primes.append(num)
            yield num
        num += 1
prime_gen = numbers()
for _ in range(20):
    prime = next(prime_gen)
    print(prime)
    
    
    
    
    
#  Ans 6
def fib():
    num1, num2 = 0, 1
    count = 0
    while count < 10:
        print(num1)
        num1, num2 = num2, num1 + num2
        count += 1
fib()





# Ans 7
string = 'pwskills'
result = [i for i in string if i in 'pwskills']
print(result)




# Ans 8
num=int(input("Enter any number:"))
temp=num
rev=0
while(num>0):
    dig=num%10
    rev=rev*10+dig
    num=num//10
if(temp==rev):
    print("The {0} number is palindrome!".format(temp))
else:
    print("Not a palindrome!")
    
    
    

# Ans 9 
odds = [i for i in range(1, 101) if i % 2 != 0]
print(odds)
