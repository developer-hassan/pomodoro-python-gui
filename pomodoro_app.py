# Import the required modules to be worked with
import tkinter as tk

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
timer = None


# ---------------------------- TIMER RESET ------------------------------- #
def reset_timer():
    """
    Resets the timer and all relevant widgets when the button is clicked.
    """
    window.after_cancel(timer)
    check_marks.config(text="")
    title_text.config(text="Timer", fg=GREEN)
    canvas.itemconfig(timer_text, text="00:00")
    restart_button["text"] = "Start"
    global reps
    reps = 0


def restart_timer():
    """
    Start the timer if it is not started already. Otherwise clears the previous timer and restarts it.
    """
    if timer:
        reset_timer()
    start_timer()


# ---------------------------- TIMER MECHANISM ------------------------------- #
def start_timer():
    """
    Start the timer of work and breaks time.
    """

    global reps
    reps += 1

    if restart_button["text"] == "Start":
        restart_button["text"] = "Restart"

    if reps % 8 == 0:
        title_text.config(text="Break", fg=RED)
        count = LONG_BREAK_MIN
    elif reps % 2 == 0:
        title_text.config(text="Break", fg=PINK)
        count = SHORT_BREAK_MIN
    else:
        title_text.config(text="Work", fg=GREEN)
        count = WORK_MIN
    count_down(count * 60)


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
def count_down(count):
    """
    Counts the time down from starting time to 0.

    Args:
        count (int): Starting time value in minutes.
    """
    count_min = int(count / 60)
    count_sec = count % 60

    if count_sec < 10:
        count_sec = "0" + str(count_sec)

    canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")
    if count > 0:
        global timer
        timer = window.after(1000, count_down, count - 1)
    else:
        if reps % 8 == 0:
            check_marks.config(text="")
        elif reps % 2 != 0:
            check_marks.config(text=check_marks["text"] + "✔")
        start_timer()


# ---------------------------- UI SETUP ------------------------------- #
# Generating the window on which the application will be rendered.
window = tk.Tk()
window.title("Pomodoro")  # Pomodoro means Tomato in Italian
window.config(padx=100, pady=50, bg=YELLOW)

# Label for title text
title_text = tk.Label(text="Timer", font=(
    FONT_NAME, 50, "bold"), fg=GREEN, bg=YELLOW)
title_text.grid(row=0, column=1)

# Image taken as PhotoImage object from tkinter class where the path of image is passed
tomato_image = tk.PhotoImage(file="./tomato.png")

# Create a canvas and place an image and a text on it. Put the canvas on screen
canvas = tk.Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
canvas.create_image(100, 112, image=tomato_image)
timer_text = canvas.create_text(
    100, 130, text="00:00", fill="white", font=(FONT_NAME, 30, "bold"))
canvas.grid(row=1, column=1)

# Button to handle the start/restart of timer
restart_button = tk.Button(text="Start", command=restart_timer, relief=tk.FLAT,
                           bg=GREEN, fg=RED, padx=10, pady=5, font=(FONT_NAME, 15, "bold"))
restart_button.grid(row=2, column=0)

# Button to reset the timer
reset_button = tk.Button(text="Reset", command=reset_timer, relief=tk.FLAT,
                         bg=GREEN, fg=RED, padx=5, pady=5, font=(FONT_NAME, 15, "bold"))
reset_button.grid(row=2, column=2)

# A label to keep track of how many work sessions are done yet
check_marks = tk.Label(text="", fg=GREEN, bg=YELLOW,
                       font=(FONT_NAME, 20, "bold"))
check_marks.grid(row=3, column=1)

window.mainloop()
