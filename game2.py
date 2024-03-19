import random
import time
class Itemlist:
    user_items = []                                # 임의의 유저 아이템 리스트
    b_range = user_items.count(5)
    b_count = user_items.count(6)
    shield_value = user_items.count(7)
    # 아이템

    def itemlist(self, value):
        if value == 5:  # 아이템 번호가 5번일 경우 리스트에 5 들어가기
            Itemlist.user_items.append(5)
            self.b_range += 1
            #print("폭탄 범위 증가")  # 중첩 가능
            return self.b_range
        elif value == 6:  # 아이템 번호가 6번일 경우 리스트에 6 들어가기
            Itemlist.user_items.append(6)
            self.b_count += 1
            #print("폭탄 개수 증가")  # 중첩 가능
            return self.b_count
        elif value in [7,8]:
            if int(value) not in Itemlist.user_items:
                # "7" 또는 "8"이 없을 때 실행할 코드
                if value == 7:  # 아이템 번호가 7번일 경우 리스트에 7 들어가기
                    Itemlist.user_items.append(7)
                    #print("방어")  # 중첩 불가능
                elif value == 8:  # 아이템 번호가 8번일 경우 리스트에 8 들어가기
                    Itemlist.user_items.append(8)
                    #print("던지기")  # 중첩 불가능
class Bomb:
    def __init__(self, x, y, user_imf, ticks):
        self.x = x
        self.y = y
        self.user_imf = user_imf
        self.ticks = ticks
        self.original_ticks = ticks
        self.user_items = [5, 6, 6, 6, 7, 8]
        self.bomb_list = []
        self.b_range = 3

    def tick(self, external_ticks=None):
        if external_ticks is not None:
            self.ticks = external_ticks

        if self.ticks == self.original_ticks + 4:
            print("폭탄이 터졌습니다!")

        return self.ticks

    def bomb_range(self):
        coordinates = []
        for i in range(-self.b_range, self.b_range + 1):
            if i != 0:
                coordinates.append((self.x + i, self.y))
            else:
                for j in range(-self.b_range, self.b_range + 1):
                    coordinates.append((self.x, self.y + j))
        up, down, left, right = [], [], [], []
        sort_list = []
        for x, y in coordinates:
            if x == self.x and y < self.y:  # 상
                up.append((x, y))
            elif x == self.x and y > self.y:  # 하
                down.append((x, y))
            elif y == self.y and x < self.x:  # 좌
                left.append((x, y))
            elif y == self.y and x > self.x:  # 우
                right.append((x, y))
        up.sort(reverse=True)
        down.sort()
        left.sort(reverse=True)
        right.sort()
        sort_list.append(up)
        sort_list.append(down)
        sort_list.append(left)
        sort_list.append(right)
        return sort_list

    def get_bomb_imf(self):
        return [self.x, self.y, self.user_imf, self.ticks, self.b_range]

    def bomb_count(self):  # 폭탄 개수 증가시키는 함수
        Itemlist.b_count += 1
        print(f"폭탄 개수가 1 증가하여 현재 폭탄 개수는 {Itemlist.b_count}개 입니다.")

        self.bomb_box()

        return Itemlist.b_count, 2

    def bomb_box(self):  # 폭탄이 담기는 리스트 함수
        new_bomb = Bomb(self.x, self.y, self.user_imf, self.original_ticks)
        for i in range(Itemlist.b_count):
            self.bomb_list.append(new_bomb)

    def bomb_count(self):  # 폭탄 개수 증가시키는 함수
        Itemlist.b_count += 1
        print(f"폭탄 개수가 1 증가하여 현재 폭탄 개수는 {Itemlist.b_count}개 입니다.")

        self.bomb_box()

        return Itemlist.b_count, 2

    def bomb_use(self): #폭탄을 사용하는 함수
        if Itemlist.b_count > 0:
            use_bomb = self.bomb_list.pop()
            print(f"폭탄 사용:{use_bomb}")
            Itemlist.b_count -= 1
            return use_bomb
        else:
            print("폭탄 부족")
            return None

    def use_bomb(self): #리스트에 담긴 폭탄 갯수만큼 사용 및 충전
        if 5 in self.user_items:
            print("폭탄을 사용합니다.")
            self.user_items.remove(6)
            time.sleep(2)
            self.user_items.append(6)
            print('폭탄이 충전되었습니다.')

    def bomb_range_increase(self):
        result = game_item.itemlist(value="5")
        if result:
            print("폭탄 범위가 +1 증가되었습니다.")
            bomb_instance.b_range += 1
            return True
        return False

