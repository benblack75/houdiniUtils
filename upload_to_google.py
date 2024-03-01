import hou

# Path to my Google Drive Desktop location
path_to_drive = 'G:/My Drive/HoudiniClass'
output_path = f'{path_to_drive}/box1.obj'

# Houdini Box node path
parent_node = hou.pwd()
target_node = parent_node.node('box1')

def export_to_drive():
    target_node.geometry().saveToFile(output_path)

export_to_drive()
