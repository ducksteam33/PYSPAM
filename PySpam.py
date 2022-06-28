import requests
import tkinter as tk
import tkinter.font as fnt


    
def SendMessage():
    requests.post(f'https://discord.com/api/v9/channels/'+ IDWINDOW_entry.get() +'/messages', data = {"content": TEXTWINDOW_text.get("1.0","end-1c") + "\n"}, headers={'authorization': TOKENWINDOW_entry.get()})

def SendMessagereREP():
    TIMES = int(TIMESWINDOW_entry.get())
    while TIMES > 0:
        SendMessage()
        TIMES -= 1


root = tk.Tk()
root.title("PYSPAM")
root.geometry("640x480")
root.resizable(False, False)
root.configure(background='black')

#Labels

TITLE1_font= fnt.Font(family = "Consolas", size = 20, weight = "bold") 

TITLE1_label = tk.Label(text="PY", font="Consolas", fg = "#4fdc00")
TITLE1_label.configure(font = TITLE1_font, background="black")
TITLE1_label.place(x=270,y=10)


TITLE2_font = fnt.Font(family = "Consolas", size = 20, weight = "bold")

TITLE2_label = tk.Label(text="SPAM", font="Consolas", fg = "#4fdc00")
TITLE2_label.configure(font = TITLE2_font, background="black")
TITLE2_label.place(x=305,y=10)


ALLABEL_font = fnt.Font(family = "Consolas", size = 10)

IDLABEL_label = tk.Label(text="Chat ID :",fg = "white")
IDLABEL_label.configure(font = ALLABEL_font, background="black")
IDLABEL_label.place(x=180,y=65)

TOKENLABEL_label = tk.Label(text="Acount Token :",fg = "white")
TOKENLABEL_label.configure(font = ALLABEL_font, background="black")
TOKENLABEL_label.place(x=140,y=90)

REPEATLABEL_label = tk.Label(text="Repeat Message :",fg = "white")
REPEATLABEL_label.configure(font = ALLABEL_font, background="black")
REPEATLABEL_label.place(x=128,y=110)


TEXTWINLABEL_label = tk.Label(text="||| SPAM |||",fg = "white")
TEXTWINLABEL_label.configure(font = ALLABEL_font, background="black")
TEXTWINLABEL_label.place(x=125,y=140)

#Buttons
STARTSPAM_button = tk.Button(text="START SPAM", command=SendMessagereREP)
STARTSPAM_button.place(x=220, y=400)

STOPSPAM_button = tk.Button(text= "QUIT",command=root.destroy)
STOPSPAM_button.place(x=340, y=400)

#Text
TEXTWINDOW_text = tk.Text(root)
TEXTWINDOW_text.place(x=130,y=160, width=400, height=200)

#Entry
IDWINDOW_entry = tk.Entry(root)
IDWINDOW_entry.place(x=250,y=65, width=200,height=20)

TOKENWINDOW_entry = tk.Entry(root, show="*")
TOKENWINDOW_entry.place(x=250,y=90,width=200,height=20)

TIMESWINDOW_entry = tk.Entry(root)
TIMESWINDOW_entry.insert(0, "1")
TIMESWINDOW_entry.place(x=250,y=115,width=20,height=20)

root.mainloop()



#by ducksteam









    
    
    


