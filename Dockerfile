FROM TeamExtremePro/ExtremeProUserbot:latest

#clonning repo 
RUN git clone https://github.com/TeamDynamic/Dynamic-Userbot.git

# Install requirements
RUN pip3 install -U -r requirements.txt

ENV PATH="/home/amanpandey/bin:$PATH"

CMD ["python3","-m","amanpandey"]
