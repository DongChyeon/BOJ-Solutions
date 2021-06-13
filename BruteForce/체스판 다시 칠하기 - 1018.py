import sys

input = sys.stdin.readline
n, m = map(int, input().split())
maze = [list(input().rstrip()) for _ in range(n)]
case_a = [list("WBWBWBWB"), list("BWBWBWBW"), list("WBWBWBWB"), list("BWBWBWBW"), list("WBWBWBWB"), list("BWBWBWBW"), list("WBWBWBWB"), list("BWBWBWBW")] 
case_b = [list("BWBWBWBW"), list("WBWBWBWB"), list("BWBWBWBW"), list("WBWBWBWB"), list("BWBWBWBW"), list("WBWBWBWB"), list("BWBWBWBW"), list("WBWBWBWB")]
answer = 64

# 8 x 8 크기로 체스판 탐색
for start_y in range(0, len(maze) - 7):
    for start_x in range(0, len(maze[0]) - 7):
        # 첫 타일이 흰색으로 시작하는 경우
        repaint_a = 0
        for y in range(start_y, start_y + 8):
            for x in range(start_x, start_x + 8):
                if case_a[y - start_y][x - start_x] != maze[y][x]:
                    repaint_a += 1
        # 첫 타일이 검은색으로 시작하는 경우            
        repaint_b = 0
        for y in range(start_y, start_y + 8):
            for x in range(start_x, start_x + 8):
                if case_b[y - start_y][x - start_x] != maze[y][x]:
                    repaint_b += 1
                    
        answer = min(repaint_a, repaint_b, answer)
                    
print(answer)
