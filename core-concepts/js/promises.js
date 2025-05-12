
// Promises are basically async function calls
// code execution halts until the promise is returned a status: pending, fulfilled, rejected
// common uses are for timeouts

new Promise((resolveOuter) => {
  resolveOuter(
    new Promise((resolveInner) => {
      setTimeout(resolveInner, 1000);
    }),
  );
});

// Chaining promises
myPromise
  .then(handleFulfilledA)
  .then(handleFulfilledB)
  .then(handleFulfilledC)
  .catch(handleRejectedAny);

