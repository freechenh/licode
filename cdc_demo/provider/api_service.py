#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @File: api_service.py
# @Author: dell
# @Date: 2021/1/18  15:47
# @Desc: 
# @Project: licode
# @Source: PyCharm


from flask import Flask, request, jsonify

app = Flask(__name__)
app.config['JSON_SORT_KEYS'] = False

rsp_body = [
    {
        "salary": 45000,
        "name": "Hatsune Miku",
        "nationality": "Japan",
        "contact": {
            "Email": "hatsune.miku@woniuxy.com",
            "Phone Numbe": "13900110001"
        }
    }, {
        "salary": 80000,
        "name": "Takamachi Nanoha",
        "nationality": "Japan",
        "contact": {
            "Email": "takamachi.nanoha@woniuxy.com",
            "Phone Number": "18800880008"
        }
    }
]


@app.route('/information', methods=['GET'])
def test():
    get_name = request.args.get("name", "").lower()
    if get_name == 'miku':
        rsp = jsonify(rsp_body[0])
    elif get_name == 'nanoha':
        rsp = jsonify(rsp_body[1])
    else:
        rsp = jsonify({'status': '404 not found.'})
    return rsp


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=1237)
