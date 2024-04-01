obj="$1"
normal_map="$2"
glb="$3"

# Convert obj to glb
obj2gltf -i "$obj" -o "$glb" --normalTexture "$normal_map" 