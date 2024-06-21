fun main() {
    val n = readLine()!!.toInt()
    val points = mutableListOf<Pair<Int,Int>>()
    repeat(n){
        val (x,y) = readLine()!!.split(" ").map{it.toInt()}
        points.add(Pair(x,y))
    }
    points.sortWith(compareBy({it.first},{it.second}))
    points.forEach{(x,y)->
    	println("$x $y")
    }  
}