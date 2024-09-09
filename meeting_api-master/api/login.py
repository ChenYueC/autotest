import requests
import config
from method.yaml_tools import Yaml_Method


def login_token(phone):
    # 获取短信验证码
    url_code = config.domain_path + Yaml_Method.yaml_read(config.api_login_path, "code")
    head = Yaml_Method.yaml_read(config.api_login_path, "header")
    code_body = {
        "account": phone
    }
    requests.post(url_code, headers=head, json=code_body)

    # 登录账户、获取token
    url_login = config.domain_path + Yaml_Method.yaml_read(config.api_login_path, "login")
    login_body = {
        "code": "1234",
        "account": phone
    }
    resp_token = requests.post(url_login, headers=head, json=login_body)
    print(resp_token.json())
    token = {{phone}: resp_token.json().get('data')}
    Yaml_Method.yaml_write(config.token, token)
