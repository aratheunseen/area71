fun main() {
    println("Have I spent more time using my phone today: ${compareTime(300, 250)}")
    println("Have I spent more time using my phone today: ${compareTime(300, 300)}")
}

fun compareTime(timeSpentToday: Int, timeSpentYesterday: Int) : Boolean {
    return timeSpentToday > timeSpentYesterday
}