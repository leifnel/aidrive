import pyglet
import config
from system.component import Component
from entities.car import Car
from entities.track import Track
from pyglet.window import key, FPSDisplay
from random import randint, choice
from system.tools import MapTools

car = Car(x=500, y=90, speed=0, maxspeed=4, heading=270)
track = Track()

class Window(pyglet.window.Window):
    def __init_(self,*args,**kwargs):
        super().__init__(*args,**kwargs)
        self.set_minimum_size(300,200)
        track.draw_outline()


def draw():
    window.clear()
    #track.draw_self()
    
    car.draw_self()
    

def update(time):
    if isinstance(car, Component):
        car.update_self()

if __name__ == '__main__' :

    window = pyglet.window.Window(width=config.window_width,height=config.window_height,caption='pyCar',resizable=False)

    @window.event
    def on_draw():
        draw()

    @window.event
    def on_key_press(symbol, modifiers):
        if symbol == key.UP:
            car.accelerate(0.05)
        elif symbol == key.LEFT:
            car.turn(-5)
        elif symbol == key.RIGHT:
            car.turn(5)
        elif symbol == key.DOWN:
            car.accelerate(-0.1)

    @window.event
    def on_key_release(symbol, modifiers):
        if symbol == key.UP:
            car.accelerate(0)
        elif symbol == key.LEFT:
            car.turn(0)
        elif symbol == key.RIGHT:
            car.turn(0)
        elif symbol == key.DOWN:
            car.accelerate(0)

    
    pyglet.clock.schedule_interval(update, 1/60.0)
    pyglet.app.run()