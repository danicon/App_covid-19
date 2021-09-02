from tkinter import *
from tkinter import ttk

# bibliotecas
from PIL import Image
import requests
import string
import json
import datetime

###############  Cores Usadas ###############
co0 = "#000000"  # black
co1 = "#cc1d4e"  # red
co2 = "#feffff"  # white
co3 = "#0074eb"  # blue
co4 = "#435e5a"  # #435e5a
co5 = "#59b356"  # green
co6 = "#d9d9d9"  # grey

# criar janela
janela = Tk()

janela.resizable(width=FALSE, height=FALSE)
janela.geometry('835x360')
janela.title('')
janela.configure(bg=co6)

#  criando frames
app_nome_frame = Frame(janela, width=840, height=50, bg=co2, relief="flat")
app_nome_frame.grid(row=0, column=0, columnspan=3, sticky=NSEW)

mostrar_frame_infectados = Frame(janela, width=220, height=100, bg=co2, relief="flat")
mostrar_frame_infectados.grid(row=1, column=0, sticky=NW, pady=5, padx=5)

mostrar_frame_recuperados = Frame(janela, width=220, height=100, bg=co2, relief="flat")
mostrar_frame_recuperados.grid(row=1, column=1, sticky=NW, pady=5, padx=5)

mostrar_frame_mortes = Frame(janela, width=220, height=100, bg=co2, relief="flat")
mostrar_frame_mortes.grid(row=1, column=2, sticky=NW, pady=5, padx=5)

selecione_frame = Frame(janela, width=840, height=50, bg=co6, relief="flat")
selecione_frame.grid(row=2, column=0, columnspan=3, sticky="n", pady=10)


# criando labels para app_nome_frame
img = Image.open('covid-19.jpg')
img = img.resize((50, 50))
img = img.save("covid.png")
imagem = PhotoImage(file = "covid.png")

app_imagem = Label(app_nome_frame, image=imagem, width=350,
             pady=20, anchor=NE, relief="flat", bg=co2)
app_imagem.grid(row=0, column=0, pady=5)

app_nome = Label(app_nome_frame, text="COVID-19", width=20, height=1,
             pady=20, relief="flat", anchor=NW, font=("Helvetica 25 bold"), bg=co2, fg=co0)
app_nome.grid(row=0, column=1, pady=5)


# chamando a API 
response = requests.get("https://covid19.mathdro.id/api")
info = response
info = json.loads(info.text)

infectados = info["confirmed"]["value"]
recuperados = info["recovered"]["value"]
mortes = info["deaths"]["value"]
dia = info["lastUpdate"]
dia = datetime.datetime.strptime(dia, "%Y-%m-%dT%H:%M:%S.000Z")
dia = dia.strftime("%c")


# criando labels para mostrar_frame_infectados
label_infetados = Label(mostrar_frame_infectados, text="infectados", width=20, height=1,
             pady=7, padx=0, relief="flat", anchor=NW, font=("Courier 15 bold"), bg=co2, fg=co0)
label_infetados.grid(row=0, column=0, pady=1, padx=13)

mostrar_infetados = Label(mostrar_frame_infectados, text=infectados, width=12, height=1,
             pady=7, padx=0, relief="flat", anchor=NW, font=("Courier 25 bold"), bg=co2, fg=co0)
mostrar_infetados.grid(row=1, column=0, pady=1)

mostrar_info = Label(mostrar_frame_infectados, text=str(dia), width=25, height=1,
             pady=7, padx=0, relief="flat", anchor=NW, font=("Courier 11 bold"), bg=co2, fg=co0)
mostrar_info.grid(row=2, column=0, pady=1)

mostrar_info = Label(mostrar_frame_infectados, text="Total casos ativos de covid-19", width=33, height=1,
             pady=7, padx=0, relief="flat", anchor=NW, font=("Courier 8 bold"), bg=co2, fg=co0)
mostrar_info.grid(row=3, column=0, pady=1, padx=13)

mostrar_azul = Label(mostrar_frame_infectados, text="", width=19, height=1,
             pady=1, padx=0, relief="flat", anchor=NW, font=("Courier 1 bold"), bg=co3, fg=co0)
mostrar_azul.grid(row=4, column=0, pady=0, padx=0, sticky=NSEW)


# criando labels para mostrar_frame_recuperados
label_recuperados = Label(mostrar_frame_recuperados, text="recuperados", width=20, height=1,
             pady=7, padx=0, relief="flat", anchor=NW, font=("Courier 15 bold"), bg=co2, fg=co0)
label_recuperados.grid(row=0, column=0, pady=1, padx=13)

