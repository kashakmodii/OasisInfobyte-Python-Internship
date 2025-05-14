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

### Screenshot
![BMI Calculator Screenshot](./BMI_Calculator/BML_Screenshot.png)

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






