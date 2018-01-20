# MCField_auto

# 魔卡领域挂机辅助
- 同学非要拉我玩这无脑刷刷刷的游戏（同阴阳师一类），玩了之后感觉。。。卡抽得还行。 手动不停的点点点好鸡儿累，重复劳动，so有了这个 -0-
- 受[教你用 Python 来玩微信跳一跳](https://github.com/xppppd/wechat_jump_game)启发，感谢
- 没有安卓机，只写了ios版本代码
- 只适配iPhone8 plus，不同屏幕尺寸适配需要更改截取图片的坐标，即战利品位置

# 原理说明
- 同微信跳一跳，通过wda获取手机当前截图
- 分析当前处于战斗页面还是战斗结算页面，分析结算页面各战利品，有魔卡掉落即停止，否则模拟点击屏幕开始下一次刷刷刷

# 更新日志

- 2018-1-13:
  - 添加自动刷魔卡材料脚本（刷到即停）
  - 添加无脑自动刷突破材料脚本

- 2018-1-20:
  - 添加andriod版本自动刷魔卡材料脚本（刷到即停）
  - 添加andriod版本无脑自动刷突破材料脚本
  
# 使用说明
## 运行环境iOS + macOS
- 使用真机调试 WDA，参考 [iOS 真机如何安装 WebDriverAgent · TesterHome](https://testerhome.com/topics/7220)
- 安装 [openatx/facebook-wda](https://github.com/openatx/facebook-wda)
- 运行安装好的 `WebDriverAgentRunner`
- 游戏里选好目标副本
- 运行对应的脚本
  - 自动刷魔卡：`python3 auto_materials.py`
  - 自动刷突破材料: `python3 auto_breaking.py`

## 运行环境android + windows
- 下载adb工具，打开手机调试模式，有问题请参考[adb连接问题](https://www.cnblogs.com/sanshuimiao/p/7809946.html)
- 把python脚本放在adb工具同目录下可不用配置path
- 游戏里选好目标副本
- 运行对应的脚本
  - 自动刷魔卡：`python3 auto_materials_andriod.py`
  - 自动刷突破材料: `python3 auto_breaking_andriod.py`
  
