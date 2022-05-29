import java.io.*
import java.util.*

fun dfs(graph: ArrayList<ArrayList<Int>>, v: Int, visited: BooleanArray) {
    // 현재 노드를 방문 처리
    visited[v] = true
    print("$v ")
    // 현재 노드와 연결된 다른 노드를 재귀적으로 방문
    for (i in graph[v]) {
        if (!visited[i]) dfs(graph, i, visited)
    }
}

fun bfs(graph: ArrayList<ArrayList<Int>>, v: Int, visited: BooleanArray) {
    // 현재 노드를 방문 처리
    visited[v] = true
    val queue: Queue<Int> = LinkedList<Int>()
    queue.add(v)
    // 큐가 빌 때까지 반복
    while (queue.isNotEmpty()) {
        // 큐에서 하나의 원소를 뽑아 출력
        var vtx = queue.poll()
        print("$vtx ")
        for (i in graph[vtx]) {
            if (!visited[i]) {
                queue.add(i)
                visited[i] = true
            }
        }
    }
}

fun main() = with(BufferedReader(InputStreamReader(System.`in`))) {
    val (n, m, v) = readLine().split(' ').map{ it.toInt() }
    val graph = ArrayList<ArrayList<Int>>()
    repeat(n + 1) {
        graph.add(ArrayList())
    }
    repeat(m) {
        val (start, end) = readLine().split(' ').map{ it.toInt() }
        graph[start].add(end)
        graph[end].add(start)
    }
    for (i in 1..n) graph[i].sort()
    
    var visited = BooleanArray(n + 1) { false }
    dfs(graph, v, visited)
    
    println()
    
    visited = BooleanArray(n + 1) { false }
    bfs(graph, v, visited)
}
