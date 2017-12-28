import time
import logging


class DigitalCurrencyExchange(object):


    # 锁
    lock = 0

    # 本金
    incipal = 100

    # difference =差价 #
    difference = 0

    # yieldrate =收益率 #
    yieldrate = None

    # transactioncost =开仓成本#
    transactioncost = 0

    # counter =计数器,计算均价 #
    couter = 0

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
    def isPrice(self, xbtc, ybtc, xy):

        # 效验参数
        if xy < 0 or xbtc < 0 or ybtc < 0:
            return


        priportion = xbtc / ybtc
        print('公允价格=%f'%(priportion))

        #偏离率
        deviation = priportion/xy *100
        print('=======偏离率 %f =========' %(deviation))

        # 根据条件建立仓位,lock==0时候,没有仓位#

        # 不断请求
        # while True:

        # 设置平仓区间
        floatxy0 = xy - xy * 0.007
        floatxy1 = xy + xy * 0.007
        if priportion <= floatxy1 and priportion >= floatxy0 and self.lock != 0:
            # 1 发车指令平仓
            print('平仓价格%f' % (xy))

            # 2 计算收益率
            difference = xy - self.transactioncost / self.couter
            yieldrate = difference / priportion * 100
            print('>>>>>>>>>>>>>>>>>>平仓收益率: %s % >>>>>>>>>>>>>>>>' % (yieldrate))

            # 3 平仓后lock==0 #
            self.ock = 0

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
            if priportion * 1.03 < xy and xy < priportion * 1.05:
                if self.lock == 0:
                    self.lock = 10

                    # 计算买入均价
                    self.transactioncost = self.transactioncost + xy
                    self.couter += 1

                    print('10发出交易指令: %s' % (xy))
                    localtime = time.asctime(time.localtime(time.time()))
                    logging.info('10发出交易指令: %s,时间:%s' % (xy, localtime))

            if priportion * 1.07 < xy and xy < priportion * 1.1:
                if lock == 10:
                    lock = 20

                    # 计算买入均价
                    transactioncost = transactioncost + xy
                    couter = couter + 1;

                    print('20发出交易指令: %s' % (xy))

            if priportion * 1.1 < xy and xy < priportion * 1.2:
                if lock == 20:
                    lock = 30

                    # 计算买入均价
                    transactioncost = transactioncost + xy
                    couter = couter + 1;

                    print('30发出交易指令: %s' % (xy))

            if priportion * 1.2 < xy and xy < priportion * 1.3:
                if lock == 30:
                    lock = 40

                    # 计算买入均价
                    transactioncost = transactioncost + xy
                    couter = couter + 1;

                    print('40发出交易指令: %s' % (xy))

            if priportion * 1.3 < xy and xy < priportion * 1.6:
                if lock == 40:
                    lock = 50

                    # 计算买入均价
                    transactioncost = transactioncost + xy
                    couter = couter + 1;

                    print('50发出交易指令: %s' % (xy))

            if priportion * 1.6 < xy and xy < priportion * 1.7:
                if lock == 50:
                    lock = 60

                    # 计算买入均价
                    transactioncost = transactioncost + xy
                    couter = couter + 1;

                    print('60发出交易指令: %s' % (xy))

            if priportion * 1.7 < xy and xy < priportion * 1.8:
                if lock == 60:
                    lock = 70

                    # 计算买入均价
                    transactioncost = transactioncost + xy
                    couter = couter + 1;

                    print('70发出交易指令: %s' % (xy))

            if priportion * 1.8 < xy and xy < priportion * 1.9:
                if lock == 70:
                    lock = 80

                    # 计算买入均价
                    transactioncost = transactioncost + xy
                    couter = couter + 1;

                    print('80发出交易指令: %s' % (xy))
            if priportion * 1.9 < xy and xy < priportion * 2:
                if lock == 80:
                    lock = 90

                    # 计算买入均价
                    transactioncost = transactioncost + xy
                    couter = couter + 1;

                    pass
            if priportion * 2.1 < xy and xy < priportion * 2.2:
                if lock == 90:
                    lock = 110

                    # 计算买入均价
                    transactioncost = transactioncost + xy
                    couter = couter + 1;

                    print('110发出交易指令: %s' % (xy))
            if priportion * 2.2 < xy and xy < priportion * 2.4:
                if lock == 110:
                    lock = 120

                    # 计算买入均价
                    transactioncost = transactioncost + xy
                    couter = couter + 1;

                    print('120发出交易指令: %s' % (xy))
            if priportion * 2.4 < xy and xy < priportion * 2.6:
                if lock == 120:
                    lock = 140

                    # 计算买入均价
                    transactioncost = transactioncost + xy
                    couter = couter + 1;

                    print('140发出交易指令: %s' % (xy))
            if priportion * 2.6 < xy and xy < priportion * 3:
                if lock == 140:
                    lock = 300
                    # 计算买入均价
                    transactioncost = transactioncost + xy
                    couter = couter + 1;

                    print('160发出交易指令: %s' % (xy))

        # 向下偏离 XY < priportion #
        if xy < priportion:

            print('向下偏离')
            if priportion * 0.97 < xy and xy < priportion * 1:
                if lock == 0:
                    lock = -10

                    # 计算卖出均价
                    transactioncost = transactioncost + xy
                    couter = couter + 1;

                    print('-10发出交易指令: %s' % (xy))
            if priportion * 0.9 < xy and xy < priportion * 0.97:
                if lock == -10:
                    lock = -20

                    # 计算卖出均价
                    transactioncost = transactioncost + xy
                    couter = couter + 1;

                    print('-20发出交易指令: %s' % (xy))
            if priportion * 0.85 < xy and xy < priportion * 0.9:
                if lock == -20:
                    lock = -30

                    # 计算卖出均价
                    transactioncost = transactioncost + xy
                    couter = couter + 1;

                    print('-30发出交易指令: %s' % (xy))
            if priportion * 0.7 < xy and xy < priportion * 0.85:
                if lock == -30:
                    lock = -40

                    # 计算卖出均价
                    transactioncost = transactioncost + xy
                    couter = couter + 1;

                    print('-40发出交易指令: %s' % (xy))

            if priportion * 0.6 < xy and xy < priportion * 0.7:
                if lock == -40:
                    lock = -50

                    # 计算卖出均价
                    transactioncost = transactioncost + xy
                    couter = couter + 1;

                    print('-50发出交易指令: %s' % (xy))

            if priportion * 0.5 < xy and xy < priportion * 0.6:
                if lock == -50:
                    lock = -60

                    # 计算卖出均价
                    transactioncost = transactioncost + xy
                    couter = couter + 1;

                    print('-60发出交易指令: %s' % (xy))

            if priportion * 0.3 < xy and xy < priportion * 0.5:
                if lock == -60:
                    lock = -70

                    # 计算卖出均价
                    transactioncost = transactioncost + xy
                    couter = couter + 1;

                    print('-70发出交易指令: %s' % (xy))

            if priportion * 0.1 < xy and xy < priportion * 0.3:
                if lock == -70:
                    lock = -80

                    # 计算卖出均价
                    transactioncost = transactioncost + xy
                    couter = couter + 1;

                    print('-80发出交易指令: %s' % (xy))

    # 延迟执行
# time.sleep(1)