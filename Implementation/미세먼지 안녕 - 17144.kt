import java.io.*

fun main() = with(BufferedReader(InputStreamReader(System.`in`))) {
    val dx = arrayOf(1, -1, 0, 0)
    val dy = arrayOf(0, 0, 1, -1)
    val purifiers = Array(2, { -1 })

    val (r, c, t) = readLine().split(' ').map{ it.toInt() }
    val room = Array(r) { IntArray(c) }
    
    for (y in 0 until r) {
        val temp = readLine().split(' ').map{ it.toInt() }.toIntArray()
        for (x in 0 until c) {
            if (temp[x] == -1) {
                // 첫번째로 발견되는 공기청정기가 위쪽 공기청정기
                if (purifiers[0] != -1) purifiers[1] = y
                else purifiers[0] = y
            }
            room[y][x] = temp[x]
        }
        room[y] = temp
    }
    
    fun spread(y: Int, x: Int, change: Array<IntArray>) {
        var count = 0
        
        for (i in 0 until 4) {
            var nx = x + dx[i]
            var ny = y + dy[i]
            
            if (nx < 0 || nx >= c || ny < 0 || ny >= r || room[ny][nx] == -1) continue
            
            change[ny][nx] += room[y][x] / 5
            count += 1
        }
        
        room[y][x] -= (room[y][x] / 5) * count
    }
    
    fun circulate(position: Int, isUp: Boolean) {
        var y = position; var x = 1
        
        if (isUp) {
            // 반시계 방향 순환
            var temp1 = room[y][x]
            room[y][x] = 0
            while (x < c - 1) {
                x += 1
                var temp2 = room[y][x]
                room[y][x] = temp1
                temp1 = temp2
            }
            while (y > 0) {
                y -= 1
                var temp2 = room[y][x]
                room[y][x] = temp1
                temp1 = temp2
            }
            while (x > 0) {
                x -= 1
                var temp2 = room[y][x]
                room[y][x] = temp1
                temp1 = temp2
            }
            // 공기청정기쪽으로 이동한 미세먼지는 제거
            while (y < position) {
                y += 1
                var temp2 = room[y][x]
                if (y != position) room[y][x] = temp1
                temp1 = temp2
            }
        } else {
            // 시계 방향 순환
            var temp1 = room[y][x]
            room[y][x] = 0
            while (x < c - 1) {
                x += 1
                var temp2 = room[y][x]
                room[y][x] = temp1
                temp1 = temp2
            }
            while (y < r - 1) {
                y += 1
                var temp2 = room[y][x]
                room[y][x] = temp1
                temp1 = temp2
            }
            while (x > 0) {
                x -= 1
                var temp2 = room[y][x]
                room[y][x] = temp1
                temp1 = temp2
            }
            // 공기청정기쪽으로 이동한 미세먼지는 제거
            while (y > position) {
                y -= 1
                var temp2 = room[y][x]
                if (y != position) room[y][x] =  temp1
                temp1 = temp2
            }
        }
    }
    
    repeat(t) {
        val change = Array(r, { IntArray(c, { 0 })})
        
        // 공기를 확산시킴
        for (y in 0 until r) {
            for (x in 0 until c) {
                if (room[y][x] > 0) spread(y, x, change)
            }
        }
        
        // 변경사항 반영
        for (y in 0 until r) {
            for (x in 0 until c) {
                if (change[y][x] > 0) room[y][x] += change[y][x]
            }
        }
        
        // 공기청정기 가동
        circulate(purifiers[0], true)
        circulate(purifiers[1], false)
    }
    
    // -1로 표시된 공기청정기 고려하여 미세먼지 총량 출력
    print(room.map { it.sum() }.sum() + 2)
}
