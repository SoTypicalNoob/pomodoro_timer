import threading
import datetime as dt
import winsound
import time
import os

# def set_up_cycle():


def pomodoro_cycle():
    current_time = dt.datetime.now()
    pomodoro_work = 25 * 60
    t_delta = dt.timedelta(0,pomodoro_work)
    pomodoro_work_end = current_time + t_delta
    pomodoro_rest = 5 * 60
    pomodoro_cycle_end = current_time + dt.timedelta(0,pomodoro_work + pomodoro_rest)

    total_pomodoros = 0
    breaks = 0
    while True:
        if current_time < pomodoro_work_end:
            print('Remainging time: {}'.format(pomodoro_work_end - current_time), end='\r')
            # print("Remaining time: ", pomodoro_work_end - current_time)
        elif pomodoro_work_end <= current_time <= pomodoro_cycle_end:
            print("in break")
            if breaks == 0:
                # if total_pomodoros == 3:
                #     break
                print("if break")
                time.sleep(10)
                for i in range(10):
                    winsound.Beep((i + 400), 700)
                print("Break time!")
                winpath = os.environ["windir"]
                os.system(winpath + r'\system32\rundll32 user32.dll, LockWorkStation')
                breaks += 1
        else:
            breaks = 0
            total_pomodoros += 1
            print("Finished pomodoros: ", total_pomodoros)
            for i in range(10):
                winsound.Beep((i + 100), 500)
            current_time = dt.datetime.now()
            pomodoro_work_end = current_time + dt.timedelta(0, pomodoro_work)
            pomodoro_cycle_end = current_time + dt.timedelta(0, pomodoro_work + pomodoro_rest)
        time.sleep(1)
        current_time = dt.datetime.now()

def main():
    pomodoro_cycle()

if __name__ == '__main__':
    main()