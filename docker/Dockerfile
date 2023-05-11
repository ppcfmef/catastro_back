FROM python:3.9

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

WORKDIR /usr/src/app/
COPY ./catastro_fiscal /usr/src/app/
COPY ./requirements.txt /usr/src/app/
COPY ./docker/entrypoint.sh /usr/src/app/

RUN apt update
RUN apt install -y gettext
RUN pip install -r requirements.txt
RUN chmod +x ./entrypoint.sh

ARG DJANGODIR=/usr/src/app/
ENV PYTHONPATH=${DJANGODIR}:${PYTHONPATH}
ENV DJANGO_SETTINGS_MODULE=catastro_fiscal.settings.${ENVIRONMENT:-local}

ENTRYPOINT ["./entrypoint.sh"]
