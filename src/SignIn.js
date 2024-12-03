// src/SignIn.js
import React, { useState } from 'react';
import { View, Text, TextInput, Button, StyleSheet } from 'react-native';
import { authenticateUser } from './accounts';

const SignIn = ({ navigation }) => {
  const [username, setUsername] = useState('');
  const [password, setPassword] = useState('');
  const handleSignIn = async () => {
    const user = await authenticateUser(username, password);
    if (user) {
      navigation.navigate('Home', { userId: user.id });
    } else {
      alert('Invalid username or password');
    }
  };

  return (
    <View style={styles.container}>
      <Text style={styles.title}>Sign In</Text>
      <TextInput placeholder="Username" value={username} onChangeText={setUsername} style={styles.input}/>
      <TextInput placeholder="Password" value={password} onChangeText={setPassword} secureTextEntry style={styles.input}/>
      <Button title="Sign In" onPress={handleSignIn} />
      <Button title="Create Account" onPress={() => navigation.navigate('SignUp')} />
    </View>
  );
};

const styles = StyleSheet.create({
  // ... styles
});

export default SignIn;
