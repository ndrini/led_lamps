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
        return money_pre - money_post

    def info(self):
        descrip = "The actual situation is a set of " + str(self.pre.number) + "bulbs" + \
                  "of " + str(self.pre.power) + " W of power and not any cost.\n" +  \
                  "The new set  of " + str(self.pre.number) + "bulbs" + \
                  "of " + str(self.post.power) + " W of power with the cost each of " + str(self.post.cost_of_one ) + " €."
        return descrip

    def ROI(self, hours,  kW_h_price=0.17, days_in_month=31, report=False, ):
        # return the number of month to get the cost of the illumination change back
        cost_now = self.post.replacement_cost()
        thrift_monthly = self.money( hours,  kW_h_price )
        try: 
            roi = cost_now / thrift_monthly
            if report:
                print self.info(), roi, "months"
            return roi
        except:
            print "Something was wrong with ROI calculation. \n May be an error ZeroDivisionError (float division by zero)\
                    Check the code!"
            return 0


 
if __name__ == '__main__':
    
    # example
    print "Define a set a lamps (also in different number)\n\
    for istance \n \t\
    the old set     60.0 W of power\t  number 15.   not any cost \n \t\
    the new set      5.5 W of power\t  number 17.   the cost each of 1.8 €"
    lamps_inc  = illumination({"power": 60. , "number":15., "cost": .0})
    lamps_leds = illumination({"power":  5.5, "number":18., "cost":1.8}) 

    print "Compute the ROI: \n\tpass a dictionary with tho objects:\
        \n\tistanciate the thrift() object and call the method ROI to compute it\
        \n\tThe result is:"
    ill_dic = {"pre": lamps_inc, "post": lamps_leds,}
    month_thrift = thrift(ill_dic)
    print month_thrift.ROI(hours=1.5,), "months"
    
    print "Use 'report=True' attibute to get more human readable informations\n\t month_thrift.ROI(hours=1.5,report=True)"
    print month_thrift.info()
    print month_thrift.ROI(hours=1.5,), "months"
    print month_thrift.ROI(hours=1.5, report=True)