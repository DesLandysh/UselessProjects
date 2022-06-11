// Python-like print function
const print = a => console.log(a);

// return array filled from 1 to desired number
const make_arr = (number) => {
  let array = [];
  array[number] = undefined;
  array = Array.from(array.keys());
  array.shift();
  return array;
};

arr = make_arr(100);
// output: [1, 2, 3... ...100]
// print(arr); // to make sure of this

// FOR OF takes values
for (let i of arr) {
  switch (true) {
    case (i % 3 === 0 && i % 5 === 0):
      print('fizzbuzz');
      break;
    case (i % 5 === 0):
      print('buzz');
      break;
    case (i % 3 === 0):
      print('fizz');
      break;
    default: print(i);
  };
}
// 1 2 ... 98 fizz buzz

print('\n')

// FOR-IN takes indexes
for (let j in arr) {
  if (j % 3 === 0 && j % 5 === 0) {
    print('fizzbuzz');
  } else if (j % 3 === 0) {
    print('fizz');
  } else if (j % 5 === 0) {
    print('buzz');
  } else {
    print(j);
  };
}
// fizzbuzz 1 2 ... 97 98 fizz
