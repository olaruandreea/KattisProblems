def check_if_hissing(user_input):
	if "ss" in user_input:
		return "hiss"
	else:
		return "no hiss"
if __name__ == '__main__':
	user_input = raw_input()
	print check_if_hissing(user_input)

