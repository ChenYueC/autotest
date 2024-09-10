<h5>api</h5> 

    login：存放登录api、用于用户登录、获取token
    meeting_admin：存放请求后台的接口方法
    meeting_admin：存放请求app的接口方法
<h5>assert_method</h5>

    存放断言方法
<h5>data</h5>

    存放数据、测试数据、接口数据、token等
<h5>report</h5>

    allure报告目录
<h5>tmp_report</h5> 

    临时报告数据目录，用于生成allure
<h5>method</h5>

    存放使用的工具方法
<h5>test_case_script</h5>

    测试用例


# 设置用例优先级
# critical： 严重缺陷（功能点缺失）P0
# normal：   一般缺陷（边界情况，格式错误）P1
# minor：    次要缺陷（界面错误与ui需求不符）P2
# trivial：  轻微缺陷（必须项无提示，或者提示不规范）P3


blocker：阻塞缺陷（功能未实现，无法下一步)；对应用例优先级 P0 (冒烟、回归)
critical：严重缺陷（功能点缺失）；对应用例优先级 P1 (核心功能)
normal：一般缺陷（边界情况，格式错误）；对应用例优先级 P2 (基本功能)
minor：次要缺陷（界面错误与ui需求不符）；对应用例优先级 P3 (非功能)
trivial：轻微缺陷（必须项无提示，或者提示不规范）；对应用例优先级 P4  (体验类)
