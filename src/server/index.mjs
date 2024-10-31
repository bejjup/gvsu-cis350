// server/index.mjs

import express from 'express';
import cors from 'cors';
import { Low } from 'lowdb';
import { JSONFile } from 'lowdb/node';
import path from 'path';
import { fileURLToPath } from 'url';

const app = express();
const port = 5000;

// Middleware
app.use(cors());
app.use(express.json());

// __filename and __dirname in ES Modules
const __filename = fileURLToPath(import.meta.url);
const __dirname = path.dirname(__filename);

// Set up Lowdb
const filePath = path.join(__dirname, 'db', 'db.json');
const adapter = new JSONFile(filePath);
const defaultData = { items: [] }; // Default data
const db = new Low(adapter, defaultData); // Initialize Low with default data

// Read data from JSON file, this will set db.data content
await db.read();

// Routes
app.get('/api/items', async (req, res) => {
  await db.read(); // Ensure data is up-to-date
  res.json(db.data.items);
});

app.post('/api/items', async (req, res) => {
  const newItem = req.body;
  await db.read();
  db.data.items.push(newItem);
  await db.write();
  res.status(201).json(newItem);
});

app.listen(port, () => {
  console.log(`Server is running on port ${port}`);
});
