#!/bin/bash
#更新apt源为清华源
echo "[Info] 正在备份默认apt源..."
cp /etc/apt/sources.list /etc/apt/sources.list.bak
echo "[Info] 正在替换apt源为清华apt源..."
echo deb https://mirrors.tuna.tsinghua.edu.cn/ubuntu/ bionic main restricted universe multiverse > /etc/apt/sources.list
echo deb https://mirrors.tuna.tsinghua.edu.cn/ubuntu/ bionic-updates main restricted universe multiverse >> /etc/apt/sources.list
echo deb https://mirrors.tuna.tsinghua.edu.cn/ubuntu/ bionic-backports main restricted universe multiverse >> /etc/apt/sources.list
echo deb https://mirrors.tuna.tsinghua.edu.cn/ubuntu/ bionic-security main restricted universe multiverse >> /etc/apt/sources.list
echo "[Info] 正在更新源..."
apt update
echo "[Info] 正在更新软件..."
apt upgrade -y

