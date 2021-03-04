x, y, w, h = map(int, input().split())
# 상하좌우 중 변과의 가장 거리가 짧은 쪽을 출력
print(min(w - x, h - y, x, y))