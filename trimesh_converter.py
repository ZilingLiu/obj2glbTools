import trimesh
import argparse

def convert_obj_to_glb(input_obj_path, output_glb_path):
    # 加载OBJ文件，trimesh会自动尝试加载相关的MTL和纹理文件
    mesh = trimesh.load(input_obj_path, force='mesh')

    # 导出为GLB格式
    with open(output_glb_path, 'wb') as f:
        f.write(mesh.export(file_type='glb'))


if __name__  == "main":
    parser = argparse.ArgumentParser()
    parser.add_argument("--obj", type=str, help="path to obj")
    parser.add_argument("--glb", type=str, help="path to glb")
    args = parser.parse_args()
    convert_obj_to_glb(args.obj, args.glb)