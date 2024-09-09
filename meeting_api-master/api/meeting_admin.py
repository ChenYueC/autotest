import requests
import config
from method.read_write_tools import Yaml_Method
import redis
import logging


class Admin_Meeting_Api:
    # 获取token
    @classmethod
    def get_admin_token(cls):
        pool = redis.ConnectionPool(host='192.168.110.52', password='root')
        r = redis.Redis(connection_pool=pool)
        token = {"admin_token": r.get('ALL:ADMIN:TOKEN:1545658878631374850').decode('utf8').strip('"')}
        Yaml_Method.yaml_write(config.token, token)
        logging.info(f"读取redis存储token,写入yaml文件：{token}")

    # 获取组局详情
    @classmethod
    def get_meeting_info(cls, token, meeting_id):
        url = f"{config.domain_path}{Yaml_Method.yaml_read(config.api_meeting_admin, 'get_meeting_info')}{meeting_id}"
        head = {
            "User-Agent": "pytest",
            "login_token": token
        }
        resp = requests.get(url, headers=head)
        logging.info("获取组局详情-admin")
        logging.info(f"请求url：{url}")
        logging.info(f"请求头：{head}")
        logging.info(f"响应结果：{resp.json()}")
        return resp.json()

    # 获取组局列表
    @classmethod
    def get_meeting_list(cls, token):
        url = f"{config.domain_path}{Yaml_Method.yaml_read(config.api_meeting_admin, 'get_meeting_list')}"
        head = {
            "User-Agent": "pytest",
            "login_token": token
        }
        resp = requests.get(url, headers=head)
        logging.info("获取组局列表-admin")
        logging.info(f"请求url：{url}")
        logging.info(f"请求头：{head}")
        logging.info(f"响应结果：{resp.json()}")
        return resp.json()

    # 报名审核通过
    @classmethod
    def apply_pass(cls, token, apply_list_id):
        url = f"{config.domain_path}{Yaml_Method.yaml_read(config.api_meeting_admin, 'apply_pass')}{apply_list_id}"
        head = {
            "User-Agent": "pytest",
            "login_token": token
        }
        resp = requests.post(url, headers=head)
        logging.info("报名审核通过-admin")
        logging.info(f"请求url：{url}")
        logging.info(f"请求头：{head}")
        logging.info(f"响应结果：{resp.json()}")
        return resp.json()

    # 报名审核拒绝
    @classmethod
    def apply_reject(cls, token, apply_list_id):
        url = f"{config.domain_path}{Yaml_Method.yaml_read(config.api_meeting_admin, 'apply_reject')}{apply_list_id}"
        head = {
            "User-Agent": "pytest",
            "login_token": token
        }
        resp = requests.post(url, headers=head)
        logging.info("报名审核拒绝-admin")
        logging.info(f"请求url：{url}")
        logging.info(f"请求头：{head}")
        logging.info(f"响应结果：{resp.json()}")
        return resp.json()

    # 设置精彩组局
    @classmethod
    def set_good_meeting(cls, token, meeting_id, t_or_f):
        url = f"{config.domain_path}{Yaml_Method.yaml_read(config.api_meeting_admin, 'set_good_meeting')}{meeting_id}"
        head = {
            "User-Agent": "pytest",
            "login_token": token
        }
        body = {
            "good": t_or_f
        }
        resp = requests.post(url, headers=head, json=body)
        logging.info("设置精彩组局-admin")
        logging.info(f"请求url：{url}")
        logging.info(f"请求头：{head}")
        logging.info(f"响应结果：{resp.json()}")
        return resp.json()

    # 推荐组局
    @classmethod
    def recommend_meeting(cls, token, meeting_id, body):
        url = f"{config.domain_path}{Yaml_Method.yaml_read(config.api_meeting_admin, 'recommend_meeting')}{meeting_id}"
        head = {
            "User-Agent": "pytest",
            "login_token": token
        }
        resp = requests.post(url, headers=head, json=body)
        logging.info("推荐组局-admin")
        logging.info(f"请求url：{url}")
        logging.info(f"请求头：{head}")
        logging.info(f"响应结果：{resp.json()}")
        return resp.json()

    # 组局报名注水
    @classmethod
    def meeting_fake(cls, token, meeting_id, num):
        url = f"{config.domain_path}{Yaml_Method.yaml_read(config.api_meeting_admin, 'meeting_fake')}{meeting_id}"
        head = {
            "User-Agent": "pytest",
            "login_token": token
        }
        body = {
            "fakerSignUpCount": num
        }
        resp = requests.post(url, headers=head, json=body)
        logging.info("组局访客注水-admin")
        logging.info(f"请求url：{url}")
        logging.info(f"请求头：{head}")
        logging.info(f"响应结果：{resp.json()}")
        return resp.json()
