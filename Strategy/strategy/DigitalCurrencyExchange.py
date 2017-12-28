import time
import logging


class DigitalCurrencyExchange(object):

    # # 锁
     #lock = 0
    #
    # # 本金

    # # difference =差价 #

    # # yieldrate =收益率 #

    # # transactioncost =开仓成本#

    # # counter =计数器,计算均价 #


    def __init__(self):
        self.incipal = 100
        self.lock = 0
        self.difference = 0
        self.yieldrate = 0
        self.transactioncost = 0
        self.couter = 0


    # x/btc y/btc :代表传入参标的最新价格
    #  xy 套利的标的市场价格
    # 通过市场价格和公允价格的比值,发送策略指令#

    # ---做空---
    def isPrice(self, xbtc, ybtc, xy):

        priportion = xbtc / ybtc
        print('公允价格=%f' % (priportion))

        #偏离率
        deviation = priportion/xy
        print('偏离率: %f ' %(deviation))

        # 设置平仓区间
        floatxy0 = xy - xy * 0.004
        floatxy1 = xy + xy * 0.004
        if priportion <= floatxy1 and priportion >= floatxy0 and self.lock != 0:

            # 1 发车指令平仓
            print('平仓价格%f' % (xy))

            if xy < self.transactioncost / self.couter:

                absolute = xy - self.transactioncost / self.couter
                self.difference = abs(absolute)
                self.yieldrate = self.difference + self.difference / priportion * 100
                print('>>>>>>>>>>>>>>>>>>平仓收益率: %f  >>>>>>>>>>>>>>>>' % (self.yieldrate))

                # 3 平仓后lock==0 #
                self.lock = 0

                # 4 平仓后difference==0
                self.difference = 0

                # 5 平仓后transactioncost==0
                self.transactioncost = 0

                # 6 平仓后counter计数器==0
                self.couter = 0

                # 7 将收益存入数据库中

            else :

                self.difference = xy - self.transactioncost / self.couter
                self.yieldrate = self.difference + self.difference / priportion * 100
                print('>>>>>>>>>>>>>>>>>>平仓收益率: %f  >>>>>>>>>>>>>>>>' % (self.yieldrate))

                # 3 平仓后lock==0 #
                self.lock = 0

                # 4 平仓后difference==0
                self.difference = 0

                # 5 平仓后transactioncost==0
                self.transactioncost = 0

                # 6 平仓后counter计数器==0
                self.couter = 0

                # 7 将收益存入数据库中

        # 向上偏离 xy > priportion #
        if xy > priportion:

            print('向上偏离')
            if priportion * 1.009 < xy and xy < priportion * 1.05:
                if self.lock == 0:
                    self.lock = 10

                    # 计算买入均价
                    self.transactioncost = self.transactioncost + xy
                    self.couter += 1

                    print('---------10发出交易指令: %s ------' % (xy))

            if priportion * 1.03 < xy and xy < priportion * 1.1:
                if self.lock == 10:
                    self.lock = 20

                    # 计算买入均价
                    self.transactioncost = self.transactioncost + xy
                    self.couter = self.couter + 1

                    print('-----20发出交易指令: %s ------' % (xy))

            if priportion * 1.1 < xy and xy < priportion * 1.2:
                if self.lock == 20:
                    self.lock = 30

                    # 计算买入均价
                    self.transactioncost = self.transactioncost + xy
                    self.couter = self.couter + 1

                    print('30发出交易指令: %s' % (xy))

            if priportion * 1.2 < xy and xy < priportion * 1.3:
                if self.lock == 30:
                    self.lock = 40

                    # 计算买入均价
                    self.transactioncost = self.transactioncost + xy
                    self.couter = self.couter + 1

                    print('40发出交易指令: %s' % (xy))

            if priportion * 1.3 < xy and xy < priportion * 1.6:
                if self.lock == 40:
                    self.lock = 50

                    # 计算买入均价
                    self.transactioncost = self.transactioncost + xy
                    self.couter = self.couter + 1

                    print('50发出交易指令: %s' % (xy))

            if priportion * 1.6 < xy and xy < priportion * 1.7:
                if self.lock == 50:
                    self.lock = 60

                    # 计算买入均价
                    self.transactioncost = self.transactioncost + xy
                    self.couter = self.couter + 1

                    print('60发出交易指令: %s' % (xy))

            if priportion * 1.7 < xy and xy < priportion * 1.8:
                if self.lock == 60:
                    self.lock = 70

                    # 计算买入均价
                    self.transactioncost = self.transactioncost + xy
                    self.couter = self.couter + 1

                    print('70发出交易指令: %s' % (xy))

            if priportion * 1.8 < xy and xy < priportion * 1.9:
                if self.lock == 70:
                    self.lock = 80

                    # 计算买入均价
                    self.transactioncost = self.transactioncost + xy
                    self.couter = self.couter + 1

                    print('80发出交易指令: %s' % (xy))




    # ---做多---
    def shortSelling(self, xbtc, ybtc, xy):

        priportion = xbtc / ybtc


        # 设置平仓区间
        floatxy0 = xy - xy * 0.004
        floatxy1 = xy + xy * 0.004
        if priportion <= floatxy1 and priportion >= floatxy0 and self.lock != 0:
            # 1 发车指令平仓
            print('平仓价格%f' % (xy))


            # 2 计算收益率
            self.difference = xy - self.transactioncost / self.couter
            self.yieldrate = self.difference + self.difference / priportion * 100
            print('>>>>>>>>>>>>>>>>>>平仓收益率: %f  >>>>>>>>>>>>>>>>' % (self.yieldrate))

            # 3 平仓后lock==0 #
            self.lock = 0

            # 4 平仓后difference==0
            self.difference = 0

            # 5 平仓后transactioncost==0
            self.transactioncost = 0

            # 6 平仓后counter计数器==0
            self.couter = 0

            # 7 将收益存入数据库中



        # 向下偏离 XY < priportion #
        if xy < priportion:
            print('向下偏离')
            if priportion * 0.987 < xy and xy < priportion * 0.991:
                if self.lock == 0:
                    self.lock = -10

                    # 计算卖出均价
                    self.transactioncost = self.transactioncost + xy
                    self.couter = self.couter + 1
                    print('========-10发出交易指令: %s' % (xy))
            if priportion * 0.98 < xy and xy < priportion * 0.987:
                if self.lock == -10:
                    self.lock = -20
                    # 计算卖出均价
                    self.transactioncost = self.transactioncost + xy
                    self.couter = self.couter + 1
                    print('=========-20发出交易指令: %s' % (xy))
            if priportion * 0.85 < xy and xy < priportion * 0.98:
                if self.lock == -20:
                    self.lock = -30
                    # 计算卖出均价
                    self.transactioncost = self.transactioncost + xy
                    self.couter = self.couter + 1
                    print('==========-30发出交易指令: %s' % (xy))
            if priportion * 0.7 < xy and xy < priportion * 0.85:
                if self.lock == -30:
                    self.lock = -40
                    # 计算卖出均
                    self.transactioncost = self.transactioncost + xy
                    self.couter = self.couter + 1
                    print('-40发出交易指令: %s' % (xy))
            if priportion * 0.6 < xy and xy < priportion * 0.7:
                if self.lock == -40:
                    self.lock = -50
                    # 计算卖出均价
                    self.transactioncost = self.transactioncost + xy
                    self.couter = self.couter + 1
                    print('-50发出交易指令: %s' % (xy))
            if priportion * 0.5 < xy and xy < priportion * 0.6:
                if self.lock == -50:
                    self.lock = -60
                    # 计算卖出均价
                    self.transactioncost = self.transactioncost + xy
                    self.couter = self.couter + 1
                    print('-60发出交易指令: %s' % (xy))
            if priportion * 0.3 < xy and xy < priportion * 0.5:
                if self.lock == -60:
                    self.lock = -70
                    # 计算卖出均价
                    self.transactioncost = self.transactioncost + xy
                    self.couter = self.couter + 1
                    print('-70发出交易指令: %s' % (xy))
            if priportion * 0.1 < xy and xy < priportion * 0.3:
                if self.lock == -70:
                    self.lock = -80
                    # 计算卖出均价
                    self.transactioncost = self.transactioncost + xy
                    self.couter = self.couter + 1
                    print('-80发出交易指令: %s' % (xy))