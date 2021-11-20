"""
File: coin_flip_runs.py
Name:
-----------------------
This program should simulate coin flip(s)
with the number of runs input by users.
A 'run' is defined as consecutive results
on either 'H' or 'T'. For example, 'HHHHHTHTT'
is regarded as a 2-run result.
Your program should stop immediately after your
coin flip results reach the runs!
"""

import random as r

def main():
	"""
	Input
		num_run: int, when to stop the program
	Output
		the result of coin flipping
	"""
	print('Let’s flip a coin!')
	num_run = int(input('Number of runs: '))
	num_conti = 0
	coin0 = r.randint(0, 1)
	coin_list = ''
	run_or_not = 'no'
	while True:
		if num_conti == num_run: break
		coin = r.randint(0, 1)
		coin_list += str(coin)
		if coin == coin0 and run_or_not == 'no':
			num_conti += 1
			run_or_not = 'yes'
		if coin != coin0:
			coin0 = coin
			run_or_not = 'no'
	coin_str = ''
	for element in coin_list:
		if element == '0': coin_str += 'H'
		else: coin_str += 'T'
	print(coin_str)

###### DO NOT EDIT CODE BELOW THIS LINE ######

if __name__ == "__main__":
	main()
