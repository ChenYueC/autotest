import requests
import config
from method.read_write_tools import Yaml_Method
# from method import time_tool
import logging


class App_Meeting_Api:
    # 新增组局
    @classmethod
    def add_meeting(cls, token_phone, body):
        url = config.domain_path + Yaml_Method.yaml_read(config.api_meeting_app, "add")
        head = {
            "User-Agent": "pytest",
            "login_token": Yaml_Method.yaml_read(config.token, token_phone)
        }
        resp = requests.post(url, headers=head, json=body)
        if resp.json().get("message") == "操作成功":
            Yaml_Method.yaml_write(config.token, {f"{token_phone}meeting_id": resp.json().get("data")})
        logging.info("新增组局-app")
        logging.info(f"请求url：{url}")
        logging.info(f"请求头：{head}")
        logging.info(f"请求体：{body}")
        logging.info(f"响应结果：{resp.json()}")
        return resp.json()

    # 取消组局
    @classmethod
    def cancel_meeting(cls, token_phone, meeting_id):
        url = f"{config.domain_path}{Yaml_Method.yaml_read(config.api_meeting_app, 'cancel_meeting')}{meeting_id}"
        head = {
            "User-Agent": "pytest",
            "login_token": Yaml_Method.yaml_read(config.token, token_phone)
        }
        resp = requests.put(url, headers=head)
        logging.info("取消组局-app")
        logging.info(f"请求url：{url}")
        logging.info(f"请求头：{head}")
        logging.info(f"响应结果：{resp.json()}")
        return resp.json()

    # 报名组局
    @classmethod
    def apply_meeting(cls, token_phone, meeting_id):
        url = f"{config.domain_path}{Yaml_Method.yaml_read(config.api_meeting_app, 'apply')}{meeting_id}"
        head = {
            "User-Agent": "pytest",
            "login_token": Yaml_Method.yaml_read(config.token, token_phone)
        }
        resp = requests.post(url, headers=head)
        logging.info("报名组局-app")
        logging.info(f"请求url：{url}")
        logging.info(f"请求头：{head}")
        logging.info(f"响应结果：{resp.json()}")
        return resp.json()

    # 取消报名组局
    @classmethod
    def cancel_apply(cls, token_phone, meeting_id):
        url = f"{config.domain_path}{Yaml_Method.yaml_read(config.api_meeting_app, 'cancel_apply')}{meeting_id}"
        head = {
            "User-Agent": "pytest",
            "login_token": Yaml_Method.yaml_read(config.token, token_phone)
        }
        resp = requests.post(url, headers=head)
        logging.info("取消报名组局-app")
        logging.info(f"请求url：{url}")
        logging.info(f"请求头：{head}")
        logging.info(f"响应结果：{resp.json()}")
        return resp.json()

    # 报名审核通过
    @classmethod
    def apply_pass(cls, token_phone, apply_list_id):
        url = f"{config.domain_path}{Yaml_Method.yaml_read(config.api_meeting_app, 'apply_pass')}{apply_list_id}"
        head = {
            "User-Agent": "pytest",
            "login_token": Yaml_Method.yaml_read(config.token, token_phone)
        }
        resp = requests.post(url, headers=head)
        logging.info("报名审核通过-app")
        logging.info(f"请求url：{url}")
        logging.info(f"请求头：{head}")
        logging.info(f"响应结果：{resp.json()}")
        return resp.json()

    # 报名审核拒绝
    @classmethod
    def apply_reject(cls, token_phone, apply_list_id):
        url = f"{config.domain_path}{Yaml_Method.yaml_read(config.api_meeting_app, 'apply_reject')}{apply_list_id}"
        head = {
            "User-Agent": "pytest",
            "login_token": Yaml_Method.yaml_read(config.token, token_phone)
        }
        resp = requests.post(url, headers=head)
        logging.info("报名审核拒绝-app")
        logging.info(f"请求url：{url}")
        logging.info(f"请求头：{head}")
        logging.info(f"响应结果：{resp.json()}")
        return resp.json()

    # 获取审核列表
    @classmethod
    def get_audit_list(cls, token_phone, meeting_id, state):
        url = f"{config.domain_path}{Yaml_Method.yaml_read(config.api_meeting_app, 'get_audit_list')}"
        head = {
            "User-Agent": "pytest",
            "login_token": Yaml_Method.yaml_read(config.token, token_phone)
        }
        query = {
            "meetingId": meeting_id,
            "pageNum": 1,
            "relateStatus": state
        }
        resp = requests.get(url, headers=head, params=query)
        if len(resp.json().get("data").get("data")) > 0:
            apply_id = resp.json().get("data").get("data")[0].get("id")
            Yaml_Method.yaml_write(config.token, {"apply_list_id": apply_id})
        logging.info("获取审核列表-app")
        logging.info(f"请求url：{url}")
        logging.info(f"请求头：{head}")
        logging.info(f"响应结果：{resp.json()}")
        return resp.json()

    # 获取我发布的组局列表
    @classmethod
    def get_my_send_meeting_list(cls, token_phone, state):
        url = f"{config.domain_path}{Yaml_Method.yaml_read(config.api_meeting_app, 'get_my_send_meeting_list')}"
        head = {
            "User-Agent": "pytest",
            "login_token": Yaml_Method.yaml_read(config.token, token_phone)
        }
        query = {
            "meetingAddressLongitude": 1,
            "meetingAddressLatitude": 1,
            "meetingStatus": {state}
        }
        resp = requests.get(url, headers=head, params=query)
        logging.info("获取我发布的组局列表-app")
        logging.info(f"请求url：{url}")
        logging.info(f"请求头：{head}")
        logging.info(f"响应结果：{resp.json()}")
        return resp.json()

    # 获取我报名的组局列表
    @classmethod
    def get_my_apply_meeting_list(cls, token_phone, apply_state):
        url = f"{config.domain_path}{Yaml_Method.yaml_read(config.api_meeting_app, 'get_my_apply_meeting_list')}"
        head = {
            "User-Agent": "pytest",
            "login_token": Yaml_Method.yaml_read(config.token, token_phone)
        }
        query = {
            "meetingAddressLongitude": 1,
            "meetingAddressLatitude": 1,
            "meetingStatus": {apply_state}
        }
        resp = requests.get(url, headers=head, params=query)
        logging.info("获取我报名的组局列表-app")
        logging.info(f"请求url：{url}")
        logging.info(f"请求头：{head}")
        logging.info(f"响应结果：{resp.json()}")
        return resp.json()

    # 获取邀请我的列表
    @classmethod
    def get_my_invite_meeting_list(cls, token_phone, invite_state):
        url = f"{config.domain_path}{Yaml_Method.yaml_read(config.api_meeting_app, 'get_my_invite_meeting_list')}"
        head = {
            "User-Agent": "pytest",
            "login_token": Yaml_Method.yaml_read(config.token, token_phone)
        }
        query = {
            "meetingAddressLongitude": 1,
            "meetingAddressLatitude": 1,
            "meetingStatus": {invite_state}
        }
        resp = requests.get(url, headers=head, params=query)
        logging.info("获取邀请我的组局列表-app")
        logging.info(f"请求url：{url}")
        logging.info(f"请求头：{head}")
        logging.info(f"响应结果：{resp.json()}")
        return resp.json()

    # 获取组局详情
    @classmethod
    def get_details(cls, token_phone, meeting_id):
        url = f"{config.domain_path}{Yaml_Method.yaml_read(config.api_meeting_app, 'get_details')}{meeting_id}"
        head = {
            "User-Agent": "pytest",
            "login_token": Yaml_Method.yaml_read(config.token, token_phone)
        }
        resp = requests.get(url, headers=head)
        logging.info("获取组局详情-app")
        logging.info(f"请求url：{url}")
        logging.info(f"请求头：{head}")
        logging.info(f"响应结果：{resp.json()}")
        return resp.json()

    # 查询今日已约局
    @classmethod
    def search_meeting(cls, token_phone):
        url = f"{config.domain_path}{Yaml_Method.yaml_read(config.api_meeting_app, 'search_meeting')}"
        head = {
            "User-Agent": "pytest",
            "login_token": Yaml_Method.yaml_read(config.token, token_phone)
        }
        resp = requests.post(url, headers=head)
        logging.info("查询今日已约局-app")
        logging.info(f"请求url：{url}")
        logging.info(f"请求头：{head}")
        logging.info(f"响应结果：{resp.json()}")
        return resp.json()

    # 有局打赏
    @classmethod
    def meeting_give_money(cls, token_phone, body):
        url = f"{config.domain_path}{Yaml_Method.yaml_read(config.api_meeting_app, 'meeting_give_money')}"
        head = {
            "User-Agent": "pytest",
            "login_token": Yaml_Method.yaml_read(config.token, token_phone)
        }
        resp = requests.post(url, headers=head, json=body)
        logging.info("有局打赏-app")
        logging.info(f"请求url：{url}")
        logging.info(f"请求头：{head}")
        logging.info(f"响应结果：{resp.json()}")
        return resp.json()
