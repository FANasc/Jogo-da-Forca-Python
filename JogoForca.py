'''
############################################################### 
Autor : Fernando Aguiar do Nascimento
Data  : 09/07/2017
Nome  : JogoForca.py
Função: Simular um jogo da forca
###############################################################
'''

# Importação de bibliotecas
from tkinter import *
import tkinter.messagebox as mbox
import random

# Definição de variáveis
strpalavrasecreta = " "

# Definição de tela e frames
tela = Tk(); tela.title("Jogo da Forca"); tela.geometry("250x300");

frame = Frame(tela); frame.pack()
frame1 = Frame(tela); frame1.pack()
frame2 = Frame(tela); frame2.pack()
frame3 = Frame(tela); frame3.pack()
frame4 = Frame(tela); frame4.pack()
frame5 = Frame(tela); frame5.pack()


# função guada_palavra, que valida a palavra secreta e a expõe para que seja adivinhada
# chamada pela função trata_sortear() e no Botão btnenviar1
def guarda_palavra():
    global strpalavrasecreta

    if txtpalavra.get() != "":  # Este textbox se preenchido significa que a palavra secreta foi digitada
        strpalavrasecreta = txtpalavra.get()  # se não preenchido a palavra secreta foi sorteada da lista
        #                 lstpalavras da função trata_sortear()

    # Consistência do conteúdo da palavra secreta   
    if len(strpalavrasecreta) > 10:
        mbox.showinfo("Mensagem de alerta", "Palavra deve conter até 10 letras!")
        txtpalavra.delete(0, END)
        txtpalavra.focus()
    elif len(strpalavrasecreta) == 0:
        mbox.showinfo("Mensagem de alerta", "Palavra não informada!")
        txtpalavra.focus()
    elif not strpalavrasecreta.isalpha():
        mbox.showinfo("Mensagem de alerta", "Palavra não pode conter números!")
        txtpalavra.delete(0, END)
        txtpalavra.focus()
    else:
        btnenviar1['state'] = DISABLED
        txtumaletra['state'] = NORMAL
        btnenviar4['state'] = NORMAL
        txtumaletra.focus()  # Obs.: Será criada uma nova função no btnenviar1 que consitirá o textbox txtpalavra
        #       que é a cadeia de if's acima

        # Conforme palavra secreta digitada ou sorteada, será exibida abaixo da figura da forca a quantidade de
        # underlines correspondentes à quantidade de caracteres da palavra secreta

        if len(strpalavrasecreta) >= 1:
            lblletra01['state'] = DISABLED  # Obs.: instrução desnecesária neste ponto
            lblletra01["foreground"] = "black"
            lblletra01['text'] = " "
            lblletra01['state'] = NORMAL  # Obs.: instrução desnecesária neste ponto, idem para os if's abaixo
        if len(strpalavrasecreta) >= 2:
            lblletra02['state'] = NORMAL
            lblletra02["foreground"] = "black"
            lblletra02['text'] = " "
        if len(strpalavrasecreta) >= 3:
            lblletra03["state"] = NORMAL
            lblletra03["foreground"] = "black"
            lblletra03["text"] = " "
        if len(strpalavrasecreta) >= 4:
            lblletra04["state"] = NORMAL
            lblletra04["foreground"] = "black"
            lblletra04["text"] = " "
        if len(strpalavrasecreta) >= 5:
            lblletra05["state"] = NORMAL
            lblletra05["foreground"] = "black"
            lblletra05["text"] = " "
        if len(strpalavrasecreta) >= 6:
            lblletra06["state"] = NORMAL
            lblletra06["foreground"] = "black"
            lblletra06["text"] = " "
        if len(strpalavrasecreta) >= 7:
            lblletra07["state"] = NORMAL
            lblletra07["foreground"] = "black"
            lblletra07["text"] = " "
        if len(strpalavrasecreta) >= 8:
            lblletra08["state"] = NORMAL
            lblletra08["foreground"] = "black"
            lblletra08["text"] = " "
        if len(strpalavrasecreta) >= 9:
            lblletra09["state"] = NORMAL
            lblletra09["foreground"] = "black"
            lblletra09["text"] = " "
        if len(strpalavrasecreta) >= 10:
            lblletra10["state"] = NORMAL
            lblletra10["foreground"] = "black"
            lblletra10["text"] = " "


