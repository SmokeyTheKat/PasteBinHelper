import requests as req
from bs4 import BeautifulSoup as bs
import lxml
import sys

mspace1 = 35
mspace2 = 10
mspace3 = 10

argv = sys.argv
argc = len(sys.argv)


def find(show):
	print("Searching PasteBin.com for: " + argv[2])
	inp = argv[argv.index("--find")+1].replace(" ", "+")
	s = req.get("https://google.com/search?q=%3Apastebin.com+" + inp + "&num=1000", headers={"user-agent": "Mozilla/5.0 (Macintosh; Intel Max OS X 10.14; rv:65.0) Gecko/20100101 Firefox/65.0"}).text
	so = bs(s, "lxml")
	art = so.findAll("div", class_="r")
	i  = 0
	j  = 0
	while 1 == 1:
		if i < len(art):
			name = art[i].h3.text
			tuid = art[i].a["href"].split("/")
			uid = tuid[len(tuid)-1]
			spacer1 = ((mspace1*2)-len(name)) * " "
			if not "http" in name and len(uid) == 8:
				j += 1
				lab = str(j) + ": "
				labs = (5-(len(lab))) * " "
				if show == None:
					print(lab, labs, name, spacer1, uid)
					ui = input("[Enter - next | show - print | num - show result by number | exit]> ")
					if ui == "exit":
						return
					elif ui == "show":
						j -= 1
						main(uid, True)
					else:
						try:
							if int(ui):
								j -= 1
								find(int(ui))
						except:
							print("\033[2A")
				elif j == show:
					main(uid, True)
			i += 1
		else:
			return


def main(uid, p):
	_r =  req.get("https://www.pastebin.com/raw/" + uid).text
	if len(argv) == 3 and not p:
		with open(argv[2], "w+") as f:
			f.write(_r)
	elif len(argv) == 2 or p:
		print(_r)



if "--help" in argv or "-help" in argv or "-h" in argv or argc == 1:
	print("PasteBin Helper:")
	print("    (pbh uid) - will print contents to screen")
	print("         EX: 'pbh A6246IWA myfile.txt'")
	print("    (pbh uid outputfile) - will output contents to file")
	print("         EX: 'pbh A6246IWA myfile.txt'")
	print("    (pbh uid > outputfile) - will output contents to file")
	print("         EX: 'pbh A6246IWA > myfile.txt'")
	print("    (pbh --find \"Search Terms\")(pbh -find \"Search Terms\") - finds pastes based on your search terms")
	print("         EX: 'pbh --find \"python script\"'")
	print("    (pbh --find \"Search Terms\" number)(pbh -find \"Search Terms\" number) - finds pastes and downloads the Nth one")
	print("         EX: 'pbh --find \"python script\" 2'")
	print("    (pbh --top)(pbh -top)(pbh --new)(pbh -new) - will show recent PasteBin.com pastes")
elif "-new" in argv or "--new" in argv or "-top" in argv or "--top" in argv:
	s = req.get("https://pastebin.com").text
	so = bs(s, "lxml")
	art = so.findAll("li");
	for i in art:
		name = i.a.text.replace("\n", "").replace("\r", "")
		uid = i.a["href"].replace("/", "")
		details = i.div.text.replace("\n", "").replace("\r", "")
		lang = details.split("|")[0].replace(" ", "")
		ptime = details.split("|")[1].replace("", "").split(" ")
		time = (ptime[len(ptime)-19] + " " + ptime[len(ptime)-18] + " " +ptime[len(ptime)-17])
		spacer1 = (mspace1-len(name)) * " "
		spacer2 = (mspace2-len(uid)) * " "
		spacer3 = (mspace2-len(lang)) * " "
		print(name, spacer1, uid, spacer2, lang, spacer3, spacer2, time)
elif "-find" in argv or "--find" in argv:
	if len(argv) == 4:
		find(int(argv[argv.index("--find")+2]))
	else:
		find(None)
else:
	main(argv[1], False)
