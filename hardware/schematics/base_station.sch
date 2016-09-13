EESchema Schematic File Version 2
LIBS:power
LIBS:device
LIBS:transistors
LIBS:conn
LIBS:linear
LIBS:regul
LIBS:74xx
LIBS:cmos4000
LIBS:adc-dac
LIBS:memory
LIBS:xilinx
LIBS:microcontrollers
LIBS:dsp
LIBS:microchip
LIBS:analog_switches
LIBS:motorola
LIBS:texas
LIBS:intel
LIBS:audio
LIBS:interface
LIBS:digital-audio
LIBS:philips
LIBS:display
LIBS:cypress
LIBS:siliconi
LIBS:opto
LIBS:atmel
LIBS:contrib
LIBS:valves
LIBS:teensy_schematic-cache
EELAYER 25 0
EELAYER END
$Descr A4 11693 8268
encoding utf-8
Sheet 1 1
Title ""
Date ""
Rev ""
Comp ""
Comment1 ""
Comment2 ""
Comment3 ""
Comment4 ""
$EndDescr
$Comp
L Teensy3.2 U?
U 1 1 57D88739
P 5300 3000
F 0 "U?" H 5300 5000 60  0000 C CNN
F 1 "Teensy3.2" H 5300 1000 60  0000 C CNN
F 2 "" H 5300 2700 60  0000 C CNN
F 3 "" H 5300 2700 60  0000 C CNN
	1    5300 3000
	1    0    0    -1  
$EndComp
$Comp
L eSP8266-01 U?
U 1 1 57D88798
P 3900 6500
F 0 "U?" H 5250 7250 60  0000 C CNN
F 1 "eSP8266-01" H 5250 7250 60  0000 C CNN
F 2 "" H 5250 7250 60  0001 C CNN
F 3 "" H 5250 7250 60  0001 C CNN
	1    3900 6500
	1    0    0    -1  
$EndComp
$Comp
L RFM22 U?
U 1 1 57D88BA2
P 1950 5450
F 0 "U?" H 1850 4750 60  0000 C CNN
F 1 "RFM22" H 2200 5950 60  0000 C CNN
F 2 "" H 1950 5450 60  0000 C CNN
F 3 "" H 1950 5450 60  0000 C CNN
	1    1950 5450
	1    0    0    -1  
$EndComp
Wire Wire Line
	4300 1200 3550 1200
Wire Wire Line
	3550 1200 3550 5550
Wire Wire Line
	3550 5550 4500 5550
Wire Wire Line
	4500 6000 4200 6000
Wire Wire Line
	4200 5550 4200 6200
Connection ~ 4200 5550
Wire Wire Line
	4200 6200 4500 6200
Connection ~ 4200 6000
Wire Wire Line
	3200 3450 3200 5700
Wire Wire Line
	3200 3450 4300 3450
Wire Wire Line
	4500 5650 3200 5650
Wire Wire Line
	1450 5050 1450 4600
Wire Wire Line
	1450 4600 3200 4600
Connection ~ 3200 4600
Wire Wire Line
	3550 4400 1250 4400
Wire Wire Line
	1250 4400 1250 6550
Wire Wire Line
	1250 5350 1450 5350
Connection ~ 3550 4400
Wire Wire Line
	1450 5250 1250 5250
Connection ~ 1250 5250
Wire Wire Line
	1450 5150 1250 5150
Connection ~ 1250 5150
$Comp
L R R?
U 1 1 57D88D43
P 3700 5850
F 0 "R?" V 3780 5850 50  0000 C CNN
F 1 "R" V 3700 5850 50  0000 C CNN
F 2 "" V 3630 5850 50  0000 C CNN
F 3 "" H 3700 5850 50  0000 C CNN
	1    3700 5850
	1    0    0    -1  
$EndComp
Wire Wire Line
	3700 5700 3700 5650
Connection ~ 3700 5650
Wire Wire Line
	3700 6000 3700 6300
Wire Wire Line
	3700 6300 4500 6300
Wire Wire Line
	4500 5750 3950 5750
Wire Wire Line
	3950 5750 3950 2850
Wire Wire Line
	3950 2850 4300 2850
Wire Wire Line
	4300 2700 3850 2700
Wire Wire Line
	3850 2700 3850 5850
Wire Wire Line
	3850 5850 4500 5850
Wire Wire Line
	1450 5600 1450 6350
Wire Wire Line
	1450 6350 2800 6350
Wire Wire Line
	2800 6350 2800 6050
Wire Wire Line
	2800 6050 2650 6050
Wire Wire Line
	2650 5950 2850 5950
Wire Wire Line
	2850 5950 2850 6450
Wire Wire Line
	2850 6450 1350 6450
Wire Wire Line
	1350 6450 1350 5500
Wire Wire Line
	1350 5500 1450 5500
Wire Wire Line
	2650 5650 2950 5650
Wire Wire Line
	2950 5650 2950 6550
Wire Wire Line
	2950 6550 1250 6550
Connection ~ 1250 5350
Wire Wire Line
	2650 5500 3650 5500
Wire Wire Line
	3650 5500 3650 2100
Wire Wire Line
	3650 2100 4300 2100
Wire Wire Line
	2650 5400 3800 5400
Wire Wire Line
	3800 5400 3800 3150
Wire Wire Line
	3800 3150 4300 3150
Wire Wire Line
	4300 3000 3700 3000
Wire Wire Line
	3700 3000 3700 5300
Wire Wire Line
	3700 5300 2650 5300
Wire Wire Line
	2650 5200 4100 5200
Wire Wire Line
	4100 5200 4100 3900
Wire Wire Line
	4100 3900 4300 3900
Wire Wire Line
	2650 5800 3050 5800
Wire Wire Line
	3050 5800 3050 4750
Wire Wire Line
	3050 4750 4200 4750
Wire Wire Line
	4200 4750 4200 4200
Wire Wire Line
	4200 4200 4300 4200
$EndSCHEMATC
