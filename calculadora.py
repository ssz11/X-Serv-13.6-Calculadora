#1/usr/bin/python3
import sys;
#import os;
argumentos = len(sys.argv);
try:
	operacion = sys.argv[1];
	operando1 = sys.argv[2];
	operando2 = sys.argv[3];
	if argumentos > 4:
		print("demasiados argumentos");
		sys.exit(0)
except IndexError:
		print("pocos argumentos");
		sys.exit(0)
	#os.system ("/usr/bin/python calculadora.py")

if operacion == 'suma' :
	print(float(operando1) + float(operando2));
elif operacion == 'resta' :
	print(float(operando1) + float(operando2));
elif operacion == 'multiplicacion' :
	print(float(operando1) * float(operando2));
elif operacion == 'division' :
	try:
		print(float(operando1) / float(operando2));
	except ZeroDivisionError:
		print("division entre 0");
