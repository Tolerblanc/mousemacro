from tkinter import *
import win32api,win32con #need win32 module
import time
import threading


xpos=str(0)
ypos=str(0) #mouse position
macrodata=[] #queue

n=0 #repeat var

class cont1: #button container 1
    def __init__(self,win):
        self.buttonframe=Frame(win)
        self.buttonframe.pack(fill=X,anchor=N)
        self.button=Button(self.buttonframe,text="delete last data",command=dellast)
        self.button.pack(side=LEFT,padx=10,pady=10)
        self.button1=Button(self.buttonframe,text="delete all",command=delall)
        self.button1.pack(side=LEFT,pady=10,padx=13)
        self.button2=Button(self.buttonframe,text="left click",command=leftclickdata)
        self.button2.pack(side=LEFT,pady=10,padx=16)
        self.button3=Button(self.buttonframe,text="right click",command=rightclickdata)
        self.button3.pack(side=LEFT,pady=10,padx=19)
        self.button3=Button(self.buttonframe,text="double click",command=doubleclickdata)
        self.button3.pack(side=LEFT,pady=10,padx=22)

class cont2: #button container 2
    def __init__(self,win):
        self.buttonframe=Frame(win)
        self.buttonframe.pack(fill=X,anchor=N)
        self.solin=Entry(self.buttonframe,width=6)
        self.solin.pack(side=LEFT,padx=1)
        self.solin1=Entry(self.buttonframe,width=6)
        self.solin1.pack(side=LEFT,padx=1)
        self.button=Button(self.buttonframe,text="move",command=positiondata)
        self.button.pack(side=LEFT,padx=5)
        self.solin2=Entry(self.buttonframe,width=5)
        self.solin2.pack(side=LEFT,padx=1)
        self.button1=Button(self.buttonframe,text="delay",command=delaydata)
        self.button1.pack(side=LEFT)
        self.button2=Button(self.buttonframe,text="show queue",command=disqueue)
        self.button2.pack(side=LEFT)

class cont3: #button container 3 
    def __init__(self,win):
        self.buttonframe=Frame(win)
        self.buttonframe.pack(fill=X,anchor=N)
        self.solin=Entry(self.buttonframe,width=6)
        self.solin.pack(side=LEFT,padx=1)
        button=Button(self.buttonframe,text="execute",width=30,command=macroon)
        button.pack(side=LEFT,anchor=N,padx=5,pady=5)
        button1=Button(self.buttonframe,text="stop",width=30,command=macrooff)
        button1.pack(side=LEFT,anchor=N,padx=5,pady=5)

class cont4: #log container
    def __init__(self,win):
        self.win=win
    def message_frame(self):
        self.buttonframe = Frame(self.win)
        self.buttonframe.pack(side=LEFT,fill=X,anchor=N)
        self.scrollbar = Scrollbar(self.win)
        self.scrollbar.pack(side=LEFT,anchor=NE,ipady=102)
        self.listbox= Listbox(self.buttonframe,yscrollcommand = self.scrollbar.set, bg="white",width=32,height=16)
        self.listbox.pack(side=LEFT)
        self.scrollbar.config(command=self.listbox.yview)
    def message_dis(self,msg) :
        self.listbox.insert(END,msg)

class cont5: #listbox container
    def __init__(self,win):
        self.win=win
    def message_frame(self):
        self.buttonframe = Frame(self.win)
        self.buttonframe.pack(side=LEFT,fill=X,anchor=N)
        self.scrollbar = Scrollbar(self.win)
        self.scrollbar.pack(side=LEFT,anchor=NE,ipady=102)
        self.listbox= Listbox(self.buttonframe,yscrollcommand = self.scrollbar.set, bg="white",width=33,height=16)
        self.listbox.pack(side=LEFT)
        self.scrollbar.config(command=self.listbox.yview)
    def message_dis(self,msg) :
        self.listbox.insert(END,msg)


win = Tk()
win.title("Micro Macro")
win.geometry("500x400+200+100")
win.resizable(0,0)

label1=Label(win,text='Mouse Position     X   :   '+xpos+'    Y   :   '+ypos)
label1.pack(padx=5,anchor=NW)

