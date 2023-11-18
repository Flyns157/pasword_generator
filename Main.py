# imports
from tkinter import *
import webbrowser

# init
VERSION = 1.0

# Functions

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
    window.geometry(f'{initialsize[0]}x{initialsize(1)}')
    window.minsize(minsize[0],minsize[1])
    window.maxsize(maxsize[0],maxsize[1])
    window.iconbitmap('logo.ico')
    window.config(bg=background)
    return window

# Execution
window = create_window('Pass-word generator')

#créer une boite
frame = Frame(window, bg = '#1f1f1f', bd = 1, relief = SUNKEN)

# ajouter du texte
label_titre = Label(frame, text = 'hello world !', font = ('Arial', 40), bg = '#1f1f1f', foreground = 'white')
label_soustitre = Label(frame, text = 'by CUISSET Mattéo', font = ('Arial', 20), bg = '#1f1f1f', fg = 'white')

# ajout d'un bouton
yt_button = Button(frame, text = 'youtube', font = ('Arial', 15), bg = 'white', fg = '#1f1f1f', command=open_yt)

# packing
label_titre.pack()
label_soustitre.pack()
yt_button.pack(pady=25, fill=X)
frame.pack(expand=True)

# afficher la fenetre
window.mainloop ()