class Map:
    def __init__(self, size=15): #size= 15 범위설정
        self.size = size
        self.map = self.create_map() #맵만드는 함수 구현(유저와 ai초기위치)
    def set_user_position(self, x, y):
        self.map[1][1] = "*"
        self.map[y][x] = 2
    def set_ai_position(self,x,y):
        self.map[13][13] = "*"
        self.map[y][x] = 3
    def del_user(self,x = 1,y = 1):
        if self.map[y][x] != 11:
            del self.map[y][x]
            self.map[y].insert(x, "*")
    def create_map(self): #맵만들기
        # 맵 초기화
        #self.set_user_position(1,1,0)
        game_map = [] #빈리스트 만들기

        for i in range(self.size):#15 행
            row = [] #행
            for j in range(self.size): #15 열
                if i == 0 or i == self.size - 1 or j == 0 or j == self.size - 1: #i가 0이거나 14이거나 j가 0이거나 j=14이거나
                    row.append(0)  # 외벽
                elif i % 2 == 0 and j % 2 == 0:
                    row.append(1)  # 고정 벽
                else:
                    row.append('-')  # 빈 공간
            game_map.append(row)
        return game_map


    def set_bomb_position(self, x, y):
        self.map[y][x] = 11
    def break_wall(self): #아이템이 나오는 벽 만들기
        for i in range(1,self.size-1): #외곽 제외
            for j in range(1,self.size-1): #외곽 제외
                if self.map[i][j]=='-': #빈칸이라면?
                    if not (i<=3 and j<=3) or (i>=11 and j>=11) : #처음 위치에서 제외범위 만들기
                        if (i % 3 == 0 and j % 3 ==0)or(i % 3 == 1 and j % 3 ==1): #규칙성 식
                            self.map[i][j]=4 #좌표에 4찍기
        self.map[1][1] = 2
        self.map[13][13] = 3
    def remove_wall_in_bomb_range(self, bomb):
        sorted_ranges = bomb.bomb_range() #이중리스트
        if bomb.ticks==bomb.original_ticks+4:
            self.map[bomb.x][bomb.y] = "+"
            for direction_range in sorted_ranges:  # 상, 하, 좌, 우 방향별로 순회 밑에서 브레이크만나면 다음방향으로
                for x, y in direction_range: #상방향이면 거기안 원소들 x,y로 출력
                    if 0 <= x < self.size and 0 <= y < self.size:
                        # 장애물에 따라 처리
                        if self.map[x][y] in [0, 1]:
                            break  # 해당 방향으로의 폭발 중단 아무일도 안벌어지게하는거임
                        elif self.map[x][y] == 4:
                            ran_list = ['-', 5, 6, 7, 8]
                            probabilities = [0.2,0.2, 0.2, 0.2, 0.2]  # 각 아이템의 확률
                            # 무작위로 아이템 선택
                            selected = random.choices(ran_list, weights=probabilities)[0]
                            self.map[x][y] = selected  # 아이템 벽은 공백으로 제거
                            break
                        else:
                            self.map[x][y] = 9  # 폭발 범위 표시

    def clear_explosion(self,bomb):
        if bomb.ticks == bomb.original_ticks + 5:
            for i in range(self.size):
                for j in range(self.size):
                    if self.map[i][j] in [9, '+']:  # 폭발 범위 또는 폭탄 위치
                        self.map[i][j] = '*'
    def display_map(self): #사이사이 띄어쓰기넣어서 출력
        for row in self.map:
            row_string = ''
            for cell in row:
                row_string += str(cell) + ' '
            print(row_string)

    def get(self):
        return self.map




