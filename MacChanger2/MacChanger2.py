import subprocess   #python uygulamsını termiinalde başlattıgımızda arkada terminalde gozukmeyen işlemleri uygulamak için
import optparse     #kullanıcıdan terminal ekranından veri almak için

def getUserInput():
    parse_object = optparse.OptionParser()
    parse_object.add_option("-i", "--interface", dest="interface", help="interface to change!") #opsiyon ekliyosun terminale girebileceği
    # destination gideceği yer interface dedik help yazarsa ne cıkacagını belirttik
    parse_object.add_option("-m", "--mac", dest="MacAddr", help="Your new mac address")

    return parse_object.parse_args()    #iki tane argüman döndürüyo

def changeNewMac(user_interface,user_MacAddr):
    subprocess.call(["ifconfig", user_interface, "down"])
    subprocess.call(["ifconfig", user_interface, "hw", "ether", user_MacAddr])
    subprocess.call(["ifconfig", user_interface, "up"])

def controlNewMac(interface):
    ifconfig = subprocess.check_output(["ifconfig", interface])     #ifconfig et0 yazarsan panele ne cıkıyosa onu arkda yaıp yazdırıyo ekrana
    print(ifconfig)

(userInput,arguments) = getUserInput()                  #fonksiyonun icindeki argumanları userInputa tek tek parcala
changeNewMac(userInput.interface, userInput.MacAddr)
controlNewMac(userInput.interface)
print("Your Mac is Changed")
