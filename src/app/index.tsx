// app/index.tsx

import React from 'react';
import { View, Text, Button, StyleSheet } from 'react-native';
import { Link } from 'expo-router';
import { theme } from './styles/theme';

export default function SignInSignUpScreen() {
  return (
    <View style={styles.container}>
      <Text style={styles.title}>Work out Prompter</Text>
      <Link href="/signin" asChild>
        <Button title="Sign In" />
      </Link>
      <Link href="/signup" asChild>
        <Button title="Sign Up" />
      </Link>
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