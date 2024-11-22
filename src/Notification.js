import * as Notifications from 'expo-notifications';
import * as Permissions from 'expo-permissions';

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
    
  // Calculates time to be 9 a.m. 
  const now = new Date(); 
  const tomorrow9AM = new Date(); 
  tomorrow9AM.setHours(9, 0, 0, 0); // Sets time to 9am
    
  if (now.getHours() >= 9) {
    tomorrow9AM.setDate(now.getDate() + 1); 
  }

  // Schedules notification
  await Notifications.scheduleNotificationAsync({
    content: {
      title: "You have a new workout suggestion",
      body: "Open the app to see your workout.", 
      data: { data: "goes here" },
    },
    trigger: {
      hour: 9,
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

export default App;
