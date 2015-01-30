# Global Variable
carPark = [0,0,0,0,0,0,0,0,0,0,0,0]

# st = Start Time, et = End Time
def park(st, et):
	global carPark
	j = st
	while j <= et:
		j += 1
		elem = j - 6
		carPark[elem] += 1
		print (carPark[elem])

def main(arg):
	fo = open(arg,'r').read()
	fo = fo.split( )
	i = 0
	while i < len(fo): 
		sh = int(int(fo[i])/100)
		eh = int(int(fo[i+1])/100)	
		park(sh, eh)
		i = i + 2


if __name__ == '__main__':
    print(main(sys.argv[1]))