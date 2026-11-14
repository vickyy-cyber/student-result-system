# Student Result Management System

## Project description
A menu-driven Python application for registering students, recording five subject scores, calculating totals, averages and grades, producing report cards, analysing class results, and storing records in a JSON file.

## Requirements
- Python 3.9 or newer
- Visual Studio Code (recommended, but not compulsory)

## Project structure
```text
student_result_system/
├── main.py
├── student.py
├── results.py
├── storage.py
├── reports.py
├── data/
│   └── students.json
└── README.md
```

## How to run the program
1. Install Python.
2. Extract the project ZIP file.
3. Open the `student_result_system` folder in Visual Studio Code.
4. Open the VS Code terminal: **Terminal > New Terminal**.
5. Confirm that the terminal is inside the `student_result_system` folder.
6. Run:
   ```bash
   python main.py
   ```
   On some Windows computers, use:
   ```bash
   py main.py
   ```
7. Use the numbered menu to register students, enter scores and generate reports.

The `data/students.json` file is created automatically when the program first saves data. Do not delete it if you want to keep your records.

## Grading scale used
- A: 70–100
- B: 60–69.99
- C: 50–59.99
- D: 45–49.99
- F: Below 45

## Section 5: GitHub and Version Control — step-by-step guide

### A. Create a GitHub account
1. Open https://github.com in your browser.
2. Click **Sign up**.
3. Enter your email address, create a password and choose a username.
4. Complete GitHub's verification steps.
5. Verify your email address and sign in.

### B. Create a new repository
1. After signing in, click the **+** icon at the top-right of GitHub.
2. Select **New repository**.
3. Enter the repository name: `student-result-system`.
4. Add this description: `Python Student Result Management System`.
5. Select **Public** so your instructor can access it, unless your instructor tells you otherwise.
6. Do not add a README on GitHub if you are uploading this project's existing README.
7. Click **Create repository**.

### C. Upload the project using GitHub's website (easiest method)
1. Open the new `student-result-system` repository.
2. Click **Add file**, then **Upload files**.
3. Open the extracted `student_result_system` folder on your computer.
4. Select the project files and the `data` folder, then drag them into the GitHub upload area. Keep the folder structure.
5. Scroll down to **Commit changes**.
6. Enter a message such as `Add initial Student Result Management System`.
7. Click **Commit changes**.
8. Check that `main.py`, `student.py`, `results.py`, `storage.py`, `reports.py`, `README.md` and the `data` folder appear in the repository.

### D. Make regular commits using Git (recommended)
1. Install Git from https://git-scm.com/downloads if it is not already installed.
2. Open the project folder in VS Code.
3. Open **Terminal > New Terminal**.
4. Run these commands one at a time:
   ```bash
   git init
   git add .
   git commit -m "Create project structure and initial files"
   ```
5. Copy your repository URL from GitHub. It will look like:
   `https://github.com/YOUR-USERNAME/student-result-system.git`
6. Connect your local folder to the GitHub repository:
   ```bash
   git branch -M main
   git remote add origin https://github.com/YOUR-USERNAME/student-result-system.git
   git push -u origin main
   ```
7. Whenever you make a new change, save your files and run:
   ```bash
   git add .
   git commit -m "Describe the change you made"
   git push
   ```
8. Use meaningful commit messages, for example:
   - `Add student registration feature`
   - `Add score calculation and grading`
   - `Add JSON data storage`
   - `Add report card and class statistics`
   - `Update project documentation`

If Git says that `origin` already exists, do not repeat the remote-add command. Use `git remote -v` to check the saved repository address.

### E. Copy your GitHub repository link
1. Open your repository page on GitHub.
2. Click the green **Code** button.
3. Copy the HTTPS URL, for example:
   `https://github.com/YOUR-USERNAME/student-result-system`
4. Paste that URL into the lecturer's official Google Form.

## Final submission checklist
- [ ] Full name
- [ ] Matriculation number
- [ ] Department
- [ ] Project title
- [ ] Short description of the system
- [ ] GitHub username
- [ ] GitHub repository URL
- [ ] Short explanation of the Python concepts used
- [ ] Confirm that the program runs without major errors
- [ ] Submit through the official Google Form

## Python concepts demonstrated
Variables and data types, type conversion, if/elif/else, while and for loops, lists, dictionaries, functions, sorting, exception handling, JSON file handling, modules, classes and objects, date/time handling, and Python standard-library modules.
