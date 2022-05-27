fun main() {
    val comb = Array(30) { Array(30) {0} }
    comb[1][0] = 1
    comb[1][1] = 1
    for (i in 2 until 30) {
        for (j in 0..i) {
            if (j == 0 || j == i) {
                comb[i][j] = 1
            } else {
                // nCr = n-1Cr-1 + n-1Cr
                comb[i][j] = comb[i - 1][j - 1] + comb[i - 1][j]
            }
        }
    }

    val t = readLine()!!.toInt()
    repeat (t) {
        val tmp = readLine()!!.split(' ')
        val n = tmp[0].toInt(); val m = tmp[1].toInt()
        
        println(comb[m][n])
    }
}
