# Joyce Choo (jxc180040)
# Partner: Taylor Kettle (tmk160430)
import socket
import os
SEPARATOR = "<SEPARATOR>"
filename = "hello.txt"
filesize = os.path.getsize("hello.txt")
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(('10.0.0.1', 6677))
info = filename + SEPARATOR + str(filesize)
s.send(info.encode())
with open("hello.txt", "rb") as f:
    bytes_read = f.read(1024)
    s.sendall(bytes_read)
print('Sending...')
flag = True
while flag:
    print("Menu: ")
    print("1. Make a copy of a file")
    print("2. Rename a file")
    print("3. Delete a file")
    print("4. Create a file:")
    print("5. Exit")
    val = input("Which file operation would you like performed? ")
    s.send(val.encode())
    if(val == "1"):
        print(s.recv(1024))
        filetocopy = input()
        s.send(filetocopy.encode())
        print(s.recv(1024))
        newnameofcopy = input()
        s.send(newnameofcopy.encode())
    if(val == "2"):
        print(s.recv(1024))
        rename = input()
        s.send(rename.encode())
        print(s.recv(1024))
        newname = input()
        s.send(newname.encode())
    if(val == "3"):
        print(s.recv(1024))
        delete = input()
        s.send(delete.encode())
    if(val == "4"):
        print(s.recv(1024))
        nameofnewfile = input()
        s.send(nameofnewfile.encode())
        print(s.recv(1024))
        content = input()
        s.send(content.encode())
    if(val == "5"):
        flag = False
s.shutdown(socket.SHUT_WR)
print(s.recv(1024))
s.close()

