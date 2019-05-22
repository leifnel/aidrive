import pyglet
import config
from system.component import Component
from entities.car import Car
from entities.track import Track
from pyglet.window import key, FPSDisplay
from random import randint, choice
from system.tools import LineTools
car = Car(x=500, y=90, speed=0, maxspeed=4, heading=270,sensors=False)
track = Track()
detectedlines = LineTools(sensors = car.sensors, lines = track.lines)

class Window(pyglet.window.Window):
    def __init_(self,*args,**kwargs):
        super().__init__(*args,**kwargs)
        self.set_minimum_size(300,200)


def draw():
    window.clear()
    #track.draw_self()
    #track.draw_outline()
    dlines = detectedlines.getLinesInBox()
    for line in dlines:
        pyglet.graphics.draw(2,pyglet.gl.GL_LINES,
            ('v2i', (line[0][0],line[0][1],line[1][0],line[1][1])),
            ('c3B', (255, 0, 0,255, 0, 0))
        )

    intersections = detectedlines.getIntesections()
    count = 0
    for s in car.sensors:
        count+=1
        text = '{}:{}'.format(s.offset,s.distance)
        label = pyglet.text.Label(text,
                          font_name='Times New Roman',
                          font_size=18,
                          x=20, y=0+(50*count),
                          anchor_x='left', anchor_y='center')
    #print(len(intersections))
        label.draw()        
    for ipoint in intersections:
        
         pyglet.graphics.draw(5,pyglet.gl.GL_POINTS,
            ('v2f', (
            ipoint[1],ipoint[0],
            ipoint[1]+1,ipoint[0],
            ipoint[1],ipoint[0]+1,
            ipoint[1]-1,ipoint[0],
            ipoint[1],ipoint[0]-1)),
            ('c3B', (0, 255, 0,0, 255, 0,0, 255, 0,0, 255, 0,0, 255, 0))
        )
    print(car.x,car.y)
    car.draw_self()
    

def update(time):
    if isinstance(car, Component):
        car.update_self()
        detectedlines.updatePOI(car.x,car.y)

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