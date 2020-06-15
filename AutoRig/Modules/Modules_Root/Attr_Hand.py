cmds.select('L_SwitchArm_CTL')
XYZ=('x','y','z')
for xyz in XYZ:
    cmds.setAttr('L_SwitchArm_CTL.t'+xyz,l=True, k=False, channelBox=False)
    cmds.setAttr('L_SwitchArm_CTL.r'+xyz,l=True, k=False, channelBox=False)
    cmds.setAttr('L_SwitchArm_CTL.s'+xyz,l=True, k=False, channelBox=False)
cmds.setAttr('L_SwitchArm_CTL.v',l=True, k=False, channelBox=False)
cmds.select(cl=True)
Fingers_Curl=['Thumb','Index','Middle','Ring','Pinky']
#CURL#
num=1
cmds.addAttr('L_SwitchArm_CTL',ln='Curl',at='enum',en="-----:")
cmds.setAttr ('L_SwitchArm_CTL.Curl', k=True)
cmds.setAttr('L_SwitchArm_CTL.Curl',l=True) 
for finger in Fingers_Curl:
    #Add_Attrs_Curl
    cmds.addAttr('L_SwitchArm_CTL',ln=finger+'_Curl',at='double',dv=0)
    cmds.setAttr ('L_SwitchArm_CTL.'+finger+'_Curl', k=True)
    cmds.select(cl=True)
    for num in range(0,4):
        cmds.shadingNode('plusMinusAverage',au=True, n='AV_'+finger+'_0'+str(num)+'_Cup_L')
        cmds.connectAttr('L_SwitchArm_CTL.'+finger+'_Curl','AV_'+finger+'_0'+str(num)+'_Cup_L.input1D[0]')
        cmds.connectAttr('AV_'+finger+'_0'+str(num)+'_Cup_L.output1D','Z_L_'+finger+'_0'+str(num)+'_CTL.rotateZ')
        num=num+1
        
#LEAN AND SPREAD#
Attrs=['Lean','Spread']
Fingers=['Index','Middle','Ring','Pinky']
num=1
for Attr in Attrs:
    cmds.addAttr('L_SwitchArm_CTL',ln=Attr,at='enum',en="-----:")
    cmds.setAttr ('L_SwitchArm_CTL.'+Attr, k=True)
    cmds.setAttr('L_SwitchArm_CTL.'+Attr,l=True)
    for finger in Fingers:
        #Add_Attrs
        cmds.addAttr('L_SwitchArm_CTL',ln=finger+'_'+Attr,at='double',dv=0)
        cmds.setAttr ('L_SwitchArm_CTL.'+finger+'_'+Attr, k=True)
        cmds.select(cl=True)
        if Attr=='Lean':
            cmds.shadingNode('plusMinusAverage',au=True, n='AV_'+finger+'_L')
            cmds.connectAttr('L_SwitchArm_CTL.'+finger+'_'+Attr,'AV_'+finger+'_L.input1D[0]')
            cmds.connectAttr('AV_'+finger+'_L.output1D','Z_L_'+finger+'_00_CTL.rotateY')
            for num in range(1,4):
                cmds.connectAttr('L_SwitchArm_CTL.'+finger+'_'+Attr,'Z_L_'+finger+'_0'+str(num)+'_CTL.rotateY')
                num=num+1
        else:
            cmds.shadingNode('multDoubleLinear',au=True,n='MD_'+finger+'_L')
            if finger=='Index':
                cmds.setAttr('MD_'+finger+'_L.input2',-1)
            elif finger=='Middle':
                cmds.setAttr('MD_'+finger+'_L.input2',-.3)
            elif finger=='Ring':
                cmds.setAttr('MD_'+finger+'_L.input2',.3)
            else:
                cmds.setAttr('MD_'+finger+'_L.input2',1)
            cmds.connectAttr('L_SwitchArm_CTL.'+finger+'_'+Attr,'MD_'+finger+'_L.input1')
            cmds.connectAttr('MD_'+finger+'_L.output','AV_'+finger+'_L.input1D[1]')
#Cup_Out
cmds.addAttr('L_SwitchArm_CTL',ln='CUP_OUT',at='enum',en="-----:")
cmds.setAttr ('L_SwitchArm_CTL.CUP_OUT', k=True)
cmds.setAttr('L_SwitchArm_CTL.CUP_OUT',l=True)            
cmds.addAttr('L_SwitchArm_CTL',ln='Cup_Out',at='double',dv=0)
cmds.setAttr ('L_SwitchArm_CTL.Cup_Out', k=True)
for finger in Fingers:
     for num in range(0,4):
        cmds.shadingNode('multDoubleLinear',au=True,n='MD_'+finger+'_0'+str(num)+'_Cup_Out_L')
        if finger=='Index':
            cmds.setAttr('MD_'+finger+'_0'+str(num)+'_Cup_Out_L.input2',-1)
        elif finger=='Middle':
            cmds.setAttr('MD_'+finger+'_0'+str(num)+'_Cup_Out_L.input2',-.8)
        elif finger=='Ring':
            cmds.setAttr('MD_'+finger+'_0'+str(num)+'_Cup_Out_L.input2',-.6)
        else:
            cmds.setAttr('MD_'+finger+'_0'+str(num)+'_Cup_Out_L.input2',-.3)
        cmds.connectAttr('L_SwitchArm_CTL.Cup_Out','MD_'+finger+'_0'+str(num)+'_Cup_Out_L.input1')
        cmds.connectAttr('MD_'+finger+'_0'+str(num)+'_Cup_Out_L.output','AV_'+finger+'_0'+str(num)+'_Cup_L.input1D[1]')   
        num=num+1
Fingers=['Index','Middle','Ring','Pinky']
#Cup_In        
cmds.addAttr('L_SwitchArm_CTL',ln='Cup_In',at='double',dv=0)
cmds.setAttr ('L_SwitchArm_CTL.Cup_In', k=True)
for finger in Fingers:
     for num in range(0,4):
        cmds.shadingNode('multDoubleLinear',au=True,n='MD_'+finger+'_0'+str(num)+'_Cup_In_L')
        if finger=='Index':
            cmds.setAttr('MD_'+finger+'_0'+str(num)+'_Cup_In_L.input2',-.3)
        elif finger=='Middle':
            cmds.setAttr('MD_'+finger+'_0'+str(num)+'_Cup_In_L.input2',-.6)
        elif finger=='Ring':
            cmds.setAttr('MD_'+finger+'_0'+str(num)+'_Cup_In_L.input2',-.8)
        else:
            cmds.setAttr('MD_'+finger+'_0'+str(num)+'_Cup_In_L.input2',-1)
        cmds.connectAttr('L_SwitchArm_CTL.Cup_In','MD_'+finger+'_0'+str(num)+'_Cup_In_L.input1')
        cmds.connectAttr('MD_'+finger+'_0'+str(num)+'_Cup_In_L.output','AV_'+finger+'_0'+str(num)+'_Cup_L.input1D[2]')   
        num=num+1         
