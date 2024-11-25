import React from 'react';
import { StatusBar } from 'expo-status-bar';
import { BrowserRouter as Router, Route, Switch } from 'react-router-dom'; 
import Home from '.src/home'
import { initializeDatabase } from './db';
import Questionnaire from './questionnaire';
import { scheduleDailyNotification } from './notification';
import Settings from './settings';

const App = () => {
  //initializeDatabase();
  //scheduleDailyNotification(); 
  return (
    <Router>
      <div>
        <h1>Workout Prompter</h1>
        <nav>
          <ul>
            <li><Link to="/">Home</Link></li>
            <li><Link to="/accountSettings">AccountSettings</Link></li>
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
