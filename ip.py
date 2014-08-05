# -*- coding: cp1254 -*-
from Tkinter import*
import urllib2
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

uagent= {'User-Agent':'Mozilla/5.0 (Windows; U; Windows NT 6.0; en-US; rv:1.9.0.6)'}
url = "http://viewdns.info/reverseip/?host=%s&t=1" % (victimiki)

try:
        req = urllib2.Request(url, headers=uagent)
        fd = urllib2.urlopen(req)
        data = fd.read()

        comp = re.compile("<tr><td>\S+</td><td")
        baglantilar = comp.findall(data)

        for i in baglantilar:
        i = i.replace("<tr><td>", "").replace("</td><td", "")

        if i.startswith("http://"):
                pass
        else:
                i = "http://"+i	

        if "Domain" not in i:
                bilgi = Label(anapen)
                bilgi.config(text=i)
                bilgi.pack()

mainloop()
