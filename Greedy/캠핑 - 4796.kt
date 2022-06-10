import java.io.*
import kotlin.math.*

fun main() = with(BufferedReader(InputStreamReader(System.`in`))) {
    var count = 0
    
    while (true) {
        count += 1
        var (l, p, v) = readLine().split(' ').map{ it.toInt() }
        // 0 0 0 을 입력하면 종료
        if (l == 0 && p == 0 && v == 0) break
        var div = (v / p).toInt()
        var answer = l * div + min((v - p * div), l)
        
        println("Case $count: $answer")
    }
}
