# FZQOJ Auto Sign System

这个工具可以自动在FZQOJ中签到，需要一个服务器，并设定计划任务。

不过就是python+selenium+javascript罢了（

## 配置

### 用户

先新建一个 `data.conf` 文件，然后编辑：

每一行输入QOJ用户名+空格+密码（对，明文的！QwQ）

e.g.

```
st20250310 1145141919
c1120241702 101010102345
c20250000 asdfghjkl
jz20242333 qertyuiop
yx20260901 ghjklzmx
```

### 环境

只写了Linux的 QwQ，Windows可以参照一下

先克隆这个包

```bash
git clone https://github.com/lyxoffical/FZQOJAutoSign.git
cd FZQOJAutoSign
```

如果是Linux的话，python已经内置，您并不需要安装（没装就自己搜）

当然你需要安装 `selenium`（有可忽略）：

```bash
pip3 install selenium
```

接下来安装一个 `chrome`（有可忽略）：

```bash
wget https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb
sudo apt install google-chrome-stable_current_amd64.deb
# 不行就：sudo dpkg -i google-chrome-stable_current_amd64.deb
```

对于非 `Debian` 系系统，可以自行搜索安装方式。

然后查看版本：

```bash
google-chrome --version
```

记录下来，然后下载 `chromedriver`

在 [http://chromedriver.storage.googleapis.com/index.html](http://chromedriver.storage.googleapis.com/index.html) 里面找到最接近的版本，然后找到 `chromedriver_linux64.zip` 并下载。

把压缩包里面的 `chromedriver` 下下来，然后放到软件目录中。

OK，删掉下载的压缩包、安装包等临时文件，然后运行：

```bash
python3 -W ignore ./index.py
```

如果得到的是：

```
FZQOJ Auto Sign System By Ariasaka v3.1.2
------------------------------------------
Start Processing
Task #0
Running st20250310
Logining
Waiting For Login
Try to Click
st20250310 OK
你已经连续签到 109 天，今日获得 3 RP值和 1 硬币
------------------------------------------
Arrage Days: 56.29 && Today RP: 3.00
```

这类提示的话，配置就差不多了。

然后配置计划任务，可以用宝塔面板，命令这么写：

```bash
sudo su ubuntu
cd {改成你的项目文件夹}
python3 -W ignore ./index.py 
```

