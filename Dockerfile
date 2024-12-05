FROM python:3.9-slim

WORKDIR /home/poewr/flask_try

COPY requirements.txt ./
RUN pip install -r requirements.txt -i https://pypi.tuna.tsinghua.edu.cn/simple

COPY . .

CMD [ "python", "./manage.py" ]

