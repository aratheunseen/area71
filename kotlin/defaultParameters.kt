fun main() {
    val operatingSystem = "Chrome OS"
    val emailId = "sample@gmail.com"

    println(displayAlertMessage(operatingSystem, emailId))
}

// Define your displayAlertMessage() below this line.
fun displayAlertMessage(operatingSystem : String, emailId : String) : String {
    return "There's a new sign-in request on $operatingSystem for your Google Account $emailId."
}