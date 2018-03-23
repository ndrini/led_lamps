# -*- coding: utf-8 -*-

class illumination():
    def __init__(self, lamp_type): 
        self.power       = lamp_type["power"]
        self.number      = lamp_type["number"]
        self.cost_of_one = lamp_type["cost"]

    def power_total(self):
        pass

    def consumption_monthly(self, hours=6, days_in_month=30, report=False):
        # for a 30 days standard month
        consumption = self.power * self.number  * days_in_month * hours / 1000  #  # *
        if report:
            print "\nMontly consumption is of ", consumption, " kW/h."   
        return consumption

    def replacement_cost(self):
        return self.cost_of_one * self.number


class thrift():
    def __init__(self, illumin_dic):
        self.pre   =   illumin_dic["pre"]
        self.post  =   illumin_dic["post"]

    def thrift_computation(self, hours, kW_h_price=0.17,):
        pass

    def money(self, hours,  kW_h_price=0.17, days_in_month=31 ):
        # return the monthly thrift due the illumination change
        money_pre  = self.pre.consumption_monthly(hours, days_in_month)   \
                                * kW_h_price   
        money_post = self.post.consumption_monthly(hours, days_in_month)  \
                                * kW_h_price   
        # print money_pre 
        # print money_post
        return money_pre - money_post

    def ROI(self, hours,  kW_h_price=0.17, days_in_month=31 ):
        # return the number of month to get the cost of the illumination change back
        cost_now = self.post.replacement_cost()
        thrift_monthly = self.money( hours,  kW_h_price )
        # risparmio_giorno * periodo = spesa --> periodo = spesa / risparmio_giorno

        try: 
            roi = cost_now / thrift_monthly
            return roi
        except:
            print "Something was wrong with ROI calculation. \n May be an error ZeroDivisionError (float division by zero)\
                    Check the code!"
            return 0

 
if __name__ == '__main__':
    
    # example

    pass