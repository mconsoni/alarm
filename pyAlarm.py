#!/usr/bin/env python3
import sys
import time
from threading import Thread
from beepy import beep


def play_alarm():
	beep(6)


def clock(alarm_time):
	alarm = Thread(target=play_alarm)
	alarmed = False
	while not (alarmed and not alarm.is_alive()):
		t = time.time()
		localtime = time.localtime(t)
		print(time.strftime("%H:%M:%S", localtime))
		if (
			alarm_time.tm_hour == localtime.tm_hour
			and alarm_time.tm_min == localtime.tm_min
			and alarm_time.tm_sec == localtime.tm_sec
		):
			alarm.start()
			alarmed = True
		time.sleep(1 - (time.time() - t))


def use():
	msg = """
Use: {} <ALARM_TIME>
	ALARM_TIME format: HH:MM:SS (24hs format)
""".format(
		sys.argv[0]
	)
	print(msg)


if __name__ == "__main__":
	if len(sys.argv) != 2:
		use()
		sys.exit(1)
	try:
		alarm_time = time.strptime(sys.argv[1], "%H:%M:%S")
		clock(alarm_time)
	except Exception as e:
		print("Error setting alarm: " + str(e))
		use()
		sys.exit(1)
	except KeyboardInterrupt:
		sys.exit(1)
