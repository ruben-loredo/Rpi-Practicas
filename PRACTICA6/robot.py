#! /usr/bin/env python
import RPi.GPIO as GPIO
import os
import time
#Define nombre de las entradas del puente H
ena = 18
in1 = 23
in2 = 24

enb = 19
in3 = 6
in4 = 5
#configura los pines segun el microprocesador Broadcom
GPIO.setmode(GPIO.BCM)
#configura los pines como salidas
GPIO.setup(ena,GPIO.OUT)
GPIO.setup(enb,GPIO.OUT)
GPIO.setup(in1, GPIO.OUT)
GPIO.setup(in2, GPIO.OUT)
GPIO.setup(in3, GPIO.OUT)
GPIO.setup(in4, GPIO.OUT)
#Define las salidas PWM q
pwm_a = GPIO.PWM(ena,500)
pwm_b = GPIO.PWM(enb,500)
#inicializan los PWM con un duty Cicly de cero
pwm_a.start(0)
pwm_b.start(0)
# funciones de sentido de giro de los motores
def  Giro_Favor_Reloj_MotorA():
	GPIO.output(in1,False)
	GPIO.output(in2,True)

def Giro_Contra_Reloj_MotorA():
	GPIO.output(in1,True)
	GPIO.output(in2,False)

def  Giro_Favor_Reloj_MotorB():
	GPIO.output(in3,False)
	GPIO.output(in4,True)

def Giro_Contra_Reloj_MotorB():
	GPIO.output(in3,True)
	GPIO.output(in4,False)


def adelante(velocidad, tiempo):
	Giro_Favor_Reloj_MotorA()
	Giro_Favor_Reloj_MotorB()
	pwm_a.ChangeDutyCycle(int(velocidad))
	pwm_b.ChangeDutyCycle(int(velocidad))
	time.sleep(tiempo)

def atras(velocidad, tiempo):
	Giro_Contra_Reloj_MotorA()
	Giro_Contra_Reloj_MotorB()
	pwm_a.ChangeDutyCycle(int(velocidad))
	pwm_b.ChangeDutyCycle(int(velocidad))
	time.sleep(tiempo)

def stopMotors(tiempo):
	pwm_a.ChangeDutyCycle(0)
	pwm_b.ChangeDutyCycle(0)
	time.sleep(tiempo)

def giro_der(velocidad,tiempo):
	Giro_Favor_Reloj_MotorA()
	Giro_Contra_Reloj_MotorB()
	pwm_a.ChangeDutyCycle(int(velocidad))
	pwm_b.ChangeDutyCycle(int(velocidad))
	time.sleep(tiempo)

def giro_izq(velocidad,tiempo):
	Giro_Contra_Reloj_MotorA()
	Giro_Favor_Reloj_MotorB()
	pwm_a.ChangeDutyCycle(int(velocidad))
	pwm_b.ChangeDutyCycle(int(velocidad))
	time.sleep(tiempo)

#limpia la pantalla
os.system('clear')
try:
	adelante(100,2)
	stopMotors(1)
	giro_der(100,0.5)
	stopMotors(1)
	adelante(100,2)
	stopMotors(1)
	giro_izq(100,0.5)
	stopMotors(1)
	adelante(100,4)
	print ("Termina trayectoria del robot")

except KeyboardInterrupt:
	pwm_a.stop()
	pwm_b.stop()
	GPIO.cleanup()
	os.system('clear')
	print
	print("Programa Terminado")
	print
	exit()
