# while loop:
number = 0 
while number <= 10: 
  print(number)
  number+=1

# for loop: 
for number in range (1,11):
  print(number)


for number in range(1,11):
  if number % 2 == 0:
    print(number)

def askUserForName():
  name = input("Please enter your name: ")
  return name

name = askUserForName()
print(name)

def askUserForAge():
  age = int(input("Please enter your age: "))
  return age

age = askUserForAge()

for number in range (age, age+21):
  print(number)


# # string manipulation

name = "kelly"
print(name[0:3])


for letter in name:
  print(letter)

# a = int(input("Pick a number: "))
# b = int(input("Pick a number: "))
# c = int(input("Pick a number: "))
# x = int(input("Pick a number: "))
# y = int(input("Pick a number: "))
# z = int(input("Pick a number: "))

# number =1
# n = 1
# summ = 0 

# result = (a+b+c+x+y+z)

# print("result")

for number in range (result, result+2001):
  print(number)

if result % 96:
  print("found one!")

summ = 0

for num in range(6):
  user = int(input("Enter the number: "))
  summ+= user

for i in range(summ, 2001):
  if i % 2 == 1:
    print (i)
  if 96 % i == 0:
    print ("found one!")

userAmount = int(input("how many dvd you want to buy: "))
each_dvd = 3

cost = userAmount*each_dvd

if cost >= 50.00:
  actualPayment= cost*.8
  print("you pay", actualPayment)
elif cost >= 30.00:
  actualPayment= cost*.9
  print("you pay", actualPayment)


print("you pay", actualPayment)


user= int(input("please enter how many dvd's you want: "))

summ = user*3

if summ >= 50.00:
  print("you pay", summ-summ*.2)

elif summ >= 30.00:
  print ("you pay", summ- summ*.1)

else:
  print("you pay", summ)


# code snippets

#variable (str, int, float, booleans)
# # if 
# loops (while and for)
# string manipulating
# functions
