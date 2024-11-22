import { initializeDatabase } from './db';
import Questionnaire from './questionnaire';

export default function App() {
  initializeDatabase();
  return <Questionnaire />;
}