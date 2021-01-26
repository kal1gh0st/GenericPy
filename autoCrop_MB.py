#Magic Beans VFX Ltd
#autoCrop_MB v3.7
#@2019 Jack Hughes. All rights reserved.
#jack_hughes@mac.com

#Add the following to your menu.py
##import autoCrop_MB
##nuke.menu( 'Nuke' ).addCommand( 'MB Tools/Run Auto Crop on Selected', autoCrop_MB.autoCrop_MB )

import nuke

def autoCrop_MB():
    #Check if a node is selected.
    try:
        n = nuke.selectedNode()
        nodeClass = n.Class()
    except:
        n = 0

    #Run if statement based on above try statement.
    if n == 0:
        print nuke.message('Please selected a node to run autoCrop_MB on...')
    else:
        #Check how many nodes are selected.
        numberOfNodes = len(nuke.selectedNodes())

        #Convert the int to a str.
        numberOfNodesInt = str(numberOfNodes)

    #Get channels from stream and sort so alpha is at the top.
    channelL = n.channels()
    channelS = channelL.sort()

    #Convert list to a string and add space.
    channelS = ' '.join(channelL)

    if nodeClass == 'Read':
        range = 'input' + ' ' + 'global' + ' ' + 'custom'
    else:
        range = 'global' + ' ' + 'custom'

    #Create and execute panel.
    p = nuke.Panel('autoCrop_MB v3.6')
    p.addEnumerationPulldown('frame range', range)
    p.addSingleLineInput('custom start', '')
    p.addSingleLineInput('custom end', '')
    p.addEnumerationPulldown('layer', channelS)
    p.addBooleanCheckBox('crop to format', False)
    p.show()
    
    increment = int('1')
    layersForCrop = p.value('layer')
    #Add quotation marks to layers variables.
    layersToAnalysis = '\"' + layersForCrop + '\"'
    
    #Work out the frame range wanted.
    if p.value('frame range') == 'custom':
        startFrame = int(p.value('custom start'))
        endFrame = int(p.value('custom end'))
    else:
        if p.value('frame range') == 'input':
            startFrame = n.knob('first').getValue()
            endFrame = n.knob('last').getValue()
        else:
            root = nuke.root()
            startFrame = int(root.knob("first_frame").value())
            endFrame = int(root.knob("last_frame").value())
	
	#Reset variables.

    first = startFrame
    last = endFrame
    inc = increment
    layer = layersToAnalysis



	#Run autocrop in curve tool.  Taken from The Foundry's nukescripts/crop.py

    # Remember original set of selected nodes...we'll need this
    original_nodes = nuke.selectedNodes()

    # Deselect everything so we can add CurveTool nodes
    all_nodes = nuke.allNodes()
    for i in all_nodes:
        i.knob("selected").setValue(False)

    for i in original_nodes:
        # Reselect originally selected nodes and create a CurveTool node,
        # which will automatically connect to the last selected.
        i.knob("selected").setValue(True)
        #Check if user wants to analysis outside the format.
        if p.value('crop to format') == True:
            autocropper = nuke.createNode("CurveTool",
                                        '''operation 0 ROI {0 0 input.width input.height} Layer %s label "Processing Crop..." selected true''' % (
                                        str(layer),), False)
        else:
            autocropper = nuke.createNode("CurveTool",
                                        '''operation 0 ROI {input.bbox.x input.bbox.y input.bbox.r input.bbox.t} Layer %s label "Processing Crop..." selected true''' % (
                                        str(layer),), False)



    # Execute the CurveTool node thru all the frames
    nuke.executeMultiple([autocropper, ], ([first, last, inc],))

    # select the curvewriter
    autocropper.knob("selected").setValue(True)

    # add crop node
    cropnode = nuke.createNode("Crop", "label AutoCrop", False)

    # put the new data from the autocrop into the new crop
    cropbox = cropnode.knob("box");
    autocropbox = autocropper.knob("autocropdata");
    cropbox.copyAnimations(autocropbox.animations())

    # turn on the animated flag
    cropnode.knob("indicators").setValue(1)

    #Add knob to add to the Bbox.
    userTab = nuke.Tab_Knob('Add to Bbox')
    cropnode.addKnob(userTab)
    k = nuke.Double_Knob('add', 'Add to Bbox')
    k.setRange(1, 100)
    k.setValue(0)
    cropnode.addKnob(k)

    cropnode.knob('box').setExpression('curve-(add)', 0)
    cropnode.knob('box').setExpression('curve-(add)', 1)
    cropnode.knob('box').setExpression('curve+(add)', 2)
    cropnode.knob('box').setExpression('curve+(add)', 3)

    # deselect everything
    all_nodes = nuke.allNodes()
    for j in all_nodes:
        j.knob("selected").setValue(False)

    # select the curvewriter and delete it
    autocropper.knob("selected").setValue(True)

    # delete the autocropper to make it all clean
    #nodes.node_delete()
    nuke.delete(autocropper)

    # deselect everything
    all_nodes = nuke.allNodes()
    for j in all_nodes:
        j.knob("selected").setValue(False)

    # select the new crop
    cropnode.knob("selected").setValue(True)

    # place it in a nice spot
    nuke.autoplace(cropnode)

    # De-Select it
    cropnode.knob("selected").setValue(False)