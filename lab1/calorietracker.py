print("Welcome to the daily Calories Tracker")
meals = []
calories = []

n = int(input(" Enter no. of meals you consume in a day ? "))
for i in range(n):
    meal_name = input("Enter meal name: ")
    cal = float(input("Enter calories for meal: "))
    meals.append(meal_name)
    calories.append(cal)

total = sum(calories)
print(total)
average = total / n
print(average)

DAILY_LIMIT = float(input("Enter your daily calorie limit"))
if total > DAILY_LIMIT:
    print("You exceeded your daily limit!")
else:
    print("You are within your daily limit")

    print("\n--- Daily Summary ---")
print(f"Total meals consumed: {n}")
print(f"Total calories: {total}")
print(f"Average calories per meal: {average:.2f}")
print(f"Daily Calorie Limit: {DAILY_LIMIT}")

if total > DAILY_LIMIT:
    print("\n⚠ You’ve exceeded your daily calorie limit. Try reducing high-calorie foods or balance it out with more physical activity tomorrow.")
else:
    print("\n✅ Great job! You stayed within your calorie limit. Keep maintaining this consistency for steady progress toward your fitness goals.")

print("\n💡 Tracking your meals daily helps you stay aware of your eating habits. "
      "By maintaining a balanced calorie intake, you can improve your energy levels, "
      "manage your weight effectively, and build a healthier lifestyle over time.")