import allure

import config
from assert_method.assert_app_meeting import Assert_Meeting_App
from method.read_write_tools import Yaml_Method
from method.sql_tool import Sql_DataBase


class Test_Cancel_Apply:
    @staticmethod
    def update_start(phone_meeting_id, start):
        with allure.step(f'连接数据库,修改组局状态为：{start}'):
            pass
        Sql_DataBase.execute_tools("explore", f"UPDATE explore_meeting SET meeting_status = '{start}' "
                                              f"WHERE id = {phone_meeting_id};")

    @allure.title("取消报名成功")
    @allure.description("正向用例、取消已报名的组局、组局状态为报名中")
    @allure.severity("critical")
    # @allure.step("取消组局")
    def test_cancel_apply_succeed(self):
        # 报名组局
        apply_phone_token = 15576597739
        phone_meeting = 15888888888
        meeting_id = Yaml_Method.yaml_read(config.token, f"{phone_meeting}meeting_id")
        Test_Cancel_Apply.update_start(meeting_id, "01")
        Assert_Meeting_App.apply_meeting(apply_phone_token, meeting_id, 200, "成功")
        # 取消组局
        Assert_Meeting_App.cancel_apply(apply_phone_token, meeting_id, 200, "操作成功")

    @allure.title("取消报名失败")
    @allure.description("逆向用例、取消已报名的组局、组局状态为进行中")
    @allure.severity("critical")
    def test_cancel_apply_fail_start_02(self):
        apply_phone_token = 15576597739
        phone_meeting = 15888888888
        meeting_id = Yaml_Method.yaml_read(config.token, f"{phone_meeting}meeting_id")
        Test_Cancel_Apply.update_start(meeting_id, "02")
        Assert_Meeting_App.cancel_apply(apply_phone_token, meeting_id, 500, "进行中,不可取消")

    @allure.title("取消报名失败")
    @allure.description("逆向用例、取消已报名的组局、组局状态为已结束")
    @allure.severity("critical")
    def test_cancel_apply_fail_start_03(self):
        apply_phone_token = 15576597739
        phone_meeting = 15888888888
        meeting_id = Yaml_Method.yaml_read(config.token, f"{phone_meeting}meeting_id")
        Test_Cancel_Apply.update_start(meeting_id, "03")
        Assert_Meeting_App.cancel_apply(apply_phone_token, meeting_id, 500, "已结束,不可取消")

    @allure.title("取消报名失败")
    @allure.description("逆向用例、取消已报名的组局、组局状态为已屏蔽")
    @allure.severity("critical")
    def test_cancel_apply_fail_start_03(self):
        apply_phone_token = 15576597739
        phone_meeting = 15888888888
        meeting_id = Yaml_Method.yaml_read(config.token, f"{phone_meeting}meeting_id")
        Test_Cancel_Apply.update_start(meeting_id, "04")
        Assert_Meeting_App.cancel_apply(apply_phone_token, meeting_id, 500, "已屏蔽,不可取消")

    @allure.title("取消报名失败")
    @allure.description("逆向用例、取消已报名的组局、组局状态为已取消")
    @allure.severity("critical")
    def test_cancel_apply_fail_start_03(self):
        apply_phone_token = 15576597739
        phone_meeting = 15888888888
        meeting_id = Yaml_Method.yaml_read(config.token, f"{phone_meeting}meeting_id")
        Test_Cancel_Apply.update_start(meeting_id, "05")
        Assert_Meeting_App.cancel_apply(apply_phone_token, meeting_id, 500, "已取消,不可取消")

    @allure.title("取消报名失败")
    @allure.description("逆向用例、取消已报名的组局、组局状态为组局失败")
    @allure.severity("critical")
    def test_cancel_apply_fail_start_03(self):
        apply_phone_token = 15576597739
        phone_meeting = 15888888888
        meeting_id = Yaml_Method.yaml_read(config.token, f"{phone_meeting}meeting_id")
        Test_Cancel_Apply.update_start(meeting_id, "06")
        Assert_Meeting_App.cancel_apply(apply_phone_token, meeting_id, 500, "组局失败,不可取消")

    @allure.title("取消报名失败")
    @allure.description("逆向用例、取消已报名的组局、组局状态为已完成")
    @allure.severity("critical")
    def test_cancel_apply_fail_start_03(self):
        apply_phone_token = 15576597739
        phone_meeting = 15888888888
        meeting_id = Yaml_Method.yaml_read(config.token, f"{phone_meeting}meeting_id")
        Test_Cancel_Apply.update_start(meeting_id, "07")
        Assert_Meeting_App.cancel_apply(apply_phone_token, meeting_id, 200, "已完成,不可取消")