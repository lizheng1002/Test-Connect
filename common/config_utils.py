#!/usr/bin/env python
# encoding: utf-8
# @author: liusir
# @file: config_utils.py
# @time: 2020/10/14 9:02 下午

import os
import configparser


config_file_path = os.path.join( os.path.dirname(__file__) ,'../config/localconfig.ini' )

class ConfigUtils:
    def __init__(self,conf_path = config_file_path):
        self.cfg = configparser.ConfigParser()
        self.cfg.read( conf_path )

    @property   # 类中的一个方法加property这个装饰器 属性方法
    def HOSTS(self):
        hosts_value = self.cfg.get('default','HOSTS')
        return hosts_value

    @property
    def REPORT_PATH(self):
        report_path_value = self.cfg.get('default','REPORT_PATH')
        return report_path_value

    @property
    def LOG_PATH(self):
        log_path_value = self.cfg.get('default','LOG_PATH')
        return log_path_value

    @property
    def LOG_LEVEL(self):
        log_level_value = int(self.cfg.get('default','LOG_LEVEL'))
        return log_level_value

    @property
    def SMTP_RECEIVER(self):
        smtp_receiver_value = self.cfg.get('default', 'SMTP_RECEIVER')
        return smtp_receiver_value


configs = ConfigUtils()
if __name__ == '__main__':
    print( type(configs.LOG_LEVEL) )