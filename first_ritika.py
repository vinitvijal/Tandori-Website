from decimal import ROUND_HALF_DOWN


Days =int(input("input days :")) *3600 *24
Hours =int(input("Input hours :"))*3600
Minutes =int(input("input minutes :"))*60
Seconds = int(input("input seconds :"))
Time = Days + Hours + Minutes + Seconds
print("Total number of seconds",Time)

