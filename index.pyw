import random
import tkinter

wts=open("settings.txt","r")
global fs
fs=int(wts.read())
print(fs)
wts.close()

def boxer():
    global cclass
    cclass="Boxer"
    gameplay()
def kickboxer():
    global cclass
    cclass="Muay Thai"
    gameplay()
def wrestler():
    global cclass
    cclass="Street Fight"
    gameplay()

def menug():
    global menu
    menu=tkinter.Tk()
    menu.title("Fight Night")
    menu.geometry("500x500")
    menu.configure(background="Green", cursor="dot")
    
    print("Game initialised.\n")

    def togglefullscreen():
        global fs
        if fs==1:
            fs-=1
            fsy.configure(text="Маленький")
            menu.attributes("-fullscreen",False)
            print("Fullscreen disabled")
            wts=open("settings.txt","w")
            wts.write("0")
            wts.close()
            
        elif fs==0:
            fs+=1
            fsy.configure(text="Большой")
            menu.attributes("-fullscreen",True)
            print("Fullscreen enabled")
            wts=open("settings.txt","w")
            wts.write("1")
            wts.close()


    title=tkinter.Label(menu, text="Текстовый игровой бой", font=("Courier", 28, "bold"), pady=20,bg="Green", fg="white")
    boxert=tkinter.Button(menu, text="Боксёр", command=boxer, pady=20, width=100)
    kickboxert=tkinter.Button(menu, text="Гопник",command=kickboxer, pady=20, width=100)
    wrestlert=tkinter.Button(menu, text="Уличный Боец",command=wrestler, pady=20, width=100)
    mexit=tkinter.Button(menu, text="Выход", command=exit)
    settings=tkinter.Label(menu, text="Настройки", font=("Courier", 20, "bold"),bg="Green", fg="white")
    flscrn=tkinter.Label(menu, text="Полный экран",font=("Courier", 14), bg="Green", fg="white")
    fsy=tkinter.Button(menu, text="", command=togglefullscreen)
    if fs==0:
        menu.attributes("-fullscreen",False)
        fsy.configure(text="Маленький")
    elif fs==1:
        menu.attributes("-fullscreen",True)
        fsy.configure(text="Большой")

    mexit.pack(fill=tkinter.X, side=tkinter.BOTTOM)
    title.pack()
    boxert.pack()
    kickboxert.pack()
    wrestlert.pack()
    settings.pack()
    flscrn.pack()
    fsy.pack()
    menu.mainloop()

