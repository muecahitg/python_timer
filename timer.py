#timer in python
import time


print("-------TIMER--------")

minutes = int(input("How long should the timer run (in minutes): "))

for i in range(minutes):
    print(str(minutes - i) + " minute(s) left")
    print("---------------------")

    time.sleep(60)    # 60sec = 1min

print("++++++++++++++")
print("+ " + "TIME IS UP" + " +")
print("++++++++++++++")

