from tkinter import *
from tkinter import messagebox
import pygame
pygame.init()

def noteC():
    sound=pygame.mixer.Sound("C:\Python Music\Music_Notes\C.wav")
    sound.play()

def noteCS():
    sound=pygame.mixer.Sound("C:\Python Music\Music_Notes\C_s.wav")
    sound.play()
    
def noteD():
    sound=pygame.mixer.Sound("C:\Python Music\Music_Notes\D.wav")
    sound.play()

def noteDS():
    sound=pygame.mixer.Sound("C:\Python Music\Music_Notes\D_s.wav")
    sound.play()
    
def noteE():
    sound=pygame.mixer.Sound("C:\Python Music\Music_Notes\E.wav")
    sound.play()

def noteF():
    sound=pygame.mixer.Sound("C:\Python Music\Music_Notes\F.wav")
    sound.play()

def noteFS():
    sound=pygame.mixer.Sound("C:\Python Music\Music_Notes\F_s.wav")
    sound.play()

def noteG():
    sound=pygame.mixer.Sound("C:\Python Music\Music_Notes\G.wav")
    sound.play()

def noteGS():
    sound=pygame.mixer.Sound("C:\Python Music\Music_Notes\G_s.wav")
    sound.play()

def noteA():
    sound=pygame.mixer.Sound("C:\Python Music\Music_Notes\A.wav")
    sound.play()
    
def noteAS():
    sound=pygame.mixer.Sound("C:\Python Music\Music_Notes\Bb.wav")
    sound.play()

def noteB():
    sound=pygame.mixer.Sound("C:\Python Music\Music_Notes\B.wav")
    sound.play()
    
def noteC2():
    sound=pygame.mixer.Sound("C:\Python Music\Music_Notes\C2.wav")
    sound.play()


root=Tk() 
root.geometry("750x680")
root.configure(background="gray")
root.title("Music Maker")


C=Button(root,text=" ",height=18,width=8,bg="white",command=noteC)
C.place(x=0,y=380)

C_sharp=Button(root,text=" ",height=10,width=8,bg="black",command=noteCS)
C_sharp.place(x=30,y=380)

D=Button(root,text=" ",height=18,width=8,bg="white",command=noteD)
D.place(x=68,y=380)

D_sharp=Button(root,text=" ",height=10,width=8,bg="black",command=noteDS)
D_sharp.place(x=98,y=380)

E=Button(root,text=" ",height=18,width=8,bg="white",command=noteE)
E.place(x=136,y=380)

F=Button(root,text=" ",height=18,width=8,bg="white",command=noteF)
F.place(x=204,y=380)

F_sharp=Button(root,text=" ",height=10,width=8,bg="black",command=noteFS)
F_sharp.place(x=234,y=380)

G=Button(root,text=" ",height=18,width=8,bg="white",command=noteG)
G.place(x=272,y=380)

G_sharp=Button(root,text=" ",height=10,width=8,bg="black",command=noteGS)
G_sharp.place(x=302,y=380)

A=Button(root,text=" ",height=18,width=8,bg="white",command=noteA)
A.place(x=340,y=380)

A_sharp=Button(root,text=" ",height=10,width=8,bg="black",command=noteAS)
A_sharp.place(x=370,y=380)

B=Button(root,text=" ",height=18,width=8,bg="white",command=noteB)
B.place(x=408,y=380)

C2=Button(root,text=" ",height=18,width=8,bg="white",command=noteC2)
C2.place(x=476,y=380)

root.bind('z',lambda event:noteC())
root.bind('s',lambda event:noteCS())
root.bind('x',lambda event:noteD())
root.bind('d',lambda event:noteDS())
root.bind('c',lambda event:noteE())
root.bind('v',lambda event:noteF())
root.bind('g',lambda event:noteFS())
root.bind('b',lambda event:noteG())
root.bind('h',lambda event:noteGS())
root.bind('n',lambda event:noteA())
root.bind('j',lambda event:noteAS())
root.bind('m',lambda event:noteB())
root.bind(',',lambda event:noteC2())


root.mainloop()