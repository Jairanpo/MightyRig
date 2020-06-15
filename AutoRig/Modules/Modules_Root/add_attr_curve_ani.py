import maya.cmds as cmds
sel=cmds.ls(selection=True)
print sel
for Ctrl in sel:
    cmds.addAttr(Ctrl,ln='fbControl',attributeType='bool')
    cmds.setAttr(Ctrl+'.fbControl',k=True)
    cmds.setAttr(Ctrl+'.fbControl',1)
    cmds.setAttr(Ctrl+'.fbControl',lock=True)
