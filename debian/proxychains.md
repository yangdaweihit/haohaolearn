# ProxyChains

[ProxyChains](http://proxychains.net/)是一个网络代理工具，可将指定程序的
任何TCP连接转向某个代理。

## 安装

```
sudo apt install proxychains
```

## 配置

- 配置文件：`.proxychains/proxychains.conf`
- 注释：`# proxy_dns`
- 在`[ProxyList]`中配置：`socks5 127.0.0.1 1080`


## 使用

- `proxychains git clone xxx.git`