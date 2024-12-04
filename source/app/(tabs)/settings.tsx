// app/(tabs)/settings.tsx

import React, { useState, useEffect } from 'react';
import { View, Text, TextInput, Button, StyleSheet, Alert } from 'react-native';
import { useUser } from '../context/UserContext';
import { useRouter } from 'expo-router';
import { theme } from '../styles/theme';

export default function SettingsScreen() {
  const router = useRouter();
  const { userInfo, setUserInfo } = useUser();

  const [email, setEmail] = useState('');
  const [username, setUsername] = useState('');
  const [password, setPassword] = useState('');

  // Load user data when the component mounts or when userInfo changes
  useEffect(() => {
    if (userInfo) {
      setEmail(userInfo.email);
      setUsername(userInfo.username);
      setPassword(userInfo.password);
    }
  }, [userInfo]);

  const handleUpdate = () => {
    if (userInfo) {
      const updatedUserInfo = {
        ...userInfo,
        email,
        username,
        password,
      };
      setUserInfo(updatedUserInfo);
      Alert.alert('Success', 'Information updated!', [
        {
          text: 'OK',
          onPress: () => {
            // Navigate back to home screen
            router.replace('/(tabs)/home');
          },
        },
      ]);
    }
  };

  const handleUpdateQuestionnaire = () => {
    // Navigate to the questionnaire screen in update mode
    router.push({
      pathname: '/questionnaire',
      params: { mode: 'update' },
    });
  };

  if (!userInfo) {
    return (
      <View style={styles.container}>
        <Text>No user data available.</Text>
      </View>
    );
  }

  return (
    <View style={styles.container}>
      <Text style={styles.title}>Settings</Text>
      <TextInput
        placeholder="Email"
        placeholderTextColor={theme.colors.inputText}
        value={email}
        onChangeText={setEmail}
        style={styles.input}
      />
      <TextInput
        placeholder="Username"
        placeholderTextColor={theme.colors.inputText}
        value={username}
        onChangeText={setUsername}
        style={styles.input}
      />
      <TextInput
        placeholder="Password"
        placeholderTextColor={theme.colors.inputText}
        value={password}
        onChangeText={setPassword}
        style={styles.input}
        secureTextEntry
      />
      <Button title="Update Information" onPress={handleUpdate} />
      <View style={{ marginTop: 20 }}>
        <Button title="Update Questionnaire" onPress={handleUpdateQuestionnaire} />
      </View>
    </View>
  );
}

const styles = StyleSheet.create({
  container: {
    flex: 1,
    backgroundColor: theme.colors.background,
    padding: 20,
    justifyContent: 'center',
  },
  title: {
    fontSize: 24,
    color: theme.colors.text,
    marginBottom: 20,
    textAlign: 'center',
  },
  input: {
    backgroundColor: theme.colors.inputBackground,
    color: theme.colors.inputText,
    borderWidth: 1,
    borderColor: '#ccc',
    padding: 10,
    marginVertical: 5,
  },
  errorInput: {
    borderColor: 'red',
  },
  button: {
    backgroundColor: theme.colors.buttonBackground,
    padding: 15,
    marginTop: 10,
    alignItems: 'center',
  },
  buttonText: {
    color: theme.colors.buttonText,
    fontSize: 16,
  },
});