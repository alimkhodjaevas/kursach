from tkinter import Tk, Button, Label
import requests


SERVER_URL = 'http://127.0.0.1:5000/'
i = 0


def request():
    global i
    r = requests.get(SERVER_URL)
    if r:
        hello_label = Label(window, text=r.content)
        hello_label.grid(column=0, row=i + 1)
        i += 1


def new_request():
    r = requests.get(SERVER_URL + 'new_url/')
    if r:
        data = r.json()
        hello_label = Label(window, text=data.get('counter'))
        hello_label.grid(column=1, row=i + 1)


window = Tk()
window.title("Welcome to LikeGeeks app")
window.geometry('350x200')
lbl = Label(window, text="Hello")
lbl.grid(column=0, row=0)
btn = Button(window, text="Click Me", command=request)
btn.grid(column=1, row=0)
btn = Button(window, text="Click Me", command=new_request)
btn.grid(column=2, row=0)
window.mainloop()
