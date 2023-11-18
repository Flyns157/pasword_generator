# =============================================== imports ===============================================
from tkinter import *
import random

# init
VERSION = 1.0

# ============================================== Functions ==============================================

def create_window(title :str, initialsize : tuple[int,int] = (1080,720), minsize : tuple[int,int] = (720,480), maxsize : tuple[int,int] = (3440,1440), background : str = '#1f1f1f')-> Tk :
    """
    Crée une nouvelle fenêtre Tkinter avec des paramètres spécifiques.

    Args:
        title (str): Le titre de la fenêtre.
        initialsize (tuple[int,int], optional): La taille initiale de la fenêtre. Par défaut à (1080,720).
        minsize (tuple[int,int], optional): La taille minimale de la fenêtre. Par défaut à (720,480).
        maxsize (tuple[int,int], optional): La taille maximale de la fenêtre. Par défaut à (3440,1440).
        background (str, optional): La couleur d'arrière-plan de la fenêtre. Par défaut à '#1f1f1f'.

    Returns:
        Tk: L'objet Tk représentant la fenêtre créée.
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
    Génère un mot de passe aléatoire.

    Args:
        size (int, optional): La longueur du mot de passe. Par défaut à 16.
        letters (bool, optional): Si vrai, inclut des lettres minuscules. Par défaut à True.
        uppercase (bool, optional): Si vrai, inclut des lettres majuscules. Par défaut à True.
        numbers (bool, optional): Si vrai, inclut des chiffres. Par défaut à True.
        specials (bool, optional): Si vrai, inclut des caractères spéciaux. Par défaut à True.

    Returns:
        str: Le mot de passe généré.
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

#créer une boite
frame = Frame(window, bg = '#1f1f1f')

# ajouter du texte
label_titre = Label(frame, text = 'Pass-word generator !', font = ('Arial', 40), bg = '#1f1f1f', foreground = 'white')
label_soustitre = Label(frame, text = 'by CUISSET Mattéo', font = ('Arial', 20), bg = '#1f1f1f', fg = 'white')
password = 'Generated password ...'
password_generated = Entry(frame, font = ('Arial', 20), bg = '#1f1f1f', fg = 'white')

# ajout d'un bouton
yt_button = Button(frame, text = 'generate', font = ('Arial', 15), bg = 'white', fg = '#1f1f1f', command=generate)

# packing
label_titre.pack()
label_soustitre.pack()
yt_button.pack(pady=25, fill=X)
password_generated.pack()
frame.pack(expand=True)

# afficher la fenetre
window.mainloop ()