#!/bin/bash

# yum upgrade
sudo yum -y upgrade

# install jdk
sudo yum -y install java-1.8.0-openjdk

# install Spark
cd /tmp
wget http://d3kbcqa49mib13.cloudfront.net/spark-2.1.0-bin-hadoop2.7.tgz
sudo tar zxvf spark-2.1.0-bin-hadoop2.7.tgz -C /opt/
cd /opt
sudo ln -s spark-2.1.0-bin-hadoop2.7 spark
cd ~

# set env for spark
SPARK_HOME="/opt/spark"
{
  echo "export SPARK_HOME=$SPARK_HOME"
  echo "export PATH=$SPARK_HOME/bin:$PATH"
} | sudo tee -a /etc/profile.d/spark.sh

source /etc/profile
