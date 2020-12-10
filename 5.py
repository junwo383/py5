# name : jun
import random
print('==================로또===================')
num = int(input("로또에 사용하실금액을넣어주세요>"))
while True :
    print("돈"+str(num)+"받았습니다.")
    print("거스름돈은 제가계산해서 드리겠습니다.")
    break
meau = input("로또번호몇장드릴까요?")
while num >0 :
    print("지금부터 로또 랜덤 번호를 드리겠습니다!")
    print("========================================")
    for number in range(int(meau)) :
        lotto = random.sample(range(1,46),6)
        lotto.sort()
        print(lotto)
    else :
        print("로또종료하겠습니다.")
        break
print("==============================================")
print("주의사항 : 로또는 최대 10만원까지만가능합니다.")
print("수수료 :1등 33% 2등:22% 3등:22% 4등,5등")