# função novo_jogo(), chamada no click do botão btnnovojogo, reinicializa variáveis e propriedades;
#                                                            habilita e desabilita botões
def novo_jogo():
    global strpalavrasecreta
    strpalavrasecreta = ""
    lblletra01["text"] = "";
    lblletra02["text"] = "";
    lblletra03["text"] = "";
    lblletra04["text"] = "";
    lblletra05["text"] = "";
    lblletra06["text"] = "";
    lblletra07["text"] = "";
    lblletra08["text"] = "";
    lblletra09["text"] = "";
    lblletra10["text"] = ""
    lblletra01["background"] = "gray94";
    lblletra02["background"] = "gray94";
    lblletra03["background"] = "gray94";
    lblletra04["background"] = "gray94";
    lblletra05["background"] = "gray94";
    lblletra06["background"] = "gray94";
    lblletra07["background"] = "gray94";
    lblletra08["background"] = "gray94";
    lblletra09["background"] = "gray94";
    lblletra10["background"] = "gray94"
    lblletra01["foreground"] = "gray94";
    lblletra02["foreground"] = "gray94";
    lblletra03["foreground"] = "gray94";
    lblletra04["foreground"] = "gray94";
    lblletra05["foreground"] = "gray94";
    lblletra06["foreground"] = "gray94";
    lblletra07["foreground"] = "gray94";
    lblletra08["foreground"] = "gray94";
    lblletra09["foreground"] = "gray94";
    lblletra10["foreground"] = "gray94"
    btnenviar1["state"] = DISABLED
    txtpalavra['show'] = ""
    txtpalavra.delete(0, END)
    txtpalavra['show'] = "*"
    txtpalavra['state'] = DISABLED
    btndigitar['state'] = NORMAL
    btnsortear['state'] = NORMAL
    txtumaletra.delete(0, END)
    txtumaletra['state'] = DISABLED
    btnenviar4['state'] = DISABLED
    lblacertos1['text'] = " "
    lblerros1['text'] = " "
    lblforca['image'] = imgforca06
    btndigitar.focus()


# função trata_digitar(), chamada no click do botão btndigitar, habilita e desabilita botões e
#        posiciona o cursor no textbox txtpalavra
def trata_digitar():
    btnenviar1['state'] = NORMAL
    txtpalavra['state'] = NORMAL
    btndigitar['state'] = DISABLED
    btnsortear['state'] = DISABLED
    txtpalavra.focus()


