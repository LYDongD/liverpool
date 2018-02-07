# this docker file uses the xhuabu inner python3.6 images as the source 


FROM centos/python-36-centos7

MAINTAINER yuedong.li <yuedong.li@xhudockerabu.com>

USER root

ENV PROJECT blog

#COPY stockmarket /var/${PROJECT}/stockmarket
COPY app_dist /var/${PROJECT}/app/

#WORKDIR /var/${PROJECT}/stockmarket/
WORKDIR /var/${PROJECT}/app/

EXPOSE 5000 8080

RUN /bin/cp /usr/share/zoneinfo/Asia/Shanghai /etc/localtime && echo 'Asia/Shanghai' >/etc/timezone;

RUN tar -zxvf blog-1.0.0.tar.gz

RUN rm blog-1.0.0.tar.gz

RUN pip3.6 install -r requirements.txt -i http://pypi.douban.com/simple --trusted-host pypi.douban.com


#CMD ["python3.6", "/var/quote/stockmarket/market/main.py"]

CMD ["gunicorn", "-c", "gunicorn.ini", "manage:app"]
