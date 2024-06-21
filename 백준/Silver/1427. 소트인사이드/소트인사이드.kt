fun sortDigitsDesc() {
    // 입력 받는 부분
    val n = readLine()!!
    
    // 각 자리수를 분리하고 내림차순으로 정렬
    val sortedN = n.toList().sortedDescending()
    
    // 정렬된 리스트를 다시 문자열로 결합하여 출력
    val sortedNStr = sortedN.joinToString("")
    println(sortedNStr)
}

fun main() {
    sortDigitsDesc()
}