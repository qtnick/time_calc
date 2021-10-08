import time
import sqlite3
import datetime


conn = sqlite3.connect('learning_time.db')

c = conn.cursor()

def create_database():
	c.execute("""CREATE TABLE if not exists learning_time (
		time_of_learning text,
		date_of_learning text
		)""")


def add_new_time(time_of_learning):
	date_of_learning = str(datetime.date.today())
	with conn:
		c.execute("""INSERT INTO learning_time VALUES
			(:time_of_learning, :date_of_learning)""",
			{'time_of_learning': time_of_learning, 'date_of_learning': date_of_learning})
			

def time_convert(sec):
	mins = int(sec // 60)
	sec = int(sec % 60)
	hours = int(mins // 60)
	mins = mins % 60
	return f"{hours}:{mins}:{sec}"
	#print(f"Time Lapsed = {hours}:{mins}:{sec}")


prompt = ("This is a stopwatch. Type 'q' for exiting.\n"
		"1 - start stopwatch\n"
		"2 - list time of learning\n3 - sum the time of learning\n"
		"4 - generate a monthly report\n"
)

active = True

while active:
	create_database()
	message = input(prompt)
	if message == 'q':
		active = False
		conn.close()
	elif str(message) == '1':	
		input("Press Enter to start")
		start_time = time.time()

		input("Press Enter to stop")
		end_time = time.time()

		time_lapsed = end_time - start_time
		add_new_time(time_convert(time_lapsed))
	elif str(message) == '2':
		pass
	elif str(message) == '3':
		pass
	elif str(message) == '4':
		pass