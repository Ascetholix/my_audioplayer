from audioplayer import AudioPlayer
import tkinter  as tk
from tkinter import filedialog

def open():   # метод открытие файла
    global media_file
    fname = filedialog.askopenfilename()  # путь к файлу
    if fname:
        media_file = AudioPlayer(fname)    # после открытия становиться объетом audioplayer
        media_file.play()         # запуск файла

media_file = None        # переменя объекта в начале пустая 

win = tk.Tk() # начало

win.title('audioplayer')    
win.geometry("270x150+300+200") 

tk.Label(text='ПРОИГРЫВАТЕЛЬ').grid(row=0,column=1)   # Надпись
 
 # кнопки запускают через лямду методы библиотеки audioplayer

btn1 = tk.Button(text='Play',command=lambda:media_file.play())    
btn2 = tk.Button(text='Stop',command=lambda:media_file.stop())
btn3 = tk.Button(text='Pause',command=lambda:media_file.pause())
btn4 = tk.Button(text='Resume',command=lambda:media_file.resume())
btn5 = tk.Button(text='Close',command=lambda:media_file.close())
btn6 = tk.Button(text='Open',command=open)


# Разположение кнопок

btn1.grid(row=1, column=0,stick = 'we')
btn2.grid(row=2, column=1,stick = 'we')  
btn3.grid(row=1, column=1,stick = 'we') 
btn4.grid(row=1, column=2,stick = 'we')  
btn5.grid(row=2, column=2,stick = 'we')  
btn6.grid(row=2, column=0,stick = 'we')  


win.grid_columnconfigure(0,minsize=80)
win.grid_columnconfigure(1,minsize=80)
win.grid_columnconfigure(2,minsize=80)

win.grid_rowconfigure(0,minsize=50)
win.grid_rowconfigure(1,minsize=50)
win.grid_rowconfigure(2,minsize=50)

win.update()
win.mainloop()    # конец