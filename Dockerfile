FROM python:3.8

WORKDIR /opt/app

COPY . .

RUN pip install --no-cache-dir -r requirements.txt
# RUN pip install --no-cache-dir -r data_processing/requirements.txt

EXPOSE 5000

ENTRYPOINT [ "python" ]
CMD [ "-u", "main.py" ]