import time


class Timer:
    def __init__(self, work_duration, rest_duration):
        self.work_duration = work_duration
        self.rest_duration = rest_duration

    def work_timer(self):
        duration = self.work_duration
        while duration > 0:
            print(duration)
            time.sleep(1)
            duration -= 1
        print("Time to take a break!")


    def rest_timer(self):
        duration = self.rest_duration
        while duration > 0:
            print(duration)
            time.sleep(1)
            duration -= 1
        print("Break's over, back to work!")

timer = Timer(5, 5)

timer.work_timer()
timer.rest_timer()
