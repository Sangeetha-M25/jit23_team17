# NeuroCart

## Overview
NeuroCart is a Brain-Computer Interface (BCI) based smart grocery recommendation system that uses EEG signals from the Muse 2 headset to detect a user's mental state and recommend grocery products accordingly.

## Features
- Live EEG signal acquisition using Muse 2
- Brain state classification (Concentration / Relaxed)
- Personalized grocery recommendations
- Interactive web dashboard
- Shopping cart with total price in ₹
- Built using Flask and Machine Learning

## Technologies Used
- Python
- Flask
- Scikit-learn
- Pandas
- NumPy
- SciPy
- Muse 2 EEG
- Lab Streaming Layer (LSL)

## Project Structure
```
NeuroCart/
├── backend/
├── Dataset/
├── models/
├── preprocessing/
├── static/
├── templates/
└── README.md
```

## How to Run

1. Clone the repository:
   ```bash
   git clone https://github.com/Sangeetha-M25/jit23_team17.git
   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Run the Flask application:
   ```bash
   python backend/app.py
   ```

4. Open your browser and go to:
   ```
   http://127.0.0.1:5000
   ```

## Team
Team 17

## License
This project is developed for educational purposes.