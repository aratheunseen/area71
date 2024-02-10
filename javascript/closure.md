A closure in JavaScript is a function that has access to its own scope, the outer function's scope, and the global scope. Closures have access to:

1. Their own scope - variables defined between its curly brackets
2. The outer function's scope - variables defined in the function's parent function
3. The global scope - variables defined outside of all functions

Closures are created every time a function is created, at function creation time.

Here's an example of a closure:

```javascript
function outerFunction(outerVariable) {
  return function innerFunction(innerVariable) {
    console.log('outerVariable:', outerVariable);
    console.log('innerVariable:', innerVariable);
  }
}

const newFunction = outerFunction('outside');
newFunction('inside'); // Logs: outerVariable: outside and innerVariable: inside
```

In this example, `innerFunction` is a closure that is returned from `outerFunction`. `innerFunction` has access to:

1. Its own scope - it has access to `innerVariable`
2. The outer function's scope - it has access to `outerVariable`
3. The global scope - it would have access to any global variables

When we call `newFunction('inside')`, the `innerFunction` is invoked. Even though `outerFunction` has finished execution, `innerFunction` still has access to `outerVariable` due to the closure. This is a powerful feature of JavaScript, and it's one of the reasons why closures are used in many JavaScript patterns.

---
---

Working with closures in JavaScript can be tricky, and there are several common pitfalls to be aware of:

1. **Unintended Capturing of Variables**: When a closure captures a variable, it's actually capturing the variable itself, not a snapshot of its value at the time the closure is created. If the variable's value changes after the closure is created, the closure will see the updated value.

   To avoid this, you can create a new scope that captures a snapshot of the variable's current value. This is often done using an immediately-invoked function expression (IIFE).

   ```javascript
   for (var i = 0; i < 5; i++) {
     (function(i) {
       setTimeout(function() {
         console.log(i); // Will log 0, 1, 2, 3, 4
       }, i * 1000);
     })(i);
   }
   ```

2. **Memory Leaks**: Closures can lead to memory leaks if they hold onto large objects that are no longer needed. To avoid this, make sure to null out any references to large objects when they're no longer needed.

   ```javascript
   function createClosure() {
     var largeObject = new Array(1000000);
     return function() {
       // Do something with largeObject
       largeObject = null; // Release the memory when done
     };
   }
   ```

3. **Overuse of Closures**: While closures are powerful, they can also make your code more complex and harder to understand if overused. Use closures judiciously, and consider other options like object-oriented programming or functional programming where appropriate.

4. **Creating Functions in a Loop**: When you create functions inside a loop that use the loop variable, they all share the same variable, which can lead to unexpected results. To avoid this, you can use `let` instead of `var` to declare the loop variable, which will give each iteration its own copy of the variable.

   ```javascript
   for (let i = 0; i < 5; i++) {
     setTimeout(function() {
       console.log(i); // Will log 0, 1, 2, 3, 4
     }, i * 1000);
   }
   ```

By being aware of these pitfalls and using closures judiciously, you can take full advantage of the power of closures while avoiding common problems.