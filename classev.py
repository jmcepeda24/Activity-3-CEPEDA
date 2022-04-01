class Classev():
 
    def statReturnD(base,iv,ev,lvl):
        #return base+iv+ev+lvl
        return (2*base+iv+(ev/4))*(lvl/100)

    def statReturnEvs(stats,nature,d,lvl):
        return (((((stats/nature)-d)*400)/lvl)/4)*4