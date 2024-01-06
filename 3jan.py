ip = input("Please provide your ip address: ")
ip_address = ip.split(".")
size = len(ip_address)

if size != 4:
    print("ip_address is not a Valid IP")
else:
 if all (0 < int(ip) <= 255 for ip in ip_address):
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