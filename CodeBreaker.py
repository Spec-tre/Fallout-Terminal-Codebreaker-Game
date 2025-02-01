import random
import time
import sys

def slow_print(text, delay=0.03):
    
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(delay)
    print()

def display_terminal_interface(): #Fallout inspired intro
    
    
    print("*" * 10, "PIP-OS(R) V7.1.0.8", "*" * 10)
    print("=" * 40)
    slow_print("ROBCO INDUSTRIES (TM) TERMLINK PROTOCOL")
    slow_print("[COPYRIGHT 2075 ROBOCO(R)]")
    slow_print("EXEC VERSION 41.10")
    slow_print("64K RAM SYSTEM")
    slow_print("38911 BYTES FREE")
    slow_print("[NO HOLOTAPE FOUND]")
    print("=" * 40)
    slow_print("""
Welcome to Vault-Tec's Codebreaker Terminal.
You have 10 attempts to guess the correct passcode.
    """)
    print("=" * 40)
    slow_print("VALID DIGITS: 1 2 3 4 5 6")
    print("=" * 40)

def generate_code():
    
    return [str(random.randint(1, 6)) for _ in range(4)]

def guess_code():
    
    while True:
        guess = input("ENTER CODE (space-separated digits): ").split()
        if len(guess) != 4 or any(num not in "123456" for num in guess):
            slow_print("INVALID ENTRY. USE FOUR DIGITS BETWEEN 1-6.")
        else:
            return guess

def check_code(guess, real_code):
    
    correct_pos = sum(1 for g, r in zip(guess, real_code) if g == r)
    incorrect_pos = sum(min(guess.count(n), real_code.count(n)) for n in set(real_code)) - correct_pos
    return correct_pos, incorrect_pos

def game_logic():
    
    code = generate_code()
    display_terminal_interface()
    
    attempts = 10
    while attempts > 0:
        guess = guess_code()
        correct_pos, incorrect_pos = check_code(guess, code)
        
        if correct_pos == 4:
            slow_print("ACCESS GRANTED. WELCOME BACK, USER.")
            return
        
        slow_print(f"CORRECT: {correct_pos} | MISPLACED: {incorrect_pos}")
        attempts -= 1
        slow_print(f"ATTEMPTS LEFT: {attempts}")
    
    slow_print("SYSTEM LOCKED. PLEASE CONTACT ADMINISTRATOR.")
    slow_print(f"THE CODE WAS: {' '.join(code)}")

if __name__ == "__main__":
    game_logic()