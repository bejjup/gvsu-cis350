# Overview
The purpose of this document is to list all of the software requirements that are project does/will meet with future updates. There are a total of 30 requirements (15 each of Functional and Non-functional). These requirements serve as completed milestones and as ideas for future updates of the application.
# Software Requirements
In this document there are 30 requirements. 15 Functional requirements and 15 non-functional requirements. Each type of requirement is broken down into three sections that describe a particular feature or section of the app. Each one of those sections contains at least five requirements. 
## Functional Requirements
### Questionnaire
| ID  | Requirement     | 
| :-------------: | :----------: | 
| FR1 | Questionnaire shall pop up during the first use of the app. | 
| FR2 | Questionnaire shall be able to be changed after filling out for the first time.  | 
| FR3 | Questionnaire shall store biological data to be used in the water tracker feature. | 
| FR4 | Questionnaire answers shall be used to determine a workout routine.  |
| FR5 | Questionnaire shall be linked to a notification, where the time of the notification is based on input from the questionnaire. |
### Sign-in and Sign-up
| ID  | Requirement     | 
| :-------------: | :----------: | 
| FR6 | Sign-up shall allow for a user to enter a username, email, and password. |
| FR7 | Sign-up feature shall store user data. |
| FR8 | Sign-in feature shall not allow access to the app without having an account registered.  |
| FR9 | Sign-in feature shall be the first screen to pop up when entering the app. |
| FR10 | If a user hits the sign-up button with account information that is already registered, then the user will have to hit the Sign-In button to enter the app. |
### Tabs and Routing / Misc. 
| ID  | Requirement     | 
| :-------------: | :----------: |
| FR11 | The first page to appear when entering the app is the sign-up/sign-in page. After clearing that screen, the user shall enter the home page. |
| FR12 | The home screen shall have a button that shall navigate to a settings page.  |
| FR13 | The settings page shall allow for the user to re-enter questionnaire answers. |
| FR14 | The settings page shall allow users to change their account information (email, name, password). |
| FR15 | The home page shall allow users to see their workout prompt. |
## Non-Functional Requirements
### Questionnaire 
| ID  | Requirement     | 
| :-------------: | :----------: | 
| NFR1 | When submitting answers into the questionnaire, the boxes shall turn red if there is missing/incorrect data to a question.  | 
| NFR2 | The questionnaire shall appear to be filled upon entering the app the first time, with answers able to be changed in the settings tab. |
| NFR3 | User questionnaire data shall be secured. |
| NFR4 | The data boxes shall be secure as to not allow for hackers to get other users data. |
| NFR5 | If an update is created that modifies the questionnaire or any of it's questions, the next time a user enters the app they shall be asked to re-enter their questionnaire data. | 
### Sign-in/Sign-up and Settings
| ID  | Requirement     | 
| :-------------: | :----------: | 
| NFR6 | When the sign-in button or sign-up button is tapped, the boxes shall turn red if there is missing/incorrect data entered. | 
| NFR7 | User profile data shall be secured. |
| NFR8 | Users shall have the option to delete their account. |
| NFR9 | The settings page shall allow users to view any data that they have entered, and the data shall be properly displayed. Passwords and other sensitive data shall be invisible until the user makes it visible.  |
| NFR10 | In the settings tab, if the delete account button is clicked, it shall prompt the user with a message 'do you really wish to delete your account?' |
### Misc.
| ID  | Requirement     | 
| :-------------: | :----------: | 
| NFR11 | The app shall have a simple design with buttons clearly labeled. | 
| NFR12 | Notifications that the app sends shall be clearly labeled with easy to understand information. |
| NFR13 | The app shall be able to resist the strain of many users. |
| NFR14 | No user data shall be visible to anyone but the user themself. |
| NFR15 | Notifications shall be integrated through iOS. |
# Software Artifacts
This section contains all of the documentation and other artifacts that we have compiled while designing our app. 
* [Gantt Chart](../artifacts/Gantt%20Chart.pdf)
* [Class Diagram](../artifacts/Class%20Diagram.pdf)
* [Use Case Diagram](../artifacts/Use%20case%20diagram.pdf)
* [Questionnaire Code](../src/app/questionnaire.tsx)
* [Indexing Code](../src/app/index.tsx)
* [Sign-In Code](../src/app/signin.tsx)
* [Sign-Up Code](../src/app/signup.tsx)
* [Layout Code](../src/app/_layout.tsx)