// Notification.js
import * as Notifications from 'expo-notifications';
import { Platform } from 'react-native';

// Set the notification handler to show notifications when the app is in the foreground
Notifications.setNotificationHandler({
  handleNotification: async () => ({
    shouldShowAlert: true,
    shouldPlaySound: true,
    shouldSetBadge: false,
  }),
});

export const scheduleNotification = async (date) => {
  // Request permissions
  const { status } = await Notifications.requestPermissionsAsync();
  if (status !== 'granted') {
    alert('Permission for notifications was not granted.');
    return;
  }

  // Cancel any existing notifications to prevent duplicates (optional)
  await Notifications.cancelAllScheduledNotificationsAsync();

  // Schedule the notification
  await Notifications.scheduleNotificationAsync({
    content: {
      title: 'Time to workout!',
      body: "Don't forget your daily exercise.",
      sound: true,
      priority: Notifications.AndroidNotificationPriority.HIGH,
    },
    trigger: date, // Pass the Date object directly
  });
};
