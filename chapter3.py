def main(name):
  # print("안녕하세요 " + name + " 입니다")
  # print("안녕하세요 %s 입니다" % name)
  # print("100")
  # print("%d" % 100)
  # print(100)
  # print("%d 과 %s" % (100+1, "안녕"))
  #
  # print("%d" %123)
  # print("%5d" %123)
  # print("%05d" %123)
  #
  # print("%f" % 123.45)
  # print("%7.1f" % 123.45)
  # print("%7.2f" % 123.45)
  # print("%7.3f" % 123.45)
  # print("%7.4f" % 123.45)
  #
  # print("%s" % "Python")
  # print("%10s" % "Python")
  #
  # print("{0:d} {1:5d} {2:05d}".format(100, 200, 300))
  #
  # print("한행입니다. \n두번째 행입니다.")

  # a = ""

  for i in range(9):
    a = ""
    for j in range(i+1):
      a = a + "*"
      # a += "*"
    print(a)



if __name__ == '__main__':
  main('sunjeehun')