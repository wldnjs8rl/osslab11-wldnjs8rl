from geo.utils import circumference, area

if __name__ == "__main__":
    radius = 5.0

    # 원의 둘레와 넓이 계산
    c = circumference(radius)
    a = area(radius)

    # 테스트 출력 형식
    print("c =", c)
    print("area =", a)