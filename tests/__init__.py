#!/usr/bin/python
# -*- coding: utf-8 -*-

'''
© 2016 I-Value Tecnologia
Authored by: Armando Miani
Licensed under CDDL 1.0
'''

import sys
import unittest
import doctest


class MyTest(unittest.TestCase):
    def test(self):
        self.assertEqual(1, 2)


def getTestSuite():
    suite = unittest.TestSuite()
    suite.addTest(unittest.makeSuite(MyTest))

    # suite.addTest(doctest.DocTestSuite(class))

    return suite

runner = unittest.TextTestRunner()
runner.run(getTestSuite())
