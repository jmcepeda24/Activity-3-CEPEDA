class Classstat():
     #This fuction is for STATS Calculator

    def statReturnHP(base,iv,ev,lvl):
        #return base+iv+ev+lvl
        return ((((2*base)+iv+(ev/4))*lvl)/100)+lvl+10

    def statReturnOtherStat(base,iv,ev,lvl,nature):
        #return base+iv+ev+lvl
        return (((((2*base)+iv+(ev/4))*lvl)/100)+5)*nature

