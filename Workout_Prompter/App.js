import { StatusBar } from 'expo-status-bar';
import { useEffect } from 'react';
import { StyleSheet, Text, View, Button } from 'react-native';
import { BrowserRouter as Router, Route, Switch } from 'react-router-dom'; 
import { scheduleDailyNotification } from './Notification';
import { registerForPushNotificationsAsync } from './Notification';
import SettingsPage from './SettingsPage';


const App = () => {
  useEffect(() => {
    scheduleDailyNotification();
  }, []); 

  return (
    <View style={{ flex: 1, justifyContent: 'center', alignItems: 'center' }}>
      <Button title="Send Notification" onPress={scheduleDailyNotification} />
    </View>
  );
};

export default App; 