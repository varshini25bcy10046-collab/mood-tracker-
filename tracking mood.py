import matplotlib.pyplot as plt

# Days of the week
days = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]

# Mood input dictionary
moods = {}

print("Mood Tracker (Enter your mood as a number 1–5)")
print("1 = Very Sad, 2 = Sad, 3 = Neutral, 4 = Happy, 5 = Very Happy\n")

# Take mood input for each day
for day in days:
    while True:
        try:
            mood = int(input(f"Enter your mood for {day} (1–5): "))
            if 1 <= mood <= 5:
                moods[day] = mood
                break
            else:
                print("Please enter a number between 1 and 5.")
        except:
            print("Invalid input. Enter a number between 1 and 5.")

# Extract mood values in order
mood_values = [moods[day] for day in days]

# Plotting the mood graph
plt.plot(days, mood_values, marker='o')
plt.xlabel("Days of the Week")
plt.ylabel("Mood Level (1 = Very Sad → 5 = Very Happy)")
plt.title("Weekly Mood Tracking Graph")
plt.grid(True)
plt.ylim(1,5)

plt.show()
