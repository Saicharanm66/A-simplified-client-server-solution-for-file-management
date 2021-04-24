"""
This is the main file where the server is initiated and functions according
to the inputs given by user.The inputs are taken using client code
and executes accordingly using opetarions_code and returns output to client
"""
import asyncio
import signal
import fileinput
from operations_code import Operations
signal.signal(signal.SIGINT, signal.SIG_DFL)
#Impliment a code that displays registration process
async def register(reader, writer):
    """
    The name of user, User name for that particular user and password is taken
    from user who is newly regestering.
    If the username already exist, it will shows a warning that saying username already exist.
    The taken username and password is stored in a txt file,
    where the file is further used in login operations
    """
    display_data = """Please create an account\n(Note : Every details are mandatory)\n
    Please enter your first name:"""
    writer.write(display_data.encode())
    data = await reader.read(1000)
    name_first= data.decode().strip()
    display_data = """        Please enter your last name                    :"""
    writer.write(display_data.encode())
    data = await reader.read(1000)
    name_last= data.decode().strip()
    display_data = """        Create a User Name                             : """
    writer.write(display_data.encode())
    data = await reader.read(1000)
    user_id = data.decode().strip()
    display_data = """        Create a Password(Please keep it confidential) :"""
    writer.write(display_data.encode())
    data = await reader.read(1000)
    password_create = data.decode().strip()
    password_re_enter = """       Re-enter password                          : """
    writer.write(password_re_enter.encode())
    data = await reader.read(1000)
    password_re_enter = data.decode().strip()
    i = False
    with open("C:\\Users\\mscrs\\Desktop\\root\\admin\\Register.txt",'r') as reader:
        for line in reader:
            if user_id in line:
                i = True
                break
    if not i:
        with open("C:\\Users\\mscrs\\Desktop\\root\\admin\\Register.txt",'a') as write:
            write.write(name_first + ' ')
            write.write(name_last + ',')
            write.write(user_id + ':')
            write.write(password_create + ' -------* \n')
        display_data = """Registration successful
        --------------Your account has been created successfully--------------------"""
        writer.write(display_data.encode())
    else:
        display_data = """Username already exists\n
-------Registration request Denied-------\n
Use different username"""
        writer.write(display_data.encode())
