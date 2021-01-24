#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @File: consumer_nanoha.py
# @Author: dell
# @Date: 2021/1/18  15:47
# @Desc: 
# @Project: licode
# @Source: PyCharm


from flask import Flask, request, jsonify, render_template
import urllib3
import json

app = Flask(__name__)


@app.route('/nanoha', methods=['GET'])
def nanoha_html():
    params = {"name": "nanoha"}
    http = urllib3.PoolManager()
    resp = http.request('GET', 'http://localhost:1237/information', params)
    result = json.loads(resp.data.decode())
    return render_template("nanoha.html", result=result)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=1236)
