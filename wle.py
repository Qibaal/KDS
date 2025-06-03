import os

# Define path to the directory
model_dir = os.path.join("frontend", "protein_fold_model")

# Get list of .cif files
cif_files = [f for f in os.listdir(model_dir) if f.endswith(".cif")]

# Sort to maintain consistent order
cif_files.sort()

for i, filename in enumerate(cif_files):
    temp = -50 + i
    new_name = f"temp_{temp}.cif"
    src_path = os.path.join(model_dir, filename)
    dst_path = os.path.join(model_dir, new_name)
    os.rename(src_path, dst_path)
    print(f"Renamed: {filename} → {new_name}")
