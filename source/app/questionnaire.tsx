// app/questionnaire.tsx

import React, { useState, useEffect } from 'react';
import {
  View,
  Text,
  TextInput,
  Button,
  StyleSheet,
  ScrollView,
  Alert,
  KeyboardAvoidingView,
  Platform,
  TouchableOpacity,
} from 'react-native';
import { useRouter, useLocalSearchParams } from 'expo-router';
import { useUser } from './context/UserContext';
import * as Notifications from 'expo-notifications';
import * as Animatable from 'react-native-animatable';
import { theme } from './styles/theme';
import { generateExerciseRoutine } from './(tabs)/home';

export default function QuestionnaireScreen() {
  const router = useRouter();
  const { email, username, password, mode } = useLocalSearchParams();
  const { userInfo, setUserInfo } = useUser();

  const isUpdateMode = mode === 'update';

  const [answers, setAnswers] = useState<string[]>(Array(10).fill(''));
  const [errors, setErrors] = useState<boolean[]>(Array(10).fill(false));

  // Load existing answers if in update mode
  useEffect(() => {
    if (isUpdateMode && userInfo && userInfo.questionnaireAnswers) {
      setAnswers(userInfo.questionnaireAnswers);
    }
  }, [isUpdateMode, userInfo]);

  const questions = [
    "What is your name?",
    "How much do you weigh? (add just the number)",
    "How old are you?",
    "Male/Female/Prefer not to mention",
    "What is your level of prior workout experience? (None/Little/Experienced/Advanced)",
    "What type of workout would you like to focus on? (Endurance/Lower Body/Upper Body/Core)",
    "How long would you like to work out in the morning? (5 mins/10 mins/15 mins/20 mins)",
    "On a scale of 1-5, how intense would you like the workouts?",
    "What time would you like to get prompted? (5 AM/ 6 AM/ 7 AM/ 8 AM/ 9 AM/ 10 AM)",
    "Would you like to be notified hourly of water intake? (Yes/No)",
  ];

  const handleInputChange = (text: string, index: number) => {
    const newAnswers = [...answers];
    newAnswers[index] = text;
    setAnswers(newAnswers);

    if (errors[index]) {
      const newErrors = [...errors];
      newErrors[index] = false;
      setErrors(newErrors);
    }
  };

  const handleComplete = async () => {
    let hasError = false;
    const newErrors = [...errors];

    for (let i = 0; i < answers.length; i++) {
      if (!answers[i]) {
        newErrors[i] = true;
        hasError = true;
      }
    }

    if (hasError) {
      setErrors(newErrors);
      Alert.alert('Error', 'Please fill out the highlighted fields.');
      return;
    }

    if (isUpdateMode && userInfo) {
      const updatedUserInfo = {
        ...userInfo,
        questionnaireAnswers: answers,
      };
      setUserInfo(updatedUserInfo);

      // Reschedule notification
      await scheduleNotification(answers[8]);

      Alert.alert('Success', 'Questionnaire updated!');
      router.replace('/(tabs)/home');
    } else {
      const newUserInfo = {
        email: email as string,
        username: username as string,
        password: password as string,
        questionnaireAnswers: answers,
      };
      setUserInfo(newUserInfo);

      // Schedule notification
      await scheduleNotification(answers[8]);

      router.replace('/(tabs)/home');
    }
  };

  const scheduleNotification = async (timeAnswer: string) => {
    // Request notification permissions
    const { status } = await Notifications.requestPermissionsAsync();
    if (status !== 'granted') {
      Alert.alert('Permission Denied', 'Cannot schedule notifications without permission.');
      return;
    }

    // Parse the time from the answer
    const timeMap: { [key: string]: number } = {
      '5 AM': 5,
      '6 AM': 6,
      '7 AM': 7,
      '8 AM': 8,
      '9 AM': 9,
      '10 AM': 10,
    };

    const hour = timeMap[timeAnswer.trim()];
    if (hour === undefined) {
      Alert.alert('Error', 'Invalid time provided.');
      return;
    }

    // Schedule the notification at the specified time every day
    const routine = generateExerciseRoutine(userInfo);

    await Notifications.scheduleNotificationAsync({
      content: {
        title: 'Morning Workout',
        body: `Time for your workout!\n${routine}`,
      },
      trigger: {
        hour,
        minute: 0,
        repeats: true,
      },
    });
  };

  return (
    <KeyboardAvoidingView
      style={styles.container}
      behavior={Platform.OS === 'ios' ? 'padding' : undefined}
    >
      <ScrollView contentContainerStyle={styles.contentContainer}>
        <Text style={styles.title}>
          {isUpdateMode ? 'Update Questionnaire' : 'Questionnaire'}
        </Text>
        {questions.map((question, index) => (
          <Animatable.View
            key={index}
            animation="fadeInUp"
            delay={index * 200}
            style={{ marginBottom: 10 }}
          >
            <Text style={styles.questionText}>{question}</Text>
            <TextInput
              placeholder="Your answer"
              placeholderTextColor={theme.colors.inputText}
              value={answers[index]}
              onChangeText={(text) => handleInputChange(text, index)}
              style={[styles.input, errors[index] && styles.errorInput]}
            />
          </Animatable.View>
        ))}
        <TouchableOpacity
          style={styles.button}
          onPress={handleComplete}
        >
          <Text style={styles.buttonText}>
            {isUpdateMode ? 'Update' : 'Complete'}
          </Text>
        </TouchableOpacity>
      </ScrollView>
    </KeyboardAvoidingView>
  );
}

const styles = StyleSheet.create({
  // ... update styles to use theme colors and new styles
  container: {
    flex: 1,
    backgroundColor: theme.colors.background,
  },
  contentContainer: {
    padding: 20,
    paddingBottom: 40,
  },
  title: {
    fontSize: 24,
    color: theme.colors.text,
    marginBottom: 20,
    textAlign: 'center',
  },
  questionText: {
    color: theme.colors.text,
    marginBottom: 5,
  },
  input: {
    backgroundColor: theme.colors.inputBackground,
    color: theme.colors.inputText,
    borderWidth: 1,
    borderColor: '#ccc',
    padding: 10,
  },
  errorInput: {
    borderColor: 'red',
  },
  button: {
    backgroundColor: theme.colors.buttonBackground,
    padding: 15,
    marginTop: 20,
    alignItems: 'center',
  },
  buttonText: {
    color: theme.colors.buttonText,
    fontSize: 16,
  },
});