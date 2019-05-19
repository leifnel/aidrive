import pyglet
from system.component import Component
import config
import math


class Car(Component):

    def __init__(self, *args, **kwargs):
        """
        Creates a sprite using a car image.
        """
        super(Car, self).__init__(*args, **kwargs)
        self.speed = kwargs.get('speed', 0)
        self.maxspeed = kwargs.get('maxspeed',5)
        self.minspeed = kwargs.get('minspeed',-1)
        self.orientation = kwargs.get('heading',0)
        self.steering=0
        self.throttle=0
        self.acceleration=0
        self.car_image = pyglet.image.load('assets\\images\\Audi.png')
        self.car_image.anchor_x=self.car_image.width//2
        self.car_image.anchor_y=self.car_image.height//2
        #self.width = self.car_image.width
        #self.height = self.car_image.height
        self.car_sprite = pyglet.sprite.Sprite(self.car_image, self.x, self.y)

        

        self.car_sprite.update(scale=0.15)
        self.width = self.car_sprite.width
        self.height = self.car_sprite.height
        
        self.x_direction = 0
        self.y_direction = 1

        print('Car Created')

    def update_self(self):
        """
        Increments x and y value and updates position.
        Also ensures that the car does not leave the screen area by changing its axis direction
        :return:
        """

        if (self.acceleration==0) and (self.speed!=0):
            if self.speed > 0 :
                self.speed-=0.02
            elif self.speed < 0 :
                self.speed+=0.02

        self.speed+=self.acceleration

        self.speed = round(self.speed,2)
        if(self.speed > self.maxspeed):
            self.speed = self.maxspeed

        if(self.speed < self.minspeed):
            self.speed = self.minspeed

        self.orientation+=self.steering
        angle = math.radians(self.orientation)

        [self.y_direction,self.x_direction] = [self.speed * math.cos(angle), self.speed * math.sin(angle)]

        self.car_sprite.update(rotation=self.orientation)
        
        if self.x < 0 or (self.x + self.width) > config.window_width:
            self.x_direction *= -1

        if self.y < 0 or (self.y + self.height) > config.window_height:
            self.y_direction *= -1


        if(self.speed > 0):
            self.x += (self.speed * self.x_direction)
            self.y += (self.speed * self.y_direction)
        else:
            self.x -= (self.speed * self.x_direction)
            self.y -= (self.speed * self.y_direction)
        self.car_sprite.set_position(self.x, self.y)

        
    def draw_self(self):
        """
        Draws our car sprite to screen
        :return:
        """

        self.draw_line(self.x,self.y,self.orientation,200)
        self.draw_line(self.x,self.y,self.orientation-25,100)
        self.draw_line(self.x,self.y,self.orientation+25,100)
        self.draw_line(self.x,self.y,self.orientation-45,75)
        self.draw_line(self.x,self.y,self.orientation+45,75)
        self.draw_line(self.x,self.y,self.orientation-90,50)
        self.draw_line(self.x,self.y,self.orientation+90,50)
        self.draw_line(self.x,self.y,self.orientation+180,50)
        self.car_sprite.draw()

    def accelerate(self,value):
        self.acceleration=value

    def turn(self,value):
        self.steering=value

    def draw_line(self,x,y,orientation,size):
        angle = math.radians(orientation)
        pyglet.graphics.draw(2, pyglet.gl.GL_LINES,
            ('v2f', (x, y, x+size*math.sin(angle), y+size*math.cos(angle)))
        )