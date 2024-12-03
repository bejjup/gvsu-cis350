import React, { useState } from 'react';
import { View, Text, TextInput, Button, StyleSheet, Alert, StatusBar } from 'react-native';
import { updateUser } from './accounts';

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
  "Would you like to be notified hourly of water intake? (Yes/No)"
];

const fieldNames = [
  "name",
  "weight",
  "age",
  "gender",
  "experience",
  "type",
  "length",
  "intensityScale",
  "promptTime",
  "hourlyWaterNotif"
];

const Questionnaire = ({ navigation, route }) => {
  const { userId } = route.params;
  const [answers, setAnswers] = useState({});
  const [currentQuestionIndex, setCurrentQuestionIndex] = useState(0);
  const [text, setText] = useState('');

  const handleSubmit = async () => {
    if (text.trim() === '') {
      Alert.alert('Validation Error', 'Please fill out the field before proceeding.');
      return;
    }

    const updatedAnswers = { 
      ...answers, 
      [fieldNames[currentQuestionIndex]]: text 
    };
    setAnswers(updatedAnswers);
    setText('');

    if (currentQuestionIndex < questions.length - 1) {
      setCurrentQuestionIndex(currentQuestionIndex + 1);
    } else {
      try {
        await updateUser(userId, updatedAnswers);
        Alert.alert('Success', 'Your answers have been saved!');
        navigation.navigate('Home', { userId });
      } catch (error) {
        console.error('Error saving to database:', error);
        Alert.alert('Error', 'Failed to save your answers. Please try again.');
      }
    }
  };

  return (
    <View style={styles.container}>
      <Text style={styles.title}>{questions[currentQuestionIndex]}</Text>
      <TextInput
        style={styles.input}
        onChangeText={setText}
        value={text}
        placeholder="Type your answer here"
      />
      <Button
        title={currentQuestionIndex === questions.length - 1 ? 'Submit' : 'Next'}
        onPress={handleSubmit}
      />
      <StatusBar styles="auto"/>
    </View>
  );
};

const styles = StyleSheet.create({
  container: {
    flex: 1,
    justifyContent: 'center',
    alignItems: 'center',
    padding: 16,
  },
  title: {
    fontSize: 20,
    marginBottom: 12,
    textAlign: 'center',
  },
  input: {
    height: 40,
    borderColor: 'gray',
    borderWidth: 1,
    paddingLeft: 8,
    width: '100%',
    marginBottom: 12,
  },
});

export default Questionnaire; 
