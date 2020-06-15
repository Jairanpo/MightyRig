import maya.cmds as cmds

def Herarchy_Parent(Child,Father):
    cmds.parent(Child,Father)
def Mult(Name):
    global Node
    Node=cmds.shadingNode('multiplyDivide',n=Name,au=True)

def Connect(Input, Output):
    cmds.connectAttr(Input,Output,f=True)
def Herarchy():
    List_Locs=['Locs_Rib_Arm_L', 'Locs_Rib_ForeArm_L', 'Locs_Rib_Arm_R', 'Locs_Rib_ForeArm_R']
    List_Groups=['Hidden_Bendy_Arm','Ctrls_Bendy_Arms','Locators_Joints_Arm','L_System_Arm','R_System_Arm']
    List_Final=['Z_Ribs_Nurb_Arm_L', 'Z_Ribs_Nurb_Arm_R', 'Ctrls_Bendy_Arms', 'Locators_Joints_Arm']
    Herarchy_Ctrls_Arm_L=['P_L_BendyArm_02_CTL','P_L_BendyArm_01_CTL','P_L_BendyArm_03_CTL','P_L_BendyForeArm_02_CTL','P_L_BendyForeArm_01_CTL','P_L_BendyForeArm_03_CTL','P_L_BendyMasterArm_CTL']
    Herarchy_Ctrls_Arm_R=['P_R_BendyArm_02_CTL','P_R_BendyArm_01_CTL','P_R_BendyArm_03_CTL','P_R_BendyForeArm_02_CTL','P_R_BendyForeArm_01_CTL','P_R_BendyForeArm_03_CTL','P_R_BendyMasterArm_CTL']
    
    num=0
    Extremidad=['Arm','ForeArm']
    for Groups in List_Groups:
        if Groups=='L_System_Arm':
            cmds.group(n=Groups,em=True)
            cmds.select(cl=True)
            Herarchy_Parent('L_System_Arm','Ctrls_Bendy_Arms')
            cmds.select(cl=True)
            for J in Extremidad:
                new_grp=cmds.group(n=J+'_L',em=True)
                Herarchy_Parent(new_grp,'L_System_Arm')
                cmds.select(cl=True)
        elif Groups=='R_System_Arm':
            cmds.group(n=Groups,em=True)
            cmds.select(cl=True)
            cmds.parent('R_System_Arm','Ctrls_Bendy_Arms')
            cmds.select(cl=True)
            for J in Extremidad:
                new_grp=cmds.group(n=J+'_R',em=True)
                Herarchy_Parent(new_grp,'R_System_Arm')
                cmds.select(cl=True)
        else:
            cmds.group(n=Groups,em=True)
            cmds.select(cl=True)
    #HERARCHY_BENDYS_L#
    for Obj in Herarchy_Ctrls_Arm_L:
        name=Obj.split('_')[2]
        print name
        if name=='BendyArm':
            print Obj
            Herarchy_Parent(Obj,'Arm_L')
            cmds.select(cl=True)
        elif name=='BendyForeArm':
            print Obj
            Herarchy_Parent(Obj,'ForeArm_L')
            cmds.select(cl=True)
        else:
            Herarchy_Parent(Obj,'L_System_Arm')
            cmds.select(cl=True)
     #HERARCHY_BENDYS_R#
    for Obj in Herarchy_Ctrls_Arm_R:
        name=Obj.split('_')[2]
        print name
        if name=='BendyArm':
            print Obj
            Herarchy_Parent(Obj,'Arm_R')
            cmds.select(cl=True)
        elif name=='BendyForeArm':
            print Obj
            Herarchy_Parent(Obj,'ForeArm_R')
            cmds.select(cl=True)
        else:
            Herarchy_Parent(Obj,'R_System_Arm')
            cmds.select(cl=True)
    for Loc in List_Locs:
        Herarchy_Parent(Loc,'Locators_Joints_Arm')
        cmds.select(cl=True)
    for Objs in List_Final:
        Herarchy_Parent(Objs,'Hidden_Bendy_Arm')
        cmds.select(cl=True)
    
    cmds.parent('Ctrls_Bendy_Arms','Ctrls_')
    cmds.parent('Hidden_Bendy_Arm','hidden' )
    cmds.select(cl=True)
    cmds.delete('Ctrls_Bendy_Arm')
    Bendys_Ctrls=['Arm','ForeArm']
    num=1
    for system in Bendys_Ctrls:
        #L
        Connect('C_mainA_ctl_0.scale','P_L_Bendy'+system+'_01_CTL.scale')
        Connect('C_mainA_ctl_0.scale','P_L_Bendy'+system+'_02_CTL.scale')
        Connect('C_mainA_ctl_0.scale','P_L_Bendy'+system+'_03_CTL.scale')
        #R
        Connect('C_mainA_ctl_0.scale','P_R_Bendy'+system+'_01_CTL.scale')
        Connect('C_mainA_ctl_0.scale','P_R_Bendy'+system+'_02_CTL.scale')
        Connect('C_mainA_ctl_0.scale','P_R_Bendy'+system+'_03_CTL.scale')
        if system=='Arm':
            Connect('C_mainA_ctl_0.scale','P_L_BendyMaster'+system+'_CTL.scale')
            Connect('C_mainA_ctl_0.scale','P_R_BendyMaster'+system+'_CTL.scale')
        for num in range(0,6):
            Connect('C_mainA_ctl_0.scale','Loc_Rivet_Rib_'+system+'_L_0'+str(num)+'.scale')
            Connect('C_mainA_ctl_0.scale','Loc_Rivet_Rib_'+system+'_R_0'+str(num)+'.scale')
