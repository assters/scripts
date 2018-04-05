import thread #import Thread
import socket 
import time

def ping(ip): 
	alive = False 
	PORT = 139 
	s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
	s.settimeout(4) 
	try: 
		exit = s.connect_ex((ip, PORT)) 
		alive = (exit!=113) # 113 - No route to host 		
		if 0 == exit:  
			print(ip) 
	finally: 
		s.close() 
	return alive 

def add_ip_to_list(ip,ips): 
	ping(ip)

def main1(): 
	# 
	#  
	ips = [] 
	for i in range(1,255): 
		ip = '192.168.12.'+str(i) 
		thread.start_new_thread(add_ip_to_list, (ip,ips))
		time.sleep(1) 
	return ips	

print("Found hosts")
ips2 = [] 
ips2 = main1()