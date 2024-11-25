import unittest
from main import app, db, Expense

class TestSpendRightApp(unittest.TestCase):
    def setUp(self):
        """set up test client and makes sure values are at zero."""
        app.config['TESTING'] = True
        app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:memory:'  # Use in-memory database for testing
        self.app = app.test_client()
        with app.app_context():
            db.create_all()
            db.session.add(Expense())  # Add a default Expense entry
            db.session.commit()

    def tearDown(self):
        """clean up test enviroment after each test."""
        with app.app_context():
            db.session.remove()
            db.drop_all()

    def test_add_expense(self):
        """add values to expenses and makes sure backend and front end communicate correctly """
        self.app.post("/", data={"category": "food", "value": "100"})
        with app.app_context():
            expense = Expense.query.first()
            self.assertEqual(expense.food, 100)

    def test_reset_expenses(self):
        """adds expense, then reset all expenses."""
        self.app.post("/", data={"category": "rent", "value": "50"})
        self.app.post("/reset")
        with app.app_context():
            expense = Expense.query.first()
            self.assertEqual(expense.rent, 0)

    def test_initial_expense_values(self):
        """Verify default expense values."""
        with app.app_context():
            expense = Expense.query.first()
            self.assertEqual(expense.rent, 0)
            self.assertEqual(expense.utilities, 0)
