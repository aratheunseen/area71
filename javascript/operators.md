JavaScript has a variety of operators. Here are some of the most common ones:

1. **Arithmetic Operators**:
   - Addition (`+`): `5 + 2 // 7`
   - Subtraction (`-`): `5 - 2 // 3`
   - Multiplication (`*`): `5 * 2 // 10`
   - Division (`/`): `5 / 2 // 2.5`
   - Modulus (`%`): `5 % 2 // 1`
   - Increment (`++`): `let a = 5; a++; // a is now 6`
   - Decrement (`--`): `let b = 5; b--; // b is now 4`

2. **Assignment Operators**:
   - Assign (`=`): `let a = 5;`
   - Add and assign (`+=`): `a += 3; // a is now 8`
   - Subtract and assign (`-=`): `a -= 2; // a is now 6`
   - Multiply and assign (`*=`): `a *= 2; // a is now 12`
   - Divide and assign (`/=`): `a /= 3; // a is now 4`
   - Modulus and assign (`%=`): `a %= 3; // a is now 1`

3. **Comparison Operators**:
   - Equal to (`==`): `5 == '5' // true`
   - Not equal to (`!=`): `5 != '6' // true`
   - Strictly equal to (`===`): `5 === '5' // false`
   - Strictly not equal to (`!==`): `5 !== '5' // true`
   - Greater than (`>`): `5 > 2 // true`
   - Less than (`<`): `5 < 2 // false`
   - Greater than or equal to (`>=`): `5 >= 5 // true`
   - Less than or equal to (`<=`): `5 <= 4 // false`

4. **Logical Operators**:
   - Logical AND (`&&`): `true && false // false`
   - Logical OR (`||`): `true || false // true`
   - Logical NOT (`!`): `!true // false`

5. **Bitwise Operators**:
   - Bitwise AND (`&`): `5 & 1 // 1`
   - Bitwise OR (`|`): `5 | 1 // 5`
   - Bitwise XOR (`^`): `5 ^ 1 // 4`
   - Bitwise NOT (`~`): `~5 // -6`
   - Left shift (`<<`): `5 << 1 // 10`
   - Right shift (`>>`): `5 >> 1 // 2`
   - Zero fill right shift (`>>>`): `-5 >>> 1 // 2147483645`

6. **Ternary Operator (Conditional)**:
   - `condition ? valueIfTrue : valueIfFalse`: `5 > 2 ? 'yes' : 'no' // 'yes'`

7. **Typeof Operator**:
   - `typeof operand`: `typeof 'Hello' // 'string'`

8. **Delete Operator**:
   - `delete object.property`: `let obj = {a: 1}; delete obj.a; // obj is now {}`

9. **Void Operator**:
   - `void expression`: `void(0) // undefined`

10. **In Operator**:
    - `prop in object`: `'length' in 'Hello' // true`

11. **Instanceof Operator**:
    - `object instanceof constructor`: `[] instanceof Array // true`

These are just some of the operators available in JavaScript. Each operator has its own specific use case and behavior, so it's important to understand what each one does to use them effectively in your code.

---
---

Here are some additional operators in JavaScript:

1. **Exponentiation Operator (`**`)**: This operator returns the base to the exponent power, that is, base^exponent.

   ```javascript
   console.log(2 ** 3); // Output: 8
   ```

2. **Nullish Coalescing Operator (`??`)**: This operator returns the first operand if it's not null or undefined. Otherwise, it returns the second operand.

   ```javascript
   let x;
   console.log(x ?? "default"); // Output: "default"
   x = "value";
   console.log(x ?? "default"); // Output: "value"
   ```

3. **Optional Chaining Operator (`?.`)**: This operator allows you to read the value of a property located deep within a chain of connected objects without having to check each individual reference in the chain.

   ```javascript
   let user = {};
   console.log(user?.address?.street); // Output: undefined
   ```

4. **Logical Assignment Operators (`&&=`, `||=`, `??=`)**: These operators perform an assignment only under certain conditions.

   ```javascript
   let a = 0, b = "default", c;
   a &&= 2; // If a is truthy, perform the assignment. Otherwise, do nothing.
   console.log(a); // Output: 0
   b ||= "value"; // If b is falsy, perform the assignment. Otherwise, do nothing.
   console.log(b); // Output: "default"
   c ??= "value"; // If c is nullish (null or undefined), perform the assignment. Otherwise, do nothing.
   console.log(c); // Output: "value"
   ```

5. **Spread Operator (`...`)**: This operator allows an iterable (like an array) to be expanded in places where zero or more arguments or elements are expected.

   ```javascript
   let arr1 = [1, 2, 3];
   let arr2 = [...arr1, 4, 5]; // arr2 is now [1, 2, 3, 4, 5]
   ```

6. **Rest Parameter (`...`)**: This syntax allows us to represent an indefinite number of arguments as an array.

   ```javascript
   function sum(...args) {
     return args.reduce((a, b) => a + b, 0);
   }
   console.log(sum(1, 2, 3, 4)); // Output: 10
   ```

7. **Destructuring Assignment (`[]`, `{}`)**: This syntax is used to unpack values from arrays, or properties from objects, into distinct variables.

   ```javascript
   let [x, y] = [1, 2]; // x is 1, y is 2
   let {a, b} = {a: 1, b: 2}; // a is 1, b is 2
   ```

These are some of the additional operators available in JavaScript. Each operator has its own specific use case and behavior, so it's important to understand what each one does to use them effectively in your code.