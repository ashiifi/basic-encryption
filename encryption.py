"""
Basic Encryption Project:
encryption(S,n) takes in a string and a number. It then moves each letter in the string
n amount of times through the alphabet. In this way, 'encrypting' the string
then decryption(W) takes in the encrypted string with the n at the end of it. like "helloworld1"
"""

def encryption(S, n):
	#this is actually quite basic, I am simply listing the entire alphabet as a starting point
	letters = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
	initial = [] #initiate an empty list for the initial characters
	encrypted = []
	for char in S: #adds each character to the list initial
		initial.append(char)
	#Now if you noticed that you could also simply just use list(S) to get initial, you are right!
	a = 0
	while a < len(initial): #starts a while loop until a is no longer smaller than the lenght if initial
		for i in range(len(initial)):
			if initial[a] == " ": #if the element is a space " ", then add it as well
				encrypted.append(" ")
			elif initial[a] in letters:
				encrypted.append(letters[(letters.index(initial[a])+n)%26])
			a = a + 1
	T = "".join(encrypted)
	W = T+str(n)

	return W

def decryption(W):
	letters = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
	numbers = ['1','2','3','4','5','6','7','8','9','0','-']
	initial = []
	decrypted = []
	num = []
	for char in W:
		initial.append(char)
	a = 0
	b = 0
	while b < len(initial):
		if initial[b] in numbers:
				num.append(initial[b])
				n = "".join(num)
		b = b + 1
	while a < len(initial):
		for i in range(len(initial)):
			if initial[a] == " ":
				decrypted.append(" ")
			elif initial[a] in letters:
				decrypted.append(letters[(letters.index(initial[a])-int(n))%26])
			a = a + 1
	b = decrypted[:len(decrypted)]
	d = "".join(b)
	return d

def main():
	S = "hello world"
	n = 1
	#print(encryption("hello world", 1))
	W = encryption(S, n)
	print(S)
	print(W)
	print(decryption(W))

main()
