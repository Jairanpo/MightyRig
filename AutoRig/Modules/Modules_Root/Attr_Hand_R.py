import maya.cmds as cmds
def Attrs_Hand_R():
    cmds.select('R_SwitchArm_CTL')
    XYZ=('x','y','z')
    for xyz in XYZ:
        cmds.setAttr('R_SwitchArm_CTL.t'+xyz,l=True, k=False, channelBox=False)
        cmds.setAttr('R_SwitchArm_CTL.r'+xyz,l=True, k=False, channelBox=False)
        cmds.setAttr('R_SwitchArm_CTL.s'+xyz,l=True, k=False, channelBox=False)
    cmds.setAttr('R_SwitchArm_CTL.v',l=True, k=False, channelBox=False)
    cmds.select(cl=True)
    Fingers_Curl=['Thumb','Index','Middle','Ring','Pinky']
    #CURL#
    num=1
    cmds.addAttr('R_SwitchArm_CTL',ln='Curl',at='enum',en="-----:")
    cmds.setAttr ('R_SwitchArm_CTL.Curl', k=True)
    cmds.setAttr('R_SwitchArm_CTL.Curl',l=True) 
    for finger in Fingers_Curl:
        #Add_Attrs_Curl
        cmds.addAttr('R_SwitchArm_CTL',ln=finger+'_Curl',at='double',dv=0)
        cmds.setAttr ('R_SwitchArm_CTL.'+finger+'_Curl', k=True)
        cmds.select(cl=True)
        for num in range(0,4):
            cmds.shadingNode('plusMinusAverage',au=True, n='AV_'+finger+'_0'+str(num)+'_Cup_R')
            cmds.connectAttr('R_SwitchArm_CTL.'+finger+'_Curl','AV_'+finger+'_0'+str(num)+'_Cup_R.input1D[0]')
            cmds.connectAttr('AV_'+finger+'_0'+str(num)+'_Cup_R.output1D','Z_R_'+finger+'_0'+str(num)+'_CTL.rotateZ')
            num=num+1
            
    #LEAN AND SPREAD#
    Attrs=['Lean','Spread']
    Fingers=['Index','Middle','Ring','Pinky']
    num=1
    for Attr in Attrs:
        cmds.addAttr('R_SwitchArm_CTL',ln=Attr,at='enum',en="-----:")
        cmds.setAttr ('R_SwitchArm_CTL.'+Attr, k=True)
        cmds.setAttr('R_SwitchArm_CTL.'+Attr,l=True)
        for finger in Fingers:
            #Add_Attrs
            cmds.addAttr('R_SwitchArm_CTL',ln=finger+'_'+Attr,at='double',dv=0)
            cmds.setAttr ('R_SwitchArm_CTL.'+finger+'_'+Attr, k=True)
            cmds.select(cl=True)
            if Attr=='Lean':
                cmds.shadingNode('plusMinusAverage',au=True, n='AV_'+finger+'_R')
                cmds.connectAttr('R_SwitchArm_CTL.'+finger+'_'+Attr,'AV_'+finger+'_R.input1D[0]')
                cmds.connectAttr('AV_'+finger+'_R.output1D','Z_R_'+finger+'_00_CTL.rotateY')
                for num in range(1,4):
                    cmds.connectAttr('R_SwitchArm_CTL.'+finger+'_'+Attr,'Z_R_'+finger+'_0'+str(num)+'_CTL.rotateY')
                    num=num+1
            else:
                cmds.shadingNode('multDoubleLinear',au=True,n='MD_'+finger+'_R')
                if finger=='Index':
                    cmds.setAttr('MD_'+finger+'_R.input2',-1)
                elif finger=='Middle':
                    cmds.setAttr('MD_'+finger+'_R.input2',-.3)
                elif finger=='Ring':
                    cmds.setAttr('MD_'+finger+'_R.input2',.3)
                else:
                    cmds.setAttr('MD_'+finger+'_R.input2',1)
                cmds.connectAttr('R_SwitchArm_CTL.'+finger+'_'+Attr,'MD_'+finger+'_R.input1')
                cmds.connectAttr('MD_'+finger+'_R.output','AV_'+finger+'_R.input1D[1]')
    #Cup_Out
    cmds.addAttr('R_SwitchArm_CTL',ln='CUP_OUT',at='enum',en="-----:")
    cmds.setAttr ('R_SwitchArm_CTL.CUP_OUT', k=True)
    cmds.setAttr('R_SwitchArm_CTL.CUP_OUT',l=True)            
    cmds.addAttr('R_SwitchArm_CTL',ln='Cup_Out',at='double',dv=0)
    cmds.setAttr ('R_SwitchArm_CTL.Cup_Out', k=True)
    for finger in Fingers:
         for num in range(0,4):
            cmds.shadingNode('multDoubleLinear',au=True,n='MD_'+finger+'_0'+str(num)+'_Cup_Out_R')
            if finger=='Index':
                cmds.setAttr('MD_'+finger+'_0'+str(num)+'_Cup_Out_R.input2',-1)
            elif finger=='Middle':
                cmds.setAttr('MD_'+finger+'_0'+str(num)+'_Cup_Out_R.input2',-.8)
            elif finger=='Ring':
                cmds.setAttr('MD_'+finger+'_0'+str(num)+'_Cup_Out_R.input2',-.6)
            else:
                cmds.setAttr('MD_'+finger+'_0'+str(num)+'_Cup_Out_R.input2',-.3)
            cmds.connectAttr('R_SwitchArm_CTL.Cup_Out','MD_'+finger+'_0'+str(num)+'_Cup_Out_R.input1')
            cmds.connectAttr('MD_'+finger+'_0'+str(num)+'_Cup_Out_R.output','AV_'+finger+'_0'+str(num)+'_Cup_R.input1D[1]')   
            num=num+1
    Fingers=['Index','Middle','Ring','Pinky']
    #Cup_In        
    cmds.addAttr('R_SwitchArm_CTL',ln='Cup_In',at='double',dv=0)
    cmds.setAttr ('R_SwitchArm_CTL.Cup_In', k=True)
    for finger in Fingers:
         for num in range(0,4):
            cmds.shadingNode('multDoubleLinear',au=True,n='MD_'+finger+'_0'+str(num)+'_Cup_In_R')
            if finger=='Index':
                cmds.setAttr('MD_'+finger+'_0'+str(num)+'_Cup_In_R.input2',-.3)
            elif finger=='Middle':
                cmds.setAttr('MD_'+finger+'_0'+str(num)+'_Cup_In_R.input2',-.6)
            elif finger=='Ring':
                cmds.setAttr('MD_'+finger+'_0'+str(num)+'_Cup_In_R.input2',-.8)
            else:
                cmds.setAttr('MD_'+finger+'_0'+str(num)+'_Cup_In_R.input2',-1)
            cmds.connectAttr('R_SwitchArm_CTL.Cup_In','MD_'+finger+'_0'+str(num)+'_Cup_In_R.input1')
            cmds.connectAttr('MD_'+finger+'_0'+str(num)+'_Cup_In_R.output','AV_'+finger+'_0'+str(num)+'_Cup_R.input1D[2]')   
            num=num+1         
