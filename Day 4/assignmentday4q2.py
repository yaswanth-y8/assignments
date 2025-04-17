from file import File 
import datetime


fs = File(".")
max_files = fs.getMaxSizeFile(2)  
print("Top largest files:", max_files)
latest_files = fs.getLatestFiles(datetime.date(2018, 2, 1))   
print("Lates Files :", latest_files)
