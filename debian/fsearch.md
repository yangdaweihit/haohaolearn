# FSearch

[FSearch](https://www.fossmint.com/fsearch-search-utility-for-linux/)是
一款快速搜索工具。作者Divine Okoi受Everything搜索引擎的启发而为Linux创造
的快速搜索工具。

## 安装

```
sudo apt install git build-essential automake autoconf libtool pkg-config intltool 
sudo apt install autoconf-archive libpcre3-dev libglib2.0-dev libgtk-3-dev libxml2-utils
sudo apt install autopoint
git clone https://github.com/cboxdoerfer/fsearch.git
cd fsearch
./autogen.sh
./configure
make && sudo make install
```