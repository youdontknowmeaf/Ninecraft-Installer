from tkinter import *
import os, sys
from tkinter import messagebox

window = Tk() # Tk window "window"

#---------------- <image shit>

def resource_path(relative_path):
    try:
        base_path = sys._MEIPASS  # PyInstaller temp folder
    except AttributeError:
        base_path = os.path.abspath(".")
    return os.path.join(base_path, relative_path)


#----------------- <Variables>

icon = PhotoImage(file=resource_path('mcpi.png'))
small_icon = icon.subsample(3, 3)

fedora = IntVar()
debian = IntVar()
arch = IntVar()


#----------------- <Functions>

def submit():
    global ultimate_path
    ultimate_path = path.get()
    messagebox.showinfo(title='info', message=f'Path: {ultimate_path}')
    path.config(state=DISABLED)

def unsupported_message():
    messagebox.showinfo(title='Information', message="Unsupported distro? Install dependencies manually! See github for instructions.")

def warning_message():
    messagebox.showerror(title='Uh, oh...', message="Something went wrong! Make sure all the data you input is correct, and that you have a stable internet connection.")

def starting_message():
    messagebox.showinfo(title='Welcome!', message="Hello and welcome to Ninecraft installer! Please make sure you are connected to internet, you have mcpe.apk installed, you run this program as sudo and that you didnt get this code from some ass source!")

def download_mc():
    try:
        os.system("git clone --recursive http://github.com/MCPI-Revival/Ninecraft.git")
        os.system(f'sudo mv {ultimate_path} Ninecraft/mcpe.apk')
        os.system(f"cd Ninecraft && make build-i686 && ./tools/extract.sh mcpe.apk")
    except:
        warning_message()


def get_linux():
    try:
        if debian.get() == 1:
            os.system("sudo apt update && sudo apt install -y git make cmake gcc g++ gcc-multilib g++-multilib libopenal-dev:i386 libx11-dev:i386 libxrandr-dev:i386 libxinerama-dev:i386 libxcursor-dev:i386 libxi-dev:i386 libgl-dev:i386 zenity unzip python3-jinja2")
        elif arch.get() == 1:
            os.system("sudo pacman -Syu --noconfirm git make cmake gcc gcc-multilib lib32-openal lib32-libx11 lib32-libxrandr lib32-libxinerama lib32-libxcursor lib32-libxi lib32-libglvnd zenity unzip python-jinja")
        elif fedora.get() == 1:
            os.system("sudo dnf install -y git make cmake gcc g++ glibc-devel.i686 libstdc++-devel.i686 openal-soft-devel.i686 libX11-devel.i686 libXrandr-devel.i686 libXinerama-devel.i686 libXcursor-devel.i686 libXi-devel.i686 libglvnd-devel.i686 zenity unzip python3-jinja2")
        else:
            unsupported_message()
    except:
        warning_message()
        
#------------------ <Window configuration>

window.geometry("800x800")
window.title("Installer")
window.iconphoto(True, icon)
window.config(background="black")

#------------------ <Labels>

label = Label(
            window, 
            text="Welcome to Ninecraft installer!", 
            font=('Arial',15,'bold'), 
            fg='brown', 
            bg='black',
            bd=10,
            padx=10,
            pady=10,
            image=small_icon,
            compound='top')

instructions = Label(
                    window,
                    text="Enter your apk path. (make sure its called mcpe.apk)",
                    font=('Arial',15,'bold'),
                    fg='brown', 
                    bg='black',
                    bd=10,
                    padx=10,
                    pady=10)

#------------------ <checkbuttons>

arch_check = Checkbutton(window,
                        text="Arch Linux (Arch Based)",
                        variable=arch,
                        onvalue=1,
                        offvalue=0,
                        fg="black",
                        bg="#807501",
                        activeforeground="#807501",
                        activebackground="white")
debian_check = Checkbutton(window,
                        text="Debian (ubuntu, mint)",
                        variable=debian,
                        onvalue=1,
                        offvalue=0,
                        fg="black",
                        bg="#807501",
                        activeforeground="#807501",
                        activebackground="white")
fedora_check = Checkbutton(window,
                        text="Fedora (RHEL, Fedora-based)",
                        variable=fedora,
                        onvalue=1,
                        offvalue=0,
                        fg="black",
                        bg="#807501",
                        activeforeground="#807501",
                        activebackground="white")

#----------------- <Entries>

path = Entry(window,
            font=("Arial",15),
            width=37)
path.insert(0,'/home/admin/Documents/mcpe.apk')

#------------------ <Buttons>

install = Button(window,
                text="Install dependencies",
                command=get_linux,
                font=('Arial', 20),
                fg="black",
                bg="#807501",
                activeforeground="#807501",
                activebackground="white",
                state=ACTIVE)


submit_button = Button(window,
                        text="submit",
                        command=submit,
                        fg="black",
                        bg="#807501",
                        activeforeground="#807501",
                        activebackground="white",
                        height=1)

download_button = Button(window,
                        text="Set up ninecraft!",
                        command=download_mc,
                        font=('Arial', 20),
                        fg="black",
                        bg="#807501",
                        activeforeground="#807501",
                        activebackground="white",
                        state=ACTIVE)
#-------------------

starting_message()

label.pack()
arch_check.place(x=0, y=200)
debian_check.place(x=205, y=200)
fedora_check.place(x=400, y=200)
install.place(x=150, y=230)
instructions.place(x=100, y=270)
path.place(x=0, y=336)
submit_button.place(x=490, y=335)
download_button.place(x=200, y=500)

window.mainloop()
