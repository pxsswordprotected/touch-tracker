import tkinter as tk
from datetime import datetime, timedelta
import json
import os
from pathlib import Path
import sys
import keyboard
from threading import Thread
import time

class FaceTouchTracker:
    def __init__(self):
        self.window = tk.Tk()
        self.window.title("Face Touch Tracker")
        self.window.geometry("300x450")  
        self.window.attributes('-topmost', True)
        
        self.data_file = os.path.join(Path.home(), "Documents", "face_touches.json")
        
        self.load_data()
        
        self.check_and_reset()
        
        self.create_widgets()
        
        # save data when closing
        self.window.protocol("WM_DELETE_WINDOW", self.on_closing)

        self.shift_times = []
        self.setup_keyboard_listener()

    def setup_keyboard_listener(self):
        def check_triple_shift():
            while True:
                keyboard.wait('shift')
                current_time = time.time()
                self.shift_times = [t for t in self.shift_times if current_time - t < 1.0]
                self.shift_times.append(current_time)
                
                if len(self.shift_times) >= 3:
                    # check if all 3 presses happened within 1 second
                    if current_time - self.shift_times[0] < 1.0:
                        self.window.after(0, self.increment_count)
                        self.shift_times = []  
                    
                if len(self.shift_times) > 3:
                    self.shift_times = self.shift_times[-3:]

        Thread(target=check_triple_shift, daemon=True).start()

    def load_data(self):
        try:
            with open(self.data_file, 'r') as f:
                self.data = json.load(f)
        except FileNotFoundError:
            self.data = {
                'Monday': 0,
                'Tuesday': 0,
                'Wednesday': 0,
                'Thursday': 0,
                'Friday': 0,
                'Saturday': 0,
                'Sunday': 0,
                'last_reset': datetime.now().strftime('%Y-%m-%d')
            }
            self.save_data()

    def save_data(self):
        os.makedirs(os.path.dirname(self.data_file), exist_ok=True)
        with open(self.data_file, 'w') as f:
            json.dump(self.data, f)

    def check_and_reset(self):
        last_reset = datetime.strptime(self.data['last_reset'], '%Y-%m-%d')
        today = datetime.now()
        
        # if it's Monday and last reset wasn't today
        if today.weekday() == 0 and last_reset.date() != today.date():
            self.reset_all_days()

    def reset_all_days(self):
        for day in ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']:
            self.data[day] = 0
        self.data['last_reset'] = datetime.now().strftime('%Y-%m-%d')
        self.save_data()
        self.update_display()

    def reset_today(self):
        today = datetime.now().strftime('%A')
        self.data[today] = 0
        self.save_data()
        self.update_display()

    def create_widgets(self):
        # counter button
        self.count_button = tk.Button(
            self.window,
            text="+ Touch",
            command=self.increment_count,
            height=2,
            width=20,
            bg='#4CAF50',
            fg='white',
            font=('Arial', 16, 'bold')
        )
        self.count_button.pack(pady=20)

        # display for today's count
        self.today_label = tk.Label(
            self.window,
            text="Today's Count:",
            font=('Arial', 12)
        )
        self.today_label.pack()

        self.today_count = tk.Label(
            self.window,
            text="0",
            font=('Arial', 24, 'bold')
        )
        self.today_count.pack()

        # reset today's count button
        self.reset_button = tk.Button(
            self.window,
            text="Reset Today's Count",
            command=self.reset_today,
            height=1,
            width=15,
            bg='#ff6b6b',
            fg='white',
            font=('Arial', 10)
        )
        self.reset_button.pack(pady=10)

        # weekly summary
        tk.Label(
            self.window,
            text="This Week:",
            font=('Arial', 12)
        ).pack(pady=(20, 10))

        self.week_frame = tk.Frame(self.window)
        self.week_frame.pack()

        self.day_labels = {}
        for day in ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun']:
            frame = tk.Frame(self.week_frame)
            frame.pack(side=tk.LEFT, padx=5)
            
            tk.Label(frame, text=day, font=('Arial', 8)).pack()
            self.day_labels[day] = tk.Label(frame, text="0", font=('Arial', 8))
            self.day_labels[day].pack()

        tk.Label(
            self.window,
            text="Press Shift 3 times quickly to add count",
            font=('Arial', 8),
            fg='gray'
        ).pack(pady=(20, 0))

        self.update_display()

    def increment_count(self):
        today = datetime.now().strftime('%A')
        self.data[today] += 1
        self.save_data()
        self.update_display()

    def update_display(self):
        today = datetime.now().strftime('%A')
        self.today_count.config(text=str(self.data[today]))
        
        # Update week summary
        day_mapping = {'Monday': 'Mon', 'Tuesday': 'Tue', 'Wednesday': 'Wed',
                      'Thursday': 'Thu', 'Friday': 'Fri', 'Saturday': 'Sat',
                      'Sunday': 'Sun'}
        
        for full_day, short_day in day_mapping.items():
            self.day_labels[short_day].config(text=str(self.data[full_day]))

    def on_closing(self):
        self.save_data()
        self.window.destroy()

    def run(self):
        self.window.mainloop()

if __name__ == "__main__":
    app = FaceTouchTracker()
    app.run()