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
			time = None
			if 'omitted' in line:
				time, text = line[2:line.find(']')], line[line.find(']')+2:]
				sender = text[:text.find(':')]
				msg = text[text.find(':')+2:]
				try:
					time = datetime.strptime(time, "%d/%m/%y, %I:%M:%S %p")
				except Exception as e:
					print(e)

				qry = "INSERT INTO media_history(time, sent_by, message) VALUES(?, ?, ?)", (time, users[sender], msg)
				dbObj.make_connection()
				dbObj.execute_query(qry)
				dbObj.close_connection()
				o += 1

			elif 'encryption' in line:
				print(line)

			else:
				time, text = line[1:line.find(']')], line[line.find(']')+2:]
				sender = text[:text.find(':')]
				msg = text[text.find(':')+2:]
				time = datetime.strptime(time, "%d/%m/%y, %I:%M:%S %p")

				qry = "INSERT INTO history(time, sent_by, message) VALUES(?, ?, ?)", (time, users[sender], msg)
				dbObj.make_connection()
				dbObj.execute_query(qry)
				dbObj.close_connection()

	print(f'omitted {o}')
	print(f'links {link}')
	print(f'{a}')


if __name__ == '__main__':
	main()
