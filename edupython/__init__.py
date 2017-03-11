from gpiozero import *

red = LED(2)
yellow = LED(3)
green = LED(4)
button = Button(17)
bz = Buzzer(22)

class kit1:
    class red:
        class led:
            def on():
                red.on()
            def off():
                red.off()
    class yellow:
        class led:
            def on():
                yellow.on()
            def off():
                yellow.off()
    class green:
        class led:
            def on():
                green.on()
            def off():
                green.off()

    class button:
        def pressed():
            button.wait_for_press()

    class buzzer:
        
        def on():
            bz.on()
        def off():
            bz.off()

    
            
