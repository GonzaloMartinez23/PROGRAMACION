Algoritmo INICIO_CARRERA
	definir valla Como caracter
	valla=" "
	tunel= " "
	laguna= " "
	Escribir "COMIENZA LA CARRERA";
	
	Escribir "¿HAY UNA VALLA?";
	Leer valla 
	Si valla = "si" Entonces
		Escribir "¡salta la valla!";
	sino 
		Escribir "SIGUE CORIENDO";
	Fin Si
	
	Escribir "¿HAY UN TUNEL?";
	Leer tunel 
	Si tunel = "si" Entonces
		Escribir "¡atravieza el tunel!";
	sino 
		Escribir "SIGUE CORIENDO";
	Fin Si
	
	Escribir "¿HAY UNA LAGUNA?";
	Leer laguna 
	Si laguna = "si" Entonces
		Escribir "¡debes nadar";
	sino 
		Escribir "FELICIDADES LLEGASTE A LA META!"
		
		Escribir "FIN DEL PROGRAMA"
	Fin Si
	
	
FinAlgoritmo
