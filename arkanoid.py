from tkinter import *
 
dx = 7
dy = dx
score = 0
 
def move_ball():
    '''Moving the ball'''
    global dx, dy, score
    if canv.coords(ball)[1] < 0:
        dy = -dy
    if canv.coords(ball)[2] > 500:
        dx = -dx
    if canv.coords(ball)[0] < 0:
        dx = -dx
    if canv.coords(ball)[3]>=480 and canv.coords(ball)[2]>=canv.coords(bar)[0] and canv.coords(ball)[0]<=canv.coords(bar)[2] and canv.coords(ball)[3]<=490:
        dy = -dy
        score+=1
        label1.set('Score : ' + str(score))
    if canv.coords(ball)[3] < 550:
        root.after(100, move_ball)
    canv.move(ball, dx, dy)
 
def move_bar(event):
    '''Moving the bar'''
    if event.keysym == 'Left':
        canv.move(bar, -10, 0)
    if event.keysym == 'Right':
        canv.move(bar, 10, 0)
    if canv.coords(bar)[0] < 0:
        canv.move(bar, -canv.coords(bar)[0], 0)
    if canv.coords(bar)[2] > 500:
        canv.move(bar, 500 - canv.coords(bar)[2], 0)
 
root = Tk()
root.title('Arkanoid')
 
canv = Canvas(root,width=500,height=500, bg='lightblue')
canv.pack()

label1 = StringVar()
label1.set('Score : 0')

label_f = Label(root, textvariable = label1, fg ='black', bg ='white')
label_f.pack(padx=20, pady=5)

ball = canv.create_oval(240,20,260,40,outline='black',fill='purple')
bar = canv.create_rectangle(200, 460, 300, 475, outline='pink', fill='black')
 
canv.focus_set()
 
canv.bind('<KeyPress>',move_bar)
 
move_ball()
 
root.mainloop()
