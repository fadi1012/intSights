# -*- coding: UTF-8 -*-
import json

import requests

from test.src.intsight_test.test_infra.exceptions.http_exception import HttpException

HTTP_REQUEST_TIMEOUT = 120


class HttpClient:
    def __init__(self):
        self.session = requests.Session()
        self.session.verify = False

    def send_request(self, req_dict):
        req = requests.Request(**req_dict)
        resp = self.session.send(self.session.prepare_request(req), timeout=HTTP_REQUEST_TIMEOUT)

        if resp.ok:
            try:
                resp.resp_data = resp.json()
            except Exception:
                resp.resp_data = {}
        else:
            text_dict = json.loads(resp.text)
            if 'error_text' in text_dict and "User unauthorized to make this request" in text_dict['error_text']:
                raise HttpException(status_code=text_dict['status_code'] if 'status_code' in text_dict else resp.status_code,
                                    error_id=text_dict['error_id'] if 'error_id' in text_dict else None, error_text=text_dict['error_text'] if 'error_text' in text_dict else resp.text,
                                    original_error_text=text_dict['original_error_text'] if 'original_error_text' in text_dict else None)
        return resp

    def post(self, url, data, params={}, headers={}, cookies={}):
        if 'Content-Type' not in headers:
            headers['Content-Type'] = 'application/json;charset=UTF-8'
            data = json.dumps(data)
        req = dict(url=url, method='POST', params=params, data=data, headers=headers, cookies=cookies)
        # return self.send_request(req).resp_data
        resp = self.send_request(req)
        return resp.resp_data

    def patch(self, url, data, params={}, headers={}, cookies={}):
        if 'Content-Type' not in headers:
            headers['Content-Type'] = 'application/json;charset=UTF-8'
            data = json.dumps(data)
        req = dict(url=url, method='PATCH', params=params, data=data, headers=headers, cookies=cookies)
        # return self.send_request(req).resp_data
        resp = self.send_request(req)
        return resp.resp_data

    def get(self, url, params={}, headers={}, cookies={}, return_resp_data=True):
        req = dict(url=url, method='GET', params=params, headers=headers, cookies=cookies)
        if 'Content-Type' not in headers:
            headers['Content-Type'] = 'application/json;charset=UTF-8'
        if return_resp_data:
            return self.send_request(req).resp_data
        return self.send_request(req)

    def delete(self, url, params={}, headers={}, cookies={}):
        req = dict(url=url, method='DELETE', params=params, headers=headers, cookies=cookies)
        return self.send_request(req).resp_data

    def put(self, url, data, params={}, headers={}, cookies={}):
        req = dict(url=url, method='PUT', data=json.dumps(data), params=params, headers=headers, cookies=cookies)
        return self.send_request(req).resp_data
