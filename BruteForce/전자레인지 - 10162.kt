import java.io.*

fun main() = with(BufferedReader(InputStreamReader(System.`in`))) {
    val buttons = arrayOf(300, 60, 10)
    var t = readLine().toInt()
    val answer = arrayOf(0, 0, 0)
    
    for (i in 0..2) {
        var x = t / buttons[i].toInt()
        t -= x * buttons[i]
        answer[i] = x
    }
    
    if (t > 0) print(-1)
    else for (x in answer) print("$x ")
}
