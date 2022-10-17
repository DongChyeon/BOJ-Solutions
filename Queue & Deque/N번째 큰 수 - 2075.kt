import java.io.*
import java.util.*

fun main() = with(BufferedReader(InputStreamReader(System.`in`))) {
    val n = readLine().toInt()
    // 최대 힙 구현
    val pq = PriorityQueue<Int> { a, b -> b.compareTo(a) }
    
    for (i in 0 until n) {
        val temp = readLine().split(' ').map{ it.toInt() }
        for (j in 0 until n) {
            pq.add(temp[j])
        }
    }
    
    for (i in 1 until n) pq.poll()
    println(pq.poll())
}
