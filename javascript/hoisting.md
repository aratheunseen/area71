Hoisting is a JavaScript mechanism where variables and function declarations are moved to the top of their containing scope during the compile phase, before the code has been executed. It's important to note that only the declarations are hoisted, not initializations.

Here are some examples:

1. **Variable Hoisting**:

   ```javascript
   console.log(myVar); // Output: undefined
   var myVar = 5;
   console.log(myVar); // Output: 5
   ```

   In this example, the declaration of `myVar` (i.e., `var myVar`) is hoisted to the top of the scope. So, when we try to log `myVar` before it's been defined, we get `undefined` instead of a ReferenceError. After `myVar` is defined, it logs the expected value.

   It's important to note that `let` and `const` are also hoisted, but they remain in a "temporal dead zone" from the start of the block until the declaration is processed. During this period, any reference to them will result in a ReferenceError.

2. **Function Declaration Hoisting**:

   ```javascript
   console.log(myFunction()); // Output: "Hello, world!"

   function myFunction() {
     return "Hello, world!";
   }
   ```

   In this example, the function declaration `myFunction` is hoisted to the top of the scope, so we can call it before its declaration in the code.

3. **Function Expression Hoisting**:

   ```javascript
   console.log(myFunction()); // Output: TypeError: myFunction is not a function

   var myFunction = function() {
     return "Hello, world!";
   }
   ```

   In this example, `myFunction` is treated as a variable, so the variable name `myFunction` is hoisted but the assignment of the function to the variable happens where it's written in the code. Therefore, trying to call `myFunction` before its definition results in a TypeError.

Understanding hoisting is crucial for avoiding bugs and writing predictable JavaScript code. It's generally a good practice to declare all variables at the top of their scope to make it clear that they are hoisted.