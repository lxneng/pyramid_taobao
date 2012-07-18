# -*- coding: utf-8 -*-
import requests
import time
import md5


class Taobao(object):

    def __init__(self, app_key, sercet_code):
        self.app_key = app_key
        self.sercet_code = sercet_code

    def get_time(self):
        t = time.localtime()
        return time.strftime('%Y-%m-%d %H:%M:%S', t)

    def get_sign(self, params):
        params.update({'app_key': self.app_key, 'timestamp': self.get_time(),
            'v': '2.0'})
        src = self.sercet_code + ''.join(["%s%s" % (k, v)\
                for k, v in sorted(params.iteritems())])
        return md5.new(src).hexdigest().upper()

    def get_result(self, params):
        params['sign'] = self.get_sign(params)
        rsp = requests.get('http://gw.api.taobao.com/router/rest',
                params=params)
        return rsp.content


def includeme(config):
    settings = config.registry.settings
    config.registry['taobao'] = Taobao(
        app_key=settings.get('taobao.app_key'),
        sercet_code=settings.get('taobao.sercet_code'))
