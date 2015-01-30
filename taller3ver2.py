class Estacionamiento:
	def __init__(self, tam):
		self.datos = []
		self.tam = tam

	def agregarI(self,inicio, final):
		inicio = inicio/100
		final = final/100
		if (inicio < 6) or (inicio > final) or (inicio > 18) or (final > 18) or (final < 6):
			print ('Valores no validos')
			return False
		self.datos.append([inicio, -1])
		self.datos.append([final, 1])
		self.ordenar()
		return True

	def ordenar(self):
		for itera in range(len(self.datos)):
			for i in range(itera):
				if (self.datos[itera][0] < self.datos[i][0]) or (self.datos[itera][0] == self.datos[i][0]  and self.datos[itera][1] < self.datos[i][1]):
					temp = self.datos[itera]
					self.datos[itera] = self.datos[i]
					self.datos[i] = temp

	def Reservar(self, inicio,final):	 
		a = self.agregarI(inicio,final)
		if not(a):
			return a
		best = 0
		cnt = 0
		for i in range(len(self.datos) - 1):
			cnt = cnt - self.datos[i][1]
			if cnt > best:
				best = cnt
				beststart = self.datos[i][0]
				bestend = self.datos[i+1][0] 	
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
			return True


