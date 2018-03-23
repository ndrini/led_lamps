# -*- coding: utf-8 -*-

import unittest
import led_lamps as ll

class TestStringMethods(unittest.TestCase):

    """
    def test_upper(self):
        self.assertEqual('foo'.upper(), 'FOO')

    def test_isupper(self):
        self.assertTrue('FOO'.isupper())
        self.assertFalse('Foo'.isupper())
	"""
    def test_lamp(self):
        # https://www.xatakahome.com/iluminacion-y-energia/cuanto-podemos-ahorrar-realmente-con-la-iluminacion-led-especial-iluminacion-led
        lamp_single = ll.illumination({"power": 60., "number":1., "cost":.0}) 
        value = lamp_single.consumption_monthly(days_in_month=31)
        self.assertEqual(value ,  11.16 ) 

        # camera laia 3; matrimoniale 5; studio 3; corridoio 4; salotto 5; bagno 3. 
        # 23 luci da 50 W
        lamp_gandhi = ll.illumination({"power": 50., "number":23., "cost":.8}) 
        value = lamp_gandhi.consumption_monthly(hours=2, days_in_month=30, ) # report=True)
        self.assertEqual(value ,  69.0 ) 

    def test_thrift(self):
        # camera laia 3; matrimoniale 5; studio 3; corridoio 4; salotto 5; bagno 3. 
        # 23 luci da 50 W
        # lamp_single_inc = {"power": 60., "number":1.}
        lamp_single_inc = ll.illumination({"power": 60., "number":1., "cost":.0})
        #lamp_single_led = {"power": 60., "number":1.} 
        lamp_single_led = ll.illumination({"power":  7., "number":1., "cost":.8}) 
        ill_dic = {"pre": lamp_single_inc, "post": lamp_single_led,}

        # print type((ill_dic["pre"]))
        month_thrift = ll.thrift(ill_dic)
        self.assertAlmostEqual( month_thrift.money(hours=6, kW_h_price=0.17,), 1.68, 2)


        lamp_gandhi_halogen = ll.illumination({"power": 50., "number":23., "cost":.0}) 
        lamp_gandhi_led 	= ll.illumination({"power":  5., "number":23., "cost":1.3}) 
        ill_dic = {"pre": lamp_gandhi_halogen, "post": lamp_gandhi_led,}
        month_thrift_gandhi = ll.thrift(ill_dic)
        self.assertAlmostEqual( month_thrift_gandhi.money(hours=1.5, kW_h_price=0.12,), 5.78, 2)
       
    def test_thrift_ROI(self):
    	lamp_gandhi_halogen = ll.illumination({"power": 50., "number":23., "cost":.0}) 
        lamp_gandhi_led 	= ll.illumination({"power":  5., "number":23., "cost":1.3}) 
        ill_dic = {"pre": lamp_gandhi_halogen, "post": lamp_gandhi_led,}
        month_thrift_gandhi = ll.thrift(ill_dic)
        self.assertAlmostEqual( month_thrift_gandhi.ROI(hours=1.5, kW_h_price=0.12,), 5.18, 2)


    	lamp_a = ll.illumination({"power": 33., "number":12., "cost":.0}) 
    	lamp_b = ll.illumination({"power": 33., "number":12., "cost":.0}) 
        ill_dic = {"pre": lamp_a, "post": lamp_b,}
        month_thrift_gandhi = ll.thrift(ill_dic)
        self.assertAlmostEqual( month_thrift_gandhi.ROI(hours=1.5, kW_h_price=0.12,), 0, 2)

 
if __name__ == '__main__':
    unittest.main()

