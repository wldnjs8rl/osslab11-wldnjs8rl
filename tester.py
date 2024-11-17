import geo.utils as utils

# 피타고라스 정리 계산
a, b = 3, 4
c = utils.pythagoras(a, b)
print('c =', c)

# 원의 넓이 계산
r = 10
area = utils.circle(r)
print('area =', area)