import tkinter

print("Let's go!")
window = tkinter.Tk()
window.title("My goal")
window.geometry("960x540")
on_click = False
var = tkinter.StringVar()
var.set("Let's make a try.")
i=0
def click():
    global i
    i=i+1
    print(i)
    canvas.move(oval,2,0)
    
def click_exchange():
    global on_click
    if on_click == False:
        on_click = True
        var.set("This is the first page!")
    else:
        on_click=False
        var.set("And the second!")
        
def point():
    var = e.get ()
    t.insert ('insert',var)

def end():
    var = e.get ()
    t.insert ('end',var)
    
def print_selection(v):
    l.config (text='you have selected '+v+'%')

def print_selec():
    if (var1.get() == 1):
        print('I love only Python ')
    if(var2.get() == 1):
        print('I love only php')
    if (var3.get() == 1):
       print('I do not love C++')
    if (var4.get() == 1):
        print('I love JavaScript')
    if (var1.get() == 1 & var2.get() == 1 & var3.get() == 1 & var4.get() == 1):
        print('I love all languages.')
label = tkinter.Label(window,
                      textvariable = var,
                      bg = 'green',
                      font  = ('Arial',12),
                      width=20,height=1
                      )
l = tkinter.Label(window, text='empty',bg='yellow', width=24)
button = tkinter.Button(window,
                        text = 'Click me',
                        bg = 'red',
                        width=10,height=1,
                        command=click
    )
exchange = tkinter.Button(window,
                          text = 'Take a try.',
                          bg='blue',
                          command=click_exchange
                          
    )

insert_point = tkinter.Button(window,
                        text = 'insert point',
                        bg = 'red',
                        width=10,height=1,
                        command=point
    )
insert_end = tkinter.Button(window,
                        text = 'insert end',
                        bg = 'red',
                        width=10,height=1,
                        command=end
    )
s = tkinter.Scale(window,
                  label = 'try me',
                  from_=0,
                  to=100,
                  orient=tkinter.HORIZONTAL,
                  length=1080,
                  resolution=0.1,
                  showvalue=1,
                  tickinterval=10,
                  command=print_selection
                  )
e =tkinter.Entry(window)
t = tkinter.Text(window,height = 2)
canvas = tkinter.Canvas(window, bg='blue', height=200, width=400)

#image_path="m.png"
#canvas.create_image (20,20,anchor='nw',image = "jump.png")      #there is always a path error.
x0,y0,x1,y1=100,100,200,200
line = canvas.create_line(x0,y0,x1,y1)
oval = canvas.create_oval(100,100,200,200,fill='red')

arc = canvas.create_arc  (300,100,400,200,fill='yellow',start=0,extent=120)


var1 = tkinter.IntVar()
var2 = tkinter.IntVar()
var3 = tkinter.IntVar()
var4 = tkinter.IntVar()
c1 = tkinter.Checkbutton(window, text='Python', variable=var1, onvalue=1, offvalue=0,
                    command=print_selec)

c2 = tkinter.Checkbutton(window, text='php', variable=var2, onvalue=1, offvalue=0,
                    command=print_selec)

c3 = tkinter.Checkbutton(window, text='C++', variable=var3, onvalue=1, offvalue=0,
                    command=print_selec)


c4 = tkinter.Checkbutton(window, text='JavaScript', variable=var4, onvalue=1, offvalue=0,
                    command=print_selec)


label.place(x=0,y=0,anchor='nw')
l.pack()
button.pack()
exchange.pack()
e.pack()
t.pack()
insert_point.pack()
insert_end.pack()
s.pack()
canvas.pack()
c1.place(x=600,y=0,anchor='nw')
c2.place(x=680,y=0,anchor='nw')
c3.place(x=760,y=0,anchor='nw')
c4.place(x=840,y=0,anchor='nw')
window.mainloop()

