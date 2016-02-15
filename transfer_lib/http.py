# -*- coding: utf-8 -*-
import urllib2
import codecs
from urllib2 import HTTPError


class HttpFileTransfer(object):
    def __init__(self, domain, user, password, is_ssl=False):
        protocol = 'http'
        if is_ssl:
            protocol = 'https'
        self.__domain = protocol + '://' + domain
        password_mgr = urllib2.HTTPPasswordMgrWithDefaultRealm()
        password_mgr.add_password(None, domain, user, password)
        handler = urllib2.HTTPBasicAuthHandler(password_mgr)
        self.__opener = urllib2.build_opener(handler)

    def get_file(self, file_path, local_file_path, local_file_encode):
        url = self.__domain + file_path
        try:
            res = self.__opener.open(url)
        except HTTPError, err:
            if err.code == 404:
                return
            else:
                raise HTTPError(err.filename, err.code, err.msg, err.hdrs, err.fp)
        result_file = codecs.open(local_file_path, 'wb', local_file_encode)
        for line in res.readlines():
            result_file.write(unicode(line, local_file_encode))
        result_file.close()
