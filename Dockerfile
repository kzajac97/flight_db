FROM python:3

RUN pip install pandas==1.1.4
RUN pip install pyramid==1.10.5
RUN pip install SQLAlchemy==1.3.20
RUN pip install psycopg2-binary
RUN pip install pyramid_chameleon
RUN pip install waitress
RUN pip install setuptools

WORKDIR /workdir
