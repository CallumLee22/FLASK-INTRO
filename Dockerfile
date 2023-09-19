FROM python:3

WORKDIR /app

COPY requirements.txt ./
RUN pip install -r requiremets.txt

COPY . .

EXPOSE 5000

COPY entrypoint.sh .
ENTRYPOINT ["./entrypoint.sh"]