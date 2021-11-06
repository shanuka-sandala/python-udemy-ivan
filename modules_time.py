import time as t
t. localtime()

time_now = t.localtime()
print ("Transaction completed at", str(time_now.tm_hour) + "h" + str(time_now.tm_min) + "m")

t.time()
## Timestamp, shows number of seconds that have passed since the Epoch. Epoch represents the point where time starts.
## Python uses the unix epoch which is Jan 1st 1970 at zero hours zero minutes and zero seconds. 
## Shows in seconds

time_now = t.time()
delivery_time = time_now + (86400 * 7) ## 86400 is seconds in a one day. into 7 means, for a week
delivery = t.localtime(delivery_time)
print (delivery)

t.sleep(5)
## After this, another code will executes in 5 seconds.