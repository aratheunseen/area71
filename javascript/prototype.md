In JavaScript, every function and object has a property called a prototype. The prototype is an object itself, and all objects created with that function (as a constructor) or from that object will inherit properties and methods from the prototype.

Here's an example:

```javascript
function Person(firstName, lastName) {
  this.firstName = firstName;
  this.lastName = lastName;
}

Person.prototype.fullName = function() {
  return `${this.firstName} ${this.lastName}`;
}

let person1 = new Person("John", "Doe");
console.log(person1.fullName()); // Output: "John Doe"
```

In this example, `Person` is a constructor function. We add a method `fullName` to the `Person` prototype. Then, when we create a new object `person1` using the `Person` constructor (`new Person("John", "Doe")`), `person1` inherits the `fullName` method from the `Person` prototype.

This is useful because it allows all instances of `Person` to share the same `fullName` method, rather than having their own separate instances of the function. This can save memory when you have many instances of `Person`.

It's important to note that the prototype is not the same as the `__proto__` property of an object. The `__proto__` property is a reference to the prototype of the object's constructor. In the example above, `person1.__proto__` would be a reference to `Person.prototype`.