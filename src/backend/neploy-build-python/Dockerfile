FROM localhost:5000/ubuntu:22.04

# update apt
RUN apt update

# install required packages
RUN apt-get install -y python3 python3-pip

# install required python packages
RUN pip3 install neo3-boa==1.0.0 flask scikit-learn numpy pandas

# copy flask script to container
COPY neploy-build-python.py .

# copy ML code optimiser script
COPY ml-code-optimiser.py .