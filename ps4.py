import SpiderG
from pyPS4Controller.controller import Controller 
import robotLight 
import switch

light = robotLight.RobotLight()
light.setColor(255, 255, 255)

#color rgb values
white = [255, 255, 255]
red = [255, 0, 0]
green = [0, 255, 0]
blue = [0, 0, 255]
purple = [106, 13, 173]
yellow = [255, 255, 0]
pink = [255, 105, 180]
orange = [255, 100, 0]

colors = [white, red, green, blue, purple, yellow, pink, orange]

index = 0
onOffS = True
onOffW = True

class MyController(Controller):

    def __init__(self, **kwargs):
        Controller.__init__(self, **kwargs)
#take input to make bot move, as well as lean, crouch, and stand
    def on_up_arrow_press(self):
        SpiderG.walk('forward')

    def on_down_arrow_press(self):
        SpiderG.walk('backward')

    def on_left_arrow_press(self):
        SpiderG.walk('turnleft')

    def on_right_arrow_press(self):
        SpiderG.walk('turnright')

    def on_x_press(self):
        SpiderG.walk('StayLow')
        
    def on_triangle_press(self):
        SpiderG.walk('StandUp')

    def on_square_press(self):
        SpiderG.walk('Lean-L')

    def on_circle_press(self):
        SpiderG.walk('Lean-R')

    def on_L1_press(self):
        SpiderG.status_GenOut(0, 150, 0)
        SpiderG.direct_M_move()

    def on_R1_press(self):
        SpiderG.status_GenOut(0, -150, 0)
        SpiderG.direct_M_move()

    #flash "head light"
    def on_share_release(self):
        switch.switch(1, 1)

    #Toggles steady mode on and off
    def on_options_release(self):
        global onOffS
        if onOffS:
            SpiderG.steadyModeOn()
            onOffS = False
        else:
            SpiderG.steadyModeOff()
            onOffS = True

    #cycle through different light colors
    def on_L3_release(self):
        global index
        r, g, b = colors[index]
        light.setColor(r, g, b)
        index += 1
        if (index == len(colors)):
            index = 0
        
#reset bot to default position after pressing buttons
    def on_L1_release(self):
        SpiderG.move_init()

    def on_R1_release(self):
        SpiderG.move_init()

    def on_square_release(self):
        SpiderG.move_init()

    def on_circle_release(self):
        SpiderG.move_init()

    def on_x_release(self):
        SpiderG.move_init()

    def on_triangle_release(self):
        SpiderG.move_init()

    def on_up_down_arrow_release(self):
        SpiderG.servoStop()

    def on_left_right_arrow_release(self):
        SpiderG.servoStop()
#resets bot to default position
    def on_R3_release(self):
        SpiderG.move_init()
    
controller = MyController(interface="/dev/input/js0", connecting_using_ds4drv=False)
while True:
    controller.listen(timeout=300)
