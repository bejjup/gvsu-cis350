// App.js
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
      await fetchItems();
    };
    initialize();
  }, []);

  const fetchItems = async () => {
    const fetchedItems = await getItems();
    setItems(fetchedItems);
    const userSettings = fetchedItems.find(item => item.id === 8);
    if (userSettings) {
      const date = new Date(userSettings.promptTime);
      await scheduleNotification(date);
    }
  };

  return (
    <NavigationContainer>
      <Stack.Navigator initialRouteName="SignIn">
        <Stack.Screen name="SignIn" component={SignIn} options={{ title: 'Sign In' }} />
        <Stack.Screen name="SignUp" component={SignUp} options={{ title: 'Create Account' }} />
        <Stack.Screen name="Questionnaire" component={Questionnaire} options={{ title: 'Questionnaire' }} />
        <Stack.Screen name="Home" component={Home} options={{ title: 'Home' }} />
        <Stack.Screen name="Settings" component={Settings} options={{ title: 'Settings' }} />
      </Stack.Navigator>
    </NavigationContainer>
  );
};

export default App;