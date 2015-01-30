class Estacionamiento:
	def __init__(self, tam):
		self.datos = []
		self.tam = tam

	def agregarI(self,inicio, final):
		self.datos.append([inicio, -1])
		self.datos.append([final, 1])
		self.ordenar()

	def ordenar(self):
		for iter in range(len(self.datos)-1,0,-1):
			for i in range(iter):
				if self.datos[i][0] > self.datos[i+1][0] and self.datos[i][1] == self.datos[i+1][1]:
					temp = self.datos[i]
					self.datos[i] = self.datos[i+1]
					self.datos[i+1] = temp

	def Reservar(self, inicio,final):	 
		self.agregarI(inicio,final)
		best = 0
		cnt = 0
		for i in range(len(self.datos) - 1):
			cnt = cnt - self.datos[i][1]
			if cnt > best:
				best = cnt
				beststart = self.datos[i][0]
				bestend = self.datos[i+1][0]
		return (beststart, bestend) 
		if best > self.tam:
			print ('No se puede reservar en este horario')
			for i in range(len(self.datos) - 1):
				if self.datos[i][0] == inicio and self.datos[i][1] == -1:
					del self.datos[i]
					break
			for i in range(len(self.datos) - 1):
				if self.datos[i][0] == final and self.datos[i][1] == 1:
					del self.datos[i]
					break
			return False
		else:
			print('Reservacion guardada satisfactoriamente')

e = Estacionamiento(10)
print (str(e.tam))