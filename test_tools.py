import unittest
from system.tools import MapTools,LineTools
from entities.car import sensor
from shapely.geometry import LineString,Point,LinearRing,Polygon
class TestTools(unittest.TestCase):
    def test_isInside(self):
        points = [
            [0,0],
            [4,0],
            [4,4],
            [0,4]
        ]
        ring=Polygon(LinearRing(points))
        points2 = [
            [1,1],
            [1,3],
            [3,3],
            [3,1]
        ]
        ring2=Polygon(LinearRing(points2))
        line=LineString([(-1,1),(3,3)])
        print(ring)
        print(ring2)
        print("road")
        road=ring.difference(ring2)
        print(road)

        self.assertEqual(road.contains(Point(2,2)),False)
        self.assertEqual(road.contains(Point(0.5,0.5)),True)


    def test_loadArray(self):
        trackArray = [
            [1,0],
            [2,2],
            [5,4],
            [3,4],
            [3,5],
            [10,10]]

        t = MapTools()
        t.loadTrackArray(trackArray)

        self.assertEqual(t.track[2][1],4)
        self.assertEqual(t.track[3][1],4)
        self.assertEqual(t.track[3][0],3)
        #self.assertEquals(t.track[5][1],10)
        self.assertEqual(t.firstPoint,[10,10])
    
    def test_findClosest(self):
        trackArray = [
            [1,0],
            [2,2],
            [5,4],
            [3,4],
            [3,5],
            [10,10]]

        t = MapTools()
        t.loadTrackArray(trackArray)

        clPoint = t.findClosestPoint(t.firstPoint)

        self.assertEqual(clPoint,[5,4])
        t.usePoint(clPoint)
        self.assertEqual(t.usedPoints[len(t.usedPoints)-1],clPoint)
        t.create_line(t.firstPoint,clPoint)
        self.assertEqual(t.lines[0],[[10,10],[5,4]])

    def test_getLines(self):
        trackArray = [
            [1,0],
            [2,2],
            [5,4],
            [3,4],
            [3,5],
            [1,7],
            [3,8],
            [6,9],
            [7,2],
            [10,10]]

        t = MapTools()
        t.loadTrackArray(trackArray)
        t.outlineTrack()

        #print(t.lines)

    def test_sensors(self):
        sensors = []

        s = sensor(size=10,offset=0)
        s.p1 = [0,0]
        s.recalculatePoints()
        sensors.append(s)
        
        s = sensor(size=10,offset=90)
        s.p1 = [0,0]
        s.recalculatePoints()
        sensors.append(s)
        

        #sensors = [[[0,0],[10,0]],[[0,0],[0,10]]]
        lines = [[[8,-5],[2,5]]]
        
        t = LineTools(sensors=sensors,lines=lines)
        t.calculatePOIBox()
        t.getLinesInBox()
        print(t.getIntesections())


if __name__=='__main__':
    unittest.main()