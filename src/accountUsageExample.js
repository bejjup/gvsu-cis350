import { initializeDatabase, addItem, getItems, updateItem, deleteItem } from './database';
import { addUser, authenticateUser, getUsers, updateUser, deleteUser } from './accounts';

(async () => {
  await initializeDatabase();

  // Example usage of database items
  await addItem({ id: 1, name: 'Item 1' });
  console.log(await getItems());

  // Example usage of user accounts
  await addUser({ id: 1, username: 'user1', password: 'pass1', email: 'user1@example.com' });
  const authenticatedUser = await authenticateUser('user1', 'pass1');
  console.log(authenticatedUser);

  console.log(await getUsers());

  await updateUser(1, { password: 'newpass1' });
  console.log(await getUsers());

  await deleteUser(1);
  console.log(await getUsers());
})();

