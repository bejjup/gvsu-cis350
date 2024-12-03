// src/Home.js
import React, { useEffect, useState } from 'react';
import { View, Text, Button, StyleSheet } from 'react-native';
import { getUserById } from './accounts';
import { scheduleNotification } from './Notification';

const Home = ({ navigation, route }) => {
  const { userId } = route.params;
  const [user, setUser] = useState(null);

  useEffect(() => {
    const fetchUser = async () => {
      const userData = await getUserById(userId);
      setUser(userData);

      // Schedule notification after fetching user data
      if (userData && userData.promptTime) {
        const promptTime = parsePromptTime(userData.promptTime);
        scheduleNotification(promptTime);
      }
    };
    fetchUser();
  }, []);

  const parsePromptTime = (timeStr) => {
    // Assuming timeStr is in format '7 AM' or '7 PM'
    const [hourStr, modifier] = timeStr.split(' ');
    let hours = parseInt(hourStr, 10);
    if (modifier.toUpperCase() === 'PM' && hours < 12) {
      hours += 12;
    }
    if (modifier.toUpperCase() === 'AM' && hours === 12) {
      hours = 0;
    }

    const now = new Date();
    const scheduledDate = new Date(
      now.getFullYear(),
      now.getMonth(),
      now.getDate(),
      hours,
      0,
      0,
      0
    );

    // If the scheduled time has already passed today, schedule for tomorrow
    if (scheduledDate <= now) {
      scheduledDate.setDate(scheduledDate.getDate() + 1);
    }

    return scheduledDate;
  };

  if (!user) {
    return (
      <View style={styles.container}>
        <Text>Loading user data...</Text>
      </View>
    );
  }

  return (
    <View style={styles.container}>
      <Text style={styles.title}>Welcome, {user.name || user.username}!</Text>
      <Text>Your chosen exercise: {user.type}</Text>
      {/* Display other account information as needed */}
      <Button
        title="Settings"
        onPress={() => navigation.navigate('Settings', { userId })}
      />
    </View>
  );
};

const styles = StyleSheet.create({
  container: {
    flex: 1,
    alignItems: 'center',
    padding: 16,
    justifyContent: 'center',
  },
  title: {
    fontSize: 24,
    marginBottom: 12,
  },
});

export default Home;
