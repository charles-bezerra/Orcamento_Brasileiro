from tkinter import Frame
from tkinter import Label
from tkinter import Button
from tkinter import Entry
from tkinter import Toplevel
from tkinter import Tk
from tkinter import Canvas
from calculos import Calculos
class Janela(Frame):
    __texto = ("""
    Aqui você irá calcular valores orçanamentaris
        de seu país de acordo com a PEC 241
     """)
    obj = Calculos()
    def __init__(self, parent):
        Frame.__init__(self, parent)
        self.parent = parent
        self.iniciar()
    def iniciar(self):
        self.msg = Label(self, text = "Bem vindo", font = "Arial 25 bold")
        self.msg2 = Label(self, text = self.__texto, font = "Times 15")
        self.bt = Button(self, text = "Avançar", bg = "White",font = "Times 15", command = self.jan1)
        self.sair = Button(self, text = "Sair", bg = "Red",font = "Times 15", command = self.quit)
        self.msg.grid(row = 0, column = 0)
        self.msg2.grid(row = 1, column = 0)
        self.bt.grid(row = 2, column = 0)
        self.sair.grid(row = 3, column = 0)
        self.pack()

    def jan1(self):
        self.destroy()
        self.mteto = Label(self.parent,text = "Digite o Teto de 2016:", font = "Arial 15")
        self.eteto = Entry(self.parent)
        self.tano = Label(self.parent,text = "Ano do novo teto:", font = "Arial 15")
        self.eano = Entry(self.parent)
        self.mpopulacao = Label(self.parent,text = "População de seu país estimado:", font = "Arial 15")
        self.epopulacao = Entry(self.parent)
        self.bt = Button(self.parent, text = "Calcular", font = "Arial 15", bg = "Blue", command = self.dados)
        self.mteto.grid(row = 0, column = 0)
        self.eteto.grid(row = 0, column = 1)
        self.tano.grid(row = 1, column = 0)
        self.eano.grid(row = 1, column = 1)
        self.mpopulacao.grid(row = 2, column = 0)
        self.epopulacao.grid(row = 2, column = 1)
        self.bt.grid(row = 3, column = 0)
        self.pack()
    def verificar(self):
        a = str(self.eteto.get())
        b = str(self.eano.get())
        c = str(self.epopulacao.get())
        if a.isnumeric() and b.isnumeric() and c.isnumeric():
            if int(b) >= 2016 and int(b) <= 2036:
                return 1
            else:
                return 0
        else:
            return 0
    def dados(self):
        if self.verificar() == 1:
            #Preenchendo valores da classe Calculos
            try:
                self.obj.setTeto(int(self.eteto.get()))
                self.obj.setAno(int(self.eano.get()))
                self.obj.setPopulacao(int(self.epopulacao.get()))

                self.result = Label(self.parent, text = "Novo teto:", font = "Arial 15", bg = "White")
                self.novo_teto = Label(self.parent, text = self.obj.getNovo_Teto(), font = "Arial 15 bold", bg = "White")

                self.result.grid(row = 4, column = 0)
                self.novo_teto.grid(row = 4, column = 1)
                self.pack()
            except:
                self.obj.setTeto(int(self.eteto.get()))
                self.obj.setAno(int(self.eano.get()))
                self.obj.setPopulacao(int(self.epopulacao.get()))

                self.result = Label(self.parent, text = "Novo teto:", font = "Arial 15", bg = "White")
                self.novo_teto = Label(self.parent, text = self.obj.getNovo_Teto(), font = "Arial 15 bold", bg = "White")

                self.result.grid(row = 4, column = 0)
                self.novo_teto.grid(row = 4, column = 1)
                self.pack()
        elif self.verificar() == 0:
            self.Lerror = Label(self.parent, text = """Por favor, preencha todos \n os tópicos corremente!""", font = "Arial 15 bold")
            self.Lerror.grid(row = 4, column = 1)
            self.pack()
    def janela2(self):
    	self
if __name__ == "__main__":
    origem = Tk()
    origem.title("Orçamento Brasileiro")
    origem.geometry("800x600")
    x = Janela(origem)
    origem.mainloop()
