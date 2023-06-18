import tkinter
from tkinter import *
from tkinter.ttk import *

window = tkinter.Tk()
window.geometry("1280x720")
window.title("CyberSecurityAssignment")
window.configure(bg='pink')

def onclick(args):
    global label
    if args == 1:
        Task1()
    if args == 2:
        Task2()
    if args == 3:
        Task3()
    if args == 4:
        Task4()
    if args == 5:
        label.destroy()
        try:
            b5.destroy()
            b6.destroy()
            main()
        except:
            main()
    if args == 6:
        label = tkinter.Label(window, text="24")
        label.pack()
        b1.destroy()
        b2.destroy()
        b3.destroy()
        b4.destroy()
        b5.destroy()
        b6.destroy()
    if args == 7:
        label = tkinter.Label(window, text="d4c3b2a1 - little endian")
        label.pack()
        b1.destroy()
        b2.destroy()
        b3.destroy()
        b4.destroy()
        b5.destroy()
        b6.destroy()
    if args == 8:
        label = tkinter.Label(window, text="Major Version: 0002\nMinor Version: 0004")
        label.pack()
        b1.destroy()
        b2.destroy()
        b3.destroy()
        b4.destroy()
        b5.destroy()
        b6.destroy()
    if args == 9:
        label = tkinter.Label(window, text="0000ffff")
        label.pack()
        b1.destroy()
        b2.destroy()
        b3.destroy()
        b4.destroy()
        b5.destroy()
        b6.destroy()
    if args == 10:
        label = tkinter.Label(window, text="01000000")
        label.pack()
        b1.destroy()
        b2.destroy()
        b3.destroy()
        b4.destroy()
        b5.destroy()
        b6.destroy()
    if args == 11:
        label = tkinter.Label(window, text="27/01/2017 22:53:08")
        label.pack()
        b1.destroy()
        b2.destroy()
        b3.destroy()
        b4.destroy()
        b5.destroy()
        b6.destroy()
        b6.destroy()
    if args == 12:
        label = tkinter.Label(window, text="22:53:08 GMT")
        label.pack()
        b1.destroy()
        b2.destroy()
        b3.destroy()
        b4.destroy()
        b5.destroy()
        b6.destroy()
        b6.destroy()
    if args == 13:
        label = tkinter.Label(window, text="348")
        label.pack()
        b1.destroy()
        b2.destroy()
        b3.destroy()
        b4.destroy()
        b5.destroy()
        b6.destroy()
        b6.destroy()
    if args == 14:
        label = tkinter.Label(window, text="Source: 5c:26:0a:02:a8:e4\nDestination: 00:d0:ba:49:2c:a1")
        label.pack()
        b1.destroy()
        b2.destroy()
        b3.destroy()
        b4.destroy()
        b5.destroy()
        b6.destroy()
        b6.destroy()
    if args == 15:
        label = tkinter.Label(window, text="Source: 172.16.4.1\nDestination: 172.16.4.193")
        label.pack()
        b1.destroy()
        b2.destroy()
        b3.destroy()
        b4.destroy()
        b5.destroy()
        b6.destroy()
        b6.destroy()
    if args == 16:
        label = tkinter.Label(window, text="Stewie-PC")
        label.pack()
        b2.destroy()
        b3.destroy()
        b4.destroy()
        b1.destroy()
        b5.destroy()
        b6.destroy()
    if args == 17:
        label = tkinter.Label(window, text="Suspected website: http://p27dochpz2n7nvgr.1jw2lx.top")
        label.pack()
        b1.destroy()
        b2.destroy()
        b3.destroy()
        b6.destroy()
    if args == 18:
        label = tkinter.Label(window, text="www.bing.com")
        label.pack()
        b1.destroy()
        b2.destroy()
        b3.destroy()
        b6.destroy()
    if args == 19:
        label = tkinter.Label(window, text="Words:\nhome\nimprovement\nremodeling\nyour\nkitchen")
        label.pack()
        b1.destroy()
        b2.destroy()
        b3.destroy()
        b6.destroy()
    if args == 20:
        label = tkinter.Label(window, text="Sites: www.homeimprovement.com/remodeling-your-kitchen-cabinets.html")
        label.pack()
        b1.destroy()
        b2.destroy()
        b3.destroy()
        b6.destroy()
        

def main():
    global b1,b2,b3,b4,Exit
    Exit = tkinter.Button(window, text="Exit", width=10, height=5, command=window.destroy)
    b1 = tkinter.Button(window, text="Task 1", width=20, height=10, command=lambda:onclick(1))
    b2 = tkinter.Button(window, text="Task 2", width=20, height=10, command=lambda:onclick(2))
    b3 = tkinter.Button(window, text="Task 3", width=20, height=10, command=lambda:onclick(3))
    b4 = tkinter.Button(window, text="Task 4", width=20, height=10, command=lambda:onclick(4))

    Exit.place(x=0,y=0)
    b1.place(x=150,y=250)
    b2.place(x=400,y=250)
    b3.place(x=650,y=250)
    b4.place(x=900,y=250)


def Task1():
    global b5
    b1.config(text="Global header length", command=lambda:onclick(6))
    b2.config(text="Magic number/endianness", command=lambda:onclick(7))
    b3.config(text="Major and minor numbers", command=lambda:onclick(8))
    b4.config(text="SnapLength", command=lambda:onclick(9))
    b5 = tkinter.Button(window, text="Data link type", width=20, height=10, command=lambda:onclick(10))
    b5.place(x=525,y=450)
    Exit.destroy()
    esc = tkinter.Button(window, text="Return", width=10, height=5, command=lambda:onclick(5))
    esc.place(x=0,y=0)

def Task2():
    global b5,b6
    b1.config(text="Packet capture timestamp", command=lambda:onclick(11))
    b2.config(text="GMT timestamp", command=lambda:onclick(12))
    b3.config(text="DHCP Frame Length", command=lambda: onclick(13))
    b4.config(text="Source/Dest MAC adresses", command=lambda:onclick(14))
    b5 = tkinter.Button(window, text="Source/Dest IP adresses", width=20, height=10, command=lambda:onclick(15))
    b5.place(x=425,y=450)
    b6 = tkinter.Button(window, text="Host name", width=20, height=10, command=lambda: onclick(16))
    b6.place(x=625, y=450)
    Exit.destroy()
    esc = tkinter.Button(window, text="Return", width=10, height=5, command=lambda:onclick(5))
    esc.place(x=0,y=0)

def Task3():
    b1.config(text="Susceptible Website\n CLICK HERE :)", command=lambda:onclick(17))
    b2.destroy()
    b3.destroy()
    b4.destroy()
    Exit.destroy()
    esc = tkinter.Button(window, text="Return", width=10, height=5, command=lambda:onclick(5))
    esc.place(x=0,y=0)

def Task4():
    b1.config(text="Seach Engine", command=lambda:onclick(18))
    b2.config(text="Words searched", command=lambda:onclick(19))
    b3.config(text="Recommended sites", command=lambda:onclick(20))
    b4.destroy()
    Exit.destroy()
    esc = tkinter.Button(window, text="Return", width=10, height=5, command=lambda:onclick(5))
    esc.place(x=0,y=0)

main()
window.mainloop()
