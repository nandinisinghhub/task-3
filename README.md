# Task-03: Text Generation using Markov Chains

## 🧠 Objective

Implement a simple text generation algorithm using **Markov Chains**.  
This model predicts the next word based on the previous word(s) and generates new text that mimics the original style.

---

## 📌 What is a Markov Chain?

A **Markov Chain** is a statistical model where the next state (word) depends only on the current state (word or pair of words).

In simple terms:  
> If you say "I am", what word usually comes next?  
> The model learns this from training text and builds probabilities like:  
> `"I am"` → `"tired"` (40%), `"happy"` (30%), `"going"` (30%)

---

## 🗂️ Files Included

- `markov_text_gen.py` → Main Python script to build model and generate text
- `input.txt` → Training text file (can be replaced with your own)
- `README.md` → This guide

---

## 🛠️ Requirements

No external libraries required! This project runs using **pure Python**  
Just make sure you're using **Python 3+**

---

## 🚀 How to Run

### 1. 📝 Prepare your input
Open `input.txt` and paste any text you want the model to learn from.  
Example:
