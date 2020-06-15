import sys
Path  = cmds.internalVar(usd = True)
PathMaster = Path + 'Autorig/Modules'
sys.path.append(PathMaster)
if cmds.window("Autorig",exists=True):
    cmds.deleteUI("Autorig")
from EJECUTABLE import *
import EJECUTABLE
reload(EJECUTABLE)