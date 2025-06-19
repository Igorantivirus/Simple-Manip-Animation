import os

if __name__ == "__main__":
    os.system("cls" if os.name == "nt" else "clear")
    os.system("manim -pqh main.py LaTexProcessor")