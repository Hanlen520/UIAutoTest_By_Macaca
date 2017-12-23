#!/usr/bin/env python
# -*- coding: utf-8 -*-
import unittest
from Public.BasePage import BasePage
from Public.Decorator import setupclass
from Public.Decorator import teardownclass
from Public.Decorator import setup
from Public.Decorator import teardown
from Public.Decorator import testcase
from macaca import WebDriverException
from App.PageObject.PlatformAppHomePage import PlatformAppHomePage
from App.PageObject.PlatformAppHomePage import back_to_app
from App.PageObject.SafeguardPage import SafeguardPage

class Bootstrap(unittest.TestCase,BasePage):
    @classmethod
    @setupclass
    def setUpClass(cls):
        pass

    @classmethod
    @teardownclass
    def tearDownClass(cls):
        pass

    @setup
    def setUp(self):
        pass

    @teardown
    def tearDown(self):
        pass

    @testcase
    def test01_login(self):
        self.driver.element_by_name('please input username').send_keys('中文+Test+12345678')
        self.driver.element_by_name('please input password').send_keys('111111')
        self.driver.element_by_name('Login').click()
        self.driver.element('name', 'PERSONAL').click()
        self.driver.element('name', 'Logout').click()


    @testcase
    def test02_erroe(self):
        self.driver.element('name', 'Logout').click()

    @testcase
    def testCase1(self):
        self.assertEqual(2, 4, "testError")


    @testcase
    def testCase2(self):
        self.assertEqual(3, 5, "testError")

    @testcase
    def testCase3(self):
        self.assertEqual(5, 5, "测试错误")
        print('这是一个打印的文字行')

    @testcase
    def testCase4(self):
        self.assertEqual(1, 1, "测试错误")


