import java.io.*
import java.util.*

fun main() = with(BufferedReader(InputStreamReader(System.`in`))) {
    val t = readLine().toInt()
    
    for (i in 0 until t) {
        var cost: Long = 0
    
        val k = readLine().toInt()
        val pq = PriorityQueue<Long>()
        pq.addAll(readLine().split(' ').map{ it.toLong() })
        
        // 가장 비용이 적은 두 파일 먼저 합침
        while (pq.size > 1) {
            var page = pq.poll() + pq.poll()
            cost += page
            pq.add(page)
        }
        println(cost)
    }
}
