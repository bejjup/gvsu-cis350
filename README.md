# Comp Sci French Fries

Our project is a new take on workout applications. Our goal is to prompt the user every morning with a workout that has been specified to their needs through their own questionnaire responses.

## Team Members and Roles

* [Dylan Toomey](https://github.com/DuckySensei/CIS350-HW2-Toomey)  (Project Lead, Database Management, Jira Coordinator, Jest Code Creator)
* [Rachael Eapen](https://github.com/Rachaeleapen/CIS350-HW2-Eapen)  (Developer, Documenter) 
* [Colin Nagley](https://github.com/NagleyC30/CIS350-HW2-Nagley) (Timeline Coordinator, Package Management, QA)
* [Lauren Applegate](https://github.com/Lauren-Applegate/CIS350-HW2-Applegate) (Questionnaire Developement, Graphical Interface Design)

## Prerequisites
1.	On an iOS device, visit the app store and download Expo Go. 

2.	Once downloaded, open the app. You may be prompted to create an account. If so, create an account to continue.
    * If there is an option to continue as a guest you may do that as well.

3.	Make sure you have access to all the files to be able to run the code. Enter your command prompt/terminal (either in VS code or command prompt).
    * You need proper access to the 'src' directory which contains the elements needed to run the code through expo. 

## Run Instructions

1. In the Expo app you will be prompted with a message that tells you to run the command ‘npx expo start’. We won’t do anything with this for now. 

2.	Enter your command prompt/terminal (either in VS code or in the command prompt). 

3.	Move into the 'src' directory which contains all the neccessary files to run the project. 

    `cd src`
    

4.	Once you are in the ‘src’ directory run this command: 

    `npx expo start` 

5.	After running the start command you will see a QR code pop up in the terminal. 

6. On an iPhone scan the QR code using the camera app. This will take you back to the Expo Go app where you will be able to see the running app. 

## Trouble Shooting

If expo won't start, please try these:

1. Check to make sure "npm" librarys are downloaded:

        npm install

2.  Check to make sure "Expo" is downloaded:

        npm install expo

3.  Dependencies used in this project: 

        npm install expo-router
        npm install expo-notification
        npm install react react-native

4. Run with a clean cache

        npx expo start -c
        or
        npx expo start reset-project

5. If all else fails, please contact one of our members!