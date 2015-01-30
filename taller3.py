def almacenar:
	

def main(arg):
	int est[12] = [0,0,0,0,0,0,0,0,0,0,0,0]
	fo = open(arg,'r').read()
	fo = fo.split( )
	i = 0
	while i < len(fo): 	
		print (int(int(fo[i])/100))
		i += 1

if __name__ == '__main__':
    print(main(sys.argv[1]))