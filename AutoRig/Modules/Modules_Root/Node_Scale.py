import maya.cmds as cmds
def Mult(Name):
    global Node
    Node=cmds.shadingNode('multiplyDivide',n=Name,au=True)

def Connect(Input, Output):
    cmds.connectAttr(Input,Output,f=True)