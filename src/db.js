// src/db.js
import AsyncStorage from '@react-native-async-storage/async-storage';
import { Low, AsyncStorage as LowdbAdapter } from 'lowdb';

const adapter = new LowdbAdapter(AsyncStorage);
export const db = new Low(adapter);

export async function initializeDatabase() {
  await db.read();
  db.data ||= { users: [], items: [] };
  await db.write();
}


/**
 * Add a new item to the database.
 * @param {Object} item - The item to add (e.g., { id: 1, name: 'Item 1' }).
 */
export async function addItem(item) {
  db.data.items.push(item);
  await db.write();
}

/**
 * Get all items from the database.
 * @returns {Array} - The array of items.
 */
export function getItems() {
  return db.data.items;
}

/**
 * Update an existing item in the database.
 * @param {number} id - The ID of the item to update.
 * @param {Object} newItem - The updated item object.
 */
export async function updateItem(id, newItem) {
  const itemIndex = db.data.items.findIndex((item) => item.id === id);
  if (itemIndex !== -1) {
    db.data.items[itemIndex] = { ...db.data.items[itemIndex], ...newItem };
    await db.write();
  }
}

/**
 * Delete an item from the database.
 * @param {number} id - The ID of the item to delete.
 */
export async function deleteItem(id) {
  db.data.items = db.data.items.filter((item) => item.id !== id);
  await db.write();
}

export async function getUserById(id) {
  await db.read();
  return db.data.users.find((user) => user.id === id);
}

export async function updateUser(id, newUserData) {
  await db.read();
  const userIndex = db.data.users.findIndex((user) => user.id === id);
  if (userIndex !== -1) {
    db.data.users[userIndex] = { ...db.data.users[userIndex], ...newUserData };
    await db.write();
  }
}
