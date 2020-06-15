import maya.cmds as cmds

def Herarchy_Parent(Child,Father):
    cmds.parent(Child,Father)
def Mult(Name):
    global Node
    Node=cmds.shadingNode('multiplyDivide',n=Name,au=True)

def Connect(Input, Output):
    cmds.connectAttr(Input,Output,f=True)
def Herarchy():
    List_Locs=['Locs_Rib_Leg_L', 'Locs_Rib_ForeLeg_L', 'Locs_Rib_Leg_R', 'Locs_Rib_ForeLeg_R']
    List_Groups=['Hidden_Bendy_Leg','Ctrls_Bendy_Legs','Locators_Joints_Leg','L_System_Leg','R_System_Leg']
    List_Final=['Z_Ribs_Nurb_Leg_L', 'Z_Ribs_Nurb_Leg_R', 'Ctrls_Bendy_Legs', 'Locators_Joints_Leg']
    Herarchy_Ctrls_Leg_L=['P_L_BendyLeg_02_CTL','P_L_BendyLeg_01_CTL','P_L_BendyLeg_03_CTL','P_L_BendyForeLeg_02_CTL','P_L_BendyForeLeg_01_CTL','P_L_BendyForeLeg_03_CTL','P_L_BendyMasterLeg_CTL']
    Herarchy_Ctrls_Leg_R=['P_R_BendyLeg_02_CTL','P_R_BendyLeg_01_CTL','P_R_BendyLeg_03_CTL','P_R_BendyForeLeg_02_CTL','P_R_BendyForeLeg_01_CTL','P_R_BendyForeLeg_03_CTL','P_R_BendyMasterLeg_CTL']
    
    num=0
    Extremidad=['Leg','ForeLeg']
    for Groups in List_Groups:
        if Groups=='L_System_Leg':
            cmds.group(n=Groups,em=True)
            cmds.select(cl=True)
            Herarchy_Parent('L_System_Leg','Ctrls_Bendy_Legs')
            cmds.select(cl=True)
            for J in Extremidad:
                new_grp=cmds.group(n=J+'_L',em=True)
                Herarchy_Parent(new_grp,'L_System_Leg')
                cmds.select(cl=True)
        elif Groups=='R_System_Leg':
            cmds.group(n=Groups,em=True)
            cmds.select(cl=True)
            cmds.parent('R_System_Leg','Ctrls_Bendy_Legs')
            cmds.select(cl=True)
            for J in Extremidad:
                new_grp=cmds.group(n=J+'_R',em=True)
                Herarchy_Parent(new_grp,'R_System_Leg')
                cmds.select(cl=True)
        else:
            cmds.group(n=Groups,em=True)
            cmds.select(cl=True)

    #HERARCHY_BENDYS_L#
    for Obj in Herarchy_Ctrls_Leg_L:
        name=Obj.split('_')[2]
        print name
        if name=='BendyLeg':
            print Obj
            Herarchy_Parent(Obj,'Leg_L')
            cmds.select(cl=True)
        elif name=='BendyForeLeg':
            print Obj
            Herarchy_Parent(Obj,'ForeLeg_L')
            cmds.select(cl=True)
        else:
            Herarchy_Parent(Obj,'L_System_Leg')
            cmds.select(cl=True)
     #HERARCHY_BENDYS_R#
    for Obj in Herarchy_Ctrls_Leg_R:
        name=Obj.split('_')[2]
        print name
        if name=='BendyLeg':
            print Obj
            Herarchy_Parent(Obj,'Leg_R')
            cmds.select(cl=True)
        elif name=='BendyForeLeg':
            print Obj
            Herarchy_Parent(Obj,'ForeLeg_R')
            cmds.select(cl=True)
        else:
            Herarchy_Parent(Obj,'R_System_Leg')
            cmds.select(cl=True)
    for Loc in List_Locs:
        Herarchy_Parent(Loc,'Locators_Joints_Leg')
        cmds.select(cl=True)
    for Objs in List_Final:
        Herarchy_Parent(Objs,'Hidden_Bendy_Leg')
        cmds.select(cl=True)
    
    cmds.parent('Ctrls_Bendy_Legs','Ctrls_')
    cmds.parent('Hidden_Bendy_Leg','hidden' )
    cmds.select(cl=True)
    cmds.delete('Ctrls_Bendy_Leg')
    Bendys_Ctrls=['Leg','ForeLeg']
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

        if system=='Leg':
            Connect('C_mainA_ctl_0.scale','P_L_BendyMaster'+system+'_CTL.scale')
            Connect('C_mainA_ctl_0.scale','P_R_BendyMaster'+system+'_CTL.scale')
        for num in range(0,6):
            Connect('C_mainA_ctl_0.scale','Loc_Rivet_Rib_'+system+'_L_0'+str(num)+'.scale')
            Connect('C_mainA_ctl_0.scale','Loc_Rivet_Rib_'+system+'_R_0'+str(num)+'.scale')