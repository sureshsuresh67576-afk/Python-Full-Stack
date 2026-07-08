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

