FROM centos:centos7
MAINTAINER Gert Van Gool <gertvangool@gmail.com>

RUN yum install -y epel-release && yum clean all
RUN yum install -y python{,-devel,-setuptools} gcc && yum clean all
RUN easy_install pip

# Create /app
RUN mkdir -p /app
WORKDIR /app

# Install python deps
ADD requirements.txt /app/
RUN mkdir -p /app/deployment/
ADD deployment/requirements.txt /app/deployment/
RUN pip install -r requirements.txt

# Add app
ADD . /app
