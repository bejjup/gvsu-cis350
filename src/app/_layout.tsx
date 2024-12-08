// app/_layout.tsx

import { Stack } from 'expo-router';
import { UserProvider } from './context/UserContext';
import { theme } from './styles/theme';
import { View } from 'react-native';
import * as Notifications from 'expo-notifications';
import { useEffect } from 'react';

Notifications.setNotificationHandler({
  handleNotification: async () => ({
    shouldShowAlert: true,
    shouldPlaySound: true,
    shouldSetBadge: false,
  }),
});

export default function RootLayout() {
  useEffect(() => {
    // This listener is fired whenever a notification is received while the app is foregrounded
    const subscription = Notifications.addNotificationReceivedListener(notification => {
      console.log('Notification Received:', notification);
    });

    return () => {
      subscription.remove();
    };
  }, []);

  return (
    <UserProvider>
      <View style={{ flex: 1, backgroundColor: theme.colors.background }}>
        <Stack />
      </View>
    </UserProvider>
  );
}