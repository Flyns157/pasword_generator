# =============================================== imports ===============================================
from tkinter import *
import random

# init
VERSION = 1.0

# ============================================== Functions ==============================================

def create_window(title :str, initialsize : tuple[int,int] = (1080,720), minsize : tuple[int,int] = (720,480), maxsize : tuple[int,int] = (3440,1440), background : str = '#1f1f1f')-> Tk :
    """
    Creates a new Tkinter window with specific parameters.

    Args:
        title (str): The window title.
        initialsize (tuple[int,int], optional): The initial size of the window. Defaults to (1080,720).
        minsize (tuple[int,int], optional): Minimum window size. Defaults to (720,480).
        maxsize (tuple[int,int], optional): Maximum window size. Defaults to (3440,1440).
        background (str, optional): Window background color. Defaults to '#1f1f1f'.

    Returns:
        Tk: The Tk object representing the created window.
    """
    window = Tk()
    window.title (title)
    window.geometry(f'{initialsize[0]}x{initialsize[1]}')
    window.minsize(minsize[0],minsize[1])
    window.maxsize(maxsize[0],maxsize[1])
    window.iconbitmap('logo.ico')
    window.config(bg=background)
    return window

def generate_password(size : int = 16, letters : bool = True, uppercase : bool = True, numbers : bool = True, specials : bool = True)-> str :
    """
    Generates a random password.

    Args:
        size (int, optional): Password length. Defaults to 16.
        letters (bool, optional): If true, includes lowercase letters. Defaults to True.
        uppercase (bool, optional): If true, includes uppercase letters. Defaults to True.
        numbers (bool, optional): If true, includes numbers. Defaults to True.
        specials (bool, optional): If true, includes special characters. Defaults to True.

    Returns:
        str: The generated password.
    """
    global_data = ['0123456789','abcdefghijklmnopqrstuvwxyz','ABCDEFGHIJKLMNOPQRSTUVWXYZ','''"«»‹›“”„'‘’‚…!¡?¿()[]{}¨´`^ˆ~˜¸#*,.:;·•¯‾-–—_|¦‌‍†‡§¶©®™&@/\◊♠♣♥♦←↑→↓↔áÁâÂàÀåÅãÃäÄæÆçÇéÉêÊèÈëËíÍîÎìÌïÏñÑóÓôÔòÒøØõÕöÖœŒšŠßðÐþÞúÚûÛùÙüÜýÝÿŸ¤€$¢£¥ƒαΑβΒγΓδΔεΕζΖηΗθΘιΙκΚλΛμΜνΝξΞοΟπΠρΡσςΣτΤυΥφΦχΧψΨωΩ°µ<>≤≥=≈≠≡±−+×÷⁄%‰¼½¾¹²³ºªƒ′″∂∏∑√∞¬∩∫''']
    concerned_data = [global_data[n] for n,ok in [(1,letters), (2,uppercase), (0,numbers), (3,specials)] if ok]
    tmp_password = ''
    N = len(concerned_data)
    for _ in range(size) :
        tmp = random.randint(0, N-1)
        tmp_password += concerned_data[tmp][int(random.random()*len(concerned_data[tmp]))]
    return tmp_password

def generate() :
    password_generated.delete(0, END)
    password_generated.insert(0, generate_password(random.randint(16,21),letters=True,uppercase=True,numbers=True,specials=True))

# ============================================== Execution ==============================================
window = create_window('Pass-word generator')

# Create a box
frame = Frame(window, bg = '#1f1f1f')

# Add text
label_titre = Label(frame, text = 'Pass-word generator !', font = ('Arial', 40), bg = '#1f1f1f', foreground = 'white')
label_soustitre = Label(frame, text = 'by CUISSET Mattéo', font = ('Arial', 20), bg = '#1f1f1f', fg = 'white')
password = 'Generated password ...'
password_generated = Entry(frame, font = ('Arial', 20), bg = '#1f1f1f', fg = 'white')

# Add a button
yt_button = Button(frame, text = 'generate', font = ('Arial', 15), bg = 'white', fg = '#1f1f1f', command=generate)

# packing
label_titre.pack()
label_soustitre.pack()
yt_button.pack(pady=25, fill=X)
password_generated.pack()
frame.pack(expand=True)

# Display the window
window.mainloop ()