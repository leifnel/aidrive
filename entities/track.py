import pyglet
import config
import math
import numpy as np
from PIL import Image, ImageFilter
from system.tools import MapTools
from shapely.geometry import LinearRing,Point,Polygon

class Track():
    def __init__(self, *args, **kwargs):
        self.border_image = pyglet.image.load('assets\\images\\track1\\background.png')
        self.tarmac_image = pyglet.image.load('assets\\images\\track1\\tarmac.png')
        self.border_sprite = pyglet.sprite.Sprite(self.border_image, 0, 0)
        self.tarmac_sprite = pyglet.sprite.Sprite(self.tarmac_image, 0, 0)
        self.border_sprite.update(scale=1.3)
        self.tarmac_sprite.update(scale=1.3)
        self.coords_map = []
        self.lines = np.load('track1.npy')
        #self.getShape()
        self.linerings_found = False
        self.linerings = []

    def isInside(self, px, py):
        pass
        self.hits=0
        self.n=0
        for ring in self.linerings:
            self.n+=1
            if ring.contains(Point(px,py)):
        #        print("Inside ring ",self.n)
                self.hits+=1
        return self.hits

    def getShape(self):
        img = Image.open('assets\\images\\track1\\trackmask.jpg')
        
        img = img.resize((self.tarmac_sprite.width, self.tarmac_sprite.height))
        edges = img.filter(ImageFilter.FIND_EDGES)
        arr = np.array(edges)
    
        point_map = np.empty([self.tarmac_sprite.height,self.tarmac_sprite.width])

        drawCount = 0

        for i,row in enumerate(arr):
            if (i == 0) or (i == len(arr)-1):
                for j,pixel in enumerate(row): #Reset the first and the last row of the image
                    arr[i][j] = [0,0,0]
                    point_map[i][j] = 0
            for j,pixel in enumerate(row):
                if (j == 0) or (j == len(row)-1): #reset the first and last pixels of 
                    arr[i][j] = [0,0,0]
                    point_map[i][j] = 0
                else:
                    if(np.sum(pixel)<250): # if there is something less than half in the pixel make it disappear
                        arr[i][j] = [0,0,0]
                        point_map[i][j] = 0
                    else:                   #else make it a point
                        arr[i][j] = [255,255,255]
                        point_map[i][j] = 1
                        
                        # self.coords_map.append([j,self.tarmac_sprite.height-i])    

                        if(drawCount>5):       #collect thined out points and append them to the coords_map
                            drawCount = 0
                            self.coords_map.append([j,self.tarmac_sprite.height-i])
                        else:
                            drawCount+=1
                    
        
        t = MapTools()
        t.loadTrackArray(self.coords_map)
        t.outlineTrack()

        self.lines = t.lines
        
        self.lines = t.thinLines(self.lines)
        self.lines = t.thinLines(self.lines)
        self.lines = t.thinLines(self.lines)

        
        print(len(self.lines))
        

        #print(self.coords_map)
                #print(coords_map)

               
                # for k,val in enumerate(pixel):
                #     if(val<127):
                #         arr[i][j][k]=0
                #     else:
                #         arr[i][j][k]=255
    def draw_outline(self):
        #draw coordsmap\
        #print(len(self.coords_map))
        for line in self.lines:
            pyglet.graphics.draw(2,pyglet.gl.GL_LINES,
                ('v2i', (line[0][0],line[0][1],line[1][0],line[1][1])),
                ('c3B', (255, 0, 0,255, 0, 0))
            )

        #     pyglet.graphics.draw(1,pyglet.gl.GL_POINTS,
        #         ('v2i', (line[0][0],line[0][1])),
        #         ('c3B', (255, 0, 0))
        #     )

        #     pyglet.graphics.draw(1,pyglet.gl.GL_POINTS,
        #         ('v2i', (line[1][0],line[1][1])),
        #         ('c3B', (255, 0, 0))
        #     )
        
        #print(*arr[250], sep = "\n") 




        # for point in self.coords_map:
        #     pyglet.graphics.draw(1,pyglet.gl.GL_POINTS,
        #         ('v2i', (point[0],point[1])),
        #         ('c3B', (255, 0, 0))
        #     )

        #Image.fromarray(arr).show()

        # for i in arr:
        #     for j in i:
        #         for k in j:
        #             if (arr[i][j][k]<127):
        #                 arr[i][j][k] = 0
        #             else:
        #                 arr[i][j][k] = 255

        # 
        

    def draw_self(self):
        
        pass
        self.border_sprite.draw()
        self.tarmac_sprite.draw()
        # pyglet.graphics.draw(2, pyglet.gl.GL_LINES,
        # ('v2i', ([100, 150, 100,300 ]))
        # )

    def find_linerings(self):
        if self.linerings_found:
            return
        # t = MapTools()
        firstpoint=self.lines[0][0]
        points=[]
        previousEnd =firstpoint[1]
        print("First point:",firstpoint)
        self.linerings_found = True
        for line in self.lines:
            # print (line[0],line[1],line[0]==previousEnd,end='')
            if points==[] or (line[0]==previousEnd).all():
                points.append(line[1])
            else: 
                ring=Polygon(LinearRing(points))
#                print("Ring length:",len(ring.coords))
                #pyglet.graphics.draw(len(ring.coords), pyglet.gl.GL_LINE_LOOP,ring)
                self.linerings.append(ring)
                print(ring)
                points=[]

            previousEnd=line[1]
        if points!=[]:
            ring=LinearRing(points)
            self.linerings.append(ring)




