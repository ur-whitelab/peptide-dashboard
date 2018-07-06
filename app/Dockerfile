FROM ubuntu
RUN apt-get update && apt-get install -y build-essential g++ python3 python3-dev python3-pip cmake git wget libboost-all-dev libboost-python-dev
RUN whereis python3
ADD . /code
WORKDIR /code
RUN pip3 install -r requirements.txt && pip3 install .
RUN git clone --single-branch -b module https://github.com/ur-whitelab/peptide-qspr peptideqspr 
WORKDIR peptideqspr 
RUN git checkout module && pip3 install --no-cache-dir scipy pandas && pip3 install -r requirements.txt && pip3 install .
WORKDIR /code
CMD pytest && pd-app
