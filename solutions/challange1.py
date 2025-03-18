from datetime import datetime
import matplotlib.pyplot as plt
import numpy as np

def is_valid_time(time_str):
    """Check if the given time string is in 24-hour format HH:MM."""
    try:
        hours, minutes = map(int, time_str.split(':'))
        if 0 <= hours < 24 and 0 <= minutes < 60:
            return True
    except ValueError:
        pass
    return False

def format_time(time_str):
    """Format the time string to ensure two digits on both sides of the colon."""
    hours, minutes = map(int, time_str.split(':'))
    return f"{hours:02}:{minutes:02}"

def get_time_input(prompt):
    """Prompt the user to enter a time and validate the input."""
    while True:
        time_str = input(prompt)
        if is_valid_time(time_str):
            return format_time(time_str)
        else:
            print("Invalid time format. Please enter the time in HH:MM format.")

def print_time_differences(times):
    """Print the time for each clock and the difference in time between these clocks and the grand clock."""
    grand_clock_time = datetime.strptime(times["grand_clock"], "%H:%M")
    differences = []
    for clock, time in times.items():
        if clock != "grand_clock":
            clock_time = datetime.strptime(time, "%H:%M")
            time_difference = (clock_time - grand_clock_time).total_seconds() // 60
            sign = "+" if time_difference >= 0 else ""
            differences.append(f"{sign}{time_difference}")
            print(f"The time for {clock} is {time}. Difference with grand clock: {sign}{time_difference} minutes.")
    print("Time differences with grand clock:", differences)

def plot_clock(time_str, title):
    """Create a visual representation of a clock with the given time."""
    time = datetime.strptime(time_str, "%H:%M")
    hours, minutes = time.hour, time.minute

    fig, ax = plt.subplots()
    ax.set_xlim(-1.5, 1.5)
    ax.set_ylim(-1.5, 1.5)
    ax.set_aspect('equal')
    ax.axis('off')

    # Draw clock face
    clock_face = plt.Circle((0, 0), 1, edgecolor='black', facecolor='white')
    ax.add_artist(clock_face)

    # Draw hour marks
    for i in range(12):
        angle = np.deg2rad(90 - (1+i) * 30)  # Adjust angle to place 12 at the top
        x = np.cos(angle)
        y = np.sin(angle)
        ax.text(0.85 * x, 0.85 * y, str(i + 1), ha='center', va='center')

    # Draw hour hand
    hour_angle = np.deg2rad(90 - (hours % 12 + minutes / 60) * 30)
    hour_hand, = ax.plot([0, 0.5 * np.cos(hour_angle)], [0, 0.5 * np.sin(hour_angle)], color='black', lw=4)

    # Draw minute hand
    minute_angle = np.deg2rad(90 - minutes * 6)
    minute_hand, = ax.plot([0, 0.8 * np.cos(minute_angle)], [0, 0.8 * np.sin(minute_angle)], color='black', lw=2)

    plt.title(title)
    plt.show()


# Get times for the grand clock and clocks 1, 2, 3, and 4
grand_clock_time = get_time_input("Enter the time for the grand clock (HH:MM): ")
clock1_time = get_time_input("Enter the time for clock 1 (HH:MM): ")
clock2_time = get_time_input("Enter the time for clock 2 (HH:MM): ")
clock3_time = get_time_input("Enter the time for clock 3 (HH:MM): ")
clock4_time = get_time_input("Enter the time for clock 4 (HH:MM): ")

# Store the times in variables
times = {
    "grand_clock": grand_clock_time,
    "clock1": clock1_time,
    "clock2": clock2_time,
    "clock3": clock3_time,
    "clock4": clock4_time
}

# Print the stored times and differences
print_time_differences(times)

# Plot the clocks
for clock, time in times.items():
    plot_clock(time, f"{clock} - {time}")