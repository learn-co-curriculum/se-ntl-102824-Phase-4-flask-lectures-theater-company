import React from 'react';
import ReactDOM from 'react-dom';
import { UserProvider } from './context/user';
import { ProductionProvider } from './context/production';
import App from './App';
import { BrowserRouter as Router } from "react-router-dom";


ReactDOM.render(
  <Router>
    <UserProvider>
      <ProductionProvider>
        <App />
      </ProductionProvider>
    </UserProvider>
  </Router>,
  document.getElementById('root')
);
