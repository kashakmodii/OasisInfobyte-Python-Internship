# 🌟 Python Programming Internship at Oasis Infobyte

This repository contains all the tasks completed during my internship at **Oasis Infobyte** under the domain of **Python Programming**. The internship provided hands-on experience in developing Python-based applications and solving real-world problems through code.

---

## 📌 Task 1: Voice Assistant

### ✅ Objective

The goal of this task is to build a **basic voice assistant** using Python that can:
- Take voice commands from the user
- Recognize the command using speech recognition
- Perform simple actions like:
  - Telling the current time/date
  - Opening websites (e.g., Google, YouTube)
  - Responding with speech output

---

### ⚙️ Technologies Used

- Python 3
- `speech_recognition`
- `pyttsx3` (Text-to-Speech)
- `datetime`
- `webbrowser`
- `os`

---

### 🚀 How It Works

1. The assistant greets the user based on the time of the day.
2. Listens for voice input.
3. Recognizes the spoken words using Google Web Speech API.
4. Based on the command, it performs actions or responds back using speech.

---

### ▶️ How to Run

1. Install the dependencies:

```bash
pip install pyttsx3 speechrecognition
```
---

## Task 2: BMI Calculator

### Objective
The goal of this task is to create a Body Mass Index (BMI) calculator application that:
- Takes user input for weight and height
- Calculates BMI based on the provided measurements
- Classifies the BMI into categories (Underweight, Normal, Overweight, Obese)
- Displays the result visually
- Optionally saves the data for future reference

### Features
- Interactive BMI calculation
- Data visualization (plotting BMI trends if multiple entries exist)
- CSV data storage for tracking history
- User-friendly interface

### Technologies Used
- Python 3
- pandas (for data handling)
- matplotlib (for visualization)
- CSV module (for data storage)

### File Structure
├── BML_Calculator/

│ ├── main.py # Main application logic

│ ├── bml_utils.py # Utility functions

│ ├── bml_plotter.py # Visualization functions

│ ├── bml_data.csv # Sample data storage

│ ├── dist_bundle.py # Distribution helper

│ └── BML_Screenshot.png # Application screenshot


### How It Works
1. User inputs their weight and height
2. System calculates BMI using formula: BMI = weight(kg) / (height(m))²
3. Result is classified and displayed
4. Data can be saved to CSV for future reference
5. Visualization shows BMI trends if historical data exists

### How to Run
1. Install dependencies:
   ```bash
   pip install pandas matplotlib

---

## 📌 Task 3: Password Generator

### Objective

The goal of this task is to build a **random password generator** in Python that can:
- Allow users to choose password length
- Allow inclusion of letters, numbers, and/or symbols
- Generate secure, randomized passwords
- Optionally copy the password to clipboard

---

### ⚙️ Technologies Used

- Python 3  
- `random` (for random character generation)  
- `string` (for predefined character sets)  
- `pyperclip` *(optional, for clipboard copy feature)*

---

### 🚀 How It Works

1. The program asks the user to specify:
   - Desired password length (between 8 and 32)
   - Whether to include letters, numbers, and/or symbols
2. Based on the user’s choices, a set of valid characters is created.
3. A random password is generated using the selected character set.
4. The password is displayed and optionally copied to the clipboard if `pyperclip` is installed.

---

### ▶️ How to Run

1. (Optional) Install the clipboard support library:

```bash
pip install pyperclip
```

---

## Task 4:Simple Weather App in Python

This is a basic terminal-based weather application built with Python. It uses the OpenWeatherMap API to fetch current weather data for any city.

## ✅ Features

- Get temperature, weather condition, humidity, and wind speed
- Simple CLI-based input and output
- Built-in OpenWeatherMap API key (for demo use)

## 🚀 How to Run

### 1. Clone the repository or download the files.

### 2. Install the required package:

```bash
pip install requests
```








