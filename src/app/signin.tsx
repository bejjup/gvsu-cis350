// app/signin.tsx

import React, { useState } from 'react';
import { View, Text, TextInput, Button, StyleSheet, Alert, TouchableOpacity } from 'react-native';
import { useRouter } from 'expo-router';
import { useUser } from './context/UserContext';
import { theme } from './styles/theme';

export default function SignInScreen() {
  const router = useRouter();
  const { setUserInfo } = useUser();

  const [email, setEmail] = useState('');
  const [password, setPassword] = useState('');
  const [errors, setErrors] = useState<{ email?: boolean; password?: boolean }>({});

  const handleSignIn = () => {
    let hasError = false;
    const newErrors: { email?: boolean; password?: boolean } = {};
  
    if (!email) {
      newErrors.email = true;
      hasError = true;
    }
  
    if (!password) {
      newErrors.password = true;
      hasError = true;
    }
  
    console.log({ email, password, hasError, newErrors }); // <-- Debugging log
  
    if (hasError) {
      setErrors(newErrors);
      Alert.alert('Error', 'Please fill out the highlighted fields.');
      return;
    }
  
    const user = {
      email,
      username: 'ExistingUser',
      password,
      questionnaireAnswers: [],
    };
    setUserInfo(user);
    router.replace('/(tabs)/home');
  };
  

  return (
    <View style={styles.container}>
      <Text style={styles.title}>Sign In</Text>
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
      <TouchableOpacity style={styles.button} onPress={handleSignIn} testID="signin-button">
        <Text style={styles.buttonText}>Sign In</Text>
      </TouchableOpacity>
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