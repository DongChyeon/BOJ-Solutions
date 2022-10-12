import java.io.*
import java.util.*
import kotlin.collections.*

fun main() = with(BufferedReader(InputStreamReader(System.`in`))) {
    var (n, m) = readLine().split(' ').map{ it.toInt() }
    var pick = readLine().split(' ').map{ it.toInt() }
    val deque = ArrayDeque<Int>()
    for (i in 1..n) deque.add(i)
    
    var answer = 0
    var rotate_cnt = 0
    var rotate_direction = ""
    
    // 큐가 빌때까지 진행
    for (i in 0 until m) {
        if (deque.size - deque.indexOf(pick[i]) < deque.indexOf(pick[i])) {
            rotate_cnt = deque.size - deque.indexOf(pick[i])
            rotate_direction = "right"
        } else {
            rotate_cnt = deque.indexOf(pick[i])
            rotate_direction = "left"
        }
        
        answer += rotate_cnt
        
        if (rotate_direction == "right") {
            for (i in 1..rotate_cnt) deque.addFirst(deque.removeLast())
        } else {
            for (i in 1..rotate_cnt) deque.addLast(deque.removeFirst())
        }

        deque.removeFirst()
    }

    println(answer)
}
