import java.io.*

fun main() = with(BufferedReader(InputStreamReader(System.`in`))) {
    val (n, m) = readLine().split(' ').map{ it.toInt() }
    val trees = readLine().split(' ').map{ it.toLong() }.toLongArray()
    var start = 0L; var end = trees.maxOrNull()!!.toLong()
    
    // 이분 탐색을 통해 절단할 높이를 찾아냄
    while (start <= end) {
        var mid = (start + end) / 2L
        var total = trees.sumOf{ if (it < mid) 0L else it - mid }
        
        if (total < m) end = mid -1
        else start = mid + 1
    }    
    print(start - 1)
}
