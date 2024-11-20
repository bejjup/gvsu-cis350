import AsyncStorage from '@react-native-async-storage/async-storage';
import { Low, AsyncStorage as LowdbAdapter } from 'lowdb';

// Set up the AsyncStorage adapter for lowdb
const adapter = new LowdbAdapter(AsyncStorage);
const db = new Low(adapter);

// Initialize the database
export async function initializeDatabase() {
  await db.read();
  db.data ||= { items: [] }; // Default structure for your database
  await db.write();
}

// Add item
export async function addItem(item) {
  db.data.items.push(item);
  await db.write();
}

// Get items
export function getItems() {
  return db.data.items;
}

// Delete item
export async function deleteItem(id) {
  db.data.items = db.data.items.filter((item) => item.id !== id);
  await db.write();
}

// Update item
export async function updateItem(id, newItem) {
  const itemIndex = db.data.items.findIndex((item) => item.id === id);
  if (itemIndex !== -1) {
    db.data.items[itemIndex] = newItem;
    await db.write();
  }
}
