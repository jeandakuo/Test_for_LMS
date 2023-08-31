FROM tsl0922/ttyd:alpine

ENV PYTHONUNBUFFERED=1
RUN apk add --update --no-cache python3 && ln -sf python3 /usr/bin/python
RUN python3 -m ensurepip
RUN pip3 install --no-cache --upgrade pip setuptools

COPY main.py .

ARG FLAG

RUN echo "${FLAG}" > /root/flag.txt

EXPOSE 80

CMD ["ttyd", "-p", "80", "--writable", "python3", "main.py"]
