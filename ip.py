# -*- coding: cp1254 -*-
from tkinter import*
from urllib.request import urlopen
from urllib.request import Request
import re
import sys
anapen = Tk()
anapen.geometry("500x500")
anapen.title("Reverse IP Lookup")

karsila = Label(anapen)
karsila.config(text=u"Test IP Arama Programına Hoş Geldiniz")
karsila.place(x=1,y=1)

cizgi = Label(text="#"*70, fg="green")
cizgi.place(y=20)


#Sistem Başlangıç
victimbir = Label(anapen)
victimbir.config(text=u"Victim:")
victimbir.place(x=1,y=50)
victimiki = Entry()
victimiki.place(x=50,y=50)
basla = Button(anapen)
basla.config(text=u"Analiz")
basla.pack()

bilgi = Label(anapen, font=('Verdana', 16))
bilgi.pack(side=BOTTOM, pady=150)

uagent= {'User-Agent':'Mozilla/5.0 (Windows; U; Windows NT 6.0; en-US; rv:1.9.0.6)'}

def baslat():
    try:
        url = "http://viewdns.info/reverseip/?host=%s&t=1" % victimiki.get()
        req = Request(url, headers=uagent)
        fd = urlopen(req)
        data = str(fd.read())

        comp = re.compile("<tr><td>\S+</td><td")
        comp2 = re.compile('\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}')
        
        baglantilar = comp.findall(data)
        for i in baglantilar:
            i = i.replace("<tr><td>", "").replace("</td><td", "")

            if i.startswith("http://"):
                pass
            else:
                i = "http://"+i   

            if "Domain" not in i:
                ip = re.findall(comp2, data)
                bilgi["text"] = ip

    except:
            pass

basla.config(command=baslat)

mainloop()
