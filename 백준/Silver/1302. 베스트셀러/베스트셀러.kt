import java.util.*

fun main() {
    val scanner = Scanner(System.`in`)
    val n = scanner.nextInt()
    scanner.nextLine() // 개행 문자 처리

    val bookCounts = mutableMapOf<String, Int>()

    for (i in 0 until n) {
        val bookTitle = scanner.nextLine()
        bookCounts[bookTitle] = bookCounts.getOrDefault(bookTitle, 0) + 1
    }

    val maxCount = bookCounts.values.maxOrNull() ?: 0
    val bestSellers = bookCounts.filter { it.value == maxCount }.keys.sorted()

    println(bestSellers.first())
}