# obj转glb脚本

## 1. Trimesh
```
pip install trimesh
```
```
python trimesh_converter.py --obj {obj_path} --glb {glb_path}
```
只保留了basecolor

## 2. Blender python API
1. Download
```
# download from https://ftp.nluug.nl/pub/graphics/blender/release/
wget https://ftp.nluug.nl/pub/graphics/blender/release/Blender2.93/blender-2.93.2-linux-x64.tar.xz
tar -xf blender-2.93.2-linux-x64.tar.xz
# set env
blender=$PWD/../blender/blender-2.93.2-linux-x64/blender
$blender -noaudio --background --python **.py
```
2. Run
```
python blender_converter.py --obj {obj_path} --glb {glb_path}
```
保留basecolor和normal，丢掉metallic texture

## 3. Javascript [obj2gltf](https://github.com/CesiumGS/obj2gltf) repo 
1. download [Node.js](https://www.runoob.com/nodejs/nodejs-install-setup.html)
2. download obj2gltf
```
npm install -g obj2gltf
```
3. 配置环境变量
```
export PATH="{*/node-v21.1.0-linux-x64/bin}:$PATH"
```
把*替换成node.js的安装目录

4. 命令行运行
```
obj2gltf -i {obj_path} -o {glb_path} --normalTexture {normal_path} 
```
保留normal，basecolor，metal texture
