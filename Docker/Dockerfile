FROM python:3.11.2
RUN mkdir /app
WORKDIR /app
RUN git clone https://github.com/barnap/ex-grs-internal.git
WORKDIR /app/ex-grs-internal
RUN pip install --no-cache-dir -r requirements.txt
EXPOSE 5000