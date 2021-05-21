FROM python:3.9
WORKDIR .
ENV PYTHONUNBUFFERED=1
COPY requirements.txt .
COPY startup.py .
RUN bash startup.py
COPY . .
CMD ["python3", "-m", "userbot"]
