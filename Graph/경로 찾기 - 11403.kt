import java.io.*

fun main() = with(BufferedReader(InputStreamReader(System.`in`))) {
    val INF = 1000000000
    val n = readLine().toInt()
    val graph = Array(n) { IntArray(n) }
    
    for (y in 0 until n) {
        val temp = readLine().split(' ').map{ it.toInt() }.toIntArray()
        for (x in 0 until n) {
            // 0일 경우 거리를 INF로 설정
            if (temp[x] == 0) graph[y][x] = INF
            else graph[y][x] = temp[x]
        }
    }
    
    // 플로이드 워셜 알고리즘 이용
    for (k in 0 until n) {
        for (a in 0 until n) {
            for (b in 0 until n) {
                graph[a][b] = minOf(graph[a][b], graph[a][k] + graph[k][b])
            }
        }
    }
    
    // 거리가 INF(닿을 수 없음)이 아닐 경우 1 출력
    for (y in 0 until n) {
        for (x in 0 until n) {
            if (graph[y][x] == INF) print("0 ")
            else print("1 ")
        }
        println()
    }
}
