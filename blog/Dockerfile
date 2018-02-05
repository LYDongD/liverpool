# this docker file uses the xhuabu inner python3.6 images as the source 


FROM centos/python-36-centos7

MAINTAINER yuedong.li <yuedong.li@xhuabu.com>

USER root

ENV PROJECT blog

#COPY stockmarket /var/${PROJECT}/stockmarket
COPY ../app_dist /var/${PROJECT}/app/

#WORKDIR /var/${PROJECT}/stockmarket/
WORKDIR /var/${PROJECT}/app/

RUN /bin/cp /usr/share/zoneinfo/Asia/Shanghai /etc/localtime && echo 'Asia/Shanghai' >/etc/timezone;

RUN pip3.6 install --no-cache-dir blog-1.0.0.tar.gz -r requirements.txt -i http://pypi.douban.com/simple --trusted-host pypi.douban.com


#CMD ["python3.6", "/var/quote/stockmarket/market/main.py"]

CMD ["gunicorn", "-c", "gunicorn.ini", "manage:app"]
