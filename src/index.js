import { AppRegistry } from 'react-native';
import App from './App'; // Ensure this points to your App.js file
import { name as appName } from './app.json';

AppRegistry.registerComponent(appName, () => App);