# função trata_sortear(), chamada no click do botão btnsortear, sorteia uma palavra de uma lista;
#        habilita e desabilita botões; chama a função guarda_palavra()
def trata_sortear():
    global strpalavrasecreta
    lstpalavras = ['ABA', 'ALA', 'AMA', 'ATA', 'ECO', 'ELO', 'SOB', 'VIL', 'FEL', 'MAL', 'SER', 'VIR', 'VER', 'PAZ',
                   'TER', 'DAR', 'BEM', 'DIA', 'ROL', 'BOM', 'EGO', 'TEZ', 'VIS', 'MAU', 'LUA', 'VOO', 'tal', 'fiz',
                   'luz', 'rua', 'era', 'mas', 'rio', 'ler', 'ato', 'lei', 'elo', 'mim', 'eis', 'dor', 'com', 'nau',
                   'ajo', 'ode', 'eco', 'boi', 'dou', 'uma', 'que', 'ora', 'foi', 'num', 'rei', 'fim', 'voz', 'sol',
                   'jaz', 'pau', 'vez', 'sem', 'seu', 'via', 'jus', 'pai', 'sim', 'agi', 'ira', 'fez', 'meu', 'rir',
                   'ali', 'som', 'boa', 'por', 'tem', 'toa', 'asa', 'nem', 'giz', 'ovo', 'uso', 'pus', 'tom', 'fio',
                   'mor', 'lhe', 'amo', 'cor', 'cal', 'hum', 'sub', 'cru', 'pia', 'lar', 'aia', 'noz', 'par', 'ido',
                   'cem', 'tio', 'sua', 'mar', 'mel', 'foz', 'ano', 'uva', 'top', 'ida', 'aio', 'dom', 'uni', 'oco',
                   'ave', 'cio', 'tua', 'nos', 'rim', 'imo', 'vau', 'tia', 'ele', 'sal', 'uns', 'mui', 'oba', 'evo',
                   'ela', 'jia', 'gol', 'aro', 'ais', 'exu', 'pio', 'pal', 'gaz', 'dez', 'dum', 'duo', 'ala', 'lia',
                   'ama', 'pua', 'opa', 'teu', 'mil', 'das', 'fato', 'amor', 'brio', 'esmo', 'apto', 'ermo', 'veio',
                   'suma', 'pois', 'ruim', 'mote', 'crer', 'mito', 'soar', 'sede', 'numa', 'pose', 'gozo', 'ente',
                   'tolo', 'cedo', 'asco', 'meio', 'cela', 'rege', 'alvo', 'alva', 'vida', 'fase', 'prol', 'sina',
                   'coxo', 'medo', 'sela', 'face', 'agir', 'rude', 'base', 'joia', 'zelo', 'nojo', 'onde', 'como',
                   'urge', 'caos', 'cota', 'jugo', 'cujo', 'auto', 'casa', 'teve', 'deus', 'traz', 'auge', 'ater',
                   'mero', 'teor', 'algo', 'seio', 'pneu', 'mais', 'alta', 'idem', 'tudo', 'todo', 'novo', 'vale',
                   'voga', 'frio', 'asno', 'rito', 'pude', 'haja', 'dote', 'alto', 'nexo', 'ante', 'nato', 'amar',
                   'algoz', 'sagaz', 'mexer', 'senso', 'afeto', 'sutil', 'inato', 'cerne', 'audaz', 'termo', 'nobre',
                   'fazer', 'vigor', 'lapso', 'negro', 'ideia', 'genro', 'desde', 'posse', 'atroz', 'torpe', 'expor',
                   'honra', 'ardil', 'gleba', 'poder', 'sanar', 'muito', 'dizer', 'gesto', 'digno', 'corja', 'justo',
                   'tenaz', 'ceder', 'anexo', 'fugaz', 'vivaz', 'pesar', 'assim', 'moral', 'dever', 'comum', 'afago',
                   'fluir', 'causa', 'ontem', 'censo', 'citar', 'impor', 'seara', 'enfim', 'prole', 'cisma', 'pudor',
                   'brado', 'regra', 'gerar', 'obter', 'louco', 'crise', 'saber', 'tenro', 'pleno', 'viril', 'parvo',
                   'bruma', 'favor', 'visar', 'temor', 'sinto', 'denso', 'tange', 'desse', 'reter', 'jeito', 'haver',
                   'sobre', 'apraz', 'senil', 'sonho', 'seria', 'labor', 'usura', 'criar', 'culto', 'temer', 'rogar',
                   'manso', 'ameno', 'adiar', 'presa', 'revel', 'forma', 'clava', 'birra', 'pedir', 'prosa', 'mundo',
                   'dogma', 'estar', 'fator', 'tempo', 'servo', 'falar', 'farsa', 'acaso', 'pulha', 'forte', 'falta',
                   'cunho', 'ainda', 'exato', 'grato', 'etnia', 'fluxo', 'amplo', 'achar', 'feixe', 'guisa', 'assaz',
                   'parco', 'doido', 'prumo', 'laico', 'atuar', 'feliz', 'tomar', 'reles', 'ritmo', 'lavra', 'praxe',
                   'haste', 'peste', 'vital', 'cruel', 'deter', 'levar', 'amigo', 'casal', 'matiz', 'anuir', 'crivo',
                   'finjo', 'algum', 'devir', 'chulo', 'beata', 'ordem', 'certo', 'rigor', 'sesta', 'casta', 'leito',
                   'bravo', 'capaz', 'vulto', 'salvo', 'sulco', 'acima', 'relva', 'mesmo', 'dorso', 'possa', 'valha',
                   'valor', 'fugir', 'vasto', 'coisa', 'valia', 'tecer', 'garbo', 'banal', 'puxar', 'sendo', 'reger',
                   'furor', 'pobre', 'igual', 'maior', 'breve', 'ativo', 'ouvir', 'falso', 'selar', 'velar', 'anelo',
                   'pouco', 'casto', 'horda', 'fitar', 'viver', 'olhar', 'toada', 'pompa', 'morar', 'gerir', 'sumir',
                   'voraz', 'cabal', 'leigo', 'morte', 'tédio', 'noite', 'remir', 'homem', 'coeso']
    txtpalavra.delete(0, END)  # Limpa textbox
    strpalavra = lstpalavras[random.randrange(len(lstpalavras))]  # sorteia palavra
    strpalavra = strpalavra.upper()  # Transforma caracteres minúsculos em maiúsculos
    strpalavrasecreta = strpalavra

    guarda_palavra()

    txtumaletra['state'] = NORMAL
    btnenviar4['state'] = NORMAL
    btndigitar['state'] = DISABLED
    btnsortear['state'] = DISABLED
    txtpalavra['state'] = DISABLED
    txtumaletra.focus()  # Posiciona cursor no textbox da letra a ser adivinhada


