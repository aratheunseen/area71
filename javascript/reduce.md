The `reduce` method in JavaScript is used to apply a function to each element in an array to reduce the array to a single value. Here are some common use cases:

1. **Summing all numbers in an array**: 

   ```javascript
   let numbers = [1, 2, 3, 4, 5];
   let sum = numbers.reduce((total, num) => total + num, 0);
   console.log(sum); // Output: 15
   ```

2. **Finding the maximum value in an array**:

   ```javascript
   let numbers = [1, 2, 3, 4, 5];
   let max = numbers.reduce((max, num) => Math.max(max, num), numbers[0]);
   console.log(max); // Output: 5
   ```

3. **Counting occurrences of each value in an array**:

   ```javascript
   let names = ['Alice', 'Bob', 'Alice', 'Charlie', 'Bob'];
   let count = names.reduce((obj, name) => {
     obj[name] = (obj[name] || 0) + 1;
     return obj;
   }, {});
   console.log(count); // Output: { Alice: 2, Bob: 2, Charlie: 1 }
   ```

4. **Flattening an array of arrays**:

   ```javascript
   let arrays = [[1, 2], [3, 4], [5, 6]];
   let flat = arrays.reduce((a, b) => a.concat(b), []);
   console.log(flat); // Output: [1, 2, 3, 4, 5, 6]
   ```

5. **Transforming an array into an object**:

   ```javascript
   let keyValueArray = [['key1', 'value1'], ['key2', 'value2']];
   let obj = keyValueArray.reduce((obj, [key, value]) => {
     obj[key] = value;
     return obj;
   }, {});
   console.log(obj); // Output: { key1: 'value1', key2: 'value2' }
   ```

These are just a few examples of how the `reduce` method can be used in JavaScript. It's a very powerful method that can handle a wide variety of tasks that involve transforming or combining elements in an array.