#!/usr/bin/python
# -*- coding: utf-8 -*-

'''
© 2016 I-Value Tecnologia
Authored by: Armando Miani
Licensed under CDDL 1.0
'''

import unittest
import doctest
import matrixsdk.api


def getTestSuite():
	suite = unittest.TestSuite()
	suite.addTest(doctest.DocTestSuite(matrixsdk.api))
	return suite

runner = unittest.TextTestRunner()
runner.run(getTestSuite())
