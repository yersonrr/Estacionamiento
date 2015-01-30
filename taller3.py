# Global Variable
carPark = [0,0,0,0,0,0,0,0,0,0,0,0]

# st = Start Time, et = End Time
def park(st, et):
	global carPark
	j = st
	while j <= et:
		elem = j - 7
		carPark[elem] += 1
		j += 1
		#print ('Elem::::::::::::'+str(carPark[elem]))
		if (carPark[elem] > 10):
			return False
	return True

def main(arg):
	global carPark
	carPark = [0,0,0,0,0,0,0,0,0,0,0,0]
	fo = open(arg,'r').read()
	fo = fo.split( )
	i = 0
	while i < len(fo): 
		sh = int(int(fo[i])/100)
		eh = int(int(fo[i+1])/100)	
		v = park(sh, eh)
		i = i + 2
		#print (str(v))
		if v == False:
			return v
	return v

if __name__ == '__main__':
    print(main(sys.argv[1]))
