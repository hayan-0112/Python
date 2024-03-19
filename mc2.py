start = ["1. 매장 식사, 2. 포장"]
catego = {"1. 추천메뉴":None, "2. 버거메뉴": {"1. 시그니처버거": [["1.1 그릴드 머쉬룸 버거", 8000],["1.2 골든 에그치즈 버거", 7800],["1.3 트리플 어니언 버거", 7900]],
                                      "2. 비프버거": [["2.1 빅맥", 4500], ["2.2 치즈버거", 3500], ["2.3 쿼터 파운더 버거", 5000], ["2.4 더블쿼터파운더 치즈버거", 6000]],
                                      "3. 치킨&슈림프버거": [["3.1 맥스파이시 상하이 버거", 4500], ["3.2 맥치킨 버거", 3500], ["3.3 맥크리스피 디럭스 버거", 4300]],
                                      "4. 불고기&기타버거": [["4.1 더블 불고기 버거", 4000],["4.2 슈비버거", 4500], ["4.3 1955버거", 5000]]},
          "3. 음료메뉴":None, "4. 사이드메뉴":None, "5. 디저트메뉴":None, "6. 해피밀":None}
recommed_menu = {"5":["빅맥",4500], "6":["1955버거",5000], "7":["맥스파이시 상하이 버거",4500], "8":["맥치킨 버거",3500]}
drink_type = ["1. 커피, 2. 탄산음료, 3. 과일음료, 4. 쉐이크"]
drink_menu = {"9": ["바닐라라떼",3000], "10":["아메리카노",2000], "11":["카페라떼",2500], "12":["카푸치노",2500], "13":["드립커피",1800], #커피
              "14":["코카콜라",1500], "15":["환타",1500], "16":["스프라이트",1500], #탄산음료
              "17":["골드 맥피즈",2000], "18":["자두 천도복숭아 칠러",2500], "19":["제주한라봉 칠러",2500], #과일음료
              "20":["초코쉐이크",2500], "21":["바닐라쉐이크",2500],"22":["딸기쉐이크",2500]} #쉐이크
side_type = ["1.스낵랩, 2. 코울슬로, 3. 치즈스틱, 4. 맥너겟, 5. 치킨텐더, 6. 감자튀김, 7. 디핑소스"]
snacklab = {"23-0":["토마토 치킨 스낵랩", 2000], "23-1":["상하이 치킨 스낵랩", 2000]}
coleslaw = {"24": ["코울슬로",1500]}
cheese_stick = {"25-0":["치즈스틱 2조각", 1800], "25-1":["치즈스틱 4조각", 3000]}
mc = {"26-0":["맥너겟 4조각", 3000], "26-1":["맥너겟 6조각", 4000]}
tender = {"27": ["치킨텐더",3500]}
potato = {"28-0":["감자튀김 S", 1000], "28-1":["감자튀김 M", 1300], "28-2":["감자튀김 L", 1500]}
ds = ["1. 라즈베리 크림치즈 파이 2. 맥플러리"]
ds_pi = {"29": ["라즈베리 크림치즈 파이",1500]}
ds_mc = {"30-0":["오레오맥플러리", 3000], "30-1":["초코오레오맥플러리", 3000], "30-2":["딸기오레오맥플러리", 3000]}
sauce = {"31-0":["디핑소스 스위트 앤 사워", 500], "31-2":["디핑소스 스위트 칠리", 500], "31-3":["디핑소스 케이준", 500]}
happy_menu = {"32-0":["맥너겟 4조각 해피밀", 3500], "32-2":["햄버거 해피밀", 3500], "32-3":["불고기버거 해피밀", 3800]}
set = ["1. 단품", "2. 일반세트(+2000)", "3. 라지세트(+2500)"]
set1 = {'1':["감자튀김", +0], '2':["감자튀김+치즈스틱 2조각", +1500], '3':["치즈스틱", 500]}
set2 = {'1':"코카콜라", '2':"스프라이트", '3':"환타"}
basket = {}
def print_basket(basket):
    print("장바구니 내역: ")
    for item, details in basket.items():
        if 'quantity' in details and 'price' in details:
            print(f"{item}: 수량 - {details['quantity']}, 가격 - {details['price']}원")
    total_amount = sum(int(menu.get("price", 0)) for menu in basket.values())
    print(f"총 금액: {total_amount}원")
    print("장바구니에 담긴 품목: ")
    for item in items_in_basket:
        print(item)

