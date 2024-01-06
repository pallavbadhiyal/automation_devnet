ip = input("Please provide your ip address: ")
ip_address = ip.split(".")
size = len(ip_address)

if size != 4:
    print("ip_address is not a Valid IP")
else:
    if all (0 < int(ip) <= 255 for ip in ip_address):
    # if int(ip_address[1]) <= 255 and int(ip_address[1]) >= 0:
    #     if int(ip_address[2]) <= 255 and int(ip_address[2]) >= 0:
    #         if int(ip_address[3]) <= 255 and int(ip_address[3]) >= 0:
        print("ip_address is a Valid IP")
    else    :    
        print("ip_address is not a Valid IP")

 
#  for ip in ip_address:
#         ip = int(ip)
#         if 0 < ip <= 255:
#             continue         
#         else:    
#             False
    
# if ip:
#     print("ip_address is a Valid IP")
# else:    
#     print("ip_address is not a Valid IP")