# função procurar_letra(), chamada no click do botão btnenviar4, verifica em qual posição a letra digitada está na
#                          palavra secreta; cada letra encontrada a visualização é liberada abaixo da figura da forca
#                          letra encontrada é exibida no Label lblacertos1, as não encontradas no lblerros1
def procurar_letra():
    global strpalavrasecreta  # decração de variável como global
    strpalavrasecreta = strpalavrasecreta.upper()  # Transformar caracter minúsculo em maiúsculo
    strletrascertas = " "
    strletraserradas = " "
    bolletracerta = False
    strletra = txtumaletra.get().upper()  # Transformar caracter minúsculo em maiúsculo
    strletrascertas = lblacertos1["text"]
    strletraserradas = lblerros1["text"]

    if txtumaletra.get() == "":  # consistência de digitação da letra
        mbox.showinfo("Mensagem de alerta", "Letra não informada!")
        txtumaletra.focus()
    elif strletra in strletrascertas or strletra in strletraserradas:
        mbox.showinfo("Mensagem de alerta", "Letra já informada!")
        txtumaletra.delete(0, END)
        txtumaletra.focus()
    else:
        i = 0
        while i < len(strpalavrasecreta):
            if strpalavrasecreta[i] == strletra:
                bolletracerta = True
                strletrascertas = strletrascertas + strletra
                if i == 0:
                    lblletra01["text"] = strletra
                    lblletra01[
                        "background"] = "gray94"  # Cor padrão de fundo, para letra correta. Obs.: comando desnecessário
                elif i == 1:
                    lblletra02["text"] = strletra
                    lblletra02["background"] = "gray94"
                elif i == 2:
                    lblletra03["text"] = strletra
                    lblletra03["background"] = "gray94"
                elif i == 3:
                    lblletra04["text"] = strletra
                    lblletra04["background"] = "gray94"
                elif i == 4:
                    lblletra05["text"] = strletra
                    lblletra05["background"] = "gray94"
                elif i == 5:
                    lblletra06["text"] = strletra
                    lblletra06["background"] = "gray94"
                elif i == 6:
                    lblletra07["text"] = strletra
                    lblletra07["background"] = "gray94"
                elif i == 7:
                    lblletra08["text"] = strletra
                    lblletra08["background"] = "gray94"
                elif i == 8:
                    lblletra09["text"] = strletra
                    lblletra09["background"] = "gray94"
                elif i == 9:
                    lblletra10["text"] = strletra
                    lblletra10["background"] = "gray94"
            i = i + 1

        # Trata letra corretas e incorretas
        if bolletracerta:
            strletrascertas = lblacertos1["text"] + strletra
            lblacertos1["text"] = strletrascertas.replace(' ', '')
            if len(strletrascertas) == len(strpalavrasecreta):
                mbox.showinfo("Mensagem de alerta", "Parabéns, acertou!")
                novo_jogo()
        else:
            strletraserradas = lblerros1["text"] + strletra
            lblerros1["text"] = strletraserradas.replace(' ', '')
            if len(lblerros1['text']) == 1:  # Altera imagem da forca conforme letra incorreta
                lblforca['image'] = imgforca1
            elif len(strletraserradas) == 2:
                lblforca['image'] = imgforca2
            elif len(strletraserradas) == 3:
                lblforca['image'] = imgforca3
            elif len(strletraserradas) == 4:
                lblforca['image'] = imgforca4
            elif len(strletraserradas) == 5:
                lblforca['image'] = imgforca5
            elif len(strletraserradas) == 6:
                lblforca['image'] = imgforca6
                mbox.showinfo("Mensagem de alerta", "Fim de jogo! A palavra secreta era: " + strpalavrasecreta)
                novo_jogo()

        txtumaletra.delete(0, END)
        txtumaletra.focus()


