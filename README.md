
# Smile Detection Project

## Overview
This project implements a smile detection model using a Logistic regression. The model detects whether a person is smiling or not from facial images, achieving an accuracy of 88.80%. The user interface is built with Streamlit, and the application is deployed on Render.com for easy access.

## Model Performance
The model was evaluated on a test dataset with the following metrics:

- **Accuracy**: 0.8880 (88.80%)
- **Confusion Matrix**:
  ```
  [[107  13]
   [ 14 107]]
  ```
  - True Negatives (Non-Smile, Class 0): 107
  - False Positives: 13
  - False Negatives: 14
  - True Positives (Smile, Class 1): 107

- **Classification Report**:
  ```
                       precision   recall  f1-score   support

  Class 0 (Non-Smile)    0.88      0.89      0.89       120
  Class 1 (Smile)        0.89      0.88      0.89       121

  Accuracy                              0.89       241
  Macro Avg             0.89      0.89      0.89       241
  Weighted Avg          0.89      0.89      0.89       241
  ```

## Features
- **Smile Detection**: Upload an image, and the model predicts whether the person is smiling.
- **Streamlit UI**: A user-friendly web interface for uploading images and viewing predictions.
- **Deployment**: Hosted on Render.com for seamless access.

## Installation
To run the project locally, follow these steps:

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/your-username/smile-detection.git
   cd smile-detection
   ```

2. **Install Dependencies**:
   Ensure you have Python 3.8+ installed. Then, install the required packages:
   ```bash
   pip install -r requirements.txt
   ```

3. **Run the Streamlit App**:
   Start the Streamlit server:
   ```bash
   streamlit run app.py
   ```
   Open your browser and navigate to `http://localhost:8501`.

## Project Structure
```
smile-detection/
├── app.py                  # Streamlit application script
├── model.pkl               # trained model file
├── scaler.pkl              # scaled features file  
├── requirements.txt        # Python dependencies
├── README.md               # Project documentation
└── datasets/               # (Optional) Directory for sample images
```

## Deployment on Render.com
The project is deployed on Render.com. To deploy your own instance:

1. **Create a Render Account**: Sign up at [Render.com](https://render.com).
2. **Create a New Web Service**:
   - Connect your GitHub repository.
   - Set the runtime to Python.
   - Specify the start command: `streamlit run app.py --server.port $PORT`.
3. **Environment Variables**:
   - Add `PYTHON_VERSION` (e.g., `3.8`).
   - Ensure dependencies are listed in `requirements.txt`.
4. **Deploy**: Trigger the deployment and access the app via the provided URL.

## Usage
1. Open the deployed app or local Streamlit server.
2. Upload an image of a person's face.
3. View the prediction: "Smiling" or "Not Smiling" with the confidence score.

## Requirements
- Python 3.8+
- Streamlit
- joblib
- scikit-learn
- NumPy
- Pillow

Install dependencies using:
```bash
pip install streamlit numpy pillow joblib scikit-learn
```

## Limitations
- The model may struggle with poor lighting, occlusions, or non-frontal faces.
- Accuracy is based on the test dataset; performance may vary with real-world images.

## Future Improvements
- Enhance model robustness with more diverse training data.
- Add real-time smile detection using webcam input.
- Optimize the model for faster inference on low-end devices.

## License
This project is licensed under the MIT License. See the `LICENSE` file for details.

## Contact
For questions or contributions, please open an issue or contact [vel.prabhakaran.ds@gmail.com](mailto:vel.prabhakaran.ds@gmail.com).
