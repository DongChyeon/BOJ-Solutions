import java.io.*
import java.util.*

fun main() = with(BufferedReader(InputStreamReader(System.`in`))) {
    val n = readLine().toInt()
    // 우선 순위 큐 구현 (데드 라인↓, 컵라면↑)
    val pq = PriorityQueue { a: Pair<Int, Int>, b: Pair<Int, Int> -> 
    	when {
            a.first != b.first -> a.first.compareTo(b.first)
            else -> b.second.compareTo(a.second)
        }
    }
    
    for (i in 0 until n) {
        var (deadline, ramen) = readLine().split(' ').map{ it.toInt() }
        pq.add(Pair(deadline, ramen))
    }
    
    // 고른 선택을 담는 우선순위 큐 (최소 힙)
    val pq2 = PriorityQueue<Int> { a, b -> a.compareTo(b) }
    var hour = 1
    
    while (pq.isNotEmpty()) {
        var temp = pq.poll()
        // 데드 라인이 걸린 시간보다 같거나 크면 진행
        if (hour <= temp.first) {
            pq2.add(temp.second)
            hour++
        } else {
            // 이전 선택을 안 고른게 더 이득일 경우
            if (pq2.peek() < temp.second) {
                pq2.poll()
                pq2.add(temp.second)
            }
        }
    }
    
    var answer: Long = 0
    while (pq2.isNotEmpty()) {
        answer += pq2.poll()
    }
    println(answer)
}
