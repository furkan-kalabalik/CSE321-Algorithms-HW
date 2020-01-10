C = [5,11,2,21,5,7,8,12,13,None]
P=[None,7,9,5,21,7,13,10,14,20]

def isProfit(startDay, gain):
    if(gain > 0):
        return True, startDay, gain
    else:
        return False, startDay,gain

def findMaxProfitDay(cost,start,end,price):
    if(end - start == 1):
        return isProfit(start, price[end]-cost[start])
    else:
        if((end-start)%2 == 0):
            mid = ((end-start)//2)+start
            isGainLeft, leftStart,leftGain = findMaxProfitDay(cost,start,mid,price)
            isGainRight, rightStart,rightGain = findMaxProfitDay(cost,mid,end,price)
            if(leftGain > rightGain):
                return isProfit(leftStart, leftGain)
            else:
                return isProfit(rightStart, rightGain)
        else:
            mid = ((end-start)//2)+start
            isGainLeft, leftStart,leftGain = findMaxProfitDay(cost,start,mid,price)
            isGainMid, midStart,midGain = findMaxProfitDay(cost,mid,mid+1,price)
            isGainRight, rightStart,rightGain = findMaxProfitDay(cost,mid+1,end,price)
            if(leftGain>midGain and leftGain >rightGain):
                return isProfit(leftStart,leftGain)
            elif(rightGain>midGain and rightGain>leftGain):
                return isProfit(rightStart, rightGain)
            else:
                return isProfit(midStart,midGain)

def printBestSellDay(cost,price):
    isGain, day, gainUnit = findMaxProfitDay(cost,0,len(cost)-1,price)
    if(isGain):
        print("Best days to buy and sell:%d-%d and gain for 500 unit will be:%d"%(day+1, day+2,gainUnit*500))
    else:
        print("No day to make money")
       

printBestSellDay(C,P) 
