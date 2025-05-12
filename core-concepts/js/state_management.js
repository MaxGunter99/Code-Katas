
// state management works in different settings

import React, { useEffect, useState } from 'React'

export default function sayHelloWorld() {
  const [ message, setMessage ] = useState("None")

  useEffect( () => {
    setMessage( "boop" )
  }, [ message ])

  return (
    <p>{ message }</p>
  )
}