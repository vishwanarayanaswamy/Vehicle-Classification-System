# Vehicle Image Classification

## Overview

This project develops a deep learning-based vehicle image classification system capable of classifying images into seven vehicle categories:

* Auto Rickshaws
* Bikes
* Cars
* Motorcycles
* Planes
* Ships
* Trains

The project compares a Custom CNN model with transfer learning models (MobileNetV2 and EfficientNetB0) to evaluate classification performance. Various evaluation techniques such as confusion matrices, classification reports, ROC curves, and SHAP visualizations are used to analyze model performance.

---

## How to Run

### Option 1: Kaggle

1. Open the notebook in Kaggle.
2. Attach the Vehicle Classification dataset.
3. Run all cells from top to bottom.
4. Generated outputs will be saved in:

```text
/kaggle/working/
```

---

### Option 2: Local System

#### Install Required Libraries

```bash
pip install tensorflow numpy pandas matplotlib seaborn scikit-learn shap pillow
```

#### Update Dataset Path

Replace the dataset path in the notebook with your local dataset location.

```python
DATASET_PATH = "your_dataset_path"
```

#### Run the Notebook

```bash
jupyter notebook
```

Open the notebook and execute all cells sequentially.

---

## Output

The notebook generates:

* Trained Models
* Accuracy and Loss Curves
* Confusion Matrices
* Classification Reports
* ROC Curves
* SHAP Visualizations
* Performance Comparison Results
