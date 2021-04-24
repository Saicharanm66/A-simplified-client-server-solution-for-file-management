"""
This file is a barrier between client and server.
It receives the input given by client and sends the
input to server and then the server
executes accordingly and returns output.
This file displays the output returned by server code.
"""
import asyncio
#------------Implement a function where it takes input from user and displays output-----------
async def tcp_echo_client():
    """
    This function takes the inputs from user starting from
    the registration process, login process, the operations
    done after login,and gives the output that sent by server.
    Initially it takesinput from user regarding registration.
    If user is not registered, it sends input to server and the
    process of registration will be initiated.If user needs to login,
    the login form is displayed and the inputs are taken.
    The taken inputs are verified and if everything is right,
    the login will be sucessful.After login, the remaining process
    is initiated.The code will be executed in server according to the
    inputs given by the user in client code.
    For example, if user gives 1 as input after login, the input 1 is
    sent to server where the server enters into if loop containing 1 as
    input.Then it calls the folder_creation function from operations_code file
    and gets executed.The further inputs given by client is taken into server and
    the final output is displayed through client code.
    """
    reader,writer = await asyncio.open_connection('127.0.0.1', 8088)
    data = await reader.read(1000)
    display_data = data.decode().strip()
    print(display_data)
    selected = input()
    writer.write(selected.encode())
    if selected in ('n', 'N', 'No', 'no'):
        data = await reader.read(1000)
        display_data = data.decode().strip()
        name_first = input(display_data)
        writer.write(name_first.encode())
        data = await reader.read(1000)
        display_data = data.decode().strip()
        name_last = input(display_data)
        writer.write(name_last.encode())
        data = await reader.read(1000)
        display_data = data.decode().strip()
        user_id = input(display_data)
        writer.write(user_id.encode())
        data = await reader.read(1000)
        display_data = data.decode().strip()
        password_create=input(display_data)
        writer.write(password_create.encode())
        data = await reader.read(100)
        display_data = data.decode().strip()
        password_re_enter=input(display_data)
        writer.write(password_re_enter.encode())
        data = await reader.read(100)
        if password_create!=password_re_enter:
            try:
                print("Confirm password and password do not match\nPlease try again")

            except Exception as err:
                print(err)

        else:
            display_data = data.decode().strip()
            print(display_data)

    elif selected in ('y', 'Y', 'Yes', 'yes'):
        data = await reader.read(1000)
        display_data = data.decode().strip()
        user_id = input(display_data)
        writer.write(user_id.encode())
        data = await reader.read(1000)
        display_data = data.decode()
        password_entered = input(display_data)
        writer.write(password_entered.encode())
        data = await reader.read(10000)
        display_data = data.decode().strip()
        print(display_data)
        if display_data in ('Access denied\\nThe user is already logged in\\nPlease restart server and client', 'Invalid Username or Password\\nPlease restart server and client', 'Invalid choice\\nPlease restart server and client'):
            exit()
        while True:
            command_given = input("Enter your choice : ")
            writer.write(command_given.encode())
            if command_given in ('1', 'create new folder', 'Create new folder', 'create_folder'):
                data = await reader.read(1000)
                display_data = data.decode().strip()
                input_file_name = input(display_data)
                writer.write(input_file_name.encode())
                data = await reader.read(1000)
                display_data = data.decode().strip()
                print(display_data)
            elif command_given in ('2', 'create a new file', 'Create a new file', 'write_file'):
                data = await reader.read(100)
                display_data = data.decode().strip()
                folder_name = input(display_data)
                writer.write(folder_name.encode())
                data = await reader.read(100)
                display_data = data.decode().strip()
                file_name = input(display_data)
                writer.write(file_name.encode())
                data = await reader.read(100)
                display_data = data.decode().strip()
                input_data = input(display_data)
                writer.write(input_data.encode())
                data = await reader.read(100000)
                display_data = data.decode().strip()
                print(display_data)
            elif command_given in ('3', 'open the file', 'Open the file', 'read_file'):
                data = await reader.read(1000)
                display_data = data.decode().strip()
                folder_name = input(display_data)
                writer.write(folder_name.encode())
                data = await reader.read(1000)
                display_data = data.decode().strip()
                file_name = input(display_data)
                writer.write(file_name.encode())
                data = await reader.read(1000)
                display_data = data.decode().strip()
                print(display_data)
            elif command_given in ('4', 'View list of folders', 'view list of folders', 'folders list', 'list'):
                data = await reader.read(1000)
                display_data = data.decode().strip()
                print(display_data)
                writer.write("hi".encode())
                data = await reader.read(100)
                show_folder_name = data.decode().strip()
                name = list(show_folder_name.split(" "))
                writer.write("hello".encode())
                data = await reader.read(20)
                show_folder_size = data.decode().strip()
                size = list(show_folder_size.split(" "))
                writer.write("hello".encode())
                data = await reader.read(90)
                show_created_time = data.decode().strip()
                created = list(show_created_time.split("  "))
                writer.write("hello".encode())
                data = await reader.read(90)
                show_modified_time = data.decode().strip()
                modified = list(show_modified_time.split("  "))
                writer.write("hello".encode())
                for folder in range(len(name)):
                    print(f"{name[folder]}  {size[folder]}   {created[folder]}  {modified[folder]}")
            elif command_given in ('5', 'change_folder', 'Change folder', 'change folder'):
                data = await reader.read(1000)
                display_data = data.decode().strip()
                folder_to_change = input(display_data)
                writer.write(folder_to_change.encode())
                data = await reader.read(1000)
                display_data = data.decode().strip()
                print(display_data)
            elif command_given in ('6', 'Rename folder', 'rename folder'):
                data = await reader.read(1000)
                display_data = data.decode().strip()
                folder_to_change = input(display_data)
                writer.write(folder_to_change.encode())
                data = await reader.read(1000)
                display_data = data.decode().strip()
                new_name = input(display_data)
                writer.write(new_name.encode())
                data = await reader.read(1000)
                display_data = data.decode().strip()
                print(display_data)
            elif command_given in ('0', 'Logout', 'logout'):
                break
        data = await reader.read(1000)
        display_data = data.decode().strip()
        print(display_data)
    else:
        data = await reader.read(1000)
        display_data = data.decode().strip()
        print(display_data)
    writer.close()
asyncio.run(tcp_echo_client())
