name = "kelly"
age = 18
distance = 18.7

print(name)

print("kelly was here")


if age ==  18:
  print("This person is 18")
elif age < 18:
  print("This person is older than 18")

else:
  print("This person is younger 18")
elif age > 18:
  print("This person is older than 18")

income = int(input("Please enter your income: "))

print(income)

if income == 450000:
  print("this person is middle class")
elif income < 450000:
  print("this person is poor")
else:
  print ("this person is rich")

number = 1
while number <= 10: 
  print(number)
  number = number + 1

print ("made it out")


number = int(input("Please guess a number: "))
print(number)

if number == 9: 
  print("hurray")
elif number > 9: 
  print("try again")
else:
  print("not quite")

answer = 9
winner = 0
guess = 0
while winner == 0 and guess < 3:
  user = int(input("Please guess a number 0-25: "))

  if user == answer: 
    print("hurray")
    winner = 1
  else:
    guess = guess +1
    print("try again")
  
  

  

