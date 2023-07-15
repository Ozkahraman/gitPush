import scapy.all as scapy   # ağ paketleriyle alakalı bir kutuphane
import optparse #komut satırlarını bolebilmek için ayrı ayrı kelime almaya yarıyo kullanıcıdan veri almak için terminal ekreanından

def get_user_input():
    parse_object = optparse.OptionParser()
    parse_object.add_option("-i", "--ipaddress", dest="ip", help="Write Your IP Address")
    (user_input, arguments) = parse_object.parse_args()                         # bunu yapmazsak degerleri cekemiyoruz degerleri ayirmamiz gerek
    return user_input

def scan_my_network(ip):
    arp_request_packet = scapy.ARP(pdst=ip)                                      #arp request olusturduk 24 arasına kadar tarayacak
    #scapy.ls(scapy.ARG())  # scapy kutuphanesine ozel hangi fonksiyonun ne is yaptigini soyluyo
    brodcats_packet = scapy.Ether(dst="ff:ff:ff:ff:ff:ff")                       #yayın yapmayı sagliyo ders 130-131
    #scapy.ls(scapy.Ether())
    combined_packet = brodcats_packet/arp_request_packet  #yukardaki iki oacketi birleştiriyo
    (answered_list,unanswered_list) = scapy.srp(combined_packet,timeout=1)       #paketi yolluyo taramya gönderiyo
    #print(list(answered_list))
    answered_list.summary()                                                     #ozetle cevap veren mac adreslerini goster

user_ip_addr = get_user_input()
scan_my_network(user_ip_addr.ip)