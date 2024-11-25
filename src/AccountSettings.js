import React, { useState, useEffect } from "react";
import { getItems } from './src/db';

const AccountSettings = () => {
    const [name, setName] = useState('');

    useEffect(() => {
        const fetchUserData = async () => {
            const items = await getItems(); 
            if (items.length > 0) {
                const firstInput = items[0];
                setName(firstInput.name || ''); // Assuming 'name' is a field in the user data
            }
        };

        fetchUserData();
    }, []);

    const handleSave = () => {
        console.log('Account settings saved', { name });
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
            <button onClick={handleSave}>Save</button>
        </div>
    );
};

export default AccountSettings;
