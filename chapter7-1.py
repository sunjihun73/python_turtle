
def main(name):
  aa = []

  for i in range(0, 4):
    aa.append(0)

  print(len(aa))

  # print(aa)
  hap = 0

  for i in range(0, 4):
    aa[i] = int(input(str(i + 1) + "번째 숫자 :"))

  for i in range(0, 4):
    hap = hap + aa[i]

  print("합계 :  %d" % hap)






# 스크립트를 실행하려면 여백의 녹색 버튼을 누릅니다.
if __name__ == '__main__':
  main('sunjihun')