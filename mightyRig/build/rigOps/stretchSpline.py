"""
ikCurve: iKCurve node
volume: bool
worldScale: bool
worldScaleObject: the object that will be used for world scale
worldScaleAttr: The attribute to be used for world scale

req:  getStretchAxis.py
      createCurveControl.py
"""
# ================================================================

"""
- Create a curveInfo node with the arclen method with
  the constructionHistory flag in order to create a node
  out of it. This node will contain the information about
  our spine curve, including the arclen.

- Get the shape of the ikCurve

- Get the ik handle

- Get the joints of the ikHandle with iKHandke.getJointList()
  foo = ikHandleNode.getJointList()

- Add a normalizedScale attribute to the curveInfo node
  as a double data type:
  curveInfo.addAttr("normalizedScale", attributeType="double")

- Get the stretch axis, this is the axis at which the 
  joint chain is pointing to, we can't do this with the first 
  joint, because its local translation will depend on the 
  world or containing group, but we can use any of the following joints by
  getting its translation values, and which ever is the larges value, then 
  this is the main axis our joint chain is traveling through in our 
  virtual space. We must return an ordered list with the largest
  axis first and then the other two.

- Create a miltiplyDivide node and name it as "M_iKCurveNormalizedScale_MDN"
"""
