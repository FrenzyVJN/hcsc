import tkinter as tk
from random import shuffle

def shuffle_teams():
    # Get the names of people from the user inputs
    names = [entry.get() for entry in name_entries]

    if len(names) < 2:
        result_label.config(text="Please enter at least 2 names.")
        return

    # Shuffle the list randomly
    shuffle(names)

    # Split the list into two teams
    midpoint = len(names) // 2
    team1 = names[:midpoint]
    team2 = names[midpoint:]

    # Display the shuffled teams
    team1_label.config(text="Team 1:\n" + "\n".join(team1))
    team2_label.config(text="Team 2:\n" + "\n".join(team2))
    result_label.config(text="Teams have been shuffled!")

# Create the main window
window = tk.Tk()
window.title("Futuristic Team Shuffler")

# Customize the colors
bg_color = "#333333"
fg_color = "#FFFFFF"
accent_color = "#FF6600"

# Set the window background color
window.configure(bg=bg_color)

# Create and pack widgets with updated styles
num_people_label = tk.Label(window, text="Enter the number of people:", bg=bg_color, fg=fg_color)
num_people_label.pack(pady=10)

num_people_entry = tk.Entry(window)
num_people_entry.pack()

add_names_button = tk.Button(window, text="Add Names", command=lambda: add_name_entries(int(num_people_entry.get())), bg=accent_color, fg=bg_color)
add_names_button.pack(pady=10)

name_entries_frame = tk.Frame(window, bg=bg_color)
name_entries_frame.pack()

def add_name_entries(num_entries):
    global name_entries
    name_entries = []  # Store the Entry widgets for later retrieval

    for i in range(num_entries):
        label = tk.Label(name_entries_frame, text=f"Name {i + 1}:", bg=bg_color, fg=fg_color)
        label.grid(row=i, column=0, padx=10, pady=5)

        entry = tk.Entry(name_entries_frame)
        entry.grid(row=i, column=1, padx=10, pady=5)

        name_entries.append(entry)

    shuffle_button.config(state=tk.NORMAL, bg=accent_color, fg=bg_color)  # Enable the shuffle button

shuffle_button = tk.Button(window, text="Shuffle Teams", command=shuffle_teams, state=tk.DISABLED, bg=accent_color, fg=bg_color)
shuffle_button.pack(pady=10)

team1_label = tk.Label(window, text="Team 1:", bg=bg_color, fg=fg_color)
team1_label.pack(side=tk.LEFT, padx=10)

team2_label = tk.Label(window, text="Team 2:", bg=bg_color, fg=fg_color)
team2_label.pack(side=tk.RIGHT, padx=10)

result_label = tk.Label(window, text="", bg=bg_color, fg=accent_color)
result_label.pack(pady=10)

# Start the GUI main loop
window.mainloop()
