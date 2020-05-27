import hou

txt = 'v@HSV = set((@Frame*0.005+(0.025*@ptnum/@numpt)),1,1);@Cd = hsvtorgb(v@HSV);'

def createNode():
        for node in hou.selectedNodes():
                sort = node.parent().createNode("sort")
                sort.setInput(0, node)
                
                sort.setPosition(node.position() + hou.Vector2(0,-1))

                sort.parm("ptsort").set("byx")
                
                wrangle = node.parent().createNode("attribwrangle")
                wrangle.setInput(0, sort)

                wrangle.parm("snippet").set(txt)

                wrangle.setPosition(sort.position() + hou.Vector2(0,-1))

                nul = node.parent().createNode("null")
                nul.setInput(0,wrangle)
                
                nul.setDisplayFlag(True)
                nul.setRenderFlag(True)
                
                nul.setPosition(wrangle.position() + hou.Vector2(0,-1))
         
                parentNode = node.parent()
                parentTxt = parentNode.path()
                
                parentNode.setDisplayFlag(False)
                
                lightNode = hou.node("/obj").createNode("hlight")
                
                lightNode.parm("light_type").set("geo")
                lightNode.parm("light_contribprimary").set(True)
                lightNode.parm("normalizearea").set(False)
                lightNode.parm("areageometry").set(parentTxt)
        
                lightNode.setPosition(parentNode.position() + hou.Vector2(0,-1))
        

if len(hou.selectedNodes())>0:
        node = hou.selectedNodes()[0]
        nodeType = hou.hscript('optype -s %s' % node.path())[0][:-1] 
        if nodeType == "sop":
                createNode()