def sum_13(isbn):
    return sum(int(a)*int(b) for a, b in zip(isbn, '1313131313131'))

def isbn13(txt):
	txt = txt.replace("-", "").replace(" ", "")

	if len(txt) == 13 and txt.isdigit() and int(txt[0:3]) == 978:
			sum = 0
			for i in range(0, 13):
					if i % 2 == 0:
							sum += int(txt[i])
					else:
							sum += int(txt[i]) * 3
			if sum % 10 == 0:
					return "Valid"
			else:
					return "Invalid"

	if len(txt) == 10:
			sum = 0
			for i in range(0, 10):
					if i == 9 and txt[i] == "X":
							sum += 10 * (10 - i)
					elif txt[i].isdigit():
							sum += int(txt[i]) * (10 - i)
					else:
							return "Invalid"
			if sum % 11 == 0:
				check = sum_13('978' + txt[:-1])%10
				return '978' + txt[:-1] + str(10 - check)

	return "Invalid"

print(isbn13("9780316066525")) # "Valid"
print(isbn13("0330301824")) # "Invalid"
print(isbn13("0316066524")) # "9780316066525"

