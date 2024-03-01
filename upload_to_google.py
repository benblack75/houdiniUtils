import hou



def export_to_drive():
    # Path to my Google Drive Desktop location
    path_to_drive = 'G:/My Drive/HoudiniClass'

    # Output path
    output_path = f'{path_to_drive}/box1.obj'

    # Create cube and export
    geo_node = hou.node('/obj').createNode('geo', 'MyGeometry', run_init_scripts=False)
    box_node = geo_node.createNode('box')
    box_node.geometry().saveToFile(output_path)

export_to_drive()
