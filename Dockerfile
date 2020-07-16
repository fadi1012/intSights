FROM python:3

WORKDIR /usr/src/app

ADD / /usr/src/app

COPY test/src/intsight_test/tests/system_tests/test_github_gist.py /usr/src/app/test_github_gist.py

COPY run-tests /usr/src/app/run-tests

ADD test/requirements.txt /requirements.txt

ENV PYTHONPATH="$PYTHONPATH:/usr/src/app/intSights"

RUN pip install -r /requirements.txt

CMD /usr/src/app/run-tests