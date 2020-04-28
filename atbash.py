# coding=utf8

def main():
	f = open("page_1", "rb").read().decode("UTF-8")

	i = 0
	while (i < len(f)):
		try:
			if f[i] not in punctuation:
				char = ab[f[i].encode('utf-8')]
				# At this point, char contained only the cipher characters.
				clearchar = to_char(28-to_dec(char)) # Atbash cipher
				print(clearchar),

			else:
				print(punctuation[f[i].encode('utf-8')]),
			i += 1;
		except:
			print("Error:", i, f[i])
			raise

ab = {
	"ᚠ": "F", 
	"ᚢ": "V",
	"ᚦ": "TH",
	"ᚩ": "O",
	"ᚱ": "R",
	"ᚳ": "C",
	"ᚷ": "G",
	"ᚹ": "W",
	"ᚻ": "H",
	"ᚾ": "N",
	"ᛁ": "I",
	"ᛄ": "J",
	"ᛇ": "EO",
	"ᛈ": "P",
	"ᛉ": "X",
	"ᛋ": "S",
	"ᛏ": "T",
	"ᛒ": "B",
	"ᛖ": "E",
	"ᛗ": "M",
	"ᛚ": "L",
	"ᛝ": "ING",
	"ᛟ": "OE",
	"ᛞ": "D",
	"ᚪ": "A",
	"ᚫ": "AE",
	"ᚣ": "Y",
	"ᛡ": "IA",
	"ᛠ": "EA"
}

dec = [
	"F", 
	"V",
	"TH",
	"O",
	"R",
	"C",
	"G",
	"W",
	"H",
	"N",
	"I",
	"J",
	"EO",
	"P",
	"X",
	"S",
	"T",
	"B",
	"E",
	"M",
	"L",
	"ING",
	"OE",
	"D",
	"A",
	"AE",
	"Y",
	"IA",
	"EA"
]

punctuation =  {
	'-' : " ",
    '/' : '',
    '.' : '.',
    '§' : '§',
    '$' : '$',
    '%' : '%',
    '\n': '',
}


def to_dec(c):
	return dec.index(c)

def to_char(n):
	return dec[n]


if __name__ == "__main__":
	""" This is executed when run from the command line """
	main()

