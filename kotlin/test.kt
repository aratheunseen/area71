fun bioData(name : String = "Ash", age : Int) : String {
    println("Its working!");
    return "Hello, $name! You are $age years old."
}

fun main() {
    println(bioData(name="Arman", age=11))
}