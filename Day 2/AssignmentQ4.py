import os
def merge_txt_files(folder,out_file):
    with open(out_file,'w') as out:
        for root,_,files in os.walk(directory):
            for file in files:
                if file.endswith(".txt"):
                    path = os.path.join(root,file)
                    with open(path,'r') as f:
                        out.write(f.read())
                        out.write("\n")
directory=r"C:\Users\Yaswanth\handson"
print(merge_txt_files(directory,"merged.txt"))