def gameplay():
    global menu
    menu.destroy()
    window=tkinter.Tk()
    window.title("Fight Night - Match")
    window.geometry("640x480")
    window.configure(background="Green", cursor="dot")
    if fs==0:
        window.attributes("-fullscreen",False)
    elif fs==1:
        window.attributes("-fullscreen",True)


    global basehp
    global health
    global cclass
    global tdmgp
    global tdmg
    tdmg=0
    tdmgp=0
    if cclass=="Boxer":
        pmodifier=1.5
        kmodifier=0.5
        gmodifier=0.25
        health=125
        basehp=125
    elif cclass=="Muay Thai":
        pmodifier=0.75
        kmodifier=1.5
        gmodifier=0.25
        health=125
        basehp=125
    elif cclass=="Street Fight":
        pmodifier=0.5
        kmodifier=0.5
        gmodifier=2
        health=175
        basehp=175

    global ehealth
    ehealth=int(round(health*1.25))
    global emodifier
    emodifier=1.3
    global ebasehp
    ebasehp=ehealth

    global pwin
    pwin=0

    def pwin():
        global ehealth
        if ehealth<=0:
            ehealthl.configure(text="Здоровье: 0"+"/"+str(ebasehp))
            print("Ты победил")
            global pwin
            pwin=1
            winner.configure(text="Ты победил")

    def ewin():
        global health
        if health<=0:
            healthl.configure(text="Здоровье: 0"+"/"+str(basehp))
            print("Враг победил")
            global pwin
            pwin=1
            winner.configure(text="Враг победил")

    def echance():
        global pwin
        global tdmg
        
        if pwin!=1:
            global health
            missche=random.randint(0,13)
            echance=random.randint(0,13)
            if echance>=5:
                if missche>=11:
                    print("Враг промахнулся атакой!")
                    enemymove.configure(text="Враг промахнулся атакой!")
                else:
                    global ehealth
                    dmgdealt=int(round(random.randint(10,20)*emodifier))
                    health-=dmgdealt
                    print("Твоё здоровье сейчас: "+str(health))
                    healthl.configure(text="Здоровье: "+str(int(round(health)))+"/"+str(basehp))
                    enemymove.configure(text="Враг использует: Удар(Урона нанёс: "+(str(dmgdealt))+")")
                    
            elif echance>=10:
                if missche>=10:
                    print("Враг промахнулся атакой!")
                    enemymove.configure(text="Враг промахнулся атакой")
                else:
                    global ehealth
                    dmgdealt=int(round(random.randint(14,26)*emodifier))
                    health-=dmgdealt
                    print("Твоё здоровье сейчас: "+str(health))
                    healthl.configure(text="Здоровье: "+str(health)+"/"+str(basehp))
                    enemymove.configure(text="Враг использует: Кик(Урона нанёс: "+(str(dmgdealt))+")")
            
            elif echance<=4:
                global tdmg
                chance=1
                while chance<7:
                    dmgdealt=random.randint(2,7)*emodifier
                    tdmg+=int(round(dmgdealt))
                    health-=dmgdealt
                    chance=int(round(random.randint(0,11)))
                    print("Твоё здоровье сейчас: "+str(health))
                    healthl.configure(text="Здоровье: "+str(int(round(health)))+"/"+str(basehp))
                enemymove.configure(text="Враг использует: Пинок(Урона нанёс: "+(str(tdmg))+")")           
            tdmg=0
    def punchp():
        global pwin
        if pwin!=1:
            global ehealth
            missch=random.randint(0,13)
            if missch>=11:
                print("Ты промахнулся атакой!")
            else:
                global dmgdealtp
                dmgdealtp=int(round(random.randint(9,21)*pmodifier))
                ehealth-=dmgdealtp
                print("Здоровье врага сейчас: "+str(ehealth))
                ehealthl.configure(text="Здоровье: "+str(int(round(ehealth)))+"/"+str(ebasehp))
                playerddealt.configure(text="Внёс урона по врагу: "+str(dmgdealtp))
            pwin()
            echance()
            ewin()


    def kickp():
        global pwin
        if pwin!=1:
            global ehealth
            missch=random.randint(0,13)
            if missch>=10:
                print("Ты промахнулся атакой!")
            else:
                global dmgdealtp
                dmgdealtp==int(round(random.randint(14,26)*kmodifier))
                ehealth-=dmgdealtp
                print("Здоровье врага сейчас: "+str(ehealth))
                ehealthl.configure(text="Здоровье: "+str(int(round(ehealth)))+"/"+str(ebasehp))
                playerddealt.configure(text="Внёс урона по врагу: "+str(dmgdealtp))
            pwin()
            echance()
            ewin()

    def grapplep():
        if pwin!=1:
            global ehealth
            global tdmgp
            chance=1
            while chance<7:
                dmgdealtp=random.randint(2,7)*gmodifier
                tdmgp+=dmgdealtp
                ehealth-=dmgdealtp
                chance=int(round(random.randint(0,11)))
                print("Здоровье врага сейчас: "+str(ehealth))
                ehealthl.configure(text="Здоровье: "+str(int(round(ehealth)))+"/"+str(ebasehp))
            playerddealt.configure(text="Внёс урона по врагу: "+str(tdmgp))
            tdmgp=0                
            pwin()
            echance()
            ewin()
    def restart():
        print("\nNew game loaded\n")
        window.destroy()
        menug()
		
    player=tkinter.Label(window, text="Ты", font=("Courier", 24, "bold"))
    healthl=tkinter.Label(window, text=("Здоровье: "+str(health)+"/"+str(basehp)), font=("Courier", 18))
    enemy=tkinter.Label(window, text="Враг", font=("Courier", 24, "bold"))
    ehealthl=tkinter.Label(window, text=("Здоровье: "+str(ehealth)+"/"+str(ebasehp)), font=("Courier", 18))
    punch=tkinter.Button(window, text="Удар",command=punchp)
    kick=tkinter.Button(window, text="Кик", command =kickp)
    grapple=tkinter.Button(window, text="Пинок", command=grapplep)
    restart=tkinter.Button(window, text="Заново", command=restart)
    texit=tkinter.Button(window, text="Выход", command=exit)
    enemymove=tkinter.Label(window,text="", font=("Courier", 14), bg="Green",fg="white")
    playerddealt=tkinter.Label(window,text="", font=("Courier", 14), bg="Green", fg="white")
    winner=tkinter.Label(window, text="", font=("Courier", 14, "bold"), bg="Green", fg="white")

    texit.pack(fill=tkinter.X, side=tkinter.BOTTOM)
    player.pack(pady=10, padx=20, fill=tkinter.X)
    healthl.pack()
    punch.pack(pady=5)
    kick.pack(pady=5)
    grapple.pack(pady=5)
    playerddealt.pack()
    enemy.pack(pady=10, padx=20, fill=tkinter.X)
    ehealthl.pack()
    enemymove.pack()
    restart.pack(fill=tkinter.X, side=tkinter.BOTTOM)
    winner.pack(side=tkinter.BOTTOM)
    window.mainloop()


menug()

