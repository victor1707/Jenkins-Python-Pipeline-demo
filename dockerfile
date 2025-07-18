FROM ubuntu:20.04
RUN apt update && apt install python3 -y && apt install python3-flask -y
COPY app1.py /tmp
EXPOSE 8080
CMD ["python3", "/tmp/app1.py"]
