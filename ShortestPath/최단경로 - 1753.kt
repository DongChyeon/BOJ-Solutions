import java.io.*
import java.util.*

fun main() = with(BufferedReader(InputStreamReader(System.`in`))) {
    val INF = 1000000000
    val (v, e) = readLine().split(' ').map{ it.toInt() }
    val start = readLine().toInt()
    val graph = ArrayList<ArrayList<Pair<Int, Int>>>()
    repeat(v + 1) {
        graph.add(ArrayList())
    }
    repeat(e) {
        val (a, b, c) = readLine().split(' ').map{ it.toInt() }
        graph[a].add(Pair(b, c))
    }
    val distance = Array(v + 1, { INF })
    
    // 다익스트라 알고리즘으로 각 정점까지의 최단거리르 구함
    // 힙을 우선순위큐로 대체
    val pq = PriorityQueue<Pair<Int, Int>>(compareBy{ it.first })
    pq.add(Pair(0, start))
    distance[start] = 0
    while (pq.isNotEmpty()) {
        val (dist, now) = pq.poll()
        if (distance[now] < dist) continue
        // first : 도착점, second : 비용
        for (i in graph[now]) {
            val cost = dist + i.second
            if (cost < distance[i.first]) {
                distance[i.first] = cost
                pq.add(Pair(cost, i.first))
            }
        }
    }
    
    for (i in 1 until distance.size) {
        if (distance[i]== INF) println("INF")
        else println(distance[i])
    }
}
