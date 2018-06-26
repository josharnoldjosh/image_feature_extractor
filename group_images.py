import os, shutil

files = [os.path.join(root, name)
             for root, dirs, files in os.walk(os.getcwd())
             for name in files
             if name.endswith((".png", ".jpg"))]

output_dir = os.path.join(os.getcwd(), 'images')

if not os.path.exists(output_dir):
	os.makedirs(output_dir)

print("Loading... (may take a while)")

i = 0
for file in files:
	output_file_name = str(i) + '.jpg'
	shutil.copy(file, os.path.join(output_dir, output_file_name))	
	i += 1

print("Script done!")