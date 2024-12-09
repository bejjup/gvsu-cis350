import {calculateDailyWaterIntake, generateExerciseRoutine} from "../(tabs)/home"

describe('Unit Tests', () => {
  it('calculates daily water intake correctly', () => {
    const mockUser = {
      questionnaireAnswers: ['John Doe', '70', '25', 'Male'], // Weight: 70kg, Age: 25
    };

    const result = calculateDailyWaterIntake(mockUser);
    expect(result).toBe('2.80'); // (Weight (70) * 0.033) * (Age/Adjustments (1.1)) * Male (1.1)
  });

  it('generates correct endurance routine', () => {
    const mockUser = {
      questionnaireAnswers: [
        'John Doe',
        '70',
        '25',
        'Male',
        'Experienced',
        'Endurance',
        '15 mins',
        '3',
      ],
    };

    const result = generateExerciseRoutine(mockUser);
    expect(result).toContain('Jumping Jacks');
    expect(result).toContain('High Knees');
  });

  it('generates correct lower body routine', () => {
    const mockUser = {
      questionnaireAnswers: [
        'John Doe',
        '70',
        '25',
        'Male',
        'Advanced',
        'Lower Body',
        '20 mins',
        '4',
      ],
    };

    const result = generateExerciseRoutine(mockUser);
    expect(result).toContain('Squats');
    expect(result).toContain('Lunges');
  });

  it('adjusts water intake based on age and gender', () => {
    const mockUser = {
      questionnaireAnswers: ['Jane Doe', '60', '60', 'Female'], // Weight: 60kg, Age: 60 (0.9), Female (0.9)
    };

    const result = calculateDailyWaterIntake(mockUser);
    expect(result).toBe('1.60');
  });
});
