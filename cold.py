def read_input(number):
	temperatures = raw_input()
	count = 0
	tokens = temperatures.split()
	for each in tokens:
		if int(each) < 0:
			count+= 1
	return count

if __name__ == '__main__':
	number = int(raw_input())
	print read_input(number)
