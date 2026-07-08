student = {"ram","shyam","sita","gita"} 
print(student[-1]) 
number = (10,20,30,40,50)
print(number[2])    
x = ("a","b","c","d","e","f")
print(x.count("b"))
num = [10,20,30,40,50]
print(num[1:4])

x = {1,2,3,2,1,1,1}
print(x)
data = {1,2,3}
data.add(4)
print(data)

a ={1,2,3,}
b = {3,4,5}
print (a|b)
 
a = {1,2,3}
b = {3,4,5}
print(a & b)
 
def greeting():
    print("Hello, welcome to the program!")
    greeting()

    def add():
        return 10 + 20
    result = add()
    print(result)

def sub():
    return 10 - 20
result = sub()
print(result)


def add(a,b):
    print(a+b)
    add(10,20)

    def add (*num):
        total = 0
        for i in num:
            total += i
            print(total)
            add(10,20,30,40,50)

def student(**details):
    print("name:",details["name"])
    print("age:",details["age"])
    print("job:",details["job"])
student(name="ram",age=20,job="student")

def sqrt(a):
    result = a ** 0.5
    print(result)
    sqrt(25)

def square(X):
    return X * X
print(square(16))
square = lambda x: x * x
print(square(16))

add = lambda a,b: a + b
print(add(10,20))

even = lambda x:"even" if x % 2 == 0 else "odd"
print(boy(10))
print(boy(7))

uppercase = lambda s: s.upper()
print(uppercase("hello world"))
lowercase = lambda s: s.lower()
print(lowercase("HELLO WORLD"))

dinga = lambda text:len(text)
print(dinga("hello world"))


file = open("myfile.txt","w")
file.write("Hello ")
file.close

print("data written successfully")

file = open("student.txt","r")
data = file.read()
print(data)
file.close()

file = open("student.txt","a")
file.write("\nhello student")
file.close()

print("data appended successfully")

file = open("student.txt","r")
data = file.read()
print(file.read())
file.close()

try:
    a = 10
    b = 0
    print(a / b)
except:
    print("somthing went wrong")


try :
    a = int(input("Enter a number: "))
    b = int(input("Enter b number: "))
    print(a / b)
except ZeroDivisionError:
    print("Error: Division by zero")
except ValueError:
    print("enter only number")

try:
    file = open("data.txt")
    print(file.read())
except:
    print("file error")

    finally:
print("program completed")

