import java.io.*

fun main() = with(BufferedReader(InputStreamReader(System.`in`))) {
    val (n, m, b) = readLine().split(' ').map{ it.toInt() }
    val field = Array(n) { IntArray(m) }
    for (i in 0 until n) field[i] = readLine().split(' ').map{ it.toInt() }.toIntArray()
    var (cost, height) = arrayOf(1000000000, 0)
    
    for (h in 0..256) {
        // 쌓아야할 블록과 제거해야할 블록을 계산함
        var (build, remove) = arrayOf(0, 0)
        for (i in 0 until n) {
            for (j in 0 until m) {
                if (h > field[i][j]) build += h - field[i][j]
                else remove += field[i][j] - h
            }
        }
        
        // (인벤토리에 있는 블록 + 제거해야할 블록)이 쌓아야할 블록과 같거나 클 경우 소요시간 계산
        if (remove + b >= build) {
            if (cost >= remove * 2 + build) {
                cost = remove * 2 + build
                height = h
            }
        }
    }
    
    print("$cost $height")
