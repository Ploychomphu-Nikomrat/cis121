human_age= float(input("what's your age: "))
dog_age= 7 * human_age

whole_dog_years = int(dog_age)
months_diff = (dog_age - whole_dog_years)*12
whole_months_diff = int(months_diff)
days_diff =int((months_diff - whole_months_diff)*30)

print("An age", human_age, "years for human should be", whole_dog_years, "years", whole_months_diff, "months", days_diff, "days in dog age")


human_age= float(input("what's your age: "))
cat_age= human_age / 2

whole_cat_age= int(cat_age)
months_diff= (cat_age - whole_cat_age)* 12
whole_months_diff= int(months_diff)
day_diff= int((months_diff - whole_months_diff)* 30)

print("An age", human_age, "years for human should be", whole_cat_age, "years", whole_months_diff, "months", day_diff, "day in cat age")


human_age= float(input("what's you age: "))
horse_age= 3*((((human_age ** 2)-47)/7)+12)

whole_horse_age= int(horse_age)
month_diff= (cat_age - whole_cat_age) * 12
whole_months_diff= int(months_diff)
day_diff= int((months_diff - whole_months_diff)* 30)

print("An age", human_age, "years for human should be", whole_horse_age, "years", whole_months_diff, "months", day_diff, "day in horse age")