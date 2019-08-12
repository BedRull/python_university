L = list((1,
	2,
	5,
	'kek',
	'word',
	(5623,4545,234),
	'one',
	'more',
	'word',
	('ha', '-', 'ha'),
	{1 : 'Jan', 2 : 'Feb', 3 : 'Mar', 4 : 'Apr', 5 : 'May'}))
with open('C:/Entertaiments/TPU/Programming/labs/FileForWriting.txt', 'w') as file:
	for i in L:
		file.write(str(i) + '\n')

with open('C:/Entertaiments/TPU/Programming/labs/FileForWriting.txt', 'r') as file:
	print(file.read())



