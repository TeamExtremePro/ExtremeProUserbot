FROM TeamExtremePro/ExtremeProUserbot:latest

#clonning repo 
RUN git clone https://github.com/TeamDynamic/Dynamic-Userbot.git

# Install requirements
RUN pip3 install -U -r requirements.txt

CMD ["python3","-m","start.py"]
