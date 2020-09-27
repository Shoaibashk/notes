import os


dirPath = r"docs"
fileExt = r".ipynb"
Exclude = ["docs","docs/MCN/Practicals"]

notebook = list()
notebooks_index = list()
notebook_md = list()

# filter
for root,dir,files in os.walk(dirPath):
    if root not in Exclude:
        print(root)
        for file in files: 
            if file.endswith(fileExt): 
                notebook.append(os.path.join(root,file))
            elif file in "index.md":
                notebooks_index.append(os.path.join(root,file))
           
            elif file.endswith(".md"):
                notebook_md.append(os.path.join(root,file))


for ad in notebook:
    nb = r"jupyter nbconvert --to markdown " + ad
    os.system(nb)


