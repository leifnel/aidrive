import unittest
from system.tools import MapTools

class TestTools(unittest.TestCase):
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

        print(t.lines)


if __name__=='__main__':
    unittest.main()