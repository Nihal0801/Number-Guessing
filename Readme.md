# 🎯 Advanced Number Guessing Game (Python)

A fun and interactive command-line game built in Python where the user guesses a randomly generated number within a chosen difficulty level.  
The game includes score tracking, input validation, and replay functionality — making it a complete beginner-to-intermediate Python project.

---

## 🧠 Features

- 🎮 **Multiple Difficulty Levels:** Easy / Medium / Hard  
- 🔢 **Random Number Generation:** Uses Python’s `randint()`  
- 🧩 **Input Validation:** Handles invalid or out-of-range input safely  
- 🏆 **Score System:** Higher points for faster guesses  
- 🔁 **Replay Option:** Play multiple rounds without restarting  
- 💻 **Clean, Modular Code:** Beginner-friendly, fully commented  

---

## 🛠️ Technologies Used

- Python 3.x  
- Built-in modules: `random`, `time`

---

## ⚙️ How It Works

1. The program welcomes you and asks for a difficulty level:  
   - Easy → (1–10) with 5 attempts  
   - Medium → (1–50) with 7 attempts  
   - Hard → (1–100) with 10 attempts  
2. A random number is generated in that range.  
3. You guess numbers until you find the correct one or run out of attempts.  
4. The fewer attempts you take, the higher your score!  
5. After each round, you can choose to play again or exit.  

---

## ▶️ How to Run

### 🧩 Option 1 — Run Locally
```bash
# Clone this repository
git clone https://github.com/Nihal0801/Number-Guessing.git

# Navigate to the folder
cd Number-Guessing

# Run the game
python NumberGuessing.py
