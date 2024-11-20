# Local Database Guide

This guide explains how to use the local database powered by `lowdb` in this project. Follow these steps to add, update, retrieve, or delete items.

---

## **Setup**

1. Import the database functions into your file:
   ```javascript
   import { initializeDatabase, addItem, getItems, updateItem, deleteItem } from './src/db';


