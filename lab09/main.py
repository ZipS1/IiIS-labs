'''
14. Сотовые вышки. Известны координаты на местности N сотовых вышек (на рисунке красные точки; N=100). 
Сигнал от вышек ослабевает обратноропорционально расстоянию от вышки. При этом сигналы от всех вышек складываются.
Зона уверенной связи имеет место в том случае, когда сигнал больше 0,1 от максимального значения сигнала –
на рисунке эта зона залита зеленым цветом.
'''
from Controller import Controller

def main():
    N = 100
    controller = Controller(N)
    controller.run()

if __name__ == "__main__":
    main()