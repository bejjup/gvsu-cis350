// src/db.js
import AsyncStorage from '@react-native-async-storage/async-storage';

const DATABASE_KEY = 'database'; // Key to store the JSON database in AsyncStorage

export async function initializeDatabase() {
  const existingData = await AsyncStorage.getItem(DATABASE_KEY);
  if (!existingData) {
    const initialData = { users: [], items: [] };
    await AsyncStorage.setItem(DATABASE_KEY, JSON.stringify(initialData));
  }
}

async function readDatabase() {
  const data = await AsyncStorage.getItem(DATABASE_KEY);
  return data ? JSON.parse(data) : { users: [], items: [] };
}

async function writeDatabase(data) {
  await AsyncStorage.setItem(DATABASE_KEY, JSON.stringify(data));
}

/**
 * Add a new item to the database.
 * @param {Object} item - The item to add.
 */
export async function addItem(item) {
  const db = await readDatabase();
  db.items.push(item);
  await writeDatabase(db);
}

/**
 * Get all items from the database.
 * @returns {Array} - The array of items.
 */
export async function getItems() {
  const db = await readDatabase();
  return db.items;
}

/**
 * Update an existing item in the database.
 * @param {number} id - The ID of the item to update.
 * @param {Object} newItem - The updated item object.
 */
export async function updateItem(id, newItem) {
  const db = await readDatabase();
  const itemIndex = db.items.findIndex((item) => item.id === id);
  if (itemIndex !== -1) {
    db.items[itemIndex] = { ...db.items[itemIndex], ...newItem };
    await writeDatabase(db);
  }
}

/**
 * Delete an item from the database.
 * @param {number} id - The ID of the item to delete.
 */
export async function deleteItem(id) {
  const db = await readDatabase();
  db.items = db.items.filter((item) => item.id !== id);
  await writeDatabase(db);
}

/**
 * Get a user by ID.
 * @param {number} id - The ID of the user to retrieve.
 * @returns {Object|null} - The user object or null if not found.
 */
export async function getUserById(id) {
  const db = await readDatabase();
  return db.users.find((user) => user.id === id) || null;
}

/**
 * Update a user in the database.
 * @param {number} id - The ID of the user to update.
 * @param {Object} newUserData - The updated user data.
 */
export async function updateUser(id, newUserData) {
  const db = await readDatabase();
  const userIndex = db.users.findIndex((user) => user.id === id);
  if (userIndex !== -1) {
    db.users[userIndex] = { ...db.users[userIndex], ...newUserData };
    await writeDatabase(db);
  }
}