class Ai:
    def __init__(self, map, tick):     # 1. 설치된 폭탄 위치, 2. 사람 위치, 3.
        self.ai_tick = 0
        self.tick = tick
        self.ai_direction = random.random()

        self.ai_loc_x = 13
        self.ai_loc_y = 13

        self.map = map
        self.mask = []

        self.bomb_temp = Bomb
        self.bomb_range = self.bomb_temp.bomb_range
        print(self.bomb_range, "-----폭탄 범위")
        self.bomb_x = -1        # 임의의 폭탄 x 좌표
        self.bomb_y = -1       # 임의의 폭탄 y 좌표
        self.bomb_d = -1

        self.case = 10

    def make_mask(self):     # ai 주변 오브젝트 정보 추출
        mask = []
        temp_mask = {}
        for i in self.map[self.ai_loc_x-2:self.ai_loc_x+3]:
            line = []
            for j in i[self.ai_loc_y-2:self.ai_loc_y+3]:
                line.append(j)
            mask.append(line)
        return mask

    def find_bomb(self):        # 폭탄 탐색
        self.bomb_range = []
        print(self.bomb_range, "------------폭탄 범위")# 임의의 폭탄 범위
        for i in range(self.bomb_x-self.bomb_d, self.bomb_x+self.bomb_d+1):
            self.bomb_range.append([i,self.bomb_y])
        for j in range(self.bomb_y-self.bomb_d, self.bomb_y+self.bomb_d+1):
            self.bomb_range.append([self.bomb_x, j])
        print(self.bomb_range)
        for i in self.bomb_range:
            if self.ai_loc_x == i[0] and self.case > 1:
                print("폭탄 감지")
                self.case = 1
            else:
                print("없음")

    def action(self):
        if self.tick > self.ai_tick:
            self.ai_tick = self.tick
            self.mask = self.make_mask()
            print(self.make_mask(), "---------mask")
            # ai 기준 상하좌우 1칸씩(다음 이동 위치)
            self.ai_fw = [
                [self.ai_loc_x, self.ai_loc_y],
                [self.ai_loc_x+1, self.ai_loc_y],
                [self.ai_loc_x-1, self.ai_loc_y],
                [self.ai_loc_x, self.ai_loc_y-1],
                [self.ai_loc_x, self.ai_loc_y+1],
            ]
            self.find_bomb()
            print(self.case,"----------case")

            if self.case == 1:      # 폭탄 범위안에 ai가 있다면
                for move in self.ai_fw:
                    if move not in self.bomb_range:
                        self.ai_loc_x = move[0]
                        self.ai_loc_y = move[1]
                        # return self.ai_loc_x, self.ai_loc_y
            else:   # 주변에 아무것도 없음
                if self.ai_direction < 0.25:
                    self.ai_loc_x -= 1
                elif self.ai_direction < 0.5:
                    self.ai_loc_y -= 1
                elif self.ai_direction < 0.75:
                    self.ai_loc_x += 1
                else:
                    self.ai_loc_y += 1
                print(self.ai_loc_x, self.ai_loc_y, "---------xy")
            return self.ai_loc_x, self.ai_loc_y
    def set_ai_xy(self, x, y):
        self.ai_loc_x = x
        self.ai_loc_y = y
    def get_ai_xy(self):
        return self.ai_loc_x, self.ai_loc_y



class User:
    user_items = [7]

    def __init__(self):  # 시작 좌표 (1, 1)
        self.x = 1
        self.y = 1
        self.has_bomb = False
        self.is_die = False
        self.life_count = 3
        self.items = []
        self.shield_value = self.user_items.count(7)
        self.b_count = self.user_items.count(6)

    # def get_list(self):
    #     if (self.x == item x 좌표) and (self.y == item y 좌표):
    #         result = self.items.append()
    #         return result

    def move_x(self, direction):
        if direction == 4:
            self.x -= 1  # 왼쪽으로 이동
        elif direction == 6:
            self.x += 1  # 오른쪽으로 이동
        return self.x

    def move_y(self, direction):
        if direction == 2:
            self.y += 1  # 아래쪽으로 이동
        elif direction == 8:
            self.y -= 1  # 위쪽으로 이동
        return self.y

    def bomb(self, direction):
        if direction == 5:
            print("폭탄이 설치되었습니다.")
            self.has_bomb = True
            return True
        return False

    def die(self, bomb):
        player_x = self.x
        player_y = self.y
        bomb = bomb.bomb_range()
        for direction_range in bomb:
            if (direction_range[0][0] <= player_x <= direction_range[-1][0] and direction_range[-1][1] <= player_y <=
                    direction_range[0][1]):
                return True
        return False

    def life(self, bomb):
        if self.die(bomb_instance):
            if self.activate_shield():
                print("쉴드가 사용되었습니다.")
            elif self.life_count > 0:
                self.life_count -= 1
                print(f"목숨 -1, 남은 목숨 {self.life_count}개")
            elif self.life_count == 0:
                self.is_die = True
        return self.life_count

    def activate_shield(self):
        if game_item.shield_value == 1 and self.die(bomb_instance):  # 쉴드가 한 개 있을 때 폭탄에 닿게 되면
            game_item.shield_value = 0  # 쉴드가 0개로 됨
            return True
        return False

    def set_xy(self, x, y):
        self.x = x
        self.y = y
    def get_xy(self):
        return self.x, self.y


