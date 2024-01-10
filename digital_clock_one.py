import tkinter as tk

import datetime

class Principal:

    def __init__(self, master):
        self.nossaTela = master
        self.lblRelogio = tk.Label(
            self.nossaTela, font=('calibri', 30, 'bold'), fg='black', anchor='center')
        
        self.nossaTela.title('Clock')

        self.lblRelogio.pack(pady=25, padx=25)
        self.alteracao()

    def alteracao(self):
        now = datetime.datetime.now()
        self.lblRelogio['text'] = now.strftime('%H:%M:%S:%p')
        self.nossaTela.after(1000, self.alteracao)

janelaMain = tk.Tk()
Principal(janelaMain)
janelaMain.mainloop()