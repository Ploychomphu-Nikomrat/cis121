#Part 1 section 2 

human_age= float(input("what's your age: "))
dog_age= 7 * human_age

whole_dog_years = int(dog_age)
months_diff = (dog_age - whole_dog_years)*12
whole_months_diff = int(months_diff)
days_diff =int((months_diff - whole_months_diff)*30)

print("An age", human_age, "years for human should be", whole_dog_years, "years", whole_months_diff, "months", days_diff, "days in dog age")

