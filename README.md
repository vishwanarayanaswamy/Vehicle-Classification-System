Here is your **complete polished README in one block** — ready to copy and paste directly into GitHub:

```markdown
# 🚗 Vehicle Image Classification System

## 📌 Overview

This project is a deep learning-based vehicle image classification system that classifies images into **7 categories**:

- Auto Rickshaws  
- Bikes  
- Cars  
- Motorcycles  
- Planes  
- Ships  
- Trains  

The project compares multiple deep learning approaches:
- Custom CNN Model  
- Transfer Learning (MobileNetV2)  
- Transfer Learning (EfficientNetB0)  

Model performance is evaluated using:
- Confusion Matrix  
- Classification Report  
- ROC Curves  
- SHAP Explainability Visualizations  

A **Streamlit web application** is also included for real-time image prediction.

---

## 🧠 Model Details

- Input Size: 224x224 images  
- Framework: TensorFlow / Keras  
- Best Model: Custom CNN (or best-performing model)  
- Loss Function: Categorical Crossentropy  
- Optimizer: Adam  

---

## 📂 Project Structure

```

Vehicle-Classification-System/
│
├── app.py                         # Streamlit frontend
├── vehicle-classification-system.ipynb   # Model training notebook
├── best_model.keras              # Trained model (not uploaded to GitHub)
├── requirements.txt
├── README.md

````

---

## 🚀 How to Run

### 🔹 1. Install Dependencies

```bash
pip install -r requirements.txt
````

OR manually:

```bash
pip install tensorflow streamlit numpy pandas matplotlib seaborn scikit-learn shap pillow
```

---

### 🔹 2. Run Streamlit App

```bash
streamlit run app.py
```

---

## ⚠️ Important Note (Model File)

The trained model file (`best_model.keras`) is not included in this repository because it exceeds GitHub's 100MB file limit.

👉 To run the project:

* Download or keep `best_model.keras` locally
* Place it in the same directory as `app.py`

---

## 📊 Outputs Generated

* Trained models
* Accuracy & loss curves
* Confusion matrices
* Classification reports
* ROC curves
* SHAP explanations
* Model comparison results

---

## 🖥️ Features of Streamlit App

* Upload vehicle image
* Real-time prediction
* Displays predicted class
* Confidence score output
* Simple and interactive UI

---

## 📌 Dataset

Dataset contains vehicle images categorized into 7 classes:
Auto Rickshaws, Bikes, Cars, Motorcycles, Planes, Ships, Trains.

Used for training and evaluating deep learning models.

---

## 🛠️ Tech Stack

* Python
* TensorFlow / Keras
* Streamlit
* NumPy / Pandas
* Matplotlib / Seaborn
* Scikit-learn
* SHAP

---

## 👨‍💻 Author

Vishwa Narayanaswamy

```

---



Just say 👍
```
