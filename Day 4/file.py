import os
from datetime import date


class File:
    def __init__(self, directory):
        self.directory = directory

    def getMaxSizeFile(self, n):
        files_size = []
        for filename in os.listdir(self.directory):
            file_path = os.path.join(self.directory, filename)
            if os.path.isfile(file_path):
                file_size = os.path.getsize(file_path)
                files_size.append((filename, file_size))
                
        files_size.sort(key=lambda x: x[1], reverse=True)
        return [file[0] for file in files_size[:n]]
        
    def getLatestFiles(self, date):
        
        latest_files = []
        for filename in os.listdir(self.directory):
            file_path = os.path.join(self.directory, filename)
            if os.path.isfile(file_path):
                file_time = os.path.getmtime(file_path)
                file_date = date.fromtimestamp(file_time)
                if file_date > date:
                    latest_files.append(filename)

        return latest_files    