# definição de imagens
imgforca0 = PhotoImage(file="C:\\Users\\User\\Documents\\Fernando\\Projeto Python\\Jogo da Forca\\forca0.png")
imgforca1 = PhotoImage(file="C:\\Users\\User\\Documents\\Fernando\\Projeto Python\\Jogo da Forca\\forca1.png")
imgforca2 = PhotoImage(file="C:\\Users\\User\\Documents\\Fernando\\Projeto Python\\Jogo da Forca\\forca2.png")
imgforca3 = PhotoImage(file="C:\\Users\\User\\Documents\\Fernando\\Projeto Python\\Jogo da Forca\\forca3.png")
imgforca4 = PhotoImage(file="C:\\Users\\User\\Documents\\Fernando\\Projeto Python\\Jogo da Forca\\forca4.png")
imgforca5 = PhotoImage(file="C:\\Users\\User\\Documents\\Fernando\\Projeto Python\\Jogo da Forca\\forca5.png")
imgforca6 = PhotoImage(file="C:\\Users\\User\\Documents\\Fernando\\Projeto Python\\Jogo da Forca\\forca6.png")

# definição de interfaces gráficas (biblioteca tkinter)
lblforca = Label(frame, image=imgforca0);
lblforca.pack()

lblletra01 = Label(frame, font="Arial 20 bold", state=DISABLED, underline=0);
lblletra01.pack(side=LEFT)
lblletra02 = Label(frame, font="Arial 20 bold", state=DISABLED, underline=0);
lblletra02.pack(side=LEFT)
lblletra03 = Label(frame, font="Arial 20 bold", state=DISABLED, underline=0);
lblletra03.pack(side=LEFT)
lblletra04 = Label(frame, font="Arial 20 bold", state=DISABLED, underline=0);
lblletra04.pack(side=LEFT)
lblletra05 = Label(frame, font="Arial 20 bold", state=DISABLED, underline=0);
lblletra05.pack(side=LEFT)
lblletra06 = Label(frame, font="Arial 20 bold", state=DISABLED, underline=0);
lblletra06.pack(side=LEFT)
lblletra07 = Label(frame, font="Arial 20 bold", state=DISABLED, underline=0);
lblletra07.pack(side=LEFT)
lblletra08 = Label(frame, font="Arial 20 bold", state=DISABLED, underline=0);
lblletra08.pack(side=LEFT)
lblletra09 = Label(frame, font="Arial 20 bold", state=DISABLED, underline=0);
lblletra09.pack(side=LEFT)
lblletra10 = Label(frame, font="Arial 20 bold", state=DISABLED, underline=0);
lblletra10.pack(side=LEFT)

lblpalavra = Label(frame1, text="Palavra secreta:");
lblpalavra.pack(side=LEFT)
btnenviar1 = Button(frame1, text="Enviar", command=guarda_palavra, state=DISABLED);
btnenviar1.pack(side=RIGHT)
txtpalavra = Entry(frame1, state=DISABLED);
txtpalavra["show"] = "*";
txtpalavra.pack(side=RIGHT)

btnnovojogo = Button(frame2, text="Novo JOGO", command=novo_jogo);
btnnovojogo.pack(side=LEFT)
btnsair = Button(frame2, text="Encerrar JOGO", command=quit);
btnsair.pack(side=LEFT)

btndigitar = Button(frame3, text="Digitar palavra", command=trata_digitar);
btndigitar.focus();
btndigitar.pack(side=LEFT)
btnsortear = Button(frame3, text="Sortear palavra", command=trata_sortear);
btnsortear.pack(side=LEFT)

lblumaletra = Label(frame4, text="Arriscar uma letra:");
lblumaletra.pack(side=LEFT)
txtumaletra = Entry(frame4, width=2, state=DISABLED);
txtumaletra.pack(side=LEFT)
btnenviar4 = Button(frame4, text="Enviar", state=DISABLED, command=procurar_letra);
btnenviar4.pack(side=LEFT)

lblacertos = Label(frame5, text="Acertos:");
lblacertos.pack(side=LEFT)
lblacertos1 = Label(frame5, text="          ", font="Arial 12 bold");
lblacertos1.pack(side=LEFT)
lblerros = Label(frame5, text="Erros:");
lblerros.pack(side=LEFT)
lblerros1 = Label(frame5, text="          ", font="Arial 12 bold");
lblerros1.pack(side=LEFT)

tela.mainloop()  # obrigatório para que as interfaces sejam exibidas e os eventos processados.
