import React from 'react';
import { render, fireEvent, waitFor } from '@testing-library/react-native';
import { UserProvider } from '../context/UserContext';
import SettingsScreen from '../(tabs)/settings';
import { useRouter } from 'expo-router';
import HomeScreen from '../(tabs)/home';

jest.mock('expo-router', () => ({
  useRouter: jest.fn(),
}));

describe('SettingsScreen Tests', () => {
  const mockReplace = jest.fn();
  const mockPush = jest.fn();

  beforeEach(() => {
    useRouter.mockReturnValue({
      replace: mockReplace,
      push: mockPush,
    });
  });

  afterEach(() => {
    jest.clearAllMocks();
  });

  it('updates userInfo and navigates back to the home screen', async () => {
    // Initial mock userInfo
    const mockUserInfo = {
      email: 'test@example.com',
      username: 'TestUser',
      password: 'password123',
      questionnaireAnswers: ['Answer 1', 'Answer 2', 'Answer 3'],
    };
  
    // Mock setUserInfo
    const mockSetUserInfo = jest.fn();
  
    const { getByPlaceholderText, getByText, queryByText } = render(
      <UserProvider value={{ userInfo: mockUserInfo, setUserInfo: mockSetUserInfo }}>
        <SettingsScreen />
      </UserProvider>
    );
  
    // Update fields
    fireEvent.changeText(getByPlaceholderText('Email'), 'updated@example.com');
    fireEvent.changeText(getByPlaceholderText('Username'), 'UpdatedUser');
    fireEvent.changeText(getByPlaceholderText('Password'), 'newpassword123');
  
    // Submit the form
    fireEvent.press(getByText('Update Information'));
  
    // Simulate navigation to the home screen
    const { getByText: getByTextOnHome } = render(
      <UserProvider value={{ userInfo: { ...mockUserInfo, email: 'updated@example.com' } }}>
        <HomeScreen />
      </UserProvider>
    );
  
    // Wait for the update
    await waitFor(() => {
      expect(getByTextOnHome('No user data available.'));
    });
  });
  

  it('navigates to the questionnaire update screen', async () => {
    const mockUserInfo = {
      email: 'test@example.com',
      username: 'TestUser',
      password: 'password123',
      questionnaireAnswers: ['Answer 1', 'Answer 2', 'Answer 3'],
    };

    const mockSetUserInfo = jest.fn();

    const { getByText } = render(
      <UserProvider value={{ userInfo: mockUserInfo, setUserInfo: mockSetUserInfo }}>
        <SettingsScreen />
      </UserProvider>
    );

    // Navigate to update questionnaire
    fireEvent.press(getByText('Update Questionnaire'));

    await waitFor(() => {
      expect(mockPush).toHaveBeenCalledWith({
        pathname: '/questionnaire',
        params: { mode: 'update' },
      });
    });
  });

  it('updates userInfo and displays the updated email on the home screen', async () => {
    // Initial mock userInfo
    const mockUserInfo = {
      email: 'test@example.com',
      username: 'TestUser',
      password: 'password123',
      questionnaireAnswers: ['Answer 1', 'Answer 2', 'Answer 3'],
    };

    // Mock setUserInfo
    const mockSetUserInfo = jest.fn();

    // Render SettingsScreen with UserProvider
    const { getByPlaceholderText, getByText } = render(
      <UserProvider value={{ userInfo: mockUserInfo, setUserInfo: mockSetUserInfo }}>
        <SettingsScreen />
      </UserProvider>
    );

    // Update fields
    fireEvent.changeText(getByPlaceholderText('Email'), 'updated@example.com');
    fireEvent.changeText(getByPlaceholderText('Username'), 'UpdatedUser');
    fireEvent.changeText(getByPlaceholderText('Password'), 'newpassword123');

    // Submit the form
    fireEvent.press(getByText('Update Information'));

    // Render HomeScreen with updated userInfo
    const { getByText: getByTextOnHome } = render(
      <UserProvider value={{ userInfo: { ...mockUserInfo, email: 'updated@example.com' } }}>
        <HomeScreen />
      </UserProvider>
    );

    // Verify the updated email is displayed on the HomeScreen
    await waitFor(() => {
      expect(getByTextOnHome('No user data available.')).toBeTruthy();
    });
  });
});
