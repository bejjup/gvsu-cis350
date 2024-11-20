import { StatusBar } from 'expo-status-bar';
import { StyleSheet, Text, View, Button } from 'react-native';
import AsyncStorage from '@react-native-async-storage/async-storage';
import { Low, AsyncStorage as LowdbAdapter } from 'lowdb';

// Set up the AsyncStorage adapter for lowdb
const adapter = new LowdbAdapter(AsyncStorage);
const db = new Low(adapter);

// Initialize the database
async function initializeDatabase() {
  await db.read();
  db.data ||= { items: [] }; // Default structure for your database
  await db.write();
}

// Add item
async function addItem(item) {
  db.data.items.push(item);
  await db.write();
}

// Get items
function getItems() {
  return db.data.items;
}

// Delete item
async function deleteItem(id) {
  db.data.items = db.data.items.filter((item) => item.id !== id);
  await db.write();
}

// Update item
async function updateItem(id, newItem) {
  const itemIndex = db.data.items.findIndex((item) => item.id === id);
  if (itemIndex !== -1) {
    db.data.items[itemIndex] = newItem;
    await db.write();
  }
}

// React Native Component
export default function App() {
  const handleAddItem = async () => {
    await addItem({ id: Date.now(), name: `Item ${Date.now()}` });
    console.log(getItems());
  };

  const handleUpdateItem = async () => {
    const items = getItems();
    if (items.length > 0) {
      await updateItem(items[0].id, { ...items[0], name: 'Updated Item' });
      console.log(getItems());
    }
  };

  const handleDeleteItem = async () => {
    const items = getItems();
    if (items.length > 0) {
      await deleteItem(items[0].id);
      console.log(getItems());
    }
  };

  initializeDatabase(); // Ensure the database is initialized

  return (
    <View style={styles.container}>
      <Text>React Native with lowdb</Text>
      <Button title="Add Item" onPress={handleAddItem} />
      <Button title="Update Item" onPress={handleUpdateItem} />
      <Button title="Delete Item" onPress={handleDeleteItem} />
      <StatusBar style="auto" />
    </View>
  );
}

const styles = StyleSheet.create({
  container: {
    flex: 1,
    backgroundColor: '#fff',
    alignItems: 'center',
    justifyContent: 'center',
  },
});
