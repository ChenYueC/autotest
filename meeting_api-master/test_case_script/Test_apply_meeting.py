import time
import allure
import pytest
import config
from method.read_write_tools import Yaml_Method
from assert_method.assert_app_meeting import Assert_Meeting_App
from method.sql_tool import Sql_DataBase


@allure.feature("有局")
@allure.story("报名有局")
class Test_Apply_Meeting:
    @staticmethod
    def teardown():
        time.sleep(1.1)
        print("\n延时等待1s，防止重复点击")

    @staticmethod
    def delete_apply_relevancy(meeting_id):
        with allure.step(f'删除组局会议报名用户'):
            pass
        Sql_DataBase.execute_tools("explore", f"DELETE FROM explore_meeting_user_relate WHERE "
                                              f"meeting_id = {meeting_id};")

    @staticmethod
    def update_start(phone_meeting_id, start):
        with allure.step(f'连接数据库,修改组局状态为：{start}'):
            pass
        Sql_DataBase.execute_tools("explore", f"UPDATE explore_meeting SET meeting_status = '{start}' "
                                              f"WHERE id = {phone_meeting_id};")

    @allure.title("报名组局成功")
    @allure.description("正向用例、报名他人发布的组局、组局状态为报名中")
    @allure.severity("critical")
    def test_apply_succeed(self):
        apply_phone_token = 15576597739
        phone_meeting = 15888888888
        meeting_id = Yaml_Method.yaml_read(config.token, f"{phone_meeting}meeting_id")
        Assert_Meeting_App.apply_meeting(apply_phone_token, meeting_id, 200, "成功")

    @allure.title("报名组局失败---报名中、已报名")
    @allure.description("逆向用例、重复报名他人发布的组局、组局状态为报名中、不可重复报名")
    @allure.severity("normal")
    def test_apply_fail_01(self):
        apply_phone_token = 15576597739
        phone_meeting = 15888888888
        meeting_id = Yaml_Method.yaml_read(config.token, f"{phone_meeting}meeting_id")
        Assert_Meeting_App.apply_meeting(apply_phone_token, meeting_id, 500, "审核中，不可报名")

    @allure.title("报名组局失败---组局进行中")
    @allure.description("逆向用例、报名他人发布的组局、组局状态为进行中，只有状态为报名中的组局才可报名")
    @allure.severity("normal")
    def test_apply_fail_02(self):
        apply_phone_token = 15576597739
        phone_meeting = 15888888888
        meeting_id = Yaml_Method.yaml_read(config.token, f"{phone_meeting}meeting_id")
        Test_Apply_Meeting.delete_apply_relevancy(meeting_id)
        Test_Apply_Meeting.update_start(meeting_id, "02")
        Assert_Meeting_App.apply_meeting(apply_phone_token, meeting_id, 500, "已结束报名")

    @allure.title("报名组局失败---组局已结束")
    @allure.description("逆向用例、报名他人发布的组局、组局状态为进行中，只有状态为报名中的组局才可报名")
    @allure.severity("normal")
    def test_apply_fail_03(self):
        apply_phone_token = 15576597739
        phone_meeting = 15888888888
        meeting_id = Yaml_Method.yaml_read(config.token, f"{phone_meeting}meeting_id")
        Test_Apply_Meeting.update_start(meeting_id, "03")
        Assert_Meeting_App.apply_meeting(apply_phone_token, meeting_id, 500, "已结束,不可报名")

    @allure.title("报名组局失败---组局已作废")
    @allure.description("逆向用例、报名他人发布的组局、组局状态为已作废，只有状态为报名中的组局才可报名")
    @allure.severity("normal")
    def test_apply_fail_04(self):
        apply_phone_token = 15576597739
        phone_meeting = 15888888888
        meeting_id = Yaml_Method.yaml_read(config.token, f"{phone_meeting}meeting_id")
        Test_Apply_Meeting.update_start(meeting_id, "04")
        Assert_Meeting_App.apply_meeting(apply_phone_token, meeting_id, 500, "已屏蔽,不可报名")

    @allure.title("报名组局失败---组局已取消")
    @allure.description("逆向用例、报名他人发布的组局、组局状态为已作废，只有状态为报名中的组局才可报名")
    @allure.severity("normal")
    def test_apply_fail_05(self):
        apply_phone_token = 15576597739
        phone_meeting = 15888888888
        meeting_id = Yaml_Method.yaml_read(config.token, f"{phone_meeting}meeting_id")
        Test_Apply_Meeting.update_start(meeting_id, "05")
        Assert_Meeting_App.apply_meeting(apply_phone_token, meeting_id, 500, "已取消,不可报名")

    @allure.title("报名组局失败---组局状态失败")
    @allure.description("逆向用例、报名他人发布的组局、组局状态为组局失败，组局失败状态，用户不可报名")
    @allure.severity("normal")
    def test_apply_fail_06(self):
        apply_phone_token = 15576597739
        phone_meeting = 15888888888
        meeting_id = Yaml_Method.yaml_read(config.token, f"{phone_meeting}meeting_id")
        Test_Apply_Meeting.update_start(meeting_id, "06")
        Assert_Meeting_App.apply_meeting(apply_phone_token, meeting_id, 500, "组局失败,不可报名")

    @allure.title("报名组局失败---组局已完成")
    @allure.description("逆向用例、报名他人发布的组局、组局状态为已作废，只有状态为报名中的组局才可报名")
    @allure.severity("normal")
    def test_apply_fail_07(self):
        apply_phone_token = 15576597739
        phone_meeting = 15888888888
        meeting_id = Yaml_Method.yaml_read(config.token, f"{phone_meeting}meeting_id")
        Test_Apply_Meeting.update_start(meeting_id, "07")
        Assert_Meeting_App.apply_meeting(apply_phone_token, meeting_id, 500, "已完成,不可报名")
