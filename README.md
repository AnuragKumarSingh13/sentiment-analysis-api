# Sentiment Analysis of Amazon Food Reviews

## Project Overview
This project performs **sentiment analysis** on Amazon customer reviews for food products using **Machine Learning**. 
The system classifies reviews as **Positive** or **Negative** based on the review text.

---

## Dataset
- **Dataset Name:** Amazon Fine Food Reviews  
- **Source:** [Kaggle](https://www.kaggle.com/datasets/snap/amazon-fine-food-reviews)  
- **Columns Used:**
  - `Text` → Review text
  - `Score` → Rating (1–5), converted to binary sentiment

**Sentiment Mapping:**
- Score 4 or 5 → Positive (1)  
- Score 1 or 2 → Negative (0)  
- Score 3 → Neutral (removed from dataset)

---

## Tech Stack
- **Programming Language:** Python
- **Libraries:** Pandas, Scikit-Learn, Joblib, Streamlit
- **Model:** Logistic Regression
- **Deployment:** Streamlit

---

## Project Structure
```
project/
│
├── Reviews.csv               # Original dataset
├── sentiment_model.pkl       # Trained ML model (generated after training)
├── vectorizer.pkl            # TF-IDF vectorizer (generated after training)
├── app.py                    # Streamlit app for prediction
└── README.md                 # Project documentation
```

---

## Installation & Setup
1. Clone the repository:
   ```bash
   git clone <your-github-repo-url>
   cd project
   ```

2. Install required libraries:
   ```bash
   pip install pandas scikit-learn joblib streamlit
   ```

3. Make sure the following files are in the project directory:
   - `sentiment_model.pkl`
   - `vectorizer.pkl`
   - `app.py`

---

## How to Run

### 1. Run in Google Colab (Optional)
- Upload `Reviews.csv` to Colab
- Execute the Python scripts step by step:
  - Load and clean data
  - Vectorize reviews
  - Train model
  - Save `sentiment_model.pkl` and `vectorizer.pkl` using Joblib

### 2. Run Streamlit App in VS Code
```bash
streamlit run app.py
```
- Open the web app in your browser
- Enter a customer review
- Click **Predict Sentiment**
- The app displays if the review is **Positive** or **Negative**

---

## Author
**Your Name**  
- GitHub: [YourGitHubUsername](https://github.com/YourGitHubUsername)  
