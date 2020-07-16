FROM python:3

WORKDIR /usr/src/app

COPY test/src/intsight_test/tests/system_tests/test_github_gist.py /usr/src/app/test_github_gist.py

ADD test/requirements.txt /requirements.txt

RUN pip install -r /requirements.txt

CMD [ "pytest", "./test_github_gist.py" ]
