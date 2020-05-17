from datetime import datetime
from db_module import Database

users = {'Rahi': 1, 'Chaitanya': 2}

def main():

	dbObj = Database()
	o = 0
	link = 0
	a = 0
	with open("./assets/Chat_backup.txt", 'r', encoding = 'utf-8') as f:
		for line in f.readlines():
			if 'omitted' in line:
				time, text = line[:line.find(']')+1].strip(']').strip('['), line[line.find(']')+2:]
				msg = msg [msg.find(':')+2:]
				sender = msg[:msg.find(':')]
				time = datetime.strptime(time, "%d/%m/%y, %I:%M:%S %p")

				qry = "INSERT INTO media_history(time, sent_by, message) VALUES(?, ?, ?)", (time, users[sender], msg)

				dbObj.make_connection()
				dbObj.execute_query(qry)
				dbObj.close_connection()
				o += 1

			elif 'encryption' in line:
				print(i)

			else:
				time, text = line[:line.find(']')+1].strip(']').strip('['), line[line.find(']')+2:]
				sender = msg[:msg.find(':')]
				msg = msg [msg.find(':')+2:]
				time = datetime.strptime(time, "%d/%m/%y, %I:%M:%S %p")

	print(f'omitted {o}')
	print(f'links {link}')
	print(f'{a}')


if __name__ == '__main__':
	main()
