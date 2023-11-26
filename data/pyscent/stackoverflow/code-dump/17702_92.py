import tkinter as tk

class App(tk.Tk):
    def __init__(self, *args, **kwargs):
        super().__init__()

        print("args type: {}".format(type(args)))
        for i in args:
            print(i)
             
        print("kwargs type: {}".format(type(kwargs)))
        for k, v in kwargs.items():
            print(k,v)

        self.title("Hello World")
        self.geometry("400x300")

if __name__ == '__main__':

    args = ('Y','Y','Z')
    kwargs={'passw': '12345', 'user': 'guest', 'server': '127.0.0.1','database': 'genbank'}
    app = App(*args, **kwargs)
    app.mainloop()
