from selenium import webdriver
import requests, time, json, re
from datetime import datetime, timedelta
from time import sleep
from lxml import etree
import socket
from hashlib import sha1
import hashlib

driver=""

def run(option):
    driver = webdriver.Chrome(options=option)
    return driver

if __name__ == '__main__':
    option = webdriver.ChromeOptions()
    option.add_argument(r"user-data-dir=C:\Users\Administrator\AppData\Local\Google\Chrome\User Data")  # 浏览器路径
    driver=run(option)
