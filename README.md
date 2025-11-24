 Weekly Mood Tracker (Python)

This project is a simple command-line Python script that allows a user to track their daily mood over a week (Monday to Sunday) and visualize the results as a line graph using the `matplotlib` library.

Features

* **Interactive Input:** Prompts the user to enter a mood score (1-5) for each day of the week.
* **Input Validation:** Ensures the user enters valid integer input within the 1-5 range.
* **Data Visualization:** Generates a clear line plot showing the trend of mood across the seven days.
* **Clear Scale:** Defines the mood scale from **1 (Very Sad)** to **5 (Very Happy)**.

Prerequisites

To run this script, you must have **Python** installed on your system.
You will also need the **`matplotlib`** library for generating the graph.

Installation

You can install `matplotlib` using `pip`:
pip install matplotlib
 How to Run the Script
1.	Save the Code: Save the provided Python code into a file named mood_tracker.py.
2.	Run from Terminal: Open your terminal or command prompt, navigate to the directory where you saved the file, and execute the script:
Bash
python mood_tracker.py
3.	Enter Your Moods: The script will prompt you for your mood score for each day of the week:
4.	Mood Tracker (Enter your mood as a number 1–5)
5.	1 = Very Sad, 2 = Sad, 3 = Neutral, 4 = Happy, 5 = Very Happy
6.	
7.	Enter your mood for Mon (1–5): 4
8.	Enter your mood for Tue (1–5): 5
9.	... (continue for all 7 days)
10.	View the Graph: Once you have entered all seven moods, a separate window will open displaying the "Weekly Mood Tracking Graph."
 Mood Scale
The script uses a standardized 5-point scale:
Score	Mood
5	Very Happy
4	Happy
3	Neutral
2	Sad
1	Very Sad
 Code Overview
The key components of the script are:
•	Data Structure: A list days defines the X-axis labels, and a dictionary moods stores the day-to-score mapping.
•	Input Handling: A for loop iterates through the days, and a while True/try-except block handles input validation.
•	Plotting: The script extracts the validated scores into mood_values and uses plt.plot() to create the line chart.
•	Visualization Customization:
o	plt.xlabel() and plt.ylabel() set the axis labels.
o	plt.ylim(1, 5) ensures the Y-axis range matches the mood scale.
o	plt.grid(True) adds a helpful background grid.

 Potential Enhancements
•	Data Persistence: Store the mood data in a file (CSV or JSON) to track moods across multiple weeks.
•	Statistics: Calculate and display the average mood score or identify the happiest/saddest day.
•	Customization: Allow the user to input custom titles or labels.
•	GUI: Transition from the command line to a graphical user interface (GUI) using libraries like Tkinter or PyQt.

SETUP STEPS 
1.	Clone the repository: https://github.com/varshini25bcy10046-collab/mood-tracker-.git
  
2.	Create and activate a virtual environment (optional but recommended)

3.	Install requied packages :pip install-r requirements  
