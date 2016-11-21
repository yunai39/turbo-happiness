from motor import Motor

"""
    Class chariot
    Un chariot est composé de deux moteur
    Ces deux moteur permettent d'avance, de reculer, de tourné etc...
"""
class Chariot:
    def __init__(self, rightMotor: Motor, leftMotor: Motor):
        self.rightMotor = rightMotor
        self.leftMotor = leftMotor
        self.rightMotor.initMotor()
        self.leftMotor.initMotor()
        self.isGoingForward = True
        self.isStarted = False

    """
        Démarrer le charriot
    """
    def start(self):
        if not self.isStarted:
            self.rightMotor.start()
            self.leftMotor.start()

    """
        Arrêter le charriot
    """
    def stop(self):
        if self.isStarted:
            self.rightMotor.stop()
            self.leftMotor.stop()

    """
        Accélère le charriot
    """
    def goFaster(self):
        self.rightMotor.speedUp()
        self.leftMotor.speedUp()

    """
        Ralenti le charriot
    """
    def goSlower(self):
        self.rightMotor.slowDown()
        self.leftMotor.slowDown()

    """
        Tourne à droite
    """
    def turnRight(self):
        self.rightMotor.slowDown()
        self.leftMotor.speedUp()

    """
        Tourne à gauche
    """
    def turnLeft(self):
        self.leftMotor.slowDown()
        self.rightMotor.speedUp()

    """
        Inverse les moteurs
    """
    def switchDirection(self):
        self.isGoingForward = not self.isGoingForward
        self.rightMotor.reverse()
        self.leftMotor.reverse()