mostrar_recuperados = Label(mostrar_frame_recuperados, text=recuperados, width=12, height=1,
             pady=7, padx=0, relief="flat", anchor=NW, font=("Courier 25 bold"), bg=co2, fg=co0)
mostrar_recuperados.grid(row=1, column=0, pady=1)

mostrar_info = Label(mostrar_frame_recuperados, text=str(dia), width=25, height=1,
             pady=7, padx=0, relief="flat", anchor=NW, font=("Courier 11 bold"), bg=co2, fg=co0)
mostrar_info.grid(row=2, column=0, pady=1)

mostrar_info = Label(mostrar_frame_recuperados, text="Total casos recuperados de covid-19", width=33, height=1,
             pady=7, padx=0, relief="flat", anchor=NW, font=("Courier 8 bold"), bg=co2, fg=co0)
mostrar_info.grid(row=3, column=0, pady=1, padx=13)

mostrar_verde = Label(mostrar_frame_recuperados, text="", width=19, height=1,
             pady=1, padx=0, relief="flat", anchor=NW, font=("Courier 1 bold"), bg=co5, fg=co0)
mostrar_verde.grid(row=4, column=0, pady=0, padx=0, sticky=NSEW)


# criando labels para mostrar_frame_mortes
label_mortes = Label(mostrar_frame_mortes, text="mortes", width=20, height=1,
             pady=7, padx=0, relief="flat", anchor=NW, font=("Courier 15 bold"), bg=co2, fg=co0)
label_mortes.grid(row=0, column=0, pady=1, padx=13)

mostrar_mortes = Label(mostrar_frame_mortes, text=mortes, width=12, height=1,
             pady=7, padx=0, relief="flat", anchor=NW, font=("Courier 25 bold"), bg=co2, fg=co0)
mostrar_mortes.grid(row=1, column=0, pady=1)

mostrar_info = Label(mostrar_frame_mortes, text=str(dia), width=25, height=1,
             pady=7, padx=0, relief="flat", anchor=NW, font=("Courier 11 bold"), bg=co2, fg=co0)
mostrar_info.grid(row=2, column=0, pady=1)

mostrar_info = Label(mostrar_frame_mortes, text="Total casos mortes de covid-19", width=33, height=1,
             pady=7, padx=0, relief="flat", anchor=NW, font=("Courier 8 bold"), bg=co2, fg=co0)
mostrar_info.grid(row=3, column=0, pady=1, padx=13)

mostrar_vermelho = Label(mostrar_frame_mortes, text="", width=19, height=1,
             pady=1, padx=0, relief="flat", anchor=NW, font=("Courier 1 bold"), bg=co1, fg=co0)
mostrar_vermelho.grid(row=4, column=0, pady=0, padx=0, sticky=NSEW)


# criando  caixa de seleção
label_pais = Label(selecione_frame, text="Selecione o pais", width=13, height=1,
             pady=7, padx=0, relief="flat", anchor=NW, font=("Ivy 12 bold"), bg=co6, fg=co0)
label_pais.grid(row=0, column=0, pady=1, padx=13)

pais = ["Global", "Angola", "Brazil", "India", "Portugal", "USA", "France", "Spain"]

combo = ttk.Combobox(selecione_frame, width=15, font=("Ivy 8 bold"))
combo["values"] = (pais)
combo.grid(row=0, column=1, padx=0, pady=13)

# chamando api
def selecionado(eventObject):
    if combo.get() == "Global":
        response = requests.get("https://covid19.mathdro.id/api")
        info = response
        info = json.loads(info.text)

        infectados = info["confirmed"]["value"]
        recuperados = info["recovered"]["value"]
        mortes = info["deaths"]["value"]

        mostrar_infetados.configure(text=infectados)
        mostrar_recuperados.configure(text=recuperados)
        mostrar_mortes.configure(text=mortes)
    else:

        sel_pais = combo.get()
        response = requests.get("https://covid19.mathdro.id/api/countries/{}".format(sel_pais))
        info = response
        info = json.loads(info.text)

        infectados = info["confirmed"]["value"]
        recuperados = info["recovered"]["value"]
        mortes = info["deaths"]["value"]
        dia = info["lastUpdate"]
        dia = datetime.datetime.strptime(dia, "%Y-%m-%dT%H:%M:%S.000Z")
        dia = dia.strftime("%c")

        mostrar_infetados.configure(text=infectados)
        mostrar_recuperados.configure(text=recuperados)
        mostrar_mortes.configure(text=mortes)

combo.bind("<<ComboboxSelected>>", selecionado)







janela.mainloop()