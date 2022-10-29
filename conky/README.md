# Conky

[Conky](https://github.com/brndnmtthws/conky)是一个轻型的系统监视器，将信息展示在桌面上。

## 用法

- 配置文件`.conf`，语法采用`Lua`形式，见[Configurations](https://github.com/brndnmtthws/conky/wiki/Configurations)。
- 启动：`conky -c /path/foo.conf &> /dev/null &`
- 一般是在`.config/`中建立目录`conky`，将主题文件夹拷贝其中，运行主题文件夹中的`start.sh`。
- 主题文件夹中一般配有相应的字体，需要安装该字体。
- 有的主题要显示天气数据，相应的脚本有`scripts/weather.sh`，其中大多用到[openweaterhmap](https://openweathermap.org/)的城市id和api_keys。
  - 城市id可在首页输入城市名后地址栏中显示其city_id; 
  - api_keys则需要注册帐号后，在用户名下拉菜单中找`My API Keys`；
  - 找到这两个变量后在`weather.sh`中替换两个变量值即可。
