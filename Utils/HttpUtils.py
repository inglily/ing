# coding:utf-8

import simplejson as json
# import logging
import logging.config
import unirest
import Configs.Log as LogConfig

logging.config.dictConfig(LogConfig.LOGGING_CONFIG)
logger = logging.getLogger('default')


def post_json(url, post_data):
    """
    调用接口成功返回0和body
    若调用接口失败返回1和错误描述
    若调用接口成功bady为None 则返回2和None
    :param url:
    :param post_data:
    :return:
    """
    try:
        logger.debug('调用接口 %s,请求数据 = %s', url, json.dumps(post_data))
        prov_result = unirest.post(url, params=json.dumps(post_data))
        if prov_result is not None:
            body = json.loads(prov_result.raw_body)
            error_code = 0
            logger.debug('获取接口 %s 返回消息= %s ', url, prov_result.raw_body)
        else:
            error_code = 2
            body = None
    except Exception, e:
        error_code = 1
        error_desc = '调用接口%s,请求数据%s, 异常=%s' % (url, post_data, e.message)
        logger.error(error_desc)
        return error_code, error_desc
    return error_code, body


def get_send(url, **post_data):
    """
    调用接口成功返回0和body
    若调用接口失败返回1和错误描述
    若调用接口成功bady为None 则返回2和None
    :param url:
    :param post_data:
    :return:
    """
    try:
        logger.debug('调用接口 %s,请求数据 = %s', url, post_data)
        if post_data:
            prov_result = unirest.get(url, **post_data)
        else:
            prov_result = unirest.get(url)
        if prov_result is not None:
            body = json.loads(prov_result.raw_body)
            error_code = 0
            logger.debug('获取接口 %s 返回消息= %s ', url, prov_result.raw_body)
        else:
            error_code = 2
            body = None
    except Exception, e:
        error_code = 1
        error_desc = '调用接口%s,请求数据%s, 异常=%s' % (url, post_data, e.message)
        logger.error(error_desc)
        return error_code, error_desc
    return error_code, body


def post_xml(url, xml_data):
    """
    发送post请求数据在body里面
    :param url:
    :param xml_data:
    :return:
    """
    try:
        logger.debug('调用接口 %s,请求数据 = %s', url, xml_data)
        prov_result = unirest.post(url, params=xml_data, headers={'content-type': "application/xml"})
        if prov_result is not None:
            body = prov_result.raw_body
            error_code = 0
            logger.debug('获取接口 %s 返回消息= %s ', url, prov_result.raw_body)
        else:
            error_code = 2
            body = None
    except Exception as e:
        error_desc = '调用接口%s,请求数据%s, 异常=%s' % (url, xml_data, e.message)
        logger.exception(error_desc, e)
        raise e
    return error_code, body


if __name__ == '__main__':
    pass
