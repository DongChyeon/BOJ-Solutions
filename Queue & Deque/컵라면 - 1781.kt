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

    // 푼 문제들을 담는 우선순위 큐 (최소 힙)
    val pq2 = PriorityQueue<Int> { a, b -> a.compareTo(b) }

    while (pq.isNotEmpty()) {
        var temp = pq.poll()
        // 데드 라인이 푼 문제 수 보다 작을 경우 진행
        if (pq2.size < temp.first) {
            pq2.add(temp.second)
        } else {
            // 푼 문제 수가 데드 라인보다 크면
            // 가장 적게 라면을 준 문제보다 현재 문제를 푸는 것이 이득인지 고려
            if (temp.second > pq2.peek()) {
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
