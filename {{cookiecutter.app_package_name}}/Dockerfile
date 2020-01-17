FROM python:3.6.5

ENV FLASK_APP="{{cookiecutter.app_package_name}}"
ENV PATH="/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin"
ENV {{cookiecutter.app_package_name}}_SETTINGS="settings.cfg"
ENV DEBIAN_FRONTEND noninteractive

RUN apt-get update && apt-get upgrade -y && apt-get clean

RUN apt-get update && apt-get install -y ca-certificates
RUN apt-get update && apt-get install -y krb5-user
RUN apt-get update && apt-get install -y libkrb5-dev
RUN apt-get update && apt-get install -y libsasl2-dev
RUN apt-get update && apt-get install -y python-dev
RUN apt-get update && apt-get install -y libldap2-dev
RUN apt-get update && apt-get install -y libssl-dev
RUN apt-get update && apt-get install -y gcc
RUN apt-get update && apt-get install -y g++
RUN apt-get update && apt-get install -y gfortran
RUN apt-get update && apt-get install -y libc-dev
RUN apt-get update && apt-get install -y python3-dev
RUN apt-get update && apt-get install -y bash
RUN apt-get update && apt-get install -y cron

ENV TZ=Europe/Zurich
RUN ln -fs /usr/share/zoneinfo/$TZ /etc/localtime && echo $TZ > /etc/timezone && dpkg-reconfigure -f noninteractive tzdata

RUN pip install --upgrade pip
RUN pip install pipenv

COPY . /app

WORKDIR /app

ENV PIPENV_VENV_IN_PROJECT=1
RUN pipenv install --skip-lock

RUN pipenv install --skip-lock waitress

RUN chmod +x /app/cron_1_m.sh

ADD mycrontab /etc/cron.d/main-crontab
RUN chmod 0644 /etc/cron.d/main-crontab
RUN /usr/bin/crontab /etc/cron.d/main-crontab

RUN chmod +x /app/run.sh
ENTRYPOINT ["/app/run.sh"]
CMD ["DEV"]
