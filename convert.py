import os


dirPath = r"docs"
fileExt = r".ipynb"
Exclude = ["docs","docs/MCN/Practicals","docs/DL/Practicals"]

notebook = list()
notebooks_index = list()
notebook_md = list()

# filter
for root,dir,files in os.walk(dirPath):
    if root not in Exclude:
        
        for file in files: 
            if file.endswith(fileExt): 
                print(root)
                notebook.append(os.path.join(root,file))
            elif file in "index.md":
                notebooks_index.append(os.path.join(root,file))
           
            elif file.endswith(".md"):
                notebook_md.append(os.path.join(root,file))


for ad in notebook:
    nb = r"jupyter nbconvert --to markdown " + ad
    os.system(nb)


