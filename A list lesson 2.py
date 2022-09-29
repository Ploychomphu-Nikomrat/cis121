name = ["kelly","michaela"]
random_stuff = [1,1.2,False,[], "string"]


print(name[1])

for item in random_stuff:
  print(type(item))


# Create a script that creates the sentence from the following list:

list_1 = ["I", "your", "dude"]
list_2 = ['am', 'boss', '.']
#1
print(list_1 [0], list_2 [0], list_1[1], list_2[1], list_1[2]+list_2 [2])
#2
for word in range (0,3):
  print(list_1[word], list_2[word],end=" ")

# Create a function that allows the user to create 2 list of len 5. The user must type in only number (int). Once all 10 numbers have been added, create a third list with the sum of the same index value

def problem_2 ():
  list_1 = []
  list_2 = []
  list_3 = []

  count = 0

  while count < 10:
    user = input("please enter a number: ")

    if user.isdigit():

      # if isinstance(int(user), int):
      if count < 5:
        list_1.append(int(user))
      else:
        list_2.append(int(user))
    
      count += 1
     
    else:
      print("please enter an actual number >:")

  for numbers in range (0, len(list_2)):
    list_3.append(list_1[index]+list_2[index])

  print("List 1: ", list_1)
  print("List 2: ", list_2)
  print("Sum of the list: ", list_3)


# Create a script that ask the user 3 family members. Then, ask them which rank they give them from 1-3. Keep track of the rank in a seperate list.

# Display a table with the info. 

#=========Ranking===========

#===========================

name = []
rank = []

count = 0

while count < 3:
  user_input = input("please enter family members: ")
  name.append(user_input)
  count += 1

  if count == 1:
    user_input = input("please enter "+name[0]+ "rank: ")
    rank.append(user_input)

  elif count == 2:
    user_input = input("please enter "+name[1]+ "rank: ")
    rank.append(user_input)

  else:
    user_input = input("please enter "+name[2]+"rank: ")
    rank.append(user_input)

print("=========Ranking===========")
for index in range (0,3):
  print(name[index], "-", rank[index])
print("===========================")
