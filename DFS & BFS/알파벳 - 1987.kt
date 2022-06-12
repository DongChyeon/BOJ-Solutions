import java.io.*
import kotlin.math.*

val dx = arrayOf(1, -1, 0, 0)
val dy = arrayOf(0, 0, 1, -1)
var nx = 0; var ny = 0
var r = 0; var c = 0
lateinit var board : Array<CharArray>
lateinit var alphabet : BooleanArray
var answer = 0

fun dfs(x: Int, y: Int, count: Int) {
    // 이동했을 때 방문한 알파벳이 이미 방문한 알파벳이라면 탐색 종료
    if (alphabet[board[y][x].code - 65]) {
        answer = max(answer, count)
        return
    }
    
    // 이동한 알파벳에 방문 표시를 함
    alphabet[board[y][x].code - 65] = true
    for (i in 0 until 4) {
        nx = x + dx[i]
        ny = y + dy[i]
        // 보드의 범위를 넘어가지 않도록 함
        if (nx < 0 || nx >= c || ny < 0 || ny >= r) continue
        dfs(nx, ny, count + 1)
    }
    alphabet[board[y][x].code - 65] = false
}

fun main() = with(BufferedReader(InputStreamReader(System.`in`))) {
    val rc = readLine().split(' ').map{ it.toInt() }
    r = rc[0]; c = rc[1]
    board = Array(r) { CharArray(c) }
    alphabet = BooleanArray(26)
    for (i in 0 until r) {
        var temp = readLine()
        for (j in 0 until c) board[i][j] = temp[j] 
    }
    
    dfs(0, 0, 0)
    print(answer)
}
