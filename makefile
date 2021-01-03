install:
	sudo echo "" > /usr/bin/pbh
	sudo echo "#!/bin/bash" >> /usr/bin/pbh
	sudo echo "python3 /usr/share/PasteBinHelper/pbh.py \"\$$@\"" >> /usr/bin/pbh
	sudo mkdir /usr/share/PasteBinHelper -p
	sudo cp ./pbh.py /usr/share/PasteBinHelper/
	sudo chmod +x /usr/bin/pbh
depends:
	pip3 install bs4
