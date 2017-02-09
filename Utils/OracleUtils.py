# coding: utf-8
import cx_Oracle
from DBUtils.PooledDB import PooledDB

from Configs import config


class OracleUtils:
    _db_pool_log = None
    _connection = None


    def __init__(self):
        pass

    @staticmethod
    def initialize_connection_pool():
        OracleUtils._db_pool_log = PooledDB(cx_Oracle, user=config.CURRENT_CONFIG['DB_CONFIG_JOURNALLOG']['USER_NAME'],
                                            password=config.CURRENT_CONFIG['DB_CONFIG_JOURNALLOG']['PASSWORD'],
                                            dsn=config.CURRENT_CONFIG['DB_CONFIG_JOURNALLOG']['DSN'],
                                            mincached=config.CURRENT_CONFIG['DB_CONFIG_JOURNALLOG']['MIN'],
                                            maxcached=config.CURRENT_CONFIG['DB_CONFIG_JOURNALLOG']['MAX'],
                                            maxconnections=config.CURRENT_CONFIG['DB_CONFIG_JOURNALLOG']['MAXCONNECTIONS'],
                                            threaded=True)

    @staticmethod
    def get_db_connection():
        """
        获取数据库连接
        :return: connection对象
        """
        if OracleUtils._connection is None:
            OracleUtils._connection = OracleUtils._db_pool_log.connection()
        return OracleUtils._connection

    @staticmethod
    def release_resources(conn, cursor):
        """
        释放资源
        :param cursor:
        :param conn:
        :return:
        """
        if hasattr(cursor, 'close'):
            cursor.close()
        if hasattr(conn, 'close'):
            conn.close()
            OracleUtils._connection = None
