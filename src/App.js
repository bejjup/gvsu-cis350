import { StatusBar } from 'expo-status-bar';
import { StyleSheet, Text, View, Button } from 'react-native';
import { initializeDatabase, addItem, getItems, deleteItem, updateItem } from './src/db';

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
      <Text>React Native with lowdb (this is to test the database)</Text>
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
