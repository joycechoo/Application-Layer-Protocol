# Joyce Choo (jxc180040)
# Partner: Taylor Kettle (tmk160430)
import socket
import os

SEPARATOR = "<SEPARATOR>"
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(("10.0.0.1", 6677))
s.listen(5)
clientsocket, address = s.accept()  # receive files and address
print('Server: Got connection from', address)
print("Server: Receiving...")
received = clientsocket.recv(1024).decode()
filename, filesize = received.split(SEPARATOR)
filename = os.path.basename(filename)
filesize = int(filesize)
with open(filename, "wb") as f:
    bytes_read = clientsocket.recv(1024)
    f.write(bytes_read)

print("Server: Done receiving")
flag = True
while flag:
    msg = clientsocket.recv(1024).decode()
    # Copying files
    if msg == "1":
        clientsocket.send(bytes("Server: Which file would you like to copy?", "utf-8"))  # send utf-8 bytes
        filetocopy = clientsocket.recv(1024).decode()
        clientsocket.send(bytes("Server: What would you like to name the copy?", "utf-8"))  # send utf-8 bytes
        newcopyname = clientsocket.recv(1024).decode()
        print("Server: Copying...")
        f = open(filetocopy, "r")
        contents = f.read()
        f.close()
        f = open(newcopyname,"w+")
        f.write(contents)
        f.close()
        print("Server: Done copying")
    # Renaming files
    elif msg == "2":
        clientsocket.send(bytes("Server: Which file would you have renamed?", "utf-8"))  # send utf-8 bytes
        rename = clientsocket.recv(1024).decode()
        print(rename)
        sourcepath = "/home/mininet/mininet/server/" + rename
        print(sourcepath)
        clientsocket.send(bytes("Server: What would you like the new file name to be?", "utf-8"))  # send utf-8 bytes
        newname = clientsocket.recv(1024).decode()
        print(newname)
        destpath = "/home/mininet/mininet/server/" + newname
        print(destpath)
        print("Server: Renaming file...")
        try:
            os.rename(sourcepath, destpath)
            print("Server: Done renaming")
        except:
            print("Server: Error renaming")
    # Deleting files
    elif msg == "3":
        clientsocket.send(bytes("Server: Which file would you like to delete?", "utf-8"))  # send utf-8 bytes
        delete = clientsocket.recv(1024).decode()
        print("Server: Deleting file...")
        os.remove(delete)
        print("Server: File has been deleted")
    # Creating new files
    elif msg == "4":
        clientsocket.send(bytes("Server: What is the name of the new file?", "utf-8"))  # send utf-8 bytes
        nameofnewfile = clientsocket.recv(1024).decode()
        clientsocket.send(bytes("Server: What would you like the file to say?", "utf-8"))  # send utf-8 bytes
        contents = clientsocket.recv(1024).decode()
        print("Server: Creating new file")
        f = open(nameofnewfile,"w+")
        f.write(contents)
        f.close()
        print("Server: Done creating")
    # Exit
    elif msg == "5":
        flag = False
    # Anything else
    else:
        clientsocket.send(bytes("Server: Invalid input, please enter an option between 1-4", "utf-8"))  # send utf-8 bytes
clientsocket.send(bytes("Server: Thank you for connecting", "utf-8"))  # send utf-8 bytes
clientsocket.close()