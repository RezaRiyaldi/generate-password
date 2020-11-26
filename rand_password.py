import random


lower = "abcdefghijklmnopqrstuvwxyz"
upper = lower.upper()
numbers = "1234567890"
symbol = "(){}+-_&"
all = lower + upper + symbol + numbers
lenght = 16
def pwd():
	password = "".join(random.sample(all, lenght))
	print(f'random password = {password}')
	print()
	
while True:
	tanya = input('Generate? [y/n] : ')
	if tanya.lower() == 'y':
		pwd()
	elif tanya.lower() == 't':
		break
	else:
		print('Masukan hanya [y/t]!!')
		continue