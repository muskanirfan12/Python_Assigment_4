import time


def countdown(t):
    while t:
        #Converting Seconds into Minutes and Seconds
        mins ,sec = divmod(t , 60)  
        #  Formatting the Timer Output#
        timer = '{:02d}:{:02d}'.format(mins , sec )
        print(timer , end="\r")
        #Pause the execution for 1 sec
        time.sleep(1)
        t -= 1
    print("Time completed!!")    




t = int(input("Enter the time in second"))

countdown(t)
