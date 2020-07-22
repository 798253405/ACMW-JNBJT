# ACMW-JNBJT
Auto Collcet Money of Well -JiangNanBaiJingTu.自动收集水井铜币，江南百景图。ios的脚本实现因为闭源很复杂。不越狱的话，则需要一台mac系统电脑（可hackintosh）+一台ios设备。本库主要在于记录繁琐的ios调试环境搭建过程。
Befor start：能用安卓用安卓，简单易操作。
如果不得不用ios：
用到的硬件：ios设备+一台mac系统的电脑，能提供同一局域网的wifi设备。
软件：appium+wda+python+xcode。
步骤：
1下载xcode，苹果官网，选择自己mac系统能支持的，同时不能太老不然难以适配ios设备的ios系统。我的选择：mac mojave 10.14.6，ios 13.5， xcode 11.2.
可以apple store 或者https://developer.apple.com/download/。
1.5wda安装编译：可选。
因为facebook的web-drive-agent是核心，但是年久失修有些问题，可以参考https://testerhome.com/topics/7220进行wda的安装编译，成功查看status/insepector后可以初步连接控制手机，但是大概率会遇到问题。
不过验证了除wda的正确性。
2appium自带wda，较新版本的wda和老攻略的地址不一样。1.17的wda地址（安装在application）：/Applications/Appium.app/Contents/Resources/app/node_modules/appium/node_modules/appium-webdriveragent而不是老攻略的 /Applications/Appium.app/Contents/Resources/app/node_modules/appium/node_modules/appium-xcuitest-driver/
