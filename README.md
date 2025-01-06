# Face Touch Tracker

A simple desktop application to help you track how many times you touch your face during the day. Built with Python and Tkinter, this app runs in the background and makes it easy to log face touches with either a button click or a keyboard shortcut.

## Features

- **Simple Interface**: Clean, minimal window that stays on top of other applications
- **Multiple Input Methods**:
  - Click the "+ Touch" button
  - Press Shift key 3 times quickly (works even when window isn't focused)
- **Weekly Tracking**:
  - Displays daily counts for the entire week
  - Automatically resets counts every Monday
  - Manual reset option for today's count
- **Persistent Storage**: Saves your data between sessions
- **Windows Integration**: Can be set to start automatically with Windows

## Installation

1. Clone the repository:
```bash
git clone https://github.com/yourusername/face-touch-tracker.git
cd face-touch-tracker
```

2. Install required dependencies:
```bash
pip install keyboard
pip install tkinter  # Usually comes with Python
```

3. Run the application:
```bash
python start.py
```

### Creating an Executable (Optional)

To create a standalone executable:

1. Install PyInstaller:
```bash
pip install pyinstaller
```

2. Create the executable:
```bash
pyinstaller --windowed --onefile face_touch_tracker.py
```

## Project Structure

```
face-touch-tracker/
├── face_touch_tracker.py   # Main application code
├── start.py               # Simple starter script
├── add_to_startup.py     # Script to add app to Windows startup
└── README.md
```

## Usage

1. **Starting the Application**:
   - Double-click `start.py`, or
   - Run `python start.py` from the command line

2. **Recording Face Touches**:
   - Click the green "+ Touch" button, or
   - Press the Shift key 3 times quickly

3. **Resetting Counts**:
   - Click the "Reset Today's Count" button to reset just today's count
   - Weekly counts automatically reset every Monday

4. **Viewing Statistics**:
   - Today's count is displayed prominently
   - Weekly summary shows counts for each day
   - Data is automatically saved when closing the app

## Auto-Start Configuration

To make the application start automatically with Windows:

1. Run `add_to_startup.py` with administrator privileges:
```bash
python add_to_startup.py
```

## Data Storage

The application stores data in:
```
C:\Users\YourUsername\Documents\face_touches.json
```

## Requirements

- Python 3.6 or higher
- Windows OS (for keyboard shortcut and startup features)
- Required Python packages:
  - keyboard
  - tkinter (usually included with Python)
