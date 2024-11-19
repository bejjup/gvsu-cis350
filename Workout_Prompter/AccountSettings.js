import React, { useState } from "react";

const AccountSettings = () => {
    const [name, setName] = useState(''); 
    const [email, setEmail] = useState(''); 

    const handleSave = () => {
        console.log('Account settings saved', { name, email }); 
    };

    return (
        <div>
            <h2>Account Settings</h2>
            <input
                type="text"
                placeholder="Name"
                value={name}
                onChange={(e) => setName(e.target.value)}
            />
            <input  
                type="email"
                placeholder="Email"
                value={email}
                onChange={(e) => setEmail(e.target.value)}
            />
            <button onClick={handleSave}>Save</button>
        </div>
    );
};

export default AccountSettings; 
