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

## 🧮 Task 2: BMI Calculator

A GUI-based Python application to calculate Body Mass Index (BMI), categorize results, store data over time, and visualize BMI trends using matplotlib.

---

## 📁 Project Structure

BMI_Calculator/

├── main.py # GUI application entry point

├── bmi_utils.py # BMI calculation and category logic

├── data_handler.py # CSV read/write functionality

├── bmi_plotter.py # Matplotlib plotting for BMI trends

├── BMI_Screenshot.png # Application screenshot


---

## 🚀 Features

- ✅ Calculate BMI using height and weight
- ✅ Categorize BMI (Underweight, Normal, Overweight, Obese)
- ✅ Save BMI records to a CSV file
- ✅ Visualize BMI trends using matplotlib
- ✅ Simple and interactive GUI using Tkinter

---

## 🖼️ Screenshot

![BMI Calculator](BMI_Screenshot.png)

---

## 📦 Requirements

Make sure you have the following libraries installed:

- `tkinter` (built-in with Python)
- `matplotlib`
- `pandas`

You can install the required packages using:

```bash
pip install matplotlib pandas





