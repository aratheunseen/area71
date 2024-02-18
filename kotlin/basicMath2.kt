fun main() {
    val firstNumber = 10
    val secondNumber = 5
    val thirdNumber = 8
    
    val result = add(firstNumber, secondNumber)
    val anotherResult = add(firstNumber, thirdNumber)
    val subtractResult = subtract(firstNumber, secondNumber)

    println("$firstNumber + $secondNumber = $result")
    println("$firstNumber + $thirdNumber = $anotherResult")
   	println("$firstNumber - $secondNumber = $subtractResult")
}

fun add(first:Int, second:Int) : Int {
    return first + second;
}

fun subtract(first:Int, second:Int) : Int {
    return first - second;
}