# coding=utf-8
import ConfigParser


def get_config():
    configParser = ConfigParser.RawConfigParser()
    configFilePath = r'config.ini'
    configParser.read(configFilePath)
    return configParser