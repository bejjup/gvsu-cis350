// Settings.js
import React, { useState, useEffect } from 'react';
import { View, Text, TextInput, Button, StyleSheet, Alert, ScrollView } from 'react-native';
import { getItems, updateItem } from './src/db'; // Import the necessary functions

const Settings = () => {
  const [answers, setAnswers] = useState({});
  const [textInputs, setTextInputs] = useState({});

  useEffect(() => {
    const fetchData = async () => {
      const items = await getItems();
      if (items.length > 0) {
        setAnswers(items[0]); // Assuming you want to edit the first item for simplicity
        setTextInputs(items[0]); // Initialize text inputs with current answers
      }
    };
    fetchData();
  }, []);

  const handleChange = (field, value) => {
    setTextInputs((prevInputs) => ({
      ...prevInputs,
      [field]: value,
    }));
  };

  const handleSave = async () => {
    try {
      await updateItem(answers.id, textInputs); // Update the item in the database
      Alert.alert('Success', 'Your settings have been updated!');
      console.log('Updated answers:', textInputs);
    } catch (error) {
      console.error('Error updating settings:', error);
      Alert.alert('Error', 'Failed to update your settings. Please try again.');
    }
  };

  return (
    <ScrollView contentContainerStyle={styles.container}>
      <Text style={styles.title}>Settings</Text>
      {Object.keys(textInputs).map((key) => (
        <View key={key} style={styles.inputContainer}>
          <Text style={styles.label}>{key}</Text>
          <TextInput
            style={styles.input}
            onChangeText={(value) => handleChange(key, value)}
            value={textInputs[key]}
            placeholder={`Enter your ${key}`}
          />
        </View>
      ))}
      <View style={styles.buttonContainer}>
        <Button title="Save" onPress={handleSave} />
      </View>
    </ScrollView>
  );
};

const styles = StyleSheet.create({
  container: {
    flexGrow: 1,
    justifyContent: 'center',
    alignItems: 'center',
    padding: 16,
  },
  title: {
    fontSize: 20,
    marginBottom: 12,
    textAlign: 'center',
  },
  inputContainer: {
    width: '100%',
    marginBottom: 12,
  },
  label: {
    fontSize: 16,
    marginBottom: 4,
  },
  input: {
    height: 40,
    borderColor: 'gray',
    borderWidth: 1,
    paddingLeft: 8,
    width: '100%',
  },
  buttonContainer: {
    marginTop: 20,
    width: '100%',
    alignItems: 'center',
  },
});

export default Settings;
