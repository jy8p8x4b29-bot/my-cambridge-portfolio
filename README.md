# 🏛️ Cambridge Python Portfolio: Advanced Logic & UI Engineering

Welcome to my personal software development portfolio. This repository contains advanced Python projects designed to demonstrate clean code architecture, data structure optimization, and human-computer interaction (HCI) concepts for my future application to the University of Cambridge.

---

## 🕹️ Project 1: Bilingual Hangman Trivia (v1.1 Patch)
A feature-rich, console-based implementation of the classic word-guessing game with advanced UI/UX modifications.

### 🚀 Core Features & Patches:
* **Press Start Sequence:** Arcade-style initialization requiring a specific key-input (`S` / `Ы`) with multi-keyboard layout protection.
* **Console UI Animation (DedSec Style Easter Egg):** Implements dynamic server connection simulation using real-time frame buffering (`sys.stdout.flush`) and animated loading bars (`█`).
* **Full Localization (RU/EN):** Dynamic multi-language dictionary mapping for menus, hidden lists, and validation.
* **Cambridge Vocabulary:** Contains 23 specialized keywords, including university culture terms (*Tripos, Matriculation, Supervisor, Gown, Punting*).
* **State Management:** Real-time tracking of points (`+10` for a hit, `-5` for a miss) and player health.

### 🧠 Computer Science Concepts Applied:
* **Python Sets (`set`):** Utilized mathematical set operations (`alphabet - used_letters`) for O(1) fast lookup execution.
* **Asynchronous Timing:** Leveraged `time.sleep` loops for frame-by-frame text rendering.

---

## 🔮 Project 2: Digital Daniel Atlas — 52 Cards Forcing
A psychological illusion engine built on the principles of cognitive science, human attention limitations, and automated data processing. Inspired by the movie *Now You See Me*.

### 🚀 Core Features:
* **Automated Deck Generation:** Programmatically populates a standard 52-card international deck in one line of code.
* **Frame-Switching Flash Effect:** Instantly clears old buffer memory using automated line spacing (`\n * 40`), preventing the user from reviewing previous cards.
* **Psychological Priming Forcing:** Executes variable-delay data rendering (650ms on the target card vs 40ms on other cards) to force the human eye to perceive only the target card.
* **Autonomy:** Features full random deck shuffling (`random.shuffle`) and dynamic victim card allocation on every run.

### 🧠 Computer Science Concepts Applied:
* **List Comprehension:** Implemented compressed, highly efficient nested generation syntax for maximum speed.
* **Stochastic Logic:** Applied random module distribution algorithms for unpredictable card combinations.

