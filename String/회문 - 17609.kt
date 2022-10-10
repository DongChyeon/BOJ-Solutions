import java.io.*

fun main() = with(BufferedReader(InputStreamReader(System.`in`))) {
    val n = readLine().toInt()
    
    for (i in 1..n) {
        val str = readLine()
        println(solve(str, false, 0, str.length - 1))
    }
}

fun solve(str: String, delChr: Boolean, p1: Int, p2: Int) : Int {
    var (left, right) = arrayOf(p1, p2)
    
    while (left < right) {
        if (str[left] == str[right]) {
            left += 1
            right -= 1
        } else {
            // 글자를 삭제한 적이 없으면 한 글자를 건너뛰면 회문이 되는지 판별
            if (!delChr && (solve(str, true, left + 1, right) == 0 || solve(str, true, left, right - 1) == 0)) {
                return 1
            }
            return 2
        }
    }
    
    return 0
}
