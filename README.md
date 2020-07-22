# ACMW-JNBJT
Auto Collcet Money of Well -JiangNanBaiJingTu.自动收集水井铜币，江南百景图。ios的脚本实现因为闭源很复杂。不越狱的话，则需要一台mac系统电脑（可hackintosh）+一台ios设备。本库主要在于记录繁琐的ios调试环境搭建过程。

Befor start：能用安卓用安卓，简单易操作。

如果不得不用ios：

用到的硬件：ios设备+一台mac系统的电脑，能提供同一局域网的wifi设备。

软件：appium+wda+python+xcode。

步骤：

1下载xcode，苹果官网，选择自己mac系统能支持的，同时不能太老不然难以适配ios设备的ios系统。我的选择：mac mojave 10.14.6，ios 13.5， xcode 11.2.

可以apple store 或者https://developer.apple.com/download/。

1.5wda安装编译：非必要。

因为facebook的web-drive-agent是核心，但是年久失修有些问题，可以参考https://testerhome.com/topics/7220 进行wda的安装编译，成功查看status/insepector后可以初步连接控制手机。
但是大概率会遇到问题。
不过验证了除wda的正确性。

2appium自带wda，较新版本的wda和老攻略的地址不一样。
参考攻略：重要且有图：https://juejin.im/post/5d7ef540f265da03bb4ada00。
1.17的wda地址（安装在
application）：/Applications/Appium.app/Contents/Resources/app/node_modules/appium/node_modules/appium-webdriveragent 而不是老攻略的 /Applications/Appium.app/Contents/Resources/app/node_modules/appium/node_modules/appium-xcuitest-driver 。

下载：先安装 homebrew：包管理
/usr/bin/ruby -e "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install)"

安相关包:
//node
brew install node

//npm
brew install npm

//carthage
brew install carthage

//libimobiledevice(真机测试需要)
brew install libimobiledevice

//ios-deploy(真机测试需要)
brew install ios-deploy

//python （Mac下默认是2.7版本 ）
brew install python

验证appium安装：

//1、安装appium-doctor验证
pm install -g appium-doctor

//2、验证(终端直接入下面命令)
appium-doctor



转到 wda路径：
cd /Applications/Appium.app/Contents/Resources/app/node_modules/appium/node_modules/appium-webdriveragent  #记得改成 WDA 的目录

./Scripts/bootstrap.sh。

wda.xproject需要进行开发者账号和bundleid更改，还需要在ios设备上添加信任。

wda.xproject需要进行开发者账号和bundleid更改，还需要在ios设备上添加信任。

wda.xproject需要进行开发者账号和bundleid更改，还需要在ios设备上添加信任。

这里重要且较麻烦，需要图，可以谷歌攻略或者看有图链接参考：https://testerhome.com/topics/14447 

build完成后，在xcode的topbar可以product-scheme-*run,  product-destineation-yourdevice， product-test，view-debugarea-activeconsole 后可以看到一串ip地址，添加/status到浏览器后有jason输出，添加/insepector到浏览器后应该有画面，如果没有不用纠结，status有即可。我用fb的官方库，可以出现inspector但是无法显示ios设备屏幕，用appium的wda无法进入inspector界面。但是status都有输出即可。

安装facebook-wda：pip3 install --pre facebook-wda

安装appium python库：pip3 install appium。

appium 启动后，会看到手机屏幕的画面。有个眼睛的图标录制操作，手动在mac里点按操作会被记录成代码，选择python版本，记录下点按操作： 主要是坐标。

然后添加wait/delay/sleep time，再嵌套一个循环函数即可。

如有更多疑问，谷歌搜索方向：微信跳一跳自动实现。

对于一个没有xcode，有一些terminal命令后经验的人：初步预估时间耗费6-9小时，包括下载+等待+搜索攻略时间。



