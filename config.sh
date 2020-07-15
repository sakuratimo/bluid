#!/bin/bash
#cp /etc/apt/sources.list /etc/apt/sources.list.bak
#cat > /etc/apt/sources.list <<EOF
# 默认注释了源码镜像以提高 apt update 速度，如有需要可自行取消注释
#deb http://mirrors.tuna.tsinghua.edu.cn/ubuntu/ bionic main restricted universe multiverse
#deb http://mirrors.tuna.tsinghua.edu.cn/ubuntu/ bionic-updates main restricted universe multiverse
#deb http://mirrors.tuna.tsinghua.edu.cn/ubuntu/ bionic-backports main restricted universe multiverse
#deb http://mirrors.tuna.tsinghua.edu.cn/ubuntu/ bionic-security main restricted universe multiverse
#EOF
#apt-key adv --recv-keys --keyserver keyserver.ubuntu.com 3B4FE6ACC0B21F32
#apt update

#pip3 install --upgrade pip
pip3 install requests  -i http://pypi.douban.com/simple/ --trusted-host pypi.douban.com
#pip3 install -r /requirements_config.txt
#echo 'Requests addon installed'
chmod +x /config.py
#echo 'ready to run config.py'
python3 /config.py  web
#echo 'config.py executed'
