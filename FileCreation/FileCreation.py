# This program creates a new text file in a specified folder on my desktop and then opens the file.
# If the file already exists in the chosen folder, the existing file will open.
# Edit line 14 to the user's specific directory.

import os;
import subprocess;

class UserInput:
    def __init__(self):
        self._folder = ""
        self._fileName = ""
    
    def GetFolder(self):
        return "C:/Users/jared/Desktop/PythonFileCreation/" + self._folder
    
    def SetFolder(self, folder):
        self._folder = folder
    
    def GetFileName(self):
        return self._fileName
    
    def SetFileName(self, filename):
        self._fileName = filename

    def UserInput(self):
        self.SetFolder(input("Enter directory name:  "))
        self.SetFileName(input("Enter the file name:  "))

    def CreateDirectoryFileDesktop(self):
        directory = self.GetFolder() + "/"
        filename = self.GetFileName() + ".txt"

        try:
            if not os.path.exists(directory):
                os.makedirs(directory)
        except OSError:
            print("Failed to create directory.")
        open(directory + filename, 'a')
        print(filename + " has been created successfully under " + directory)
        subprocess.Popen(['notepad.exe', directory + filename])



user = UserInput()

user.UserInput()
user.CreateDirectoryFileDesktop()