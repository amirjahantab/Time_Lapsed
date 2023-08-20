import tkinter as tk
import time

class StopWatch:
    def __init__(self, root):
        self.root = root
        self.root.title("Stopwatch")

        self.running = False
        self.elapsed_time = 0

        self.time_label = tk.Label(root, text="00:00:00", font=("Helvetica", 48))
        self.time_label.pack()

        self.start_button = tk.Button(root, text="Start", command=self.start)
        self.start_button.pack()

        self.stop_button = tk.Button(root, text="Stop", command=self.stop)
        self.stop_button.pack()

        self.reset_button = tk.Button(root, text="Reset", command=self.reset)
        self.reset_button.pack()

    def start(self):
        if not self.running:
            self.running = True
            self.start_time = time.time()
            self.update_time()

    def stop(self):
        if self.running:
            self.running = False

    def reset(self):
        self.running = False
        self.elapsed_time = 0
        self.time_label.config(text="00:00:00")

    def update_time(self):
        if self.running:
            elapsed_seconds = int(time.time() - self.start_time) + self.elapsed_time
            hours = elapsed_seconds // 3600
            minutes = (elapsed_seconds % 3600) // 60
            seconds = elapsed_seconds % 60
            self.time_label.config(text="{:02d}:{:02d}:{:02d}".format(hours, minutes, seconds))
            self.root.after(1000, self.update_time)

root = tk.Tk()
stopwatch = StopWatch(root)
root.mainloop()
