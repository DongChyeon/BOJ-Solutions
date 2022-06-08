import java.io.*

val image = Array(2187, { CharArray(2187, { ' ' } ) })

fun solve(x: Int, y: Int, num: Int) {
    if (num == 1) {
        image[y][x] = '*'
        return
    }
    // 9개의 정사각형으로 쪼개서 해결
    for (i in 0..2) {
        for (j in 0..2) {
            // 아래 조건문은 가운데만 비우기 위함
            if (i != 1 || j != 1) solve(y + (i * num / 3), x + (j * num / 3), num / 3)
        }
    }
}

fun main() = with(BufferedReader(InputStreamReader(System.`in`))) {
    val bw = BufferedWriter(OutputStreamWriter(System.out))
    val n = readLine().toInt()
    solve(0, 0, n)
    
    for (i in 0..n - 1) {
        for (j in 0..n - 1) {
            bw.write(image[i][j].toString())
        }
        bw.write("\n")
    }
    bw.flush()
    bw.close()
}
