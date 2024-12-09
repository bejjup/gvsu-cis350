// app/(tabs)/home.tsx

import React from 'react';
import { View, Text, StyleSheet, ScrollView, Button, TouchableOpacity } from 'react-native';
import { useUser } from '../context/UserContext';
import * as Notifications from 'expo-notifications';
import { theme } from '../styles/theme';

export default function HomeScreen() {
  const { userInfo } = useUser();

  const [notificationTime, setNotificationTime] = React.useState('8:00 AM'); // Default notification time

  const sendTestNotification = async () => {
    await Notifications.scheduleNotificationAsync({
      content: {
        title: 'Test Notification',
        body: 'This is a test notification.',
      },
      trigger: null,
    });
  };

  if (!userInfo) {
    return (
      <View style={styles.container}>
        <Text style={styles.buttonText}>No user data available.</Text>
      </View>
    );
  }

  return (
    <View style={styles.container}>
      <ScrollView contentContainerStyle={styles.contentContainer}>
        <Text style={styles.title}>Welcome, {userInfo.username}!</Text>
        <View style={styles.card}>
          <Text style={styles.cardTitle}>Your Information</Text>
          <Text style={styles.cardText}>Email: {userInfo.email}</Text>
          <Text style={styles.cardText}>
            Water Intake Goal: {calculateDailyWaterIntake(userInfo)} liters/day
          </Text>
        </View>

        <View style={styles.card}>
          <Text style={styles.cardTitle}>Your Exercise Routine</Text>
          <Text style={styles.cardText}>{generateExerciseRoutine(userInfo)}</Text>
        </View>

        <View style={styles.card}>
          <Text style={styles.cardTitle}>Notification Time</Text>
          <Text style={styles.cardText}>
            You will be notified at: {notificationTime}
          </Text>
        </View>

        <TouchableOpacity style={styles.button} onPress={sendTestNotification}>
          <Text style={styles.buttonText}>Send Test Notification</Text>
        </TouchableOpacity>
      </ScrollView>
    </View>
  );
}

// Updated styles

const styles = StyleSheet.create({
  container: {
    flex: 1,
    backgroundColor: theme.colors.background,
  },
  contentContainer: {
    padding: 20,
  },
  title: {
    fontSize: 28,
    color: theme.colors.text,
    marginBottom: 20,
    textAlign: 'center',
  },
  card: {
    backgroundColor: '#004080', // Slightly lighter navy blue
    padding: 15,
    borderRadius: 10,
    marginBottom: 20,
  },
  cardTitle: {
    fontSize: 20,
    color: theme.colors.text,
    marginBottom: 10,
    fontWeight: 'bold',
  },
  cardText: {
    fontSize: 16,
    color: theme.colors.text,
    marginBottom: 5,
  },
  button: {
    backgroundColor: theme.colors.buttonBackground,
    padding: 15,
    marginTop: 10,
    alignItems: 'center',
    borderRadius: 5,
  },
  buttonText: {
    color: theme.colors.buttonText,
    fontSize: 16,
  },
});

// Define the functions for water intake and exercise routine

export function calculateDailyWaterIntake(userInfo) {
  // Extract necessary data
  const weight = parseFloat(userInfo.questionnaireAnswers[1]); // Assuming weight is at index 1
  const age = parseInt(userInfo.questionnaireAnswers[2]); // Assuming age is at index 2
  const gender = userInfo.questionnaireAnswers[3]; // Assuming gender is at index 3

  // Basic water intake calculation
  // This is a simplified formula and may vary
  let waterIntake = weight * 0.033; // Liters per day

  // Adjust based on age
  if (age < 30) {
    waterIntake *= 1.1;
  } else if (age > 55) {
    waterIntake *= 0.9;
  }

  // Adjust based on gender
  if (gender.toLowerCase() === 'male') {
    waterIntake *= 1.1;
  } else if (gender.toLowerCase() === 'female') {
    waterIntake *= 0.9;
  }

  return waterIntake.toFixed(2);
}


export function generateExerciseRoutine(userInfo) {
  // Extract necessary data
  const experience = userInfo.questionnaireAnswers[4]; // Assuming experience is at index 4
  const focus = userInfo.questionnaireAnswers[5]; // Assuming focus is at index 5
  const duration = userInfo.questionnaireAnswers[6]; // Assuming duration is at index 6
  const intensity = parseInt(userInfo.questionnaireAnswers[7]); // Assuming intensity is at index 7

  // Generate routine based on focus area
  let routine = '';

  switch (focus.toLowerCase()) {
    case 'endurance':
      routine = generateEnduranceRoutine(duration, intensity);
      break;
    case 'lower body':
      routine = generateLowerBodyRoutine(duration, intensity);
      break;
    case 'upper body':
      routine = generateUpperBodyRoutine(duration, intensity);
      break;
    case 'core':
      routine = generateCoreRoutine(duration, intensity);
      break;
    default:
      routine = 'General full-body workout including cardio and strength exercises.';
  }

  return routine;
}

// Implement specific routine generators
function generateEnduranceRoutine(duration, intensity) {
  return `Your ${duration} endurance routine:\n- Jumping Jacks\n- High Knees\n- Butt Kicks\n- Mountain Climbers\nIntensity Level: ${intensity}`;
}

function generateLowerBodyRoutine(duration, intensity) {
  return `Your ${duration} lower body routine:\n- Squats\n- Lunges\n- Glute Bridges\n- Calf Raises\nIntensity Level: ${intensity}`;
}

function generateUpperBodyRoutine(duration, intensity) {
  return `Your ${duration} upper body routine:\n- Push-ups\n- Tricep Dips\n- Shoulder Taps\n- Arm Circles\nIntensity Level: ${intensity}`;
}

function generateCoreRoutine(duration, intensity) {
  return `Your ${duration} core routine:\n- Planks\n- Russian Twists\n- Leg Raises\n- Bicycle Crunches\nIntensity Level: ${intensity}`;
}
