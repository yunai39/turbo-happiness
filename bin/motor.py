import RPi.GPIO as GPIO

class Motor:
    name = 'motor1'
    direction = True
    gpioDirection = 0
    gpioPWM = 0
    pwmFrequency = 100
    pwmRapport = 50
    isStarted = False

    def __init__(self, name, gpioDirection, gpioPWM, pwmFrequency = 100):
        self.name = name
        self.pwmFrequency = pwmFrequency
        self.gpioDirection = gpioDirection
        self.gpioPWM = gpioPWM
        self.initMotor()

    def initMotor(self):
        GPIO.setmode(GPIO.BOARD)
        GPIO.setup(self.gpioDirection, GPIO.OUT)
        GPIO.setup(self.gpioPWM, GPIO.OUT)
	GPIO.output(self.gpioDirection, GPIO.LOW)

    def getName(self):
        return self.name

    """
        Permet de changer le rapport
    """
    def setPwmRapport(self, pwmRapport):
        self.pwmRapport = pwmRapport
        return self

    def start(self):
        if(self.isStarted == False):
            self.isStarted = True
            self.p = GPIO.PWM(10, 10)
            self.p.start(50)
        return self

    def stop(self):
        if(self.isStarted == True):
            self.isStarted = False
            self.p.stop()
        return self

    def clear(self):
        GPIO.cleanup()
        return self

    """
        Permet d'inverse le sens du moteur
    """
    def reverse(self, start = False):
        if(self.isStarted == True):
            self.isStarted = False
            self.stop()
        self.direction = not self.direction
        if(self.direction == True):
            GPIO.output(self.gpioDirection, GPIO.LOW)
        if(self.direction == True):
            GPIO.output(self.gpioDirection, GPIO.HIGH)
        if(start):
            self.start()
            self.isStarted = True
        return self
