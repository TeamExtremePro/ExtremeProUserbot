FROM python:3.9.5
RUN chmod +x /usr/local/bin/*
RUN wget startup/startup.sh
RUN sh deploy.sh
WORKDIR /root/ExtremeProuserbot/
CMD ["bash", "startup/startup.sh"]
