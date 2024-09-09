import time
import allure
from parameterized import parameterized

import config
from method.read_write_tools import Json_Method

from assert_method.assert_app_meeting import Assert_Meeting_App
from method import time_tool


@allure.feature("有局")
@allure.story("新增有局")
class Test_Add_Meeting:
    @staticmethod
    def teardown_method():
        print("延时等待1s，防止重复点击")
        time.sleep(1)

    @parameterized.expand(Json_Method.json_read(f"{config.data_path}add_meeting.json"))
    def test_add_meeting(self, case_title, case_description, token_phone, start_times, end_times, body, code, msg):
        allure.dynamic.title(case_title)
        allure.dynamic.description(case_description)
        # allure.dynamic.severity()
        body_time = {
            "meetingStartTime": time_tool.meeting_start_time(start_times),
            "meetingEndTime": time_tool.meeting_start_time(end_times)
        }
        if start_times != 0 and end_times != 0:
            body["meetingStartTime"] = body_time.get("meetingStartTime")
            body["meetingEndTime"] = body_time.get("meetingEndTime")
        elif start_times == 0:
            body["meetingEndTime"] = body_time.get("meetingEndTime")
        else:
            body["meetingStartTime"] = body_time.get("meetingStartTime")
        Assert_Meeting_App.add_meeting_assert(token_phone, body, code, msg)
