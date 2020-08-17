import React from 'react';
import './App.css';
import HeaderName from './Components/headerName';
import HeaderBug from './Components/headerBug';

function App() {
  return (
    <div className="App">
      <header className="App-header">
        <HeaderBug />
        <HeaderName />
      </header>
    </div>
  );
}

export default App;
