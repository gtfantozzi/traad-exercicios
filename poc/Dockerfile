FROM python:3
ADD requirements.txt /
RUN pip install -r requirements.txt
ADD poc.py /
CMD [ "python", "./poc.py" ]