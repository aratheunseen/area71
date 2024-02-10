function stopwatch() {
  var startTimestamp = Date.now();

  function getElapsedTime() {
    console.log(Date.now() - startTimestamp);
  }

    return getElapsedTime;
}

var timer = stopwatch();

for (var i = 0; i < 1000000; i++) {
    if (i === 999999) {
        console.log('done');
    }
}


console.dir(timer());