def setAmount():
    amount_value = 1
    while True:
        amount = input("1.수량(+) 2.수량(-) /그 외 입력 다음 단계: ")
        if amount == "1":
            amount_value += 1
        elif amount == "2":
            if amount_value > 1:
                amount_value -= 1
            else:
                print("1개 이하 설정 불가")
        else:
            return amount_value

def price():
    if c == 1 or c == 2:
        s = input(set)
        price_to_add = 0
        if s == '2' or s == '3':
            select_menu1 = input(set1)
            if select_menu1 == '1':
                price_to_add += 0
            elif select_menu1 == '2':
                price_to_add += 1500
            elif select_menu1 == '3':
                price_to_add += 500

            select_menu2 = input(set2)
            if s == '2':
                price_to_add += 2000
            elif s == '3':
                price_to_add += 2500
        return price_to_add
items_in_basket = []

while True:
    place = input(start)
    print("*"*50)
    print(catego.keys())
    c = int(input("카테고리를 선택하세요: "))

    if c == 1: #추천메뉴 선택
        print(recommed_menu)
        select_number = input("메뉴 번호를 선택하세요: ")
        menu_price = price()

        if select_number in recommed_menu:
            quantity = int(input("수량을 입력하세요: "))
            item_price = recommed_menu[select_number][1]
            total_price = item_price * quantity + menu_price

            if select_number in basket:
                for select_number in basket:
                    try:
                        basket[select_number]["quantity"] += quantity
                    except KeyError:
                        basket[select_number]["price"] += total_price
                        items_in_basket.append(select_number)
            else:
                basket[select_number] = {"quantity": quantity, "price": total_price}
                items_in_basket.append(select_number)

        print(basket)
        print("-"*50)
        print_basket(basket)

    elif c == 2: #버거메뉴 선택
        selected_burger_menu = catego["2. 버거메뉴"]
        burger_type = input((selected_burger_menu.keys()))
        if burger_type == '1': #시그니처버거
            signature_burgers = catego["2. 버거메뉴"]["1. 시그니처버거"]
            print(signature_burgers)
            select_number = input("메뉴를 선택하세요: ")
            menu_price = price()

            if select_number in catego:
                quantity = int(input("수량을 입력하세요: "))
                item_price = catego[select_number][1]
                total_price = item_price * quantity + menu_price

                if select_number in basket:
                    for select_number in basket:
                        try:
                            basket[select_number]["quantity"] += quantity
                        except KeyError:
                            basket[select_number]["price"] += total_price
                            items_in_basket.append(select_number)
                else:
                    basket[select_number] = {"quantity": quantity, "price": total_price}
                    items_in_basket.append(select_number)

            print(basket)
            print("-" * 50)
            print_basket(basket)
        elif burger_type == '2': #비프버거
            signature_burgers = catego["2. 버거메뉴"]["2. 비프버거"]
            print(signature_burgers)
            select_number = input("메뉴를 선택하세요: ")
            menu_price = price()

            if select_number in catego:
                quantity = int(input("수량을 입력하세요: "))
                item_price = catego[select_number][1]
                total_price = item_price * quantity + menu_price

                if select_number in basket:
                    for select_number in basket:
                        try:
                            basket[select_number]["quantity"] += quantity
                        except KeyError:
                            basket[select_number]["price"] += total_price
                            items_in_basket.append(select_number)
                else:
                    basket[select_number] = {"quantity": quantity, "price": total_price}
                    items_in_basket.append(select_number)

            print(basket)
            print("-" * 50)
            print_basket(basket)

        elif burger_type == '3': #치킨&슈림프버거
            signature_burgers = catego["2. 버거메뉴"]["3. 치킨&슈림프버거"]
            print(signature_burgers)
            select_number = input("메뉴를 선택하세요: ")
            menu_price = price()

            if select_number in catego:
                quantity = int(input("수량을 입력하세요: "))
                item_price = catego[select_number][1]
                total_price = item_price * quantity + menu_price

                if select_number in basket:
                    for select_number in basket:
                        try:
                            basket[select_number]["quantity"] += quantity
                        except KeyError:
                            basket[select_number]["price"] += total_price
                            items_in_basket.append(select_number)
                else:
                    basket[select_number] = {"quantity": quantity, "price": total_price}
                    items_in_basket.append(select_number)

            print(basket)
            print("-" * 50)
            print_basket(basket)

        elif burger_type == '4': #불고기&기타버거
            signature_burgers = catego["2. 버거메뉴"]["4. 불고기&기타버거"]
            print(signature_burgers)
            select_number = input("메뉴를 선택하세요: ")
            menu_price = price()

            if select_number in catego:
                quantity = int(input("수량을 입력하세요: "))
                item_price = catego[select_number][1]
                total_price = item_price * quantity + menu_price

                if select_number in basket:
                    for select_number in basket:
                        try:
                            basket[select_number]["quantity"] += quantity
                        except KeyError:
                            basket[select_number]["price"] += total_price
                            items_in_basket.append(select_number)
                else:
                    basket[select_number] = {"quantity": quantity, "price": total_price}
                    items_in_basket.append(select_number)

            print(basket)
            print("-" * 50)
            print_basket(basket)

    elif c == 3:  # 음료메뉴 선택
        print(drink_type)
        dt = int(input("음료종류를 선택하세요: "))
        if dt == 1:
            selected_drinks = {"9":drink_menu["9"], "10": drink_menu["10"],
                               "11":drink_menu["11"], "12":drink_menu["12"]}
            print(selected_drinks)
            select_number = input("메뉴를 선택하세요: ")
            menu_price = price()

            if select_number in drink_menu:
                quantity = int(input("수량을 입력하세요: "))
                item_price = drink_menu[select_number][1]
                total_price = item_price * quantity

                if select_number in basket:
                    for select_number in basket:
                        try:
                            basket[select_number]["quantity"] += quantity
                        except KeyError:
                            basket[select_number]["price"] += total_price
                            items_in_basket.append(select_number)
                else:
                    basket[select_number] = {"quantity": quantity, "price": total_price}
                    items_in_basket.append(select_number)

            print(basket)
            print("-" * 50)
            print_basket(basket)
        elif dt == 2:
            selected_drinks = {"13": drink_menu["13"], "14": drink_menu["14"], "15": drink_menu["15"]}
            print(selected_drinks)
            select_number = input("메뉴를 선택하세요: ")
            menu_price = price()

            if select_number in drink_menu:
                quantity = int(input("수량을 입력하세요: "))
                item_price = drink_menu[select_number][1]
                total_price = item_price * quantity

                if select_number in basket:
                    for select_number in basket:
                        try:
                            basket[select_number]["quantity"] += quantity
                        except KeyError:
                            basket[select_number]["price"] += total_price
                            items_in_basket.append(select_number)
                else:
                    basket[select_number] = {"quantity": quantity, "price": total_price}
                    items_in_basket.append(select_number)

            print(basket)
            print("-" * 50)
            print_basket(basket)
        elif dt == 3:
            selected_drinks = {"16": drink_menu["16"], "17": drink_menu["17"], "18": drink_menu["18"]}
            print(selected_drinks)
            select_number = input("메뉴를 선택하세요: ")
            menu_price = price()

            if select_number in drink_menu:
                quantity = int(input("수량을 입력하세요: "))
                item_price = drink_menu[select_number][1]
                total_price = item_price * quantity

                if select_number in basket:
                    for select_number in basket:
                        try:
                            basket[select_number]["quantity"] += quantity
                        except KeyError:
                            basket[select_number]["price"] += total_price
                            items_in_basket.append(select_number)
                else:
                    basket[select_number] = {"quantity": quantity, "price": total_price}
                    items_in_basket.append(select_number)

            print(basket)
            print("-" * 50)
            print_basket(basket)
        elif dt == 4:
            selected_drinks = {"19": drink_menu["19"], "20": drink_menu["20"], "21": drink_menu["21"]}
            print(selected_drinks)
            select_number = input("메뉴를 선택하세요: ")
            menu_price = price()

            if select_number in drink_menu:
                quantity = int(input("수량을 입력하세요: "))
                item_price = drink_menu[select_number][1]
                total_price = item_price * quantity

                if select_number in basket:
                    for select_number in basket:
                        try:
                            basket[select_number]["quantity"] += quantity
                        except KeyError:
                            basket[select_number]["price"] += total_price
                            items_in_basket.append(select_number)
                else:
                    basket[select_number] = {"quantity": quantity, "price": total_price}
                    items_in_basket.append(select_number)
            print(basket)
            print("-" * 50)
            print_basket(basket)
    elif c == 4: #사이드메뉴 선택
        print(side_type)
        ds = int(input("사이드종류를 선택하세요: "))
        if ds == 1: #스낵랩
            print(snacklab)
            select_number = input("메뉴를 선택하세요: ")
            menu_price = price()

            if select_number in snacklab:
                quantity = int(input("수량을 입력하세요: "))
                item_price = snacklab[select_number][1]
                total_price = item_price * quantity
                if select_number in basket:
                    for select_number in basket:
                        try:
                            basket[select_number]["quantity"] += quantity
                        except KeyError:
                            basket[select_number]["price"] += total_price
                            items_in_basket.append(select_number)
                else:
                    basket[select_number] = {"quantity": quantity, "price": total_price}
                    items_in_basket.append(select_number)
            print(basket)
            print("-" * 50)
            print_basket(basket)
        elif ds == 2: #코울슬로
            print(coleslaw)
            select_number = input("메뉴를 선택하세요: ")
            menu_price = price()

            if select_number in coleslaw:
                quantity = int(input("수량을 입력하세요: "))
                item_price = coleslaw[select_number][1]
                total_price = item_price * quantity
                if select_number in basket:
                    for select_number in basket:
                        try:
                            basket[select_number]["quantity"] += quantity
                        except KeyError:
                            basket[select_number]["price"] += total_price
                            items_in_basket.append(select_number)
                else:
                    basket[select_number] = {"quantity": quantity, "price": total_price}
                    items_in_basket.append(select_number)

            print(basket)
            print("-" * 50)
            print_basket(basket)
        elif ds == 3:  # 치즈스틱
            print(cheese_stick)
            select_number = input("메뉴를 선택하세요: ")
            menu_price = price()

            if select_number in cheese_stick:
                quantity = int(input("수량을 입력하세요: "))
                item_price = cheese_stick[select_number][1]
                total_price = item_price * quantity
                if select_number in basket:
                    for select_number in basket:
                        try:
                            basket[select_number]["quantity"] += quantity
                        except KeyError:
                            basket[select_number]["price"] += total_price
                            items_in_basket.append(select_number)
                else:
                    basket[select_number] = {"quantity": quantity, "price": total_price}
                    items_in_basket.append(select_number)

            print(basket)
            print("-" * 50)
            print_basket(basket)
        elif ds == 4:  # 맥너겟
            print(mc)
            select_number = input("메뉴를 선택하세요: ")
            menu_price = price()

            if select_number in mc:
                quantity = int(input("수량을 입력하세요: "))
                item_price = mc[select_number][1]
                total_price = item_price * quantity
                if select_number in basket:
                    for select_number in basket:
                        try:
                            basket[select_number]["quantity"] += quantity
                        except KeyError:
                            basket[select_number]["price"] += total_price
                            items_in_basket.append(select_number)
                else:
                    basket[select_number] = {"quantity": quantity, "price": total_price}
                    items_in_basket.append(select_number)

            print(basket)
            print("-" * 50)
            print_basket(basket)
        elif ds == 5:  # 치킨텐더
            print(tender)
            select_number = input("메뉴를 선택하세요: ")
            menu_price = price()

            if select_number in tender:
                quantity = int(input("수량을 입력하세요: "))
                item_price = tender[select_number][1]
                total_price = item_price * quantity
                if select_number in basket:
                    for select_number in basket:
                        try:
                            basket[select_number]["quantity"] += quantity
                        except KeyError:
                            basket[select_number]["price"] += total_price
                            items_in_basket.append(select_number)
                else:
                    basket[select_number] = {"quantity": quantity, "price": total_price}
                    items_in_basket.append(select_number)
            print(basket)
            print("-" * 50)
            print_basket(basket)
        elif ds == 6:  # 감자튀김
            print(potato)
            select_number = input("메뉴를 선택하세요: ")
            menu_price = price()

            if select_number in potato:
                quantity = int(input("수량을 입력하세요: "))
                item_price = potato[select_number][1]
                total_price = item_price * quantity
                if select_number in basket:
                    for select_number in basket:
                        try:
                            basket[select_number]["quantity"] += quantity
                        except KeyError:
                            basket[select_number]["price"] += total_price
                            items_in_basket.append(select_number)
                else:
                    basket[select_number] = {"quantity": quantity, "price": total_price}
                    items_in_basket.append(select_number)

            print(basket)
            print("-" * 50)
            print_basket(basket)
        elif ds == 7:  # 디핑소스
            print(sauce)
            select_number = input("메뉴를 선택하세요: ")
            menu_price = price()

            if select_number in sauce:
                quantity = int(input("수량을 입력하세요: "))
                item_price = sauce[select_number][1]
                total_price = item_price * quantity
                if select_number in basket:
                    for select_number in basket:
                        try:
                            basket[select_number]["quantity"] += quantity
                        except KeyError:
                            basket[select_number]["price"] += total_price
                            items_in_basket.append(select_number)
                else:
                    basket[select_number] = {"quantity": quantity, "price": total_price}
                    items_in_basket.append(select_number)

            print(basket)
            print("-" * 50)
            print_basket(basket)
    elif c == 5:  # 디저트메뉴 선택
        print(ds)
        dst = int(input("사이드종류를 선택하세요: "))
        if dst == 1:  # 라즈베리 크림치즈 파이
            print(ds_pi)
            select_number = input("메뉴를 선택하세요: ")
            menu_price = price()

            if select_number in ds_pi:
                quantity = int(input("수량을 입력하세요: "))
                item_price = ds_pi[select_number][1]
                total_price = item_price * quantity
                if select_number in basket:
                    for select_number in basket:
                        try:
                            basket[select_number]["quantity"] += quantity
                        except KeyError:
                            basket[select_number]["price"] += total_price
                            items_in_basket.append(select_number)
                else:
                    basket[select_number] = {"quantity": quantity, "price": total_price}
                    items_in_basket.append(select_number)

            print(basket)
            print("-" * 50)
            print_basket(basket)
        elif dst == 2:  # 맥플러리
            print(ds_mc)
            select_number = input("메뉴를 선택하세요: ")
            menu_price = price()

            if select_number in ds_mc:
                quantity = int(input("수량을 입력하세요: "))
                item_price = ds_mc[select_number][1] * quantity
                total_price = item_price * quantity
                if select_number in basket:
                    for select_number in basket:
                        try:
                            basket[select_number]["quantity"] += quantity
                        except KeyError:
                            basket[select_number]["price"] += total_price
                            items_in_basket.append(select_number)
                else:
                    basket[select_number] = {"quantity": quantity, "price": total_price}
                    items_in_basket.append(select_number)

            print(basket)
            print("-" * 50)
            print_basket(basket)
    elif c == 6: #해피밀 선택
        import datetime as dt

        now = dt.datetime.now().time()
        opening_time = dt.time(9, 30)
        closing_time = dt.time(23, 0)
        if opening_time <= now <= closing_time:
            print(happy_menu)
            select_number = input("메뉴를 선택하세요: ")
            menu_price = price()

            if select_number in happy_menu:
                quantity = int(input("수량을 입력하세요: "))
                item_price = happy_menu[select_number][1] * quantity
                total_price = item_price * quantity
                if select_number in basket:
                    for select_number in basket:
                        try:
                            basket[select_number]["quantity"] += quantity
                        except KeyError:
                            basket[select_number]["price"] += total_price
                            items_in_basket.append(select_number)
                else:
                    basket[select_number] = {"quantity": quantity, "price": total_price}
                    items_in_basket.append(select_number)

            print(basket)
            print("-" * 50)
            print_basket(basket)
        else:
            print("현재 운영 시간이 아닙니다.")
            break
    print(setAmount())

    mode = 1
    while mode:
        print()
        mode = input("1. 수량변경 2. 품목삭제 3. 추가주문 4. 결제: ")
        if mode == "3":
            break
        elif mode == "4":
            break
        elif mode == "1":
            target_idx = input("수량변경하려는 품목의 번호입력: ")
            amount_value = input("수량변경하려는 품목의 수량 입력: ")
            basket[list(basket.keys())[int(target_idx)-1]] = int(amount_value)
            continue
        elif mode == "2":
            target_idx = input("삭제하려는 품목의 번호입력: ")
            del basket[list(basket.keys())]
            continue
    if mode == "4":
            service = input("1.테이블 서비스 2. 셀프 서비스: ")
            if service == "1":
                print("자리로 직접 가져다 드리겠습니다. 이용해주셔서 감사합니다.")
            else:
                print("이용해 주셔서 감사합니다.")
            print("결제완료 후 첫화면 진입")
            break