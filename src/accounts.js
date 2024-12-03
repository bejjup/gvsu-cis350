// src/accounts.js
import { db } from './db';

export async function addUser(user) {
  await db.read();
  db.data.users.push(user);
  await db.write();
}

export async function authenticateUser(username, password) {
  await db.read();
  const user = db.data.users.find((u) => u.username === username && u.password === password);
  return user || null;
}

export async function getUserById(id) {
  await db.read();
  const user = db.data.users.find((u) => u.id === id);
  return user || null;
}

export async function updateUser(id, newUser) {
  await db.read();
  const userIndex = db.data.users.findIndex((u) => u.id === id);
  if (userIndex !== -1) {
    db.data.users[userIndex] = { ...db.data.users[userIndex], ...newUser };
    await db.write();
  }
}
