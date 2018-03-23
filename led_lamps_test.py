# -*- coding: utf-8 -*-

import unittest
import led_lamps as ll

class TestStringMethods(unittest.TestCase):

    def setUp(self):
        self.lamp_single_inc = ll.illumination({"power": 60., "number":1., "cost":.0})
        self.lamp_single_led = ll.illumination({"power":  7., "number":1., "cost":.8}) 

        self.lamps_g_halogen = ll.illumination({"power": 50., "number":23., "cost":.0}) 
        self.lamps_g_led 	= ll.illumination({"power":  5., "number":23., "cost":1.3}) 

    def test_lamp(self):
        # https://www.xatakahome.com/iluminacion-y-energia/cuanto-podemos-ahorrar-realmente-con-la-iluminacion-led-especial-iluminacion-led
        value = self.lamp_single_inc.consumption_monthly(days_in_month=31)
        self.assertEqual(value ,  11.16 ) 

        lamp_gandhi = ll.illumination({"power": 50., "number":23., "cost":.8}) 
        value = lamp_gandhi.consumption_monthly(hours=2, days_in_month=30, ) # report=True)
        self.assertEqual(value ,  69.0 ) 

    def test_thrift(self):
        ill_dic = {"pre": self.lamp_single_inc, "post": self.lamp_single_led,}
        month_thrift = ll.thrift(ill_dic)
        self.assertAlmostEqual( month_thrift.money(hours=6, kW_h_price=0.17,), 1.68, 2)

        ill_dic = {"pre": self.lamps_g_halogen, "post": self.lamps_g_led,}
        month_thrift_g = ll.thrift(ill_dic)
        self.assertAlmostEqual( month_thrift_g.money(hours=1.5, kW_h_price=0.12,), 5.78, 2)
       
    def test_thrift_ROI(self):
        ill_dic = {"pre": self.lamps_g_halogen, "post": self.lamps_g_led,}
        month_thrift_g = ll.thrift(ill_dic)
        self.assertAlmostEqual( month_thrift_g.ROI(hours=1.5, kW_h_price=0.12,), 5.18, 2)

        # case not any thrift (zero division)
        ill_dic = {"pre": self.lamps_g_halogen, "post": self.lamps_g_halogen,}
        month_thrift_g = ll.thrift(ill_dic)
        self.assertAlmostEqual( month_thrift_g.ROI(hours=1.5, kW_h_price=0.12,), 0, 2)

 
if __name__ == '__main__':
    unittest.main()

