// app/signup.tsx

import React, { useState } from 'react';
import { View, Text, TextInput, Button, StyleSheet, Alert } from 'react-native';
import { useRouter } from 'expo-router';
import { theme } from './styles/theme';

export default function SignUpScreen() {
  const router = useRouter();
  const [email, setEmail] = useState('');
  const [username, setUsername]=useState('');
  const [password, setPassword] = useState('');
  const [errors, setErrors] = useState<{ email?: boolean; username?: boolean; password?: boolean }>({});

  const handleSignUp = () => {
    let hasError = false;
    const newErrors = {};
  
    if (!email) {
      newErrors.email = true;
      hasError = true;
    }
  
    if (!username) {
      newErrors.username = true;
      hasError = true;
    }
  
    if (!password) {
      newErrors.password = true;
      hasError = true;
    }
  
    if (hasError) {
      setErrors(newErrors);
      Alert.alert('Error', 'Please fill out the highlighted fields.');
      return;
    }
  
    // Navigate only if there are no errors
    router.push({
      pathname: '/questionnaire',
      params: { email, username, password },
    });
  };
  
  return (
    <View style={styles.container}>
      <Text style={styles.title}>Sign Up</Text>
      <TextInput
        placeholder="Email"
        placeholderTextColor={theme.colors.inputText}
        value={email}
        onChangeText={(text) => {
          setEmail(text);
          if (errors.email) {
            setErrors((prev) => ({ ...prev, email: false }));
          }
        }}
        style={[styles.input, errors.email && styles.errorInput]}
        autoCapitalize="none"
        keyboardType="email-address"
      />
      <TextInput
        placeholder="Username"
        placeholderTextColor={theme.colors.inputText}
        value={username}
        onChangeText={(text) => {
          setUsername(text);
          if (errors.username) {
            setErrors((prev) => ({ ...prev, username: false }));
          }
        }}
        style={[styles.input, errors.username && styles.errorInput]}
        autoCapitalize="none"
      />
      <TextInput
        placeholder="Password"
        placeholderTextColor={theme.colors.inputText}
        value={password}
        onChangeText={(text) => {
          setPassword(text);
          if (errors.password) {
            setErrors((prev) => ({ ...prev, password: false }));
          }
        }}
        style={[styles.input, errors.password && styles.errorInput]}
        secureTextEntry
      />
      <Button 
        title="Sign Up" 
        onPress={handleSignUp}
        testID="signup-button"
      />
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
