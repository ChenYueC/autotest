import time
import allure
from parameterized import parameterized

from assert_method.assert_app_meeting import Assert_Meeting_App
from method import time_tool


@allure.feature("有局")
class Test_Add_Meeting:
    @staticmethod
    def teardown_method():
        time.sleep(1.2)

    @allure.title("新增有局成功")
    @allure.description("新增有局---仅必填项填写，预期：新增成功")
    def test_add_success1(self):
        body = {
            "meetingTitle": "pytest_有局",
            "meetingChooseType": "测试",
            "meetingAddress": "地址",
            "meetingAddressDetail": "详细地址",
            "meetingStartTime": time_tool.meeting_start_time(3600),
            "meetingEndTime": time_tool.meeting_start_time(7200),
            "meetingAddressLatitude": 39.903179,
            "meetingAddressLongitude": 116.397755,
            "meetingPaymentType": "03",
            "meetingType": "02",
            "meetingSeat": 2
        }
        Assert_Meeting_App.add_meeting_assert(15888888888, body, 200, "成功")

    @allure.title("新增有局失败")
    @allure.description("新增有局---组局开始时间为空，预期：开始时间为空、新增失败")
    def test_add_failure_start_time(self):
        body = {
            "meetingTitle": "pytest_有局",
            "meetingChooseType": "测试",
            "meetingAddress": "地址",
            "meetingAddressDetail": "详细地址",
            # "meetingStartTime": time_tool.meeting_start_time(3600),
            "meetingEndTime": time_tool.meeting_start_time(7200),
            "meetingAddressLatitude": 39.903179,
            "meetingAddressLongitude": 116.397755,
            "meetingPaymentType": "03",
            "meetingType": "02",
            "meetingSeat": 2
        }
        Assert_Meeting_App.add_meeting_assert(15888888888, body, 500, "开始时间不能为空")

    @allure.title("新增有局失败")
    @allure.description("新增有局---组局结束时间为空，预期：结束时间为空、新增失败")
    def test_add_failure_end_time(self):
        body = {
            "meetingTitle": "pytest_有局",
            "meetingChooseType": "测试",
            "meetingAddress": "地址",
            "meetingAddressDetail": "详细地址",
            "meetingStartTime": time_tool.meeting_start_time(3600),
            # "meetingEndTime": time_tool.meeting_start_time(7200),
            "meetingAddressLatitude": 39.903179,
            "meetingAddressLongitude": 116.397755,
            "meetingPaymentType": "03",
            "meetingType": "02",
            "meetingSeat": 2
        }
        Assert_Meeting_App.add_meeting_assert(15888888888, body, 500, "结束时间不能为空")

    # @allure.title("新增有局失败")
    # @allure.description("新增有局---组局地址纬度为空，预期：纬度不能为空、新增失败")
    # def test_add_failure_latitude(self):
    #     body = {
    #         "meetingTitle": "pytest_有局",
    #         "meetingChooseType": "测试",
    #         "meetingAddress": "地址",
    #         "meetingAddressDetail": "详细地址",
    #         "meetingStartTime": time_tool.meeting_start_time(3600),
    #         "meetingEndTime": time_tool.meeting_start_time(7200),
    #         # "meetingAddressLatitude": 39.903179,
    #         "meetingAddressLongitude": 116.397755,
    #         "meetingPaymentType": "03",
    #         "meetingType": "02",
    #         "meetingSeat": 2
    #     }
    #     Assert_Meeting_App.add_meeting_assert(15888888888, body, 500, "开始时间不能为空")
    #
    # @allure.title("新增有局失败")
    # @allure.description("新增有局---组局地址京都为空，预期：经度不能为空、新增失败")
    # def test_add_failure_longitude(self):
    #     body = {
    #         "meetingTitle": "pytest_有局",
    #         "meetingChooseType": "测试",
    #         "meetingAddress": "地址",
    #         "meetingAddressDetail": "详细地址",
    #         "meetingStartTime": time_tool.meeting_start_time(3600),
    #         "meetingEndTime": time_tool.meeting_start_time(7200),
    #         "meetingAddressLatitude": 39.903179,
    #         # "meetingAddressLongitude": 116.397755,
    #         "meetingPaymentType": "03",
    #         "meetingType": "02",
    #         "meetingSeat": 2
    #     }
    #     Assert_Meeting_App.add_meeting_assert(15888888888, body, 500, "开始时间不能为空")
    @allure.title("新增有局失败")
    @allure.description("新增有局---开放局、费用方式为空，预期：付款方式为空、新增失败")
    def test_add_failure_pay(self):
        body = {
            "meetingTitle": "pytest_有局",
            "meetingChooseType": "测试",
            "meetingAddress": "地址",
            "meetingAddressDetail": "详细地址",
            "meetingStartTime": time_tool.meeting_start_time(3600),
            "meetingEndTime": time_tool.meeting_start_time(7200),
            "meetingAddressLatitude": 39.903179,
            "meetingAddressLongitude": 116.397755,
            # "meetingPaymentType": "03",
            "meetingType": "02",
            "meetingSeat": 2
        }
        Assert_Meeting_App.add_meeting_assert(15888888888, body, 500, "付款方式不能为空")

    @allure.title("新增有局失败")
    @allure.description("新增有局---组局方式为空，预期：组局方式为空、新增失败")
    def test_add_failure_type(self):
        body = {
            "meetingTitle": "pytest_有局",
            "meetingChooseType": "测试",
            "meetingAddress": "地址",
            "meetingAddressDetail": "详细地址",
            "meetingStartTime": time_tool.meeting_start_time(3600),
            "meetingEndTime": time_tool.meeting_start_time(7200),
            "meetingAddressLatitude": 39.903179,
            "meetingAddressLongitude": 116.397755,
            "meetingPaymentType": "03",
            # "meetingType": "02",
            "meetingSeat": 2
        }
        Assert_Meeting_App.add_meeting_assert(15888888888, body, 500, "类型不能为空")

    @allure.title("新增有局失败")
    @allure.description("新增有局---席位数为空，预期：席位为空、新增失败")
    def test_add_failure_seat(self):
        body = {
            "meetingTitle": "pytest_有局",
            "meetingChooseType": "测试",
            "meetingAddress": "地址",
            "meetingAddressDetail": "详细地址",
            "meetingStartTime": time_tool.meeting_start_time(3600),
            "meetingEndTime": time_tool.meeting_start_time(7200),
            "meetingAddressLatitude": 39.903179,
            "meetingAddressLongitude": 116.397755,
            "meetingPaymentType": "03",
            "meetingType": "02",
            # "meetingSeat": 2
        }
        Assert_Meeting_App.add_meeting_assert(15888888888, body, 500, "座位数不能为空")
