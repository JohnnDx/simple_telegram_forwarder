FROM python:3.9

ENV LANG=C.UTF-8

COPY ./ /app/

RUN pip install --upgrade pip
RUN pip install --no-cache-dir -r /app/requirements.txt

WORKDIR /app/
CMD ["python3 bot.py"]
