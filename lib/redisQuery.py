# coding:utf-8
import redis
import time
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

class OprRedis(object):

    def __init__(self,host,port,db):
        try:
            pool=redis.ConnectionPool(host=host,port=port,db=db)
            self.rconnection=redis.Redis(connection_pool=pool)
        except Exception as e:
            print e
            sys.exit(-1)
    def get(self,name):
        """获取key对应的value值"""
        return self.rconnection.get(name)

    def get_smembers(self,name):
        return self.rconnection.smembers(name)

    def get_hget(self,name,key):
        return self.rconnection.hget(name,key)

    def get_hkeys(self,name):
        return self.rconnection.hkeys(name)

    def get_zrange(self,name,start,end,desc=False,withscores=False,score_cast_func=float):
        """获取有序集合的值"""
        return self.rconnection.zrange(name,start,end,desc=desc,withscores=withscores,score_cast_func=score_cast_func)

if __name__ == '__main__':
    opr=OprRedis('172.16.100.210',6379,0)
    print opr.get("HY_TOTAL_IN_SALE")

    print opr.get_zrange("HY_ASSIGNMENT",0,1,withscores=True)


