"""Convert ip address from "a.b.c.d" format into integer and viceversa"""

ip_address=list(map(int,input().split(".")))
ip_int=	(ip_address[0] * (256**3)) + (ip_address[1] * (256**2)) + (ip_address[2] * (256**1)) + (ip_address[3])
print(ip_int)