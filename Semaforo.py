#!/usr/bin/python
# -*- coding: utf-8 -*-
import RPi.GPIO as GPIO
import time
import os
#declaracion de gpios de calle A
rojo_calleA = 4
amarillo_calleA = 17
verde_calleA = 27
#declaracion de gpios de calle B
rojo_calleB = 23
amarillo_calleB = 24
verde_calleB = 25
tiempoCambio = 5
tiempoPreventivo = 2
#configuraciones de los puertos
GPIO.setmode(GPIO.BCM)
GPIO.setup(rojo_calleA, GPIO.OUT)
GPIO.setup(amarillo_calleA, GPIO.OUT)
GPIO.setup(verde_calleA, GPIO.OUT)
GPIO.setup(rojo_calleB, GPIO.OUT)
GPIO.setup(amarillo_calleB, GPIO.OUT)
GPIO.setup(verde_calleB, GPIO.OUT)
os.system('clear')
#funcion de control de trafico
def semaforo():
	print('Calle A= Verde, Calle B = Rojo')	
	GPIO.output(verde_calleA,True)
	GPIO.output(rojo_calleB,True)
	GPIO.output(amarillo_calleA,False)
	GPIO.output(rojo_calleA,False)
	GPIO.output(verde_calleB,False)
	GPIO.output(amarillo_calleB,False)
	time.sleep(tiempoCambio)

	print('Calle A = Amarillo, Calle B = Rojo')
	GPIO.output(verde_calleA,False)
	GPIO.output(amarillo_calleA,True)
	time.sleep(tiempoPreventivo)

	print('Calle A = Rojo, Calle B = verde')
	GPIO.output(amarillo_calleA,False)
	GPIO.output(rojo_calleA,True)
	GPIO.output(verde_calleB,True)
	GPIO.output(rojo_calleB,False)
	time.sleep(tiempoCambio)

	print('Calle A = Rojo, Calle B = Amarillo')	
	GPIO.output(verde_calleB,False)
	GPIO.output(amarillo_calleB,True)
	time.sleep(tiempoPreventivo)
try:
	while (True):					#repite indefinidamente
		semaforo()
except KeyboardInterrupt:			#hasta que el usuario interrumpe con Ctrl-C por teclado
	os.system('clear')
	print("Apaga los LED'S" )
	GPIO.cleanup()
	print
	print("Programa Terminado por el usuario")
	print
	exit()
