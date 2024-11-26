import React, { useEffect } from 'react';
import { BrowserRouter as Router, Route, Switch, Link } from 'react-router-dom'; 
import Home from './src/home'
import Settings from '.src/settings'; 
import Questionnaire from '.src/questionnaire';
import { initializeDatabase, getItems } from './src/db'; 
import { scheduleNotification } from './notification';

const App = () => {
  const [items, setItems] = useState([]); 

  useEffect(() => {
  // Initialize the database when the app starts
  const initialize = async () => {
    await initializeDatabase(); 
    fetchItems(); 
  } ;
  initialize();   
}, []);

  // Fetch items from the database
  const fetchItems = async () => {
    const fetchedItems = getItems(); 
    setItems(fetchedItems); 
    const userSettings = fetchedItems.find(item => item.id === 8); 
    if (userSettings) {
      scheduleNotification(new Date(userSettings.promptTime)); 
    }
  };  

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
