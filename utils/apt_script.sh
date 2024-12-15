# 备份自带的源配置文件
cp  /etc/apt/sources.list /etc/apt/sources.list.bak

# 下面两条设置中国科技大学的apt-get镜像源, 速度杠杠的 &_& 比阿里云快!
sed -i s@/archive.ubuntu.com/@/mirrors.ustc.edu.cn/@g /etc/apt/sources.list
sed -i s@/security.ubuntu.com/@/mirrors.ustc.edu.cn/@g /etc/apt/sources.list

# 清理并且更新
apt-get clean
apt-get update

