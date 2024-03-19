#3가지 함수 이상 포함
#하나의 주제에 대한 모듈 ex)원의 둘레 부피 등 계산
#모듈에 포함된 함수명, 매개변수, 사용법 메뉴얼을 txt로 제공
#모듈 내 함수에서 자체적 print 사용하지 않음
#return 형태로 결과값 반환
#예외처리 적용, 매개변수 오류시 예외처리로 프로세스 종료 방지

def deg_to_rad(x): #degree -> radian / x = 도
    try:
        rad = x * 3.14 / 180
        formatted_rad = "{:.1f}".format(rad)
        return (formatted_rad)
    except ValueError:
        return "degree -> radian 변환이 되지 않았습니다."

def rad_to_deg(x): #radian -> degree / x = 라디안
    try:
        deg = x * 180 / 3.14
        formatted_deg = "{:.1f}".format(deg)
        return formatted_deg
    except ValueError:
        return "radian -> degree 변환이 되지 않았습니다."

def to_sin_asin(x,y,z): #x:밑변, y:높이, z:빗변
    try:
        sin = y / z
        asin = z / y
        formatted_sin = "{:.1f}".format(sin)
        formatted_asin = "{:.1f}".format(asin)
        return formatted_sin, formatted_asin
    except ValueError:
        return "sin/asin 계산이 되지 않았습니다."


def to_cos_acos(x,y,z):
    try:
        cos = x / z
        acos = z / x
        formatted_cos = "{:.1f}".format(cos)
        formatted_acos = "{:.1f}".format(acos)
        return formatted_cos, formatted_acos
    except ValueError:
        return "cos/acos 계산이 되지 않았습니다."


def to_tan_atan(x,y,z):
    try:
        tan = y / x
        atan = x / y
        formatted_tan = "{:.1f}".format(tan)
        formatted_atan = "{:.1f}".format(atan)
        return formatted_tan, formatted_atan
    except ValueError:
        return "tan/atan 계산이 되지 않았습니다."