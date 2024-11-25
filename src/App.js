import React, { useEffect } from 'react';
import { BrowserRouter as Router, Route, Switch, Link } from 'react-router-dom'; 
import Home from './src/home'
import Settings from '.src/settings'; 
import Questionnaire from '.src/questionnaire';
import { initializeDatabase } from './src/db'; 

const App = () => {
  useEffect(() => {
  // Initialize the database when the app starts
  const initialize = async () => {
    await initializeDatabase(); 
  } ;
  initialize(); 
}, []); 

  return (
    <Router>
      <div>
        <h1>Workout Prompter</h1>
        <nav>
          <ul>
            <li><Link to="/">Home</Link></li>
            <li><Link to="/settings">AccountSettings</Link></li>
            <li><Link to="/questionnaire">Questionnaire</Link></li>
          </ul>
        </nav>
        <Switch>
          <Route exact path="/" component={Home} />
          <Route path="/settings" component={Settings} />
          <Route path="/questionnaire" component={Questionnaire} /> 
        </Switch>
      </div>
    </Router>
  );
};

export default App; 
