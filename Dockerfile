# THIS DOCKERFILE IS USED TO SEAMLESSLY DEPLOY THE RAZOR ENGINE
# IN A CLEAN AND CONTROLLED ENVIROMENT

FROM ubuntu

RUN apt-get update

RUN apt-get install -y python3-pip

RUN apt-get install nodejs

RUN apt-get install npm

COPY .aws/config ~.aws/

COPY interactions/ .

RUN python3 -m pip install -r requirements

RUN npm install -g serverless

CMD ["serverless", "deploy"]
