import bpy
import sys
import argparse
# obj_file_path = '/ssd-sata1/lzl/TAPALL/obj2glb/obj_models/toy/mesh.obj'  # OBJ文件路径
# glb_file_path = '/ssd-sata1/lzl/TAPALL/obj2glb/glbs/blender_toy.glb'  # GLB文件导出路径
def blender_converter(obj_file_path, glb_file_path):
    # 清除当前场景中的所有对象
    bpy.ops.wm.read_factory_settings(use_empty=True)

    # 导入OBJ文件
    bpy.ops.import_scene.obj(filepath=obj_file_path)

    # 导出为GLB
    bpy.ops.export_scene.gltf(filepath=glb_file_path, export_format='GLB', export_apply=True, export_materials='EXPORT')

if __name__  == "main":
    parser = argparse.ArgumentParser()
    parser.add_argument("--obj", type=str, help="path to obj")
    parser.add_argument("--glb", type=str, help="path to glb")
    args = parser.parse_args()
    blender_converter(args.obj, args.glb)