import { db } from './database';


export async function addUser(user) {
  db.data.users.push(user);
  await db.write();
}

export async function authenticateUser(username, password) {
  await db.read();
  const user = db.data.users.find((u) => u.username === username && u.password === password);
  return user || null;
}


export async function getUsers() {
  await db.read();
  return db.data.users;
}


export async function updateUser(id, newUser) {
  const userIndex = db.data.users.findIndex((u) => u.id === id);
  if (userIndex !== -1) {
    db.data.users[userIndex] = { ...db.data.users[userIndex], ...newUser };
    await db.write();
  }
}


export async function deleteUser(id) {
  db.data.users = db.data.users.filter((user) => user.id !== id);
  await db.write();
}

