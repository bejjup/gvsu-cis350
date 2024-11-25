import React from 'react';
import { BrowserRouter as Router, Route, Switch } from 'react-router-dom'; 
import Home from '.src/home'
import { initializeDatabase } from './db';
import Questionnaire from './questionnaire';
import { scheduleDailyNotification } from './notification';
import AccountSettings from './accountSettings';

const App = () => {
  initializeDatabase();
  Questionnaire(); 
  scheduleDailyNotification(); 
  return (
    <Router>
      <div>
        <h1>Workout Prompter</h1>
        <nav>
          <ul>
            <li><Link to="/">Home</Link></li>
            <li><Link to="/accountSettings">AccountSettings</Link></li>
          </ul>
        </nav>
        <Switch>
          <Route exact path="/" component={Home} />
          <Route path="/Settings" component={AccountSettings} /> 
        </Switch>
      </div>
    </Router>
  );
};

export default App; 
