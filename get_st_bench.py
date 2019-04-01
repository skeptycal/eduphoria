#!/usr/bin/env python3
# -*- encoding: utf-8 -*-
""" module get_st_bench

    collect and return formatted student data from Eduphoria

    Account and login required
    https://victoria.schoolobjects.com/eduphoria_webcontrols/Login.aspx?ReturnUrl=%2feduphoria_webcontrols%2fApplications.aspx
    """
# import operator
import re
# from collections import Counter
from typing import AnyStr  #, List, Dict

from bs4 import BeautifulSoup
import requests
from requests.exceptions import HTTPError

BG_COLOR: AnyStr = "[48;5;230m"
HEADER: AnyStr = "[38;5;18m" + BG_COLOR
BLUE: AnyStr = "[38;5;27m" + BG_COLOR
PURPLE: AnyStr = "[38;5;92m" + BG_COLOR
RESET: AnyStr = "[0m"


def call_get(url: str) -> requests.Response:
    """[call_get - requests GET wrapper with error checking]

    Arguments:
        url {str} -- [url to get]

    Returns:
        requests.Response -- [response to get]
    """
    # for url in ['https://api.github.com', 'https://api.github.com/invalid']:
    try:
        resp: requests.Response = requests.get(url)

        # If the response was successful, no Exception will be raised
        resp.raise_for_status()
    except HTTPError as http_err:
        print(f'HTTP error occurred: {http_err}')  # Python 3.6
    except Exception as err:  # pylint: disable=broad-except
        print(f'Other error occurred: {err}')  # Python 3.6
    else:
        print('Success!')


def get_test(test_url: AnyStr, test_color: AnyStr) -> requests.Response:
    """[uses requests.get to get information from url]

    Arguments:
        test_url {AnyStr} -- [url to get]
        test_color {AnyStr} -- [highlight color]

    Returns:
        resp -- [requests module response]
    """
    resp: requests.Response = requests.get(test_url)
    resp_code: int = resp.status_code
    print(test_color, "Module Requests Get Test: ", test_url)
    print(test_color, "Status code: ", RESET, resp_code)
    if resp_code == 200:
        print(test_color, "Apparent Encoding: ", RESET, resp.apparent_encoding)
        # print(test_color, "Text: ", RESET, resp.text)
        # print(test_color, "Content:", RESET, resp.content)
        stripped: str = re.sub('<[^<]+?>', '', resp.text)
        print(test_color, "Stripped: ", RESET, stripped)
        print(test_color, "Lines: ", RESET, resp.text.splitlines()[0])
    else:
        print("error code: ", resp_code)
    return resp


if __name__ == "__main__":
    # ? TEST to use if script is run from the command line
    # ! html test
    # response = get_test('https://www.google.com', PURPLE)
    # ! json test
    # response = get_test('https://jsonplaceholder.typicode.com/todos/1', BLUE)

    url: str = 'https://victoria.schoolobjects.com/aware/Analysis/TEAnalysis/ViewListGenerator.aspx?all=3449'

    headers: dict = {"content-type": "text"}

    r = requests.get(url, headers)

    print("Response Status Code: ", r.status_code)
    print("Apparent Encoding: ", r.apparent_encoding)
    print("Text: ", r.text)

    # response = get_test(eduphoria_page, BLUE)

    # response = reqs.get(eduphoria_page)
    # r=requests.get("http://www.example.com/", headers={"content-type":"text"})
