import java.util.Scanner

fun main(){
    val scanner = Scanner(System.`in`)
    val N = scanner.nextInt()
    scanner.nextLine()
    
    var checkedWord = 0
    for (i in 0 until N){
        val word = scanner.nextLine().trim()
        val seen = mutableSetOf<Char>()
        var lastSeen:Char? = null
        var isGroupWord = true
        
        for (char in word){
            if (char in seen&&lastSeen!=char){
                isGroupWord = false
                break
            } else{
                seen.add(char)
                lastSeen = char
            }
        }
        if (isGroupWord){
            checkedWord += 1
        }
    }
    println(checkedWord)
}