#Implement a function that makes client to login if satisfies conditions
async def login(reader, writer):
    """
    This function makes the user login.If the input user name or password
    is wrong or doesn't exists,
    it gives a notification that the username or password is wrong.
    If the user is already loggedin and tries to login again,
    it shows a warning that the access denied to the person who is trying to login again.
    If the user name and password are correct and the user is logging in without
    any active login record,the login will be made successful and displays the further action
    that the user want to perform.
    Now the user selects the required option.
    if the option is '1' or 'Create new folder' or 'create new folder',
    a folder with desired name is created.
    if the option is '2' or 'Create a new file' or 'create a new file',
    a file in the desired folder with desired name having data
    entered by client is created.
    if the option is 3 or 'Open the file' or 'open the file', the created file can be read.
    if the option is 4 or 'View list of folders' or 'view list of folders'
    or 'folders list', it displays the list of folders, the data it consumed,
    date of creation and date of modification.
    if the option is 5 or 'change_folder',user can change folder path.
    if the option is 6 or 'Rename folder',user can rename folder.
    if the option is '0' or 'Logout' or 'logout', the user will be logged out from the client space.
    All these functions of selected options will be imported from operations code
    """

    display_data = """\t\tPlease enter your login details
    USER ID   : """
    writer.write(display_data.encode())
    data = await reader.read(1000)
    user_id = data.decode().strip()
    display_data = """      PASSWORD : """
    writer.write(display_data.encode())
    data = await reader.read(1000)
    password_entered = data.decode().strip()
    filepath = "C:\\Users\\mscrs\\Desktop\\root\\admin\\Register.txt"
    init = 0
    i = True
    #If user already logged in, The login access should be denied
    with open(filepath,'r') as regis:
        for line in regis:
            if user_id in line:
                if password_entered in line:
                    init = 1
                    if "Status : Logged in" in line:
                        display_data = "Access denied\nThe user is already logged in\nPlease restart server and client"
                        writer.write(display_data.encode())
                        i =False
                        break
    if i:
        for line in fileinput.FileInput(filepath,inplace=1):
            if user_id in line:
                if  password_entered in line:
                    line = line.rstrip()
                    line = line.replace(line, line +"Status : Logged in\n")
            print(line,end='')
    #If username or password is wrong, a warning should be displayed
    if init == 0 :
        display_data = "Invalid Username or Password\nPlease restart server and client"
        writer.write(display_data.encode())
    #If username and password correct, user will be logged in
    elif init == 1 and i:
        try:
            display_data = """--------------------Welcome :)--------------------\n
How can I help you
                1   -->  Create new folder
                2   -->  Create a new file
                3   -->  Open the file
                4   -->  View list of folders
                5   -->  Change folder or directory
                6   -->  Rename folder
                0   -->  Logout
                Please select the option :  """
            writer.write(display_data.encode())
            user_operations = Operations(user_id)
            while True:
                data = await reader.read(1000)
                command_given = data.decode().strip()
                if command_given in ('1', 'create new folder', 'Create new folder', 'create_folder'):
                    display_data = "Name : "
                    writer.write(display_data.encode())
                    data = await reader.read(1000)
                    input_file_name = data.decode().strip()
                    filenamed = user_operations.folder_creation(input_file_name)
                    if filenamed:
                        display_data = "Folder Created!"
                        writer.write(display_data.encode())
                    else:
                        display_data = "Folder Exists,please give another name"
                        writer.write(display_data.encode())
                elif command_given in ('2', 'create a new file', 'Create a new file', 'write_file'):
                    display_data = "Enter folder name : "
                    writer.write(display_data.encode())
                    data = await reader.read(100)
                    folder_name = data.decode().strip()
                    display_data = "Enter file name : "
                    writer.write(display_data.encode())
                    data = await reader.read(100)
                    file_name = data.decode().strip()
                    display_data = "Enter the data : "
                    writer.write(display_data.encode())
                    data = await reader.read(100)
                    input_data = data.decode().strip()
                    i = user_operations.write_file(folder_name,file_name,input_data)
                    if i:
                        display_data = "File Created"
                        writer.write(display_data.encode())
                    else:
                        display_data="Folder doesn't exist"
                        writer.write(display_data.encode())
                elif command_given in ('3', 'open the file', 'Open the file', 'read_file'):
                    display_data = "Enter folder name : "
                    writer.write(display_data.encode())
                    data = await reader.read(500)
                    folder_name = data.decode().strip()
                    display_data = "Name of the file : "
                    writer.write(display_data.encode())
                    data = await reader.read(500)
                    file_name = data.decode().strip()
                    fil=user_operations.read_the_file(folder_name,file_name)
                    if fil:
                        read_file = str(user_operations.read_the_file(folder_name,file_name))
                        writer.write(read_file.encode())
                    else:
                        display_data="File doesn't exist"
                        writer.write(display_data.encode())
                elif command_given in ('4', 'View list of folders', 'view list of folders', 'folders list', 'list'):
                    name_of_file,size_of_file,created_time,modified_time = user_operations.list_of_directories()
                    display_data = "Name Size     Date of creation      Date of modification"
                    writer.write(display_data.encode())
                    data = await reader.read(100)
                    display_data = data.decode().strip()
                    show_folder_name = str(" ".join(map(str,name_of_file)))
                    writer.write(show_folder_name.encode())
                    data = await reader.read(100)
                    display_data = data.decode().strip()
                    show_folder_size = str(" ".join(map(str,size_of_file)))
                    writer.write(show_folder_size.encode())
                    data = await reader.read(100)
                    display_data = data.decode().strip()
                    show_created_time = str("  ".join(map(str,created_time)))
                    writer.write(show_created_time.encode())
                    data = await reader.read(100)
                    display_data = data.decode().strip()
                    show_modified_time = str("  ".join(map(str,modified_time)))
                    writer.write(show_modified_time.encode())
                    data = await reader.read(100)
                    display_data = data.decode().strip()
                elif command_given in ('5', 'change_folder', 'Change folder', 'change folder'):
                    display_data = "Enter Folder name : "
                    writer .write(display_data.encode())
                    data = await reader.read(10000)
                    old_name_of_folder = data.decode().strip()
                    new = user_operations.change_folder_path(old_name_of_folder)
                    if new :
                        display_data = "Path changed successfully"
                    else:
                        display_data = "Path not changed"
                    writer.write(display_data.encode())
                elif command_given in ('6', 'Rename folder', 'rename folder'):
                    display_data = "Enter Folder name : "
                    writer .write(display_data.encode())
                    data = await reader.read(10000)
                    old_name_of_folder = data.decode().strip()
                    display_data = "Rename : "
                    writer.write(display_data.encode())
                    data = await reader.read(1000)
                    new_name = data.decode().strip()
                    new = user_operations.change_folder_name(old_name_of_folder,new_name)
                    if new :
                        display_data = "Rename successful"
                    else:
                        display_data = "Folder name exists"
                    writer.write(display_data.encode())
                elif command_given in ('0', 'Logout', 'logout'):
                    break
        except Exception as excep:
            print(excep)
        finally:
            for line in fileinput.FileInput(filepath,inplace=1):
                if user_id in line:
                    if  password_entered in line:
                        line = line.rstrip()
                        line = line.replace(line, f"{user_id}:{password_entered},\n")
                print(line,end='')
            display_data = "Logged out"
            writer.write(display_data.encode())
    else:
        data = await reader.read(1000)
        display_data="Invalid choice\nPlease restart the client\nIf not working kindly restart server"
        writer.write(display_data.encode())
#----------Implement a function where user selects to register or login----------
async def choose(reader,writer):

    """
    This function askes user if user is registers or not
    and according to the answer,it will navigate to the login function
    or register function.
    """

    message = """
Are you a registered user?
press y to yes
press n to no
Enter your choice :"""
    writer.write(message.encode())
    data = await reader.read(1000)
    choice_selected = data.decode().strip()
    if choice_selected in ('n', 'N', 'No', 'no'):
        await register(reader,writer)
    elif choice_selected in ('y', 'Y', 'Yes', 'yes'):
        await login(reader,writer)
    else:
        display_data = "Invalid choice\nPlease restart server and client"
        writer.write(display_data.encode())
#----------Implement a function too initiate server----------
async def main():

    """
    Thus function initiates a server where the space is created
    for the client to store their files in the given IP Address
    and port number
    """
    server = await asyncio.start_server(
        choose, '127.0.0.1', 8088)

    addr = server.sockets[0].getsockname()
    print(f'Serving on {addr}')

    async with server:
        await server.serve_forever()

asyncio.run(main())
