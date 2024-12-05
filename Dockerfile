FROM python:3.9-slim

WORKDIR /home/poewr/flask_try

#USER root

VOLUME ["app/logs/"]

COPY ./utils/apt_script.sh /apt_script.sh

# 运行脚本
RUN chmod +x /apt_script.sh && /apt_script.sh

COPY requirements.txt ./
RUN pip install -r requirements.txt -i https://pypi.tuna.tsinghua.edu.cn/simple

COPY . .

CMD [ "python", "./manage.py" ]

