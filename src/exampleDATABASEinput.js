import { initializeDatabase, addItem, getItems, updateItem, deleteItem } from './src/db';

async function exampleUsage() {
  // Initialize the database
  await initializeDatabase();

  // Add an item
  await addItem({ id: 1, name: 'Sample Item' });

  // Get all items
  const items = getItems();
  console.log('Items:', items);

  // Update an item
  await updateItem(1, { name: 'Updated Sample Item' });

  // Delete an item
  await deleteItem(1);
}
exampleUsage();
