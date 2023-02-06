###################################
#      UOF-STATUS-CLIENT-PY       #
# (c) 2023 THE UNIVERSITY OF FOOL #
#   -licensed under MIT license-  #
###################################

import requests
import time

# 回报服务器状态的间隔，以秒为单位
_interval = 60  

# 回报状态类型（只在特殊情况下修改）
_status = True

# 客户端 token
_token = ""

# 客户端 ID
_id = 1

# status 服务器 api 地址
_serverIp = "http://127.0.0.1:4044/api"

##################################


timeStarted = time.time()
counter = 0


def update2server(i, t, s):

    data = {
        "serverId": i,
        "token": t,
        "online": s
    }

    
    try:
        r = requests.post(f"{_serverIp}/status/put", json=data)

        if(r.status_code != 200):
            print(data)
            print(f"在上报数据时发生了错误。code = {r.status_code}")
            print(r.text)
    
    except Exception as e:
        print('发生了内部错误。')
        print(str(e))

# 循环体
while True:
    counter += 1
    print(f"Sending #{counter}, uptime = {time.time()-timeStarted}")
    update2server(_id, _token, _status)
    time.sleep(_interval)
