In JavaScript, `var`, `let`, and `const` are used to declare variables. They have different scoping rules and behaviors:

1. **var**: `var` is function-scoped, meaning a variable declared with `var` is accessible within the function it's declared in. If it's not declared inside any function, it's globally scoped. `var` variables can be re-declared and updated.

   ```javascript
   var x = 10;
   if (true) {
     var x = 20; // x is updated
     console.log(x); // Output: 20
   }
   console.log(x); // Output: 20
   ```

2. **let**: `let` is block-scoped, meaning a variable declared with `let` is only accessible within the block it's declared in. `let` variables can be updated but not re-declared.

   ```javascript
   let y = 10;
   if (true) {
     let y = 20; // a new y is declared in the block scope
     console.log(y); // Output: 20
   }
   console.log(y); // Output: 10
   ```

3. **const**: `const` is also block-scoped, but it cannot be updated or re-declared. This does not mean the variable itself is immutable, just that the variable identifier cannot be reassigned. For instance, if the variable is an object, the object's properties can still be updated.

   ```javascript
   const z = 10;
   // z = 20; // Error: Assignment to constant variable.

   const obj = { a: 1 };
   obj.a = 2; // This is fine
   // obj = { a: 2 }; // Error: Assignment to constant variable.
   ```

In general, it's recommended to use `let` and `const` over `var` in modern JavaScript to avoid issues with hoisting and scoping. Use `const` when the variable's value should not be changed, and `let` when it should.