import os
# 获取运行目录
Run_Path = os.path.dirname(os.path.realpath(__file__))

# 域名
domain_path = "http://192.168.110.52/jurenmai"

# token目录
token = f"{Run_Path}/data/token.yaml"

# 登录api
api_login_path = f"{Run_Path}/data/api_login.yaml"

# 有局api---app
api_meeting_app = f"{Run_Path}/data/api_meeting_app.yaml"

# 有局api---admin
api_meeting_admin = f"{Run_Path}/data/api_meeting_admin.yaml"

# 数据存放目录
data_path = f"{Run_Path}/data/"

