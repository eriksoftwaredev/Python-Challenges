import sched
import time
import winsound

def play_alarm():
    frequency = 1500 
    duration = 1000  # Set duration to 1000 ms (1 second)
    winsound.Beep(frequency, duration)

def set_alarm(alarm_time):
    s = sched.scheduler(time.time, time.sleep)
    s.enterabs(alarm_time, 1, play_alarm)
    s.run()

# Test the function:
alarm_time = time.time() + 3
set_alarm(alarm_time)
