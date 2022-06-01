import java.io.*

fun main() = with(BufferedReader(InputStreamReader(System.`in`))) {
    val parts = readLine().split('-').toTypedArray()
    // +부분을 모두 먼저 더함 (괄호를 침) 
    for (i in parts.indices) {
        val plus_parts = parts[i].split('+').map{ it.toInt() }.toIntArray()
        parts[i] = plus_parts.sum().toString()
    }
    
    // +한 부분들을 모두 빼줌
    var answer = parts[0].toInt()
    for (i in 1 until parts.size) answer -= parts[i].toInt()
    
    print(answer)
}
