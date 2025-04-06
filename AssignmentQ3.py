import os 
def max_size_file(directory):
    max_size=0
    max_file=None
    for root,_,files in os.walk(directory):
        for file in files:
            path= os.path.join(root,file)
            size=os.path.getsize(path)
            if size>max_size:
                max_size=size
                max_file=path
    return max_file,max_size

directory=r"C:\Users\Yaswanth\handson"
print(max_size_file(directory))
            
                
        