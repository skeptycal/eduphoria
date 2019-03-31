#!/usr/bin/env python3
# -*- encoding: utf-8 -*-
""" module get_st_bench

    collect and return formatted student data from Eduphoria

    Account and login required
    https://victoria.schoolobjects.com/eduphoria_webcontrols/Login.aspx?ReturnUrl=%2feduphoria_webcontrols%2fApplications.aspx
    """

from typing import AnyStr  # , List, Dict
import requests as r
import markdown as m

eduphoria_page: AnyStr = 'https://victoria.schoolobjects.com/eduphoria_webcontrols/Login.aspx?ReturnUrl=%2feduphoria_webcontrols%2fApplications.aspx'

# ! html test
url: AnyStr = 'https://www.google.com'
response = r.get(url)
print(m.markdown(response.apparent_encoding))
print(m.markdown(response.text))

# ! json test
url = 'https://jsonplaceholder.typicode.com/todos/1'
response = r.get(url)  # execute get request
print("Get: ", url)
print("Status code: ", response.status_code)  # print http response code
print("Text: ", response.text)  # print formatted JSON response
print("Content: ", response.content)  # print 'content'

url = eduphoria_page

# response = reqs.get(eduphoria_page)
