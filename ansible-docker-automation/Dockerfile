FROM ubuntu:22.04
ENV DEBIAN_FRONTEND=noninteractive
RUN apt-get update && apt-get install -y \
    python3 \
    python3-pip \
    curl \
    && rm -rf /var/lib/apt/lists/*

RUN pip3 install requests
WORKDIR /app
COPY python_script.py .
RUN chmod +x python_script.py
CMD ["python3", "./python_script.py"]

# Запуск:

# docker run -d --name checker http-checker
# docker logs checker

# docker run -it http-checker python3 ./http_checker.py