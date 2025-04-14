FROM python:3.11

COPY requirements.txt /srv/app/
RUN pip3 install --no-cache-dir -r /srv/app/requirements.txt 

COPY src /srv/app/
WORKDIR /srv/app/

CMD ["gunicorn", "-w", "1", "-b", "0.0.0.0:5000", "app:app"]