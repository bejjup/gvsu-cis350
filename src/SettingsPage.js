import React  from "react";
import AccountSettings from './AccountSettings'; 
import QuestionnaireSettings from './QuestionnaireSettings'; 

const SettingsPage = () => {
    return (
        <div>
            <h1>Settings</h1>
            <AccountSettings />
            <QuestionnaireSettings />
        </div>
    );
};

export default SettingsPage; 
