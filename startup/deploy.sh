echo "
	      ╔╦╦╦══╦═╦═╦══╦══╗
	      ║║║╠╗╔╣╬║║╠║║╩╗╗║
	      ║║║╚╣║║╗╣║╠║║╦╩╝║
	      ╚═╩═╩╝╚╩╩═╩══╩══╝
	    °•° Deployment Begins •°•
"
echo '
        •• Getting Packages and Installing
'


ln -snf /usr/share/zoneinfo/$TZ /etc/localtime && echo $TZ > /etc/timezone

apt-get update
apt-get upgrade -y
apt-get install -y --no-install-recommends ffmpeg neofetch mediainfo megatools
apt-get autoremove --purge

echo '
        •• Cloning Repository
'
git clone https://github.com/TeamExtremePro/ExtremeProUserbot.git /root/ExtremeProUserbot/

echo '
	•• Getting Libraries and Installing
'
pip install --upgrade pip setuptools wheel
pip install search-engine-parser
pip install -r https://github.com/TeamExtremePro/ExtremeProUserbot/blob/master/requirements.txt

echo "
			      ┏┳┓╋┏┓╋╋╋╋┏┓┏┓
			      ┃┃┣┓┃┗┳┳┳━╋╋┛┃
			      ┃┃┃┗┫┏┫┏┫╋┃┃╋┃
			      ┗━┻━┻━┻┛┗━┻┻━┛
			•°• Deployed Successfully °•°
		   •• Wait till python images are pushed
	   •• Give build logs in @EXTREMEPRO_USERBOT if build fails
"
