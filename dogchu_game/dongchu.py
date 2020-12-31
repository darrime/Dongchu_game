import pygame
import random

pygame.init()  # 초기화 작업 (반드시 필요)

# 화면 크기 설정
screen_width = 1280  # 가로 크기
screen_height = 720  # 세로 크기
screen = pygame.display.set_mode((screen_width, screen_height))

# 화면 타이틀
pygame.display.set_caption("dongchu game")  # 게임 이름

# FPS
clock = pygame.time.Clock()

# 배경 이미지 불러오기
background = pygame.image.load("C:\python_test\dongchugame_background.jpg")

# 캐릭터 불러오기
character = pygame.image.load("C:\python_test\character_space.jpg")
character_size = character.get_rect().size  # 이미지의 크기 구해옴
character_width = character_size[0]  # 세로 크기
character_height = character_size[1]  # 가로 크기
character_x_pos = (screen_width / 2) - (character_width / 2)  # 화면 가로의 절반 크기
character_y_pos = screen_height - character_height

# 이동할 좌표
to_x = 0
to_y = 0

# 이동 속도
character_speed = 0.6

# 적 캐릭터
enemy = pygame.image.load("C:\python_test\enemy_usung.jpg")
enemy_size = character.get_rect().size  # 이미지의 크기 구해옴
enemy_width = enemy_size[0]  # 세로 크기
enemy_height = enemy_size[1]  # 가로 크기
enemy_x_pos = (screen_width / 2) - (enemy_width / 2)  # 화면 가로의 절반 크기
enemy_y_pos = (screen_height / 2) - (enemy_height / 2)

# 폰트 정의
game_font = pygame.font.Font(None, 40)  # 폰트객체 생성, (폰트, 크기)

# 총 시간
total_time = 10

# 시작 시간 정보
start_ticks = pygame.time.get_ticks()

# 이벤트 루프
running = True  # 게임이 진행중인가?
while running:
    dt = clock.tick(144)  # 게임화면의 초당 프레임 수를 설정

    # 캐릭터가 1초 동안에 100만큼 이동을 해야함
    # 10 fps : 1초 동안에 10번 동작 -> 100 / 10 = 10(번동작)
    # 20 fps : 1초 동안에 20번 동작 -> 100 / 20 = 5(번 동작)

    for event in pygame.event.get():  # 어떤 이벤트가 발생하였는가?
        if event.type == pygame.QUIT:  # 창이 닫히는 이벤트가 발생하였는가?
            running = False  # 게임이 진행중이 아님

        if event.type == pygame.KEYDOWN:  # 키가 눌러졌는지 확인
            if event.key == pygame.K_LEFT:  # 캐릭터를 왼쪽으로
                to_x = to_x - character_speed
            elif event.key == pygame.K_RIGHT:  # 캐릭터를 오른쪽으로
                to_x = to_x + character_speed
            elif event.key == pygame.K_UP:  # 캐릭터를 위쪽으로
                to_y = to_y - character_speed
            elif event.key == pygame.K_DOWN:  # 캐릭터를 아래쪽으로
                to_y = to_y + character_speed

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                to_x = 0
            elif event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                to_y = 0

    character_x_pos += to_x * dt
    character_y_pos += to_y * dt

    # 가로 경계값 처리
    if character_x_pos < 0:
        character_x_pos = 0
    elif character_x_pos > screen_width - character_width:
        character_x_pos = screen_width - character_width

    # 세로 경계값 처리
    if character_y_pos < 0:
        character_y_pos = 0
    elif character_y_pos > screen_height - character_height:
        character_y_pos = screen_height - character_height

    # 충돌 처리를 위한 rect 정보 업데이트
    character_rect = character.get_rect()
    character_rect.left = character_x_pos
    character_rect.top = character_y_pos

    enemy_rect = enemy.get_rect()
    enemy_rect.left = enemy_x_pos
    enemy_rect.top = enemy_y_pos

    # 충돌 체크
    if character_rect.colliderect(enemy_rect):
        print("충돌했어요")
        running = False

    # 경과 시간 계산
    elapsed_time = (pygame.time.get_ticks() - start_ticks) / 1000
    timer_1 = total_time - elapsed_time
    fortune = random.randrange(1, 10)
    # if timer_1 < 0:
    # print("시간 초과")
    # running = False

    # 경과 시간(ms) 를 1000 으로 나누어서 초(s) 단위로 표시
    timer = game_font.render(str(int(total_time - elapsed_time)), True, (0, 0, 0))
    stopwatch = game_font.render(str(int(elapsed_time)), True, (0, 0, 0))

    screen.blit(background, (0, 0))  # 배경 그리기
    screen.blit(character, (character_x_pos, character_y_pos))  # 캐릭터 그리기
    screen.blit(enemy, (enemy_x_pos, enemy_y_pos))
    screen.blit(timer, (10, 10))
    # screen.blit(stopwatch, (10, 10))

    pygame.display.update()  # 게임화면을 다시 그리기!(중요)

# pygame 종료
pygame.quit()