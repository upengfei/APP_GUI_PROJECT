# -*- coding:utf-8 -*-
import time

from behave import *
from func import conf_read
from func import PySelenium


@Given("Access qyd website")
def open_qyd(context):
    context.ps = PySelenium.PySelenium()
    context.ps.open_url("http://www.qingyidai.com")
    context.ps.window_max()
    context.ps.click_text(u'用户登录')


@When("input {username} and {password}")
def qyd_login(context, username, password):
    context.ps.input_type('css=>#username', username)

    context.ps.input_type('css=>#password', password)
    context.ps.click('css=>#login')
    time.sleep(3)


@Then("sucess login the website")
def browser_close(context):
    context.ps.quit()


