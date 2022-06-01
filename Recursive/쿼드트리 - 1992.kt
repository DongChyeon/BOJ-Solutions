import java.io.*

var answer = ""

// size만큼의 이미지가 같은 색인지 판별
fun check(image: Array<IntArray>, x: Int, y: Int, size: Int): Boolean {
    val color = image[y][x]
    for (i in y until y + size) {
        for (j in x until x + size) {
            if (image[i][j] != color) return false
        }
    }
    
    return true
}

// 이미지가 같은 색이 아니라면 4분할
fun divide(image: Array<IntArray>, x: Int, y: Int, size: Int) {
    if (check(image, x, y, size)) answer += image[y][x].toString()
    else {
        val nsize = size / 2
        answer += "("
        for (i in 0 until 2) {
            for (j in 0 until 2) {
                divide(image, x + nsize * j, y + nsize * i, nsize)
            }
        }
        answer += ")"
    }
}

fun main() = with(BufferedReader(InputStreamReader(System.`in`))) {
    val n = readLine().toInt()
    val image = Array(n, { IntArray(n) })
    
    for (y in 0 until n) {
        val temp = readLine()
        for (x in 0 until n) {
            image[y][x] = temp[x].digitToInt()
        }
    }
    
    divide(image, 0, 0, n)
    
    print(answer)
}
