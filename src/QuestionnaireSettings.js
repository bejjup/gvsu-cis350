import React, { useState } from "react";

const QuestionnarieSettings = () => {
    const [answers, setAnswers] = useState({ q1: '', q2: '' });

    const handleSave = () => {
        console.log('Questionnaire answers saved', answers); 
    };

    return (
        <div>
            <h2>Questionnaire Settings</h2>
            <input
                type="text"
                placeholder="Answer 1"
                value={answers.q1}
                onChange={(e) => setAnswers({ ...answers, q1: e.target.value })}
            />
            <input
                type="text"
                placeholder="Answer 2"
                value={answers.q2}
                onChange={(e) => setAnswers({ ...answers, q2: e.target.value })}
            />
            <button onClick={handleSave}>Save</button>
        </div>
    );
};

export default QuestionnarieSettings; 
