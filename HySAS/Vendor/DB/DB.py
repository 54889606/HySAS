# -*- coding: utf-8 -*-
"""
# Created on
# @author:
# @contact:
"""
# 以下是自动生成的 #
# --- 导入系统配置
import HySAS.core.util as util
from HySAS.core.Vendor import Vendor
# --- 导入自定义配置
# 以上是自动生成的 #
import pymysql

import redis


class DB(Vendor):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def get_mongodb(self, config="mongodb.json", timeout=1500):
        import os
        if "/" in config:
            cfg = util.read_config(config)
        else:
            cfg = util.read_config(
                os.path.join(os.getcwd(), "config", config)
            )
        host = cfg["host"]
        port = cfg["port"]
        try:
            self.logger.info("尝试连接到Mongodb")
            client = MongoClient(host=host, port=port,
                                 serverSelectionTimeoutMS=timeout,
                                 connect=False
                                 )
            client.server_info()
            self.logger.info("已经成功连接到mongodb")
            return client
        except:
            self.logger.warning(
                ">>>>>>>>>>>>>>>>>>连接到mongodb失败<<<<<<<<<<<<<<<<<<<")
            return False

    def get_redis(self, config="redis.json"):
        import os
        if "/" in config:
            cfg = util.read_config(config)
        else:
            cfg = util.read_config(
                os.path.join(os.getcwd(), "config", config)
            )
        host = cfg["host"]
        port = cfg["port"]

        try:
            self.logger.info("Trying to connect to redis")
            self.redis = redis.StrictRedis(
               # decode_responses=True,
                host=host,
                port=port
            )
            self.redis.client_list()
            return self.redis
        except:
            self.logger.warning("Failed to connect to redis")
            return False
