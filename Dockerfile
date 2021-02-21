FROM python:3.9
WORKDIR /userbot
RUN git clone https://github.com/Bristi-OP/MEGASTAR.git .
RUN apt-get install -y pv tree mediainfo
RUN pip3 install -U -r requirements.txt
ENV PATH="/home/userbot/bin:$PATH"
CMD ["python3","-m","userbot"]
