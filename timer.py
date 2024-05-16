import tkinter as tk

class StopwatchApp:
    def __init__(self, master):
        self.master = master
        self.master.title("Stop Watch in python")

        self.timer = 0
        self.entered = False

        self.label = tk.Label(master, text="Press the button to start timing.")
        self.label.pack()

        self.input_entry = tk.Entry(master)
        self.input_entry.pack()

        self.button = tk.Button(master, text="Start", command=self.start_timing)
        self.button.pack()

        self.close_button = tk.Button(master, text="Close", command=self.close_window)
        self.close_button.pack()

    def start_timing(self):
        self.entered = False
        self.timer = 0
        self.label.config(text="Timing started.")
        self.update_timer()

    def update_timer(self):
        if not self.entered:
            self.timer += 1
            self.label.config(text=f"Time: {self.timer}")
            if len(self.input_entry.get()) == 100:
                self.entered = True
                self.label.config(text="Input completed.")
            else:
                self.master.after(1000, self.update_timer)

    def close_window(self):
        self.master.destroy()

def main():
    root = tk.Tk()
    app = StopwatchApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()
