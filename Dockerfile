# python3.8 lambda base image
#FROM public.ecr.aws/lambda/python:3.8
FROM public.ecr.aws/lambda/python:3.10-x86_64
#FROM python:3.11.1-slim

WORKDIR /app
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
# copy requirements.txt to container
COPY requirements.txt .
# installing dependencies
RUN pip3 install -r requirements.txt
# Copy function code to container
#COPY app.py ./
COPY . .

# setting the CMD to your handler file_name.function_name
RUN cd service/pr
CMD [ "app.handler" ]

