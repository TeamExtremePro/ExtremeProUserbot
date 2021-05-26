FROM koala21/kampangbot:buster

# COPYRIGHT TEAM EXTREME PRO (C) 2021-2022
RUN git clone -b ExtremeProUserbot https://github.com/TeamExtremePro/ExtremeProUserbot /root/amanpandey
RUN mkdir /root/amanpandey/.bin
RUN pip install --upgrade pip setuptools
WORKDIR /root/amanpandey

#Install python requirements
RUN pip3 install -r https://raw.githubusercontent.com/TeamExtremePro/ExtremeProUserbot/main/requirements.txt

CMD ["python3","-m","amanpandey"]
