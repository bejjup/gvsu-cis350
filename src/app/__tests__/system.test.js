// app/__tests__/system.test.js
import React from 'react';
import { render, fireEvent, waitFor } from '@testing-library/react-native';
import { Alert } from 'react-native';
import SignUpScreen from '../signup';
import QuestionnaireScreen from '../questionnaire';
import HomeScreen from '../(tabs)/home';
import { UserProvider } from '../context/UserContext';

const mockPush = jest.fn();
const mockReplace = jest.fn();

jest.mock('expo-router', () => ({
  useRouter: () => ({
    push: mockPush,
    replace: mockReplace,
  }),
  useLocalSearchParams: () => ({
    email: 'test@example.com',
    username: 'testuser',
    password: 'password123',
  }),
}));

jest.mock('expo-notifications', () => ({
  requestPermissionsAsync: jest.fn(async () => ({ status: 'granted' })),
  scheduleNotificationAsync: jest.fn(),
}));


jest.mock('../(tabs)/home', () => ({
  generateExerciseRoutine: jest.fn(() => 'Workout Routine: 10 push-ups, 10 squats'),
}));

describe('System Tests', () => {
  describe('Sign Up Screen', () => {
    it('should allow the user to sign up and navigate to the questionnaire', async () => {
      const { getByPlaceholderText, getAllByText } = render(
        <UserProvider>
          <SignUpScreen />
        </UserProvider>
      );

      fireEvent.changeText(getByPlaceholderText('Email'), 'test@example.com');
      fireEvent.changeText(getByPlaceholderText('Username'), 'testuser');
      fireEvent.changeText(getByPlaceholderText('Password'), 'password123');

      const signUpElements = getAllByText("Sign Up");
      fireEvent.press(signUpElements[signUpElements.length - 1]);

      await waitFor(() => {
        expect(mockPush).toHaveBeenCalledWith({
          pathname: '/questionnaire',
          params: {
            email: 'test@example.com',
            username: 'testuser',
            password: 'password123',
          },
        });
      });
    });

    it('should show an error and not navigate if required fields are missing', async () => {
      const alertSpy = jest.spyOn(Alert, 'alert');

      const { getByPlaceholderText, getByTestId, queryByText } = render(
        <UserProvider>
          <SignUpScreen />
        </UserProvider>
      );

      fireEvent.changeText(getByPlaceholderText('Email'), 'test@example.com');

      fireEvent.press(getByTestId('signup-button'));

      await waitFor(() => {
        expect(queryByText('Questionnaire')).toBeNull();
        expect(alertSpy).toHaveBeenCalledWith(
          'Error',
          'Please fill out the highlighted fields.'
        );
      });

      alertSpy.mockRestore();
    });
  });

  describe('Questionnaire Screen', () => {
    it('should show an error if required fields are missing', async () => {
      const alertSpy = jest.spyOn(Alert, 'alert');

      const { getByText, queryByText } = render(
        <UserProvider>
          <QuestionnaireScreen />
        </UserProvider>
      );

      fireEvent.press(getByText('Complete'));

      await waitFor(() => {
        expect(alertSpy).toHaveBeenCalledWith('Error', 'Please fill out the highlighted fields.');
        expect(queryByText('Welcome, testuser!')).toBeNull();
      });

      alertSpy.mockRestore();
    });
  });
});
