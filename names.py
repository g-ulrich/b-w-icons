# Python program to rename all file
# names in your directory
import os
 
os.chdir('C:\\desktop2\\projects\\github\\b-w-icons\\icons\\24x24b')
print(os.getcwd())
 
for count, f in enumerate(os.listdir()):
    name, ext = os.path.splitext(f)
    new = f"{name.replace('cil-inv-', '').replace('-', '_')}{ext}"
    os.rename(f, new)
    print("Success -", new)