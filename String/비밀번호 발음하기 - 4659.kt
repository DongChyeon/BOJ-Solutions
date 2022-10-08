import java.io.*

fun main() = with(BufferedReader(InputStreamReader(System.`in`))) {
    while (true) {
        var pw = readLine()
        if (pw == "end") break
        
        if (isAcceptablePw(pw)) {
            println("<$pw> is acceptable.")
        } else {
            println("<$pw> is not acceptable.")
        }
    }
}

fun isAcceptablePw(pw: String) : Boolean {
    // 모음 포함하는지 검사
    if (!pw.contains('a') && !pw.contains('e') && !pw.contains('i') && !pw.contains('o') && !pw.contains('u')) {
        return false
    }
    
    // 자음이나 모음이 세 번이상 반복되는지 검사
    for (i in 0..pw.length - 3) {
        if (isConsonant(pw[i]) && isConsonant(pw[i + 1]) && isConsonant(pw[i + 2])) return false
        if (isVowel(pw[i]) && isVowel(pw[i + 1]) && isVowel(pw[i + 2])) return false
    }
    
    // e 와 o 가 아닌 글자가 두 번이상 반복되는지 검사
    for (i in 0..pw.length - 2) {
        if (pw[i] == pw[i + 1] && pw[i] != 'e' && pw[i] != 'o') return false
    }

    return true
}

fun isConsonant(chr: Char) : Boolean {
    if (chr != 'a' && chr != 'e' && chr != 'i' && chr != 'o' && chr != 'u') {
        return true
    }
    return false
}

fun isVowel(chr: Char) : Boolean{
    if (chr == 'a' || chr == 'e' || chr == 'i' || chr == 'o' || chr == 'u') {
        return true
    }
    return false
}
