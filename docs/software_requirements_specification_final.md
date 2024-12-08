# Functional Requirements
<ol type="1">
  <li>User Authentication</li>
  <ol type="1">
    <li>User is able to create a login and password.</li>
    <li>User is able to log in with those credentials, and the website redirects them to their account.</li>
    <li>The code has a database to save user data.</li>
    <li>When logged in, users must be redirected to the dashboard upon successful login.</li>
    <li>The system must log out users and clear their session when logout is clicked.</li>
  </ol>

  <li>Dashboard Usability</li>
  <ol type="1">
    <li>User is able to input the amount of their expense.</li>
    <li>User is able to select from a drop-down menu of the categories of the expense.</li>
    <li>The dashboard displays a welcome back message to the specific user using login information.</li>
    <li>User is able to reset expenses back to zero.</li>
    <li>The system must be able to take away from expenses when inputted.</li>
  </ol>

  <li>Display of Charts</li>
  <ol type="1">
    <li>All expenses inputted by the user are displayed on the pie chart.</li>
    <li>All expenses inputted by the user are shown in a table.</li>
    <li>When resetting the expenses, both the table and pie chart will be updated accordingly.</li>
    <li>If a user removes a specific amount from a specific category, the pie chart and table will display the new amount.</li>
    <li>A total amount of expenses will be shown to let users know the full amount of expenses.</li>
  </ol>
</ol>

# Non-Functional Requirements
<ol type="1">
  <li>Performance</li>
  <ol type="1">
    <li>The system must load the login page in under 2 seconds on a standard internet connection.</li>
    <li>The system must process expense additions within 1 second.</li>
    <li>The system must scale to handle at least 100 simultaneous users without crashing.</li>
    <li>The system must render the pie chart within 1 second after data is updated.</li>
    <li>The system must perform efficiently on both desktop and mobile browsers.</li>
  </ol>

  <li>Security</li>
  <ol type="1">
    <li>The system must hash and salt people's passwords before storing them in the database.</li>
    <li>The system must prevent SQL injection attacks through inputs.</li>
    <li>The system must clear session data after a logout is performed.</li>
    <li>The system restricts access to the dashboard for unauthorized users.</li>
    <li>The system must encrypt sensitive user data during communication with the HTTPS server.</li>
  </ol>

  <li>Usability</li>
  <ol type="1">
    <li>The login must be user-friendly with clear instructions and an intuitive place to type.</li>
    <li>Buttons and hyperlinks must provide visual feedback when clicked.</li>
    <li>The application must have a consistent and appealing design.</li>
    <li>The system must provide meaningful error messages if inputs are incorrect.</li>
    <li>The website must be able to run on multiple screens and possibly a phone.</li>
  </ol>
</ol>
