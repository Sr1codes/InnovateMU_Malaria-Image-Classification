 # InnovateMU Hackathon





# Malaria Image Classification using CNN
A **Convolutional Neural Network (CNN)** based machine learning model to detect **malaria-infected blood cells**. This project was developed for the **InnovateMU Hackathon** to demonstrate how AI can assist in early malaria diagnosis.

## Project Overview
Malaria is a life-threatening disease affecting millions worldwide. Early and accurate detection is critical but often limited by resource constraints and reliance on manual microscopy. This project automates malaria detection using **cell image classification**, providing fast, reliable predictions.

Key features:
* Classifies blood cell images as **Parasitized** or **Uninfected**.
* CNN-based model trained on the **Kaggle Malaria Dataset**.
* High validation accuracy (~94%).
* **Interactive Streamlit App** for image upload and instant predictions.

## Getting Started
### Prerequisites
Make sure you have Python 3.x installed. Install required packages:
``` bash
pip install -r requirements.txt
```

### Run the Streamlit App
Launch the web app to test predictions:
``` bash
streamlit run app.py
```

## Dataset
The model uses the [Cell Images for Detecting Malaria dataset](https://www.kaggle.com/datasets/iarunava/cell-images-for-detecting-malaria) from Kaggle.
* Contains images of **Parasitized** and **Uninfected** blood cells.
* Images are resized to 128x128 pixels for model training.

## Model
* **Architecture**: CNN with Conv2D, MaxPooling, Dense layers, and Dropout
* **Loss Function**: Binary cross-entropy
* **Optimizer**: Adam
* **Performance**: Validation accuracy ~94%, with evaluation metrics including **confusion matrix** and **classification report**.

## Usage
1. Clone the repository:
``` bash
git clone <repository-url>
cd InnovateMUMachineLearningModel
```
2. Install dependencies:
``` bash
pip install -r requirements.txt
```

3. Run the Streamlit app:
``` bash
streamlit run app.py
```
4. Upload an image of a blood cell and see the prediction (Parasitized vs Uninfected).

## Acknowledgements
* Dataset: [Kaggle - Cell Images for Detecting Malaria](https://www.kaggle.com/datasets/iarunava/cell-images-for-detecting-malaria)
* Hackathon: **InnovateMU 2025**
