import java.io.*
import java.util.*

fun main() = with(BufferedReader(InputStreamReader(System.`in`))) {
    var n = readLine().toInt()
    var dict = HashMap<String, Int>()
    
    for (i in 1..n) {
        var (name, extension) = readLine().split('.')
        
        if (dict.containsKey(extension)) {
            dict[extension] = dict[extension]!! + 1
        } else {
            dict[extension] = 1
        }
    }

    for ((key, value) in dict.toSortedMap()) {
        println("${key} ${value}")
    }
}
