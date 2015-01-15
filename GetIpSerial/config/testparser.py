__author__ = 'gong'
from simpleconfigparser import simpleconfigparser

config = simpleconfigparser()
config.read('config.ini')

print(config.setting.WaitTime)


