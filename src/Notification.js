import * as Notifications from 'expo-notifications';
import * as Permissions from 'expo-permissions';
import { getItems } from './src/db';

export const registerForPushNotificationsAsync = async () => {
  const { status } = await Permissions.askAsync(Permissions.NOTIFICATIONS);
  if (status !== 'granted') {
    alert('Failed to get push token for push notification!');
    return;
  }
  const token = (await Notifications.getExpoPushTokenAsync()).data;
  console.log(token);
};
registerForPushNotificationsAsync();


export const scheduleDailyNotification = async () => {
  await Notifications.cancelAllScheduledNotificationsAsync();
    
  // Calculates time and sets equal to input from questionnaire 
  const now = new Date(); 
  const scheduledTime = new Date(); 
  const items = getItems(); 
  const timeItem = items[8]; 
  scheduledTime.setHours(timeItem, 0, 0, 0); // Sets time to read from questionnaire
    
  if (now.getHours() >= timeItem) {
    scheduledTime.setDate(now.getDate() + 1); 
  }

  // Schedules notification
  await Notifications.scheduleNotificationAsync({
    content: {
      title: "You have a new workout suggestion",
      body: "Open the app to see your workout.", 
      data: { data: "goes here" },
    },
    trigger: {
      hour: timeItem,
      minute: 0, 
      repeats: true, 
    },
  });
};

return (
  <View style={{ flex: 1, justifyContent: 'center', alignItems: 'center' }}>
    <Button title="Send Notification" onPress={handleNotification} />
  </View>
);
