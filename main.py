from concurrent.futures.thread import ThreadPoolExecutor
import random
import json
from fastapi.responses import PlainTextResponse
from fastapi import FastAPI, Request, BackgroundTasks
from fastapi.responses import HTMLResponse
import requests
from datetime import datetime
import json
import concurrent.futures
from fastapi.responses import FileResponse

app = FastAPI(docs_url=None, redoc_url=None, openapi_url=None)


@app.get("/num/verify/{num}/{msg}/{deviceid}" , response_class=PlainTextResponse)
async def cusapicallkrishi(num, msg , deviceid):
    try:
        headers = {
            'Host': 'thekrishi.com',
            'Accept': 'application/json;charset=UTF-8',
            'Content-Type': 'multipart/form-data; boundary=f32dd0bf-ca26-4be6-9d71-5652a6eee3cb',
            # 'Content-Length': '1202',
            # 'Accept-Encoding': 'gzip, deflate, br',
            'User-Agent': 'okhttp/4.9.0',
            'Connection': 'close',
        }

        params = {
            'lang': 'en',
            'ver': '296',
            'android_id': f'{deviceid}',
        }

        data = f'--f32dd0bf-ca26-4be6-9d71-5652a6eee3cb\r\nContent-Disposition: form-data; name="name"\r\nContent-Transfer-Encoding: binary\r\nContent-Type: text/plain; charset=UTF-8\r\nContent-Length: 4\r\n\r\ntera\r\n--f32dd0bf-ca26-4be6-9d71-5652a6eee3cb\r\nContent-Disposition: form-data; name="country_code"\r\nContent-Transfer-Encoding: binary\r\nContent-Type: text/plain; charset=UTF-8\r\nContent-Length: 2\r\n\r\n91\r\n--f32dd0bf-ca26-4be6-9d71-5652a6eee3cb\r\nContent-Disposition: form-data; name="phone_no"\r\nContent-Transfer-Encoding: binary\r\nContent-Type: text/plain; charset=UTF-8\r\nContent-Length: 10\r\n\r\n{num}\r\n--f32dd0bf-ca26-4be6-9d71-5652a6eee3cb\r\nContent-Disposition: form-data; name="source"\r\nContent-Transfer-Encoding: binary\r\nContent-Type: text/plain; charset=UTF-8\r\nContent-Length: 7\r\n\r\nandroid\r\n--f32dd0bf-ca26-4be6-9d71-5652a6eee3cb\r\nContent-Disposition: form-data; name="count"\r\nContent-Transfer-Encoding: binary\r\nContent-Type: text/plain; charset=UTF-8\r\nContent-Length: 1\r\n\r\n1\r\n--f32dd0bf-ca26-4be6-9d71-5652a6eee3cb\r\nContent-Disposition: form-data; name="sms_hash"\r\nContent-Transfer-Encoding: binary\r\nContent-Type: text/plain; charset=UTF-8\r\nContent-Length: 15\r\n\r\n{msg}\r\n--f32dd0bf-ca26-4be6-9d71-5652a6eee3cb--\r\n'
        esponse = requests.post('https://thekrishi.com/v2/otp/get', params=params, headers=headers,
                                 data=data)
        response = esponse.json()
        print(response)
        out = response["status"]
        if out == "success":
            return "success"
        else:
            return "fail"

    except Exception as e:

        return "fail"
