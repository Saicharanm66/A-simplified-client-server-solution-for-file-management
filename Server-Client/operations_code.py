"""
This python file contains operations(functions) such as
creating folder, creating file, writing in that created file, reading the file that is created,
changing path of folder, changing folder name and logging out where
these functions are further called in server code after a successful login and executed
accordingly
"""
import os
import time
#Create a class to implement certain functions to perform after login
class Operations:
    """
    >>> test1 = Operations("Sai")
    >>> test_folder1 = test1.folder_creation("Charan")
    >>> test_folder1
    True
    >>> test_file1 = test1.write_file("Charan","test1",'Testing text1')
    >>> test_file1
    True
    >>> test_read1 = test1.read_the_file("Charan","test1")
    >>> test_read1
    'Testing text1'
    >>> test_change_folder_name1=test1.change_folder_name("Charan","Changed_name1")
    >>> test_change_folder_name1
    True
    >>> test2 = Operations("Sai1")
    >>> test_folder2 = test2.folder_creation("Charanfolder")
    >>> test_folder2
    True
    >>> test_file2 = test2.write_file("Charanfolder","test2",'Testing text2')
    >>> test_file2
    True
    >>> test_read2= test2.read_the_file("Charanfolder","test2")
    >>> test_read2
    'Testing text2'
    >>> test3 = Operations("Sai2")
    >>> test_folder3 = test3.folder_creation("Charanfoldertest3")
    >>> test_folder3
    True
    >>> test_file3 = test3.write_file("Charanfoldertest3","test3",'Testing text3')
    >>> test_file3
    True
    >>> test_read3= test3.read_the_file("Charanfoldertest3","test3")
    >>> test_read3
    'Testing text3'
    """
    def __init__(self,user_id):
        """
        This initiates the operations class and define all the terms
        """
        self.user_id = user_id
        self.path = f"C:\\Users\\mscrs\\Desktop\\root\\{self.user_id}\\"
        try:
            os.makedirs(self.path)
        except Exception:
            pass
        self.bool=True
        self.folder_name=str
        self.file_name=str
        self.file_input=str
        self.folder_path=str
        self.file_path=str
        self.old_name=str
        self.new_name=str
        self.folder=str
        self.input=str
        self.data=str
        self.size=str
        self.created=str
        self.modified=str
        self.fol=str
        self.verif=str
#----------------Implement a function to create a file for client-----------------
    def folder_creation(self,name):
        """This function is used to create a folder in clients location.
        If the folder with same name already exists, it doesn't
        create folder and gives an alert that the file already exists

        Args:
            name (str): Name of teh foldder that should be created

        Returns:
            A folder with desired name for a particular client
            will be created in the space gven to particular client
        """
        self.folder_name = name
        self.bool = False
        self.folder = os.path.join(self.path,self.folder_name)
        try:
            os.makedirs(self.folder)
            self.bool = True
        except FileExistsError:
            print("File already exists")
        finally:
            return self.bool
#----------Implement a function to create file and write data in it----------
    def write_file(self,folder_name,file_name,file_input):
        """
        This function is used to write a file in a client's folder
        where the file is created only if the path is correct
        Args:
        folder_name (str): This is the folder name where user needs to store the file
        file_name (str): This is the file name which user needs to write the data in file
        file_input (str): This is teh input data given by user in file
        Returns:
            A file containing desired data is stored in the desired file
        """
        self.file_name = file_name
        self.folder_name = f"{folder_name}\\"
        self.input = file_input
        self.bool = False
        try:
            self.folder_path = os.path.join(self.path,self.folder_name)
            self.file_path = os.path.join(self.folder_path,self.file_name)
            with open(self.file_path,'w') as writefile:
                writefile.write(self.input)
                self.bool = True
        except Exception as excep:
            print(excep)
        finally:
            return self.bool
#----------------Implement a function to read certain file-----------------
    def read_the_file(self,folder_name,file_name):
        """
        The file which has been created can be read by using this function

        Args:
            folder_name(str) : This is the folder name where user stored the file
            file_name (str)  : This is the file name which user needs to read the data in file
        Returns:
            The display of data that was written in the file
        """
        self.file_name = file_name
        self.folder_name = f"{folder_name}\\"
        self.data = ''
        try:
            self.folder_path = os.path.join(self.path,self.folder_name)
            self.file_path = os.path.join(self.folder_path,self.file_name)
            with open(self.file_path,'r') as reader:
                self.data = reader.readlines()
        except Exception as excep:
            return print(excep)
        finally:
            return " ".join(self.data)
#------------Implement a function that shows folder details--------------
    def list_of_directories(self):
        """
        The list of the folders present in the client area is shown here.Along with names,
        the created date, modified date and data space used also displayed
        """
        self.folder_name = os.listdir(self.path)
        self.size = []
        self.created = []
        self.modified = []
        total_size = 0
        for afile in self.folder_name:
            self.fol = os.path.join(self.path,afile)
            self.modified.append(time.ctime(os.path.getmtime(f"{self.fol}")))
            self.created.append(time.ctime(os.path.getctime(f"{self.fol}")))
            for path,dirs,files in os.walk(self.fol):
                for thefile in files:
                    file_path = os.path.join(path, thefile)
                    total_size += os.path.getsize(file_path)
            self.size.append(total_size)
        return self.folder_name,self.size,self.created,self.modified
    def change_folder_path(self,old_name):
        """
        This is to change the current directory to the required
        Args:
            old_name (str): This is the name of the folder needed to change
        Returns:
            Changed path
        """
        self.old_name = f"{old_name}\\"
        self.bool = False
        self.verif = os.path.join(self.path, self.old_name)
        try:
            os.chdir(self.verif)
            self.bool =True
        except Exception :
            pass
        finally:
            return self.bool
    def change_folder_name(self,old_name,new_name):
        """

        Args:
            old_name (str): This is the old name of the forlder needed to change
            new_name (str): This is the new name to be given to folder

        Returns:
            Folder with new_name
        """
        self.old_name = old_name
        self.new_name = new_name
        self.bool = False
        os.chdir(self.path)
        try:
            os.rename(old_name,new_name)
            self.bool =True
        except Exception :
            pass
        finally:
            return self.bool