# 📩 SMS Spam Classifier (AI/ML Project)

## About the Project
This project is a Machine Learning application that classifies SMS messages as **Spam** or **Not Spam**. 
It uses a Naive Bayes classifier to analyze the text and make predictions.  
This is a practical AI/ML project suitable for beginners, showing real-world application of supervised learning.

## Objective
The goal of this project is to automatically detect spam messages, which can help in filtering unwanted or harmful messages in messaging platforms.

## Tech Stack
- Python
- Pandas
- Numpy
- Scikit-learn

## Dataset
- Save the dataset as `spam.csv` in the project folder.
- Format:

label,message  
ham,Hello how are you  
spam,Win money now!!!

- **Label:** `ham` = not spam, `spam` = spam message  
- **Message:** The actual SMS text  
- A sample dataset is included for testing.

## How to Run the Project
1. Install dependencies  
Open terminal/command prompt in the project folder and run:

pip install -r requirements.txt

2. Run the program

python main.py

3. Test messages  
- Type any message to see if it is predicted as Spam or Not Spam  
- Type `exit` to stop the program

## Output
- Shows model accuracy on test data  
- Predicts whether a custom message is Spam or Not Spam in real time  
- Interactive and user-friendly terminal interface

## Features
- Supervised learning with Naive Bayes  
- Text preprocessing using CountVectorizer  
- Command-line interface for easy testing  
- Ready for dataset expansion



## Prolog Implementation

This project also includes a Prolog-based approach for spam detection using logical rules.

File: spam_detection.pl

It demonstrates rule-based AI, where spam messages are identified based on predefined keywords.


## Conclusion
Machine Learning can effectively detect spam messages in SMS. This project demonstrates a real-life application of AI and ML, combining data preprocessing, model training, and interactive prediction.

![Spam SMS Classifier Screenshot](https://github.com/yug25bce10639-png/spam-sms-classifier-ml/blob/main/screenshots/Screenshot%202026-03-22%20000411.png)

![Spam SMS Classifier Screenshot](https://github.com/yug25bce10639-png/spam-sms-classifier-ml/blob/main/screenshots/Screenshot%202026-03-22%20000145.png)

![Spam SMS Classifier Screenshot](https://github.com/yug25bce10639-png/spam-sms-classifier-ml/blob/main/screenshots/Screenshot%202026-03-22%20000215.png)

![Spam SMS Classifier Screenshot](https://github.com/yug25bce10639-png/spam-sms-classifier-ml/blob/main/screenshots/Screenshot%202026-03-22%20000312.png)

![Spam SMS Classifier Screenshot](https://github.com/yug25bce10639-png/spam-sms-classifier-ml/blob/main/screenshots/Screenshot%202026-03-22%20000333.png)
