# -*- coding:utf-8 -*-
import unittest
import maya.cmds as cmds
import maya.mel as mel
import metan.core as mtn

from metan.datatype.euler import EulerRotation
from metan.datatype.matrix import Matrix
from metan.datatype.quaternion import Quaternion
from metan.datatype.vector import Vector


class TestScene(unittest.TestCase):

    def test_get(self):
        cmds.file(new=True, f=True)
        cube = cmds.polyCube()[0]
        print cube
        m = mtn.M(u"pCube1")

        print 'm.t.get()', m.t.get()
        print 'm.translate.get()', m.translate.get()
        print 'm.tx.get()', m.tx.get()
        print 'm.translateX.get()', m.translateX.get()
        print 'm.t.x.get()', m.t.x.get()
        print 'm.translate.x.get()', m.translate.x.get()
        print 'm.t.tx.get()', m.t.tx.get()
        print 'm.translate.translateX.get()', m.translate.translateX.get()
        print " "
        print 'm.attr("t").get()', m.attr("t").get()
        print 'm.attr("translate").get()', m.attr("translate").get()
        print 'm.attr("tx").get()', m.attr("tx").get()
        print 'm.attr("translateX").get()', m.attr("translateX").get()
        print 'm.attr("t").x.get()', m.attr("t").x.get()
        print 'm.attr("translate").x.get()', m.attr("translate").x.get()
        print 'm.attr("t").tx.get()', m.attr("t").tx.get()
        print 'm.attr("translate").tx.get()', m.attr("translate").tx.get()
        print 'm.attr("t").attr("x").get()', m.attr("t").attr("x").get()
        print 'm.attr("translate").attr("x").get()', m.attr("translate").attr("x").get()
        print 'm.attr("t").attr("tx").get()', m.attr("t").attr("tx").get()
        print 'm.attr("translate").attr("translateX").get()', m.attr("translate").attr("translateX").get()
        print " "
        print 'm.m.get()', m.m.get()
        print 'm.matrix.get()', m.matrix.get()
        print 'm.pim.get()', m.pim.get()
        print 'm.parentInverseMatrix.get()', m.parentInverseMatrix.get()
        print 'm.pim[0].get()', m.pim[0].get()
        print 'm.parentInverseMatrix[0].get()', m.parentInverseMatrix[0].get()
        print 'm.attr("pim").get()', m.attr("pim").get()
        print 'm.attr("parentInverseMatrix").get()', m.attr("parentInverseMatrix").get()
        print 'm.attr("pim")[0].get()', m.attr("pim")[0].get()
        print 'm.attr("parentInverseMatrix")[0].get()', m.attr("parentInverseMatrix")[0].get()
        print 'm.attr("pim[0]").get()', m.attr("pim[0]").get()
        print 'm.attr("parentInverseMatrix[0]").get()', m.attr("parentInverseMatrix[0]").get()

        assert(repr(m.t.getChildren()) == u'[Attribute("pCube1.translateX"), Attribute("pCube1.translateY"), Attribute("pCube1.translateZ")]')

        print "="*20

        cmds.circle()
        m = mtn.M(u"nurbsCircleShape1")
        assert(m.wn.get() == [[0.0, 0.0, 1.0]])
        assert(m.attr("wn").get() == [[0.0, 0.0, 1.0]])
        assert(m.worldNormal.get() == [[0.0, 0.0, 1.0]])
        assert(m.attr("worldNormal").get() == [[0.0, 0.0, 1.0]])
        assert(m.wn[0].get() == [0.0, 0.0, 1.0])
        assert(m.attr("wn")[0].get() == [0.0, 0.0, 1.0])
        assert(m.attr("wn[0]").get() == [0.0, 0.0, 1.0])
        assert(m.worldNormal[0].get() == [0.0, 0.0, 1.0])
        assert(m.attr("worldNormal")[0].get() == [0.0, 0.0, 1.0])
        assert(m.attr("worldNormal[0]").get() == [0.0, 0.0, 1.0])
        assert(m.wn.wnx.get() == 0.0)
        assert(m.attr("wn").wnx.get() == 0.0)
        assert(m.attr("wn").attr("wnx").get() == 0.0)
        assert(m.worldNormal.wnx.get() == 0.0)
        assert(m.attr("worldNormal").wnx.get() == 0.0)
        assert(m.attr("worldNormal").attr("wnx").get() == 0.0)
        assert(m.worldNormal.worldNormalX.get() == 0.0)
        assert(m.attr("worldNormal").worldNormalX.get() == 0.0)
        assert(m.attr("worldNormal").attr("worldNormalX").get() == 0.0)
        assert(m.wn.x.get() == 0.0)
        assert(m.attr("wn").x.get() == 0.0)
        assert(m.attr("wn").attr("x").get() == 0.0)
        assert(m.worldNormal.x.get() == 0.0)
        assert(m.attr("worldNormal").x.get() == 0.0)
        assert(m.attr("worldNormal").attr("x").get() == 0.0)
        assert(m.worldNormal[0].wnx.get() == 0.0)
        assert(m.attr("worldNormal")[0].wnx.get() == 0.0)
        assert(m.attr("worldNormal")[0].attr("wnx").get() == 0.0)
        assert(m.attr("worldNormal[0]").wnx.get() == 0.0)
        assert(m.attr("worldNormal[0]").attr("wnx").get() == 0.0)
        assert(m.worldNormal[0].x.get() == 0.0)
        assert(m.attr("worldNormal")[0].x.get() == 0.0)
        assert(m.attr("worldNormal")[0].attr("x").get() == 0.0)
        assert(m.attr("worldNormal[0]").x.get() == 0.0)
        assert(m.attr("worldNormal[0]").attr("x").get() == 0.0)
        assert(m.worldNormal[0].worldNormalX.get() == 0.0)
        assert(m.attr("worldNormal")[0].worldNormalX.get() == 0.0)
        assert(m.attr("worldNormal")[0].attr("worldNormalX").get() == 0.0)
        assert(m.attr("worldNormal[0]").worldNormalX.get() == 0.0)
        assert(m.attr("worldNormal[0]").attr("worldNormalX").get() == 0.0)
        assert(m.mmv.get() == [0.0, 8.0])
        assert(m.minMaxValue.get() == [0.0, 8.0])
        assert(m.obcc.get() == [0.0, 0.0, 0.0])
        assert(m.attr("obcc").get() == [0.0, 0.0, 0.0])
        assert(m.objectColorRGB.get() == [0.0, 0.0, 0.0])
        assert(m.attr("objectColorRGB").get() == [0.0, 0.0, 0.0])
        assert(m.obcc.obcr.get() == 0.0)
        assert(m.attr("obcc").obcr.get() == 0.0)
        assert(m.attr("obcc").attr("obcr").get() == 0.0)
        assert(m.objectColorRGB.obcr.get() == 0.0)
        assert(m.attr("objectColorRGB").obcr.get() == 0.0)
        assert(m.attr("objectColorRGB").attr("obcr").get() == 0.0)
        assert(m.objectColorRGB.objectColorR.get() == 0.0)
        assert(m.attr("objectColorRGB").attr("objectColorR").get() == 0.0)
        assert(m.objectColorR.get() == 0.0)
        assert(m.attr("objectColorR").get() == 0.0)

        m = mtn.M(u"pCubeShape1")
        assert(m.vertexColor[0].vertexFaceColor[0].get() == [[0.0, 0.0, 0.0], 1.0])
        assert(m.attr("vertexColor")[0].vertexFaceColor[0].get() == [[0.0, 0.0, 0.0], 1.0])
        assert(m.attr("vertexColor")[0].attr("vertexFaceColor")[0].get() == [[0.0, 0.0, 0.0], 1.0])
        assert(m.attr("vertexColor[0]").attr("vertexFaceColor")[0].get() == [[0.0, 0.0, 0.0], 1.0])
        assert(m.attr("vertexColor[0]").attr("vertexFaceColor[0]").get() == [[0.0, 0.0, 0.0], 1.0])
        assert(m.vertexColor[0].vertexFaceColor[0].vertexFaceColorRGB.get() == [0.0, 0.0, 0.0])
        assert(m.vertexColor[0].vertexFaceColor[0].attr("vertexFaceColorRGB").get() == [0.0, 0.0, 0.0])
        assert(m.vertexColor[0].attr("vertexFaceColor")[0].vertexFaceColorRGB.get() == [0.0, 0.0, 0.0])
        assert(m.attr("vertexColor")[0].vertexFaceColor[0].vertexFaceColorRGB.get() == [0.0, 0.0, 0.0])
        assert(m.attr("vertexColor")[0].attr("vertexFaceColor")[0].vertexFaceColorRGB.get() == [0.0, 0.0, 0.0])
        assert(m.attr("vertexColor")[0].attr("vertexFaceColor")[0].attr("vertexFaceColorRGB").get() == [0.0, 0.0, 0.0])
        assert(m.attr("vertexColor[0]").attr("vertexFaceColor")[0].attr("vertexFaceColorRGB").get() == [0.0, 0.0, 0.0])
        assert(m.attr("vertexColor[0]").attr("vertexFaceColor[0]").attr("vertexFaceColorRGB").get() == [0.0,0.0,0.0])

        assert(m.vertexColor[0].vertexFaceColor[0].vertexFaceColorRGB.vertexFaceColorB.get() == 0.0)

        mel.eval("curve -d 3 -p -6.875966 0 1.086021 -p -5.392687 0 2.925972 -p -2.426129 0 6.605875 \
         -p 5.887674 0 7.227014 -p 2.9318 0 2.277118 -p -8.971029 0 -5.450958 -p 1.340971 0 4.394752 \
         -p -1.974355 0 6.056083 -p -3.632019 0 6.886748 -k 0 -k 0 -k 0 -k 1 -k 2 -k 3 -k 4 -k 5 -k 6 -k 6 -k 6 ;")
        m = mtn.M(u"curveShape1")
        assert(m.cp.name() == u"curveShape1.controlPoints")
        assert(m.attr("cp").name() == u"curveShape1.controlPoints")
        assert(m.attr("controlPoints").name() == u"curveShape1.controlPoints")
        assert(m.cp.size() == 9)
        assert(m.attr("cp").size() == 9)
        assert(m.attr("controlPoints").size() == 9)
        assert(len(m.cp) == 9)
        assert(len(m.attr("cp")) == 9)
        assert(len(m.attr("controlPoints")) == 9)
        for a in m.controlPoints:
            print a.name(), a.get()


        assert(mtn.M(u"pCube1.t").name() == u'pCube1.translate')
        assert(mtn.M(u"pCube1.translate").name() == u'pCube1.translate')
        assert(mtn.M(u"pCube1.t.tx").name() == u'pCube1.translateX')
        assert(mtn.M(u"pCube1.translate.translateX").name() == u'pCube1.translateX')
        assert(mtn.M(u"pCube1.tx").name() == u'pCube1.translateX')
        assert(mtn.M(u"pCube1.translateX").name() == u'pCube1.translateX')
        assert(mtn.M(u"pCube1.wm").name() == u'pCube1.worldMatrix')
        assert(mtn.M(u"pCube1.wm[0]").name() == u'pCube1.worldMatrix[0]')

        assert(mtn.M(u"pCubeShape1.vertexColor.vertexFaceColor.vertexFaceColorRGB.vertexFaceColorB").name()
                == u'pCubeShape1.vertexColor[0].vertexFaceColor[0].vertexFaceColorB')

        assert(mtn.M(u"pCubeShape1.vertexColor[0].vertexFaceColor[0].vertexFaceColorRGB.vertexFaceColorB").name()
               == u'pCubeShape1.vertexColor[0].vertexFaceColor[0].vertexFaceColorB')



    def test_types(self):
        print("start : node type test.")
        cmds.file(new=True, f=True)

        m = mtn.M(cmds.polyCube()[0])
        _name = m.name()
        m2 = mtn.M(_name)
        assert(m.nodeType() == u'transform')
        assert(hash(m) == hash(m2))
        assert(hash(m.t) == hash(m2.attr("t")))
        assert(hash(m.translate) == hash(m2.attr("t")))
        assert(hash(m.t) == hash(m2.attr("translate")))
        assert(hash(m.t.tx) == hash(m2.attr("translate").tx))
        assert(hash(m.tx) == hash(m2.attr("translate").attr("tx")))
        assert(hash(m.translateX) == hash(m2.attr("translate").attr("tx")))
        assert(hash(m.pim) == hash(m2.attr("pim")))
        assert(hash(m.pim) == hash(m2.pim))
        assert(hash(m.pim[0]) != hash(m2.pim))
        assert(hash(m.pim[0]) == hash(m2.pim[0]))
        assert(hash(mtn.M(_name+".translateX")) == hash(mtn.M(_name).attr("t").attr("tx")))
        assert(hash(mtn.M(_name+".translateX")) == hash(mtn.M(_name).attr("t.translateX")))
        assert(m == m2)
        assert(m.t == m2.attr("t"))
        assert(m.translate == m2.attr("t"))
        assert(m.t == m2.attr("translate"))
        assert(m.t.tx == m2.attr("translate").tx)
        assert(m.tx == m2.attr("translate").attr("tx"))
        assert(m.translateX == m2.attr("translate").attr("tx"))
        assert(m.pim == m2.attr("pim"))
        assert(m.pim == m2.pim)
        assert(m.pim[0] != m2.pim)
        assert(m.pim[0] == m2.pim[0])
        assert(mtn.M(_name+".translateX") == mtn.M(_name).attr("t").attr("tx"))
        assert(mtn.M(_name+".translateX") == mtn.M(_name).attr("t.translateX"))

        j = mtn.M(cmds.createNode(u"joint"))
        assert(j.nodeType() == u'joint')

        t = mtn.M(u"time1")
        assert(t.nodeType() == u'time')

        print("end : node type test.")

    def testset_useapi(self):
        cmds.file(new=True, f=True)
        cube = cmds.polyCube()[0]
        print cube
        m = mtn.M(u"pCube1")
        m.tx.set(1); assert(m.tx.get() == 1)
        m.tx.set_useapi(2); assert(m.tx.get() == 2)
        m.t.set(1,1,1); assert(m.t.get() == [1,1,1])
        m.t.set_useapi(1,1,1); assert(m.t.get() == [1,1,1])
        m.t.set([1,2,3]); assert(m.t.get() == [1,2,3])
        m.t.set_useapi([1,2,3]); assert(m.t.get() == [1,2,3])
        m.t.set(Vector(3,1,2)); assert(m.t.get() == [3,1,2])
        m.t.set_useapi(Vector(3,1,2)); assert(m.t.get() == [3,1,2])

        m.rx.set(0.349); self.failUnlessAlmostEqual(m.rx.get(), 0.349)
        m.rx.set(0); assert(m.rx.get() == 0)
        m.rx.set_useapi(0.349); self.failUnlessAlmostEqual(m.rx.get(), 0.349)
        m.rx.set_useapi(0); assert(m.rx.get() == 0)
        m.r.set(.3,.4,.5);
        self.failUnlessAlmostEqual(m.rx.get(), 0.3)
        self.failUnlessAlmostEqual(m.ry.get(), 0.4)
        self.failUnlessAlmostEqual(m.rz.get(), 0.5)
        m.r.set_useapi(.1,.2,.3)
        self.failUnlessAlmostEqual(m.rx.get(), 0.1)
        self.failUnlessAlmostEqual(m.ry.get(), 0.2)
        self.failUnlessAlmostEqual(m.rz.get(), 0.3)

        m.sx.set(2); assert(m.sx.get() == 2)
        m.sx.set_useapi(1); assert(m.sx.get() == 1)
        m.s.set(1,1,1); assert(m.s.get() == [1,1,1])
        m.s.set_useapi(1,1,1); assert(m.s.get() == [1,1,1])
        m.s.set([1,2,3]); assert(m.s.get() == [1,2,3])
        m.s.set_useapi([1,2,3]); assert(m.s.get() == [1,2,3])
        m.s.set(Vector(3,1,2)); assert(m.s.get() == [3,1,2])
        m.s.set_useapi(Vector(3,1,2)); assert(m.s.get() == [3,1,2])

        m = mtn.M("pCubeShape1")
        # bool
        m.colorSet[0].clamped.set(False); assert(m.colorSet[0].clamped.get() == False)
        m.colorSet[0].clamped.set_useapi(False); assert(m.colorSet[0].clamped.get() == False)
        m.colorSet[0].clamped.set(1); assert(m.colorSet[0].clamped.get() == True)
        m.colorSet[0].clamped.set_useapi(1); assert(m.colorSet[0].clamped.get() == True)
        # enum
        m.colorSet[0].representation.set(2); assert(m.colorSet[0].representation.get() == 2)
        m.colorSet[0].representation.set_useapi(2); assert(m.colorSet[0].representation.get() == 2)
        m.colorSet[0].representation.set(4); assert(m.colorSet[0].representation.get() == 4)
        m.colorSet[0].representation.set_useapi(4); assert(m.colorSet[0].representation.get() == 4)
        # string
        m.currentColorSet.set(u"hokuhoku"); assert(m.currentColorSet.get() == u"hokuhoku")
        m.currentColorSet.set(u""); assert(m.currentColorSet.get() == u"")
        m.currentColorSet.set_useapi(u"hokuhoku"); assert(m.currentColorSet.get() == u"hokuhoku")
        m.currentColorSet.set_useapi(u""); assert(m.currentColorSet.get() == u"")
        # int
        m = mtn.M("polyCube1")
        m.subdivisionsWidth.set(2); assert(m.subdivisionsWidth.get() == 2)
        m.subdivisionsWidth.set_useapi(2); assert(m.subdivisionsWidth.get() == 2)
        m.subdivisionsWidth.set(1); assert(m.subdivisionsWidth.get() == 1)
        m.subdivisionsWidth.set_useapi(1); assert(m.subdivisionsWidth.get() == 1)

        cmds.circle()
        m = mtn.M(u"nurbsCircleShape1")
        assert(m.mmv.get() == [0.0, 8.0])
        assert(m.minMaxValue.get() == [0.0, 8.0])

        # simple compound attribute
        cmds.createNode("quatAdd")
        m = mtn.M("quatAdd1")
        m.input1Quat.set(1, 1, 1, 1); assert(m.input1Quat.get() == [1.0,1.0,1.0,1.0])
        m.input1Quat.set(2, 3, 4, 5); assert(m.input1Quat.get() == [2.0,3.0,4.0,5.0])
        m.input1Quat.set_useapi(1, 1, 1, 1); assert(m.input1Quat.get() == [1.0,1.0,1.0,1.0])
        m.input1Quat.set_useapi(2, 3, 4, 5); assert(m.input1Quat.get() == [2.0,3.0,4.0,5.0])

        # matrix
        cmds.createNode(u"addMatrix")
        m = mtn.M(u"addMatrix1")
        # cmds
        m.i[0].set(5,1,1,1,5,1,1,1,5,1,1,1,5,1,1,1)
        assert(repr(m.matrixSum.get()) == 'Matrix(((5, 1, 1, 1), (5, 1, 1, 1), (5, 1, 1, 1), (5, 1, 1, 1)))')
        m.i[0].set([0,0,0,0,1,1,1,1,2,2,2,2,3,3,3,3])
        assert(repr(m.matrixSum.get()) == 'Matrix(((0, 0, 0, 0), (1, 1, 1, 1), (2, 2, 2, 2), (3, 3, 3, 3)))')
        m.i[0].set(mtn.Matrix())
        assert(repr(m.matrixSum.get()) == 'Matrix(((1, 0, 0, 0), (0, 1, 0, 0), (0, 0, 1, 0), (0, 0, 0, 1)))')
        # m.i[0].set([[0,0,0,0],[1,1,1,1],[2,2,2,2],[3,3,3,3]])
        # assert(repr(m.matrixSum.get()) == 'Matrix(((0, 0, 0, 0), (1, 1, 1, 1), (2, 2, 2, 2), (3, 3, 3, 3)))')
        # m.i[0].set([5,1,1,1],[5,1,1,1],[5,1,1,1],[5,1,1,1])
        # assert(repr(m.matrixSum.get()) == 'Matrix(((5, 1, 1, 1), (5, 1, 1, 1), (5, 1, 1, 1), (5, 1, 1, 1)))')

        # api
        m.i[0].set_useapi(5,1,1,1,5,1,1,1,5,1,1,1,5,1,1,1)
        assert(repr(m.matrixSum.get()) == 'Matrix(((5, 1, 1, 1), (5, 1, 1, 1), (5, 1, 1, 1), (5, 1, 1, 1)))')
        m.i[0].set_useapi([0,0,0,0,1,1,1,1,2,2,2,2,3,3,3,3])
        assert(repr(m.matrixSum.get()) == 'Matrix(((0, 0, 0, 0), (1, 1, 1, 1), (2, 2, 2, 2), (3, 3, 3, 3)))')
        m.i[0].set_useapi(mtn.Matrix())
        assert(repr(m.matrixSum.get()) == 'Matrix(((1, 0, 0, 0), (0, 1, 0, 0), (0, 0, 1, 0), (0, 0, 0, 1)))')
        m.i[0].set_useapi([[0,0,0,0],[1,1,1,1],[2,2,2,2],[3,3,3,3]])
        assert(repr(m.matrixSum.get()) == 'Matrix(((0, 0, 0, 0), (1, 1, 1, 1), (2, 2, 2, 2), (3, 3, 3, 3)))')
        m.i[0].set_useapi([5,1,1,1],[5,1,1,1],[5,1,1,1],[5,1,1,1])
        assert(repr(m.matrixSum.get()) == 'Matrix(((5, 1, 1, 1), (5, 1, 1, 1), (5, 1, 1, 1), (5, 1, 1, 1)))')


    def test_listattr(self):
        cmds.file(new=True, f=True)
        cube = cmds.polyCube()[0]
        m = mtn.M(u"pCube1")
        m.listAttrStr("rotateQuaternion", "selectHandle")
        m.listAttrStr("pCube1.rotateQuaternion", "pCube1.selectHandle")
        m.listAttrStr(array=True)
        m.listAttrStr("rotateQuaternion", "selectHandle", array=True)

        m._listAttr("rotateQuaternion", "selectHandle")
        m._listAttr("pCube1.rotateQuaternion", "pCube1.selectHandle")
        m._listAttr(array=True)
        m._listAttr("rotateQuaternion", "selectHandle", array=True)

    def test_hasattr(self):
        print(u"test_hasattr")
        cmds.file(new=True, f=True)
        cube = cmds.polyCube()[0]
        m = mtn.M(u"pCube1")
        assert(m.hasAttr(u"t.tx") == True)
        assert(m.hasAttr(u"t") == True)
        assert(m.hasAttr(u"tx") == True)
        assert(m.hasAttr(u"aaa") == False)
        assert(m.hasAttr(u"wm") == True)
        assert(m.hasAttr(u"wm[0]") == True)

        assert(m.hasAttr(m.t) == True)
        assert(m.hasAttr(m.tx) == True)
        assert(m.hasAttr(m.wm) == True)
        assert(m.hasAttr(m.wm[0]) == True)

    def test_cached_attribute(self):
        print(u"test_cached_attribute")
        cmds.file(new=True, f=True)
        cube = cmds.polyCube()[0]
        m1 = mtn.M(u"pCube1")
        # m1._cache = True # default:True
        m2 = mtn.M(u"pCube1")
        m2._cache = False
        assert(m1._cache_attribute == {})
        assert(m2._cache_attribute == {})
        m1.t
        m2.t
        assert(u"t" in m1._cache_attribute)
        assert(u"t" not in m2._cache_attribute)
        assert(m1._cache == True)
        assert(m2._cache == False)
        assert(m1.t._cache == True)
        assert(m2.t._cache == False)
        assert(m1.t.tx._cache == True)
        assert(m2.t.tx._cache == False)

    def test_listconnections(self):
        print(u"test_listconnections")
        cmds.file(new=True, f=True)
        cube = cmds.polyCube()[0]
        m = mtn.M(u"pCube1")

        cmds.setKeyframe("pCube1.tx", "pCube1.ty", "pCube1.tz",
                         "pCube1.rx", "pCube1.ry", "pCube1.rz",
                         "pCube1.sx", "pCube1.sy", "pCube1.sz")

        assert(type(m.listConnections()) == list)
        assert(m.listConnections(asGenerator=True).__class__.__name__ == "generator")
        m.listConnections(asGenerator=True, c=True)
        m.listConnections(asGenerator=True, p=True)
        m.listConnections(asGenerator=True, c=True, p=True)
        m.listConnections(c=True)
        m.listConnections(p=True)
        m.listConnections(c=True, p=True)
        assert(m.listConnections(c=True,s=False) == [])
        assert(m.listConnections(p=True,s=False) == [])

    def test_connect(self):
        print(u"test_connect")
        cmds.file(new=True, f=True)
        cube1 = cmds.polyCube()[0]
        cube2 = cmds.polyCube()[0]
        cube3 = cmds.polyCube()[0]
        n1 = mtn.M(u"pCube1")
        n2 = mtn.M(u"pCube2")
        n3 = mtn.M(u"pCube3")

        n1.t.connect(n2.t)
        n1.rx.connect(n2.rx)
        n1.t.inputs()
        n1.t.outputs()
        n1.t.connections()
        assert(n1.t.isConnected() == True)
        assert(n1.t.isConnected(inputs=True, outputs=False) == False)
        assert(n1.t.isConnected(inputs=False, outputs=True) == True)
        assert(n2.t.isConnected(inputs=True, outputs=False) == True)
        assert(n2.t.isConnected(inputs=False, outputs=True) == False)
        n1.t.disconnect(n2.t)
        n1.rx.disconnect(n2.rx)

        n1.t.connect(n2.t)
        n2.t.connect(n3.t)
        n2.t.disconnectInputs()
        assert(n1.t.isConnected() == False)
        n1.t.connect(n2.t)
        n2.t.disconnectOutputs()
        assert(n3.t.isConnected() == False)
        n2.t.connect(n3.t)
        n2.t.disconnect()
        assert(n1.t.isConnected() == False)
        assert(n3.t.isConnected() == False)

    def test_cmds(self):
        print(u"test_cmds")
        cmds.file(new=True, f=True)
        cube1 = cmds.polyCube()[0]
        cube2 = cmds.polyCube()[0]
        cube3 = cmds.polyCube()[0]
        n1 = mtn.M(u"pCube1")
        n2 = mtn.M(u"pCube2")
        n3 = mtn.M(u"pCube3")

        assert(mtn.ls("pCube*")[0].name() == "pCube1")
        mtn.setAttr(n1.t, 1, 0, 0)
        assert(mtn.getAttr(n1.t) == [(1.0, 0.0, 0.0)])
        mtn.select(cl=True)
        mtn.select(n2)
        assert(mtn.ls(sl=True)[0] == n2)

    def runTest(self):
        self.test_get()
        self.test_types()
        self.testset_useapi()
        self.test_listattr()
        self.test_hasattr()
        self.test_cached_attribute()
        self.test_listconnections()
        self.test_connect()
        self.test_cmds()



