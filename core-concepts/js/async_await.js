
// Async / await are the bones to make any function async
// the only caveat is that any function that 
// utilizes an async function ( await ) must be an async function

async function do_thing() {
  return "doing a thing"
}

async function call_me() {
  const do_thing_response = await do_thing()
  console.log( do_thing_response )
}

call_me()