import time

import allure
import pytest

from method.sql_tool import Sql_DataBase

import config
from method.read_write_tools import Yaml_Method

from assert_method.assert_app_meeting import Assert_Meeting_App


@allure.feature("有局")
@allure.story("取消有局")
class Test_Cancel_Meeting:
    # phone = None
    # start = None

    # @pytest.fixture(scope="function")
    # def update_start(self):
    #     time.sleep(1.2)
    #     yield
    #     with allure.step(f'连接数据库修改状态为{Test_Cancel_Meeting.start}'):
    #         pass
    #     Sql_DataBase.execute_tools("explore",
    #                              f"UPDATE explore_meeting SET meeting_status = {Test_Cancel_Meeting.start} WHERE id ="
    #                                f"{Yaml_Method.yaml_read(config.token,f'{Test_Cancel_Meeting.phone}meeting_id')};")

    @staticmethod
    def teardown():
        time.sleep(1.1)
        print("\n延时等待1s，防止重复点击")

    @staticmethod
    def update_start(phone_meeting_id, start):
        with allure.step(f'连接数据库,修改组局状态为：{start}'):
            pass
        Sql_DataBase.execute_tools("explore", "UPDATE explore_meeting SET"
                                              f" meeting_status = '{start}' WHERE id = "
                                              f"{Yaml_Method.yaml_read(config.token, f'{phone_meeting_id}meeting_id')};")

    @allure.title("取消组局成功")
    @allure.description("正向用例、取消自己发布的组局、组局状态为报名中")
    @allure.severity("critical")
    # @allure.step("取消组局")
    def test_cancel_succeed(self):
        phone = 15888888888
        Test_Cancel_Meeting.update_start(phone, "01")
        Assert_Meeting_App.cancel_meeting(phone, Yaml_Method.yaml_read(config.token, f"{phone}meeting_id"), 200, "成功")

    @allure.title("取消组局失败---组局进行中")
    @allure.description("逆向用例、取消自己发布的组局、组局状态为进行中")
    @allure.severity("normal")
    # @allure.step("取消组局")
    def test_cancel_fail_start_02(self):
        phone = 15888888888
        Test_Cancel_Meeting.update_start(phone, "02")
        Assert_Meeting_App.cancel_meeting(phone, Yaml_Method.yaml_read(config.token, f"{phone}meeting_id"), 500,
                                          "进行中,不可取消")

    @allure.title("取消组局失败---组局已结束")
    @allure.description("逆向用例、取消自己发布的组局、组局状态为已结束")
    @allure.severity("normal")
    # @allure.step("取消组局")
    def test_cancel_fail_start_03(self):
        phone = 15888888888
        Test_Cancel_Meeting.update_start(phone, "03")
        Assert_Meeting_App.cancel_meeting(phone, Yaml_Method.yaml_read(config.token, f"{phone}meeting_id"), 500,
                                          "已结束,不可取消")

    @allure.title("取消组局失败---组局已作废")
    @allure.description("逆向用例、取消自己发布的组局、组局状态为已作废")
    # @allure.step("取消组局")
    @allure.severity("normal")
    def test_cancel_fail_start_04(self):
        phone = 15888888888
        Test_Cancel_Meeting.update_start(phone, "04")
        Assert_Meeting_App.cancel_meeting(phone, Yaml_Method.yaml_read(config.token, f"{phone}meeting_id"), 500,
                                          "已屏蔽,不可取消")

    @allure.title("取消组局失败---组局已取消")
    @allure.description("逆向用例、取消自己发布的组局、组局状态为已取消")
    # @allure.step("取消组局")
    @allure.severity("normal")
    def test_cancel_fail_start_05(self, ):
        phone = 15888888888
        Test_Cancel_Meeting.update_start(phone, "05")
        Assert_Meeting_App.cancel_meeting(phone, Yaml_Method.yaml_read(config.token, f"{phone}meeting_id"), 500,
                                          "已取消,不可取消")

    @allure.title("取消组局失败---组局已失败")
    @allure.description("逆向用例、取消自己发布的组局、组局状态为组局失败")
    # @allure.step("取消组局")
    @allure.severity("normal")
    def test_cancel_fail_start_08(self):
        phone = 15888888888
        Test_Cancel_Meeting.update_start(phone, "06")
        Assert_Meeting_App.cancel_meeting(phone, Yaml_Method.yaml_read(config.token, f"{phone}meeting_id"), 500,
                                          "组局失败,不可取消")

    @allure.title("取消组局失败---组局已完成")
    @allure.description("逆向用例、取消自己发布的组局、组局状态为已完成")
    # @allure.step("取消组局")
    @allure.severity("normal")
    def test_cancel_fail_start_07(self):
        phone = 15888888888
        Test_Cancel_Meeting.update_start(phone, "07")
        Assert_Meeting_App.cancel_meeting(phone, Yaml_Method.yaml_read(config.token, f"{phone}meeting_id"), 500,
                                          "已完成,不可取消")
