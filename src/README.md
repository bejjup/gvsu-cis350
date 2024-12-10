Placeholder for source code

Before you start, ensure you have the following installed:
1.	Python 3.9 or above
2.	Git: Install Git f
3.	Visual Studio Code (VS Code): Install from 
4.	Python Extension for VS Code: Install the Python extension in VS Code.
5.	Pip: Python's package manager (included with Python).
________________________________________
Setup Instructions
Step 1: Clone the Repository
1.	Open VS Code and press Ctrl+Shift+P (or Cmd+Shift+P on macOS) to open the Command Palette.
2.	Type "Git: Clone" and select it.
3.	Enter the repository URL:
https://github.com/your_team_repo/GVSU-CIS350-GPJ.git
4.	Select a folder to clone the repository to.
Alternatively, you can clone it from the terminal:
git clone https://github.com/your_team_repo/GVSU-CIS350-GPJ.git
Step 2: Open the Project
1.	Open the cloned folder in VS Code:
o	Click File > Open Folder.
o	Navigate to the folder you just cloned (e.g., GVSU-CIS350-GPJ) and open it.
Step 3: Set Up the Python Environment
1.	Create a Virtual Environment: Open the integrated terminal in VS Code (Ctrl+ or Cmd+) and run:
python -m venv venv
2.	Activate the Virtual Environment:
o	On Windows:
venv\Scripts\activate
o	On macOS/Linux:
source venv/bin/activate
3.	Install Project Dependencies: Install required libraries by running:
pip install -r requirements.txt
________________________________________
Running the Project
Step 4: Run the Flask Server
1.	In VS Code, ensure your virtual environment is selected:
o	Click on the Python version in the bottom-left corner of the window.
o	Select the interpreter from your venv folder (e.g., .venv or venv).
2.	Run the application: Open the integrated terminal in VS Code and run:
python app.py
3.	Open the application in your browser at:

http://127.0.0.1:5000/