def positiondata():
    try:
        macrodata.append(["posmove",container2.solin.get(),container2.solin1.get()])
        container4.message_dis("좌표 이동 추가 : X="+str(container2.solin.get())+"  Y="+str(container2.solin1.get()))
        container5.message_dis(macrodata)
    except ValueError:
        print("")
    container2.solin.delete(0,len(container2.solin.get()))
    container2.solin1.delete(0,len(container2.solin1.get()))

def delaydata():
    macrodata.append(["delay",container2.solin2.get()])
    container4.message_dis(str(container2.solin2.get())+"초 딜레이 추가")
    container5.message_dis(macrodata)
    container2.solin2.delete(0,len(container2.solin2.get()))

def leftclickdata():
    macrodata.append(["lclick",1])
    container4.message_dis("마우스 왼쪽 클릭 추가")
    container5.message_dis(macrodata)

def rightclickdata():
    macrodata.append(["rclick",1])
    container4.message_dis("마우스 오른쪽  클릭 추가")
    container5.message_dis(macrodata)

def doubleclickdata():
    macrodata.append(["dclick",1])
    container4.message_dis("마우스 더블 클릭 추가")
    container5.message_dis(macrodata)

def dellast():
    try:
        macrodata.pop()
    except IndexError  :
        print("",end="")
        
    container4.message_dis("작업큐의 가장 최근 데이터 삭제")
    container5.message_dis(macrodata)

def delall():
    try:
        for data in macrodata[0:]:
            macrodata.pop()
    
    except IndexError:
        print("",end="")
    container4.message_dis("작업큐 모두 삭제")
    container5.message_dis(macrodata)

def disqueue():
    container4.message_dis("작업큐 보기")
    if len(macrodata)==0:
        container5.message_dis("NONE")
    else:
        container5.message_dis(macrodata)

def macrooff():
    escapemacro = 1
    

def macroon():
    k=int(len(macrodata))
    escapemacro=0
    if container3.solin.get() == "":
        container4.message_dis("반복 횟수를 입력해주세요")
    else:
        n=int(container3.solin.get())
        container4.message_dis("---------매크로 시작---------")

    try:    
        for j in range(0,n,1):
            for i in range(0,k,1) :
                if escapemacro == 1:
                    break
                if macrodata[i][0]=="posmove":
                    container4.message_dis("좌표 이동 :  X="+macrodata[i][1]+"  Y="+macrodata[i][2])
                    m_x=int(macrodata[i][1])
                    m_y=int(macrodata[i][2])
                    win32api.SetCursorPos((m_x,m_y))
                if macrodata[i][0]=="delay":
                    container4.message_dis(macrodata[i][1]+"초 딜레이")
                    time.sleep(int(macrodata[i][1]))
                if macrodata[i][0]=="lclick":
                    container4.message_dis("마우스 왼쪽 클릭")
                    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,0,0,0,0)
                    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,0,0,0,0)
                if macrodata[i][0]=="rclick":
                    container4.message_dis("마우스 오른쪽 클릭")
                    win32api.mouse_event(win32con.MOUSEEVENTF_RIGHTDOWN,0,0,0,0)
                    win32api.mouse_event(win32con.MOUSEEVENTF_RIGHTUP,0,0,0,0)
                if macrodata[i][0]=="dclick":
                    container4.message_dis("마우스 더블 클릭")
                    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,0,0,0,0)
                    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,0,0,0,0)
                    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,0,0,0,0)
                    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,0,0,0,0)
        container4.message_dis("---------매크로 종료---------")
    except UnboundLocalError:
        print("")
        
    
            

def cur_po():
    mouse_p=win32api.GetCursorPos()
    xpos=str(mouse_p[0])
    ypos=str(mouse_p[1])
    label1.configure(text='Current Mouse Position     X   :   '+xpos+'    Y   :   '+ypos)
    win.after(50,cur_po)


container1 = cont1(win)
container2 = cont2(win)
container3 = cont3(win)
container4 = cont4(win)
container5 = cont5(win)

    
container4.message_frame()
container5.message_frame()


win.after(0,cur_po())

win.mainloop()
