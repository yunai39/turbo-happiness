import RPi.GPIO as GPIO

"""
    Class motor
    Controle d'un moteur
"""


class Motor:
    name = 'motor1'
    direction = True
    pwmFrequency = 100
    pwmRapport = 30
    isStarted = False

    def __init__(self, name: str, gpioDirection: int, gpioDirection2: int, pwmRapport: int, pwmFrequency: int = 100):
        self.name = name
        self.pwmFrequency = pwmFrequency
        self.gpioDirection = gpioDirection
        self.gpioDirection2 = gpioDirection2
        self.pwmRapport = pwmRapport
        self.initMotor()

    def initMotor(self):
        GPIO.setmode(GPIO.BOARD)
        GPIO.setup(self.gpioDirection, GPIO.OUT)
        GPIO.setup(self.pwmRapport, GPIO.OUT)
        GPIO.output(self.gpioDirection, GPIO.LOW)
        GPIO.setup(self.gpioDirection2, GPIO.OUT)
        GPIO.output(self.gpioDirection, GPIO.HIGH)

    def getName(self):
        return self.name

    """
        Permet de changer le rapport
    """

    def setPwmRapport(self, pwmRapport: int):
        self.pwmRapport = pwmRapport
        return self

    """
        Permet de démarrer
    """

    def start(self):
        if (self.isStarted == False):
            self.isStarted = True
            self.p = GPIO.PWM(10, 10)
            self.p.start(self.pwmRapport)
        return self

    """
        Permet d'arreter
    """

    def stop(self):
        if (self.isStarted == True):
            self.isStarted = False
            self.p.stop()
        return self

    def clear(self):
        GPIO.cleanup()
        return self

    """
        Permet de ralentir
    """

    def slowDown(self):
        if (self.pwmRapport > 2):
            self.pwmRapport = self.pwmRapport - 2
        self.p.ChangeFrequency(self.pwmRapport)

    """
        Permet d'accélerer
    """

    def speedUp(self):
        if (self.pwmRapport < 98):
            self.pwmRapport = self.pwmRapport + 2
        self.p.ChangeFrequency(self.pwmRapport)

    """
        Permet d'inverse le sens du moteur
    """

    def reverse(self, start: bool=False):
        if (self.isStarted == True):
            self.isStarted = False
            self.stop()
        self.direction = not self.direction
        if (self.direction == False):
            GPIO.output(self.gpioDirection, GPIO.LOW)
            GPIO.output(self.gpioDirection2, GPIO.HIGH)
        else:
            GPIO.output(self.gpioDirection, GPIO.HIGH)
            GPIO.output(self.gpioDirection2, GPIO.LOW)
        if (start):
            self.start()
            self.isStarted = True
        return self
