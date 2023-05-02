def print_hello():
	animals = ['dog', 'cat', 'cow', 'tiger'] # in one line
	foods = ['Pizza',
'Chicken',
'Waffle'] # w/o trailing comma
	names = ['John', 
'Jane', 
'Gil-dong',
'Dong-eun',
] # w/ trailing comma
	for f_name in names:
		print(f"hello, {f_name}")

if __name__ == '__main__':
	print_hello()

