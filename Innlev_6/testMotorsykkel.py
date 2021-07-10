from motorsykkel import Motorsykkel


def hovedprogram():
    motor1 = Motorsykkel("Honda",123,10)
    motor1.kjor(1)
    motor1.hentKilometerstand()
    motor1.SkrivUt()

hovedprogram()