FROM python:3.8.1

WORKDIR /usr/src/app

COPY . .

RUN python -m pip install --user nawah_cli
RUN python -m pip install -r requirements.txt

Run nawah install_deps

EXPOSE 8081

CMD [ "nawah", "launch" ]