import { addItem, getItems } from './src/db';

async function saveNewItem() {
  await addItem({ id: 2, name: 'New Item' });
  console.log(getItems());
}