class Game():
    def __init__(self):
        pass

    def gui(self, tick ,map= [[]]):
        print("\n"*10)
        for i in range(len(map)):
            for j in range(len(map[i])):
                if map[i][j] == 0:
                    print("🟫", end=" ")  # 외벽
                elif map[i][j] == 1:
                    print("🟫", end=" ")  # 벽
                elif map[i][j] == 2:
                    print("🤖", end=" ")  # user
                elif map[i][j] == 3:
                    print("👾", end=" ")  # ai
                elif map[i][j] == 4:
                    print("🗑️", end=" ")  # 부숴지는 벽
                elif map[i][j] == 11:
                    print("💣", end=" ")  # user 폭탄
                elif map[i][j] == 9:
                    print("🎇", end=" ")  # user 폭탄 터지는 것
                elif map[i][j] == 5:
                    print("💥", end=" ")  #print("폭탄 범위 증가")  # 중첩 가능
                elif map[i][j] == 6:
                    print("➕", end=" ")  #print("폭탄 개수 증가")  # 중첩 가능
                elif map[i][j] == 7:
                    print("🛡️", end=" ")  #print("방어")  # 중첩 불가능
                elif map[i][j] == 8:
                    print("🏏", end=" ")  #print("던지기")  # 중첩 불가능
                # elif self.map[i][j] == 8:
                #     print("🧨", end=" ")  # ai 폭탄
                # elif self.map[i][j] == 4:
                #     print("🎆", end=" ")  # ai 폭탄 터지는 것
                elif map[i][j] == "*":
                    print("⬛", end=" ")  # 지나다닐수있는 길
                elif map[i][j] == "-":
                    print("⬛", end=" ")  # 지나다닐수있는 길
                elif map[i][j] == "+":
                    print("⬛", end=" ")  # 지나다닐수있는 길
                else:
                    print("🍀", end=" ")  # 아이템박스
            print()
        print("[Tick = {}]".format(tick))
        print("\n" * 2)
    def collision_check(self,x,y,dir,map = [[]]):
        if map[y][x] == 0 or map[y][x] == 1 or map[y][x] == 4:
            if dir == 2:
                y -= 1
            elif direction == 8:
                y += 1
            elif direction == 4:
                x += 1
            elif direction == 6:
                x -= 1
            return x, y
        else:
            return x, y

    def ai_collision_check(self,ai_x,ai_y,map=[[]]):
        if ai_x == 0:
            ai_x += 1
        elif ai_y == 0:
            ai_y += 1
        elif ai_x == 14:
            ai_x -= 1
        elif ai_y == 14:
            ai_y -= 1
        elif map[ai_y][ai_x] == 4:
            return ai_x, ai_y
            pass
        else:
            return ai_x, ai_y
        return ai_x, ai_y

    def item_check(self,x,y,map=[[]]):
        item_no = 200
        if map[y][x] == 5:
            item_no = 5
        elif map[y][x] == 6:
            item_no = 6
        elif map[y][x] == 7:
            item_no = 7
        elif map[y][x] == 8:
            item_no = 8
        return item_no



tick111 = 1
max = 10000
game_user = User()
game_map = Map()
game = Game()
game_map.create_map()
game_map.break_wall()
game_item = Itemlist()
x_ai_set = 13
y_ai_set = 13
bomb_instance = Bomb(0, 0, "user1", max)
x_set = 1
y_set = 1
game_ai = Ai(game_map.get(), tick111)
bomb_instance.bomb_range_increase()
while True:
    map = game_map.get()
    game.gui(tick111, map)
    #game_map.display_map()
    direction = int(input("이동 방향을 입력하세요 (2: 아래, 4: 왼쪽, 6: 오른쪽, 8: 위쪽): "))
    game_user.move_x(direction)
    game_user.move_y(direction)
    game_map.del_user(x_set, y_set)
    x_set, y_set = game_user.get_xy()
    x_set, y_set = game.collision_check(x_set, y_set, direction, map)
    item = game.item_check(x_set, y_set, map)
    print(item)
    game_user.set_xy(x_set, y_set)
    game_map.set_user_position(x_set, y_set)
    print(x_set, y_set)
    bomb_instance.bomb_count()
    if direction == 5:
        game_map.set_bomb_position(x_set, y_set)
        bomb_instance = Bomb(y_set, x_set, "user1", tick111)
        bomb_coordinates = bomb_instance.bomb_range()
        if x_set in bomb_coordinates:
            print("위험")
        else:
            print("플레이어가 안전함")
    else:
        print("현재 좌표: ({}, {})".format(x_set, y_set))
    bomb_instance.tick(tick111)
    game_map.remove_wall_in_bomb_range(bomb_instance)
    game_map.clear_explosion(bomb_instance)
    x_ai_set, y_ai_set = game_ai.get_ai_xy()
    x_ai_set, y_ai_set = game.ai_collision_check(x_ai_set, y_ai_set, map)
    game_ai.action()
    game_ai.set_ai_xy(x_ai_set, y_ai_set)
    game_map.set_ai_position(x_ai_set, y_ai_set)

    tick111 += 1