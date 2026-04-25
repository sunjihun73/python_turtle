
def main(name):
  aa = []
  bb = [100, 100, 30, "선지헌"]

  print(bb.count(100))
  
  # 문자열과 숫자가 섞여 있으면 sort() 시 TypeError 발생 가능
  try:
    bb.sort()
    print(bb)
  except TypeError:
    print("리스트에 정렬할 수 없는 서로 다른 타입의 데이터가 포함되어 있습니다.")

  for i in range(0, 4):
    aa.append(0)

  print(f"리스트 aa의 길이: {len(aa)}")

  hap = 0

  for i in range(0, 4):
    while True:
      try:
        aa[i] = int(input(str(i + 1) + "번째 숫자 :"))
        break
      except ValueError:
        print("숫자만 입력 가능합니다. 다시 입력해주세요.")

  aa.sort()
  print("입력된 숫자 정렬:", aa)

  for i in range(0, 4):
    hap = hap + aa[i]

  print("합계 :  %d" % hap)






# 스크립트를 실행하려면 여백의 녹색 버튼을 누릅니다.
if __name__ == '__main__':
  main('sunjihun')