ip = input("Please provide your ip address: ")
ip_address = ip.split(".")
size = len(ip_address)
if size==4 and all (0 < int(ip) <= 255 for ip in ip_address):
    print("ip_address is a Valid IP")
else    :    
    print("ip_address is not a Valid IP")

