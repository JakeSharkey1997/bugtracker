import React from 'react';

export default function HeaderName(props) {
  if (props.name) {
    return <h2>Hey there, {props.name}!</h2>;
  } else {
    return <h2>Hey there, stranger</h2>;
  }
}
//<h1 className="App-header">Bug Tracker</h1>,