# put your python code here
card1, card2 = input().split()
trump = input()
value = ['6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']

def cards(a, b):
	if value.index(a[:-1]) == value.index(b[:-1]) or (a[-1:] != b[-1:]):
		print('Error')
	elif value.index(a[:-1]) > value.index(b[:-1]):
		print('First')
	else:
		print('Second')
		
def trumps(a, b):
	if (a[-1:]==trump and b[-1:]==trump) or (a[-1:]!=trump and b[-1:]!=trump):
		cards(a, b)
	elif a[-1:] == trump:
		print('First')
	else:
		print('Second')
		
trumps(card1, card2)



 