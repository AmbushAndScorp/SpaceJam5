# from direct.showbase.ShowBase import ShowBase
# from direct.showbase.Loader import *
from CollideObjectBase import *
# from panda3d.core import NodePath
# from panda3d.core import Vec3

class Missile(SphereCollideObject):
    # empty definitions for the missiles, plus the amount of missiles
    fireModels = {}
    cNodes = {}
    collisionSolids = {}
    Intervals = {}
    missileCount = 0

    # set up for making the missiles
    def __init__(self, loader: Loader, modelPath: str, parentNode: NodePath, nodeName: str, texPath: str, posVec: Vec3, scaleVec: float = 1.0):
        super(Missile, self).__init__(loader, modelPath, parentNode, nodeName, Vec3(0,0,0), 3.0)
        self.modelNode.setScale(scaleVec)
        self.modelNode.setPos(posVec)
#         Missile.missileCount += 1
#         Missile.fireModels[nodeName] = self.modelNode
#         Missile.cNodes[nodeName] = self.collisionNode

#         Missile.collisionSolids[nodeName] = self.collisionNode.node().getSolid(0)
#         Missile.cNodes[nodeName].show()
#         print("Fire missle #" + str(Missile.missileCount))