// App.js
import React, { useEffect } from 'react';
import { NavigationContainer } from '@react-navigation/native';
import { createNativeStackNavigator } from '@react-navigation/native-stack';
import SignIn from './src/SignIn';
import SignUp from './src/SignUp';
import Questionnaire from './src/Questionnaire';
import Home from './src/Home';
import Settings from './src/Settings';
import { initializeDatabase } from './src/db';

const Stack = createNativeStackNavigator();

const App = () => {
  useEffect(() => {
    const initialize = async () => {
      await initializeDatabase();
    };
    initialize();
  }, []);

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
