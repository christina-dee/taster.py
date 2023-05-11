import RPi.GPIO as GPIO

# Festlegung des GPIO-Pins für den Taster
btnStop = 11	# phys. Pin 7

# Festlegung des GPIO-Pin 22 als LED-Pin
redLED = 7 # phys. Pin 29

# Festlegung des GPIO-Pin-Modes
GPIO.setmode(GPIO.BOARD)

# Festlegung der Pins als Ein-/Ausgänge
GPIO.setup(redLED, GPIO.OUT)
GPIO.setup(btnStop, GPIO.IN)

try:
    while True:
        # einlesen und speichern des Tasterstatus
        btnState = GPIO.input(btnStop)
        if btnState == 1:
            GPIO.output(redLED, GPIO.HIGH)
        else:
            GPIO.output(redLED, GPIO.LOW)
        # Ausgabe des Tasterstatus
        print("Tasterstatus:", btnState)

except KeyboardInterrupt:
    print("\nAbbruch durch Benutzer.")
    GPIO.cleanup()
