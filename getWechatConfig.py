#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2017-11-09 16:16:21
# @Author  : Your Name (you@example.org)
# @Link    : http://example.org
# @Version : $Id$
from AppLoggin import logging
from AppConfig import myRedis, redisKey, weChat_api, myWeChat
import redis
import datetime
import time
import requests
import json

smtime = 600
settime = 1800

pool = redis.ConnectionPool(**myRedis)
r = redis.Redis(connection_pool=pool)
print('获取公众号token ticket 脚本启动...')

while True:
    try:
        # 获取token
        check_key_token = r.get(redisKey['token_tmp'])
        # print(check_key_token)
        if not check_key_token:
            token_url = weChat_api['access_token'] % (myWeChat['appID'], myWeChat['appsecret'])
            # logging.info(token_url)

            try:
                token_result = requests.get(token_url, verify=False)
                logging.info('token result: %s' % token_result.text)
                token_res = token_result.json()

                if token_res.get('access_token'):
                    access_token = token_res['access_token'].encode('utf-8')

                    r.set(redisKey['access_token'], access_token)
                    r.set(redisKey['token_tmp'], access_token, settime)
                    check_key_token = access_token

                    logging.info('[INFO] set token %s ' % token_res['access_token'])

            except Exception as e:
                print(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"), '[ERROR] get token. ', str(e))

        # 获取ticket
        check_key_ticket = r.get(redisKey['ticket_tmp'])
        if not check_key_ticket and check_key_token:

            ticket_url = weChat_api['ticket'] % check_key_token.decode('utf-8')
            # logging.info(ticket_url)

            try:
                ticket_result = requests.get(ticket_url, verify=False)
                logging.info('ticket result: %s' % ticket_result.text)
                ticket_res = ticket_result.json()
                if ticket_res.get('ticket'):
                    ticket = ticket_res['ticket'].encode('utf-8')

                    r.set(redisKey['ticket'], ticket)
                    r.set(redisKey['ticket_tmp'], ticket, settime)

                    logging.info('[INFO] set ticket %s ' % ticket_res['ticket'])

            except Exception as e:
                print(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"), '[ERROR] get ticket. ', str(e))

        time.sleep(smtime)
    except Exception as e:
        print(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"), '[ERROR] redis err. ', str(e))
        exit()
