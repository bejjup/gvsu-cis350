import React, { useEffect, useState } from 'react';
import { NavigationContainer } from '@react-navigation/native';
import { createStackNavigator } from '@react-navigation/stack';
import Home from './home.js';
import Settings from './settings.js';
import Questionnaire from './questionnaire.js';
import { initializeDatabase, getItems } from './db.js';
import { scheduleNotification } from './Notification.js';

const Stack = createStackNavigator();

const App = () => {
  const [items, setItems] = useState([]);

  useEffect(() => {
    const initialize = async () => {
      await initializeDatabase();
      fetchItems();
    };
    initialize();
  }, []);

  const fetchItems = async () => {
    const fetchedItems = await getItems();
    setItems(fetchedItems);
    const userSettings = fetchedItems.find(item => item.id === 8);
    if (userSettings) {
      scheduleNotification(new Date(userSettings.promptTime));
    }
  };

  return (
    <NavigationContainer>
      <Stack.Navigator initialRouteName="Home">
        <Stack.Screen name="Home" component={Home} />
        <Stack.Screen name="Settings" component={Settings} />
        <Stack.Screen name="Questionnaire" component={Questionnaire} />
      </Stack.Navigator>
    </NavigationContainer>
  );
};

export default App;
