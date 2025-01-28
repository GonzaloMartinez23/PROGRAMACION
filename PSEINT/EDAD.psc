Algoritmo sin_titulo
	Definir EDAD, NUM COMO ENTERO; 
	Definir NOMBRE COMO CARACTER;

	NUM=94512548
	Escribir "ESCRIBA SU NOMBRE:"
	Leer NOMBRE;
	Escribir "ESCRIBA SU EDAD:"
	Leer EDAD;

	SI EDAD<12 Entonces
		Escribir "ES MENOR UN NIÑO";
	SiNO 
		SI EDAD>=12 o EDAD<=18 Entonces
			Escribir "USTED ES ADOLECENTE";
		SiNo
			Escribir "MAYOR DE EDAD";
		FIN SI	
		
		
		
	Fin Si

FINPROCESO
