import socket
from tkinter import *
from tkinter import filedialog



def openSENDNewWindow():
     #Toplevel object which will
     #be treated as a new window
    newWindow = Toplevel(root, bg = "white")

     #sets the title of the
     #Toplevel widget
    newWindow.title("SEND Window")

     #sets the geometry of toplevel
    newWindow.geometry("400x200")
    
    def location():
        filepath = filedialog.askopenfilename()
        print(f"Your desired file path is: {filepath}")
    btn_connect = Button(newWindow,text="Get File Location", command=location, bg="lightblue", padx=20,
        pady=20).place(x=130, y=100)



s = socket.socket()
host = socket.gethostname()
port = 8080
s.bind((host, port))
s.listen(1)
print(host)
print("Waiting for any incoming connections...")



conn, addr = s.accept()
print(addr, "Has connected to the server")



root = Tk()
root.title("File Share")
root.geometry("800x600")
root.config(bg="lightblue")
button_send = Button(root,text ="SEND",command=openSENDNewWindow, bg="white", padx=20, pady=20)
button_send.place(x=350, y=450)


l1 = Label(root, text="Welcome to file share.",font=("Courier", 20)).place(x=230, y=250)
l2 = Label(root, text="Use the button to navigate To sending page",font=("Courier", 20)).place(x=50, y=310)
l4 = Label(root, text="To select the file that You want to share.",font=("Courier", 20)).place(x=50, y=370)

img=PhotoImage(file='file_share.png')
Label(root,image=img).place(x=280, y=20)

root.mainloop()



filename = input("Please enter the filename you wish to transfer : ")
file = open(filename, 'rb')
file_data = file.read(1024*3000)
conn.send(file_data)
print("Data transmission successful")

