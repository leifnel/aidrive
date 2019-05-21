import math
import numpy as np

class MapTools():
    def __init__(self, *args, **kwargs):
        self.track = []
        self.usedPoints = []
        self.unusedPoints = []
        self.lines = []
        self.firstPoint = []
        self.lastPoint = []

    def loadTrackArray(self,track):
        self.track = track
        self.unusedPoints = self.track
        self.firstPoint = self.unusedPoints.pop()
        self.lastPoint = self.firstPoint
        self.usedPoints.append(self.firstPoint)
    

    def findClosestPoint(self,point):
        print("looking for ", point,len(self.unusedPoints))
        
        min_dist = 100000000000
        
        for i,p in enumerate(self.unusedPoints):
            distance = math.sqrt((p[0]-point[0])**2)+((p[1]-point[1])**2)
            if(min_dist>distance):
                candidate = p
                min_dist = min(min_dist,distance)
        return candidate

    def create_line(self, p1,p2):
        self.lines.append([p1,p2])

    def usePoint(self,point):
        self.unusedPoints.remove(point)
        self.usedPoints.append(point)
        self.lastPoint = point

    def outlineTrack(self):
        while len(self.unusedPoints)>0:
            clPoint = self.findClosestPoint(self.lastPoint)
            self.create_line(self.lastPoint, clPoint)
            self.usePoint(clPoint)
        
        self.create_line(self.lastPoint, self.firstPoint)

        