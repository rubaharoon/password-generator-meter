import re
import random
import string
import streamlit as st

def check_password_strength(password):
    score = 0
    feedback = []
    
    # Blacklist common passwords
    common_passwords = ["password", "123456", "password123", "qwerty", "abc123", "letmein"]
    if password.lower() in common_passwords:
        return 1, "This password is too common. Choose a more unique one."
    
    # Length Check
    if len(password) >= 8:
        score += 1
    else:
        feedback.append("Increase the password length to at least 8 characters.")
    
    # Upper and Lower Case Check
    if re.search(r"[a-z]", password) and re.search(r"[A-Z]", password):
        score += 1
    else:
        feedback.append("Include both uppercase and lowercase letters.")
    
    # Digit Check
    if re.search(r"\d", password):
        score += 1
    else:
        feedback.append("Add at least one numeric digit (0-9).")
    
    # Special Character Check
    if re.search(r"[!@#$%^&*]", password):
        score += 1
    else:
        feedback.append("Use at least one special character (!@#$%^&*).")
    
    # Assign Strength Level
    if score <= 2:
        strength = "Weak"
    elif score <= 4:
        strength = "Moderate"
    else:
        strength = "Strong"
    
    return score, strength, feedback

def generate_strong_password(length=12):
    characters = string.ascii_letters + string.digits + "!@#$%^&*"
    return ''.join(random.choice(characters) for _ in range(length))

def main():
    st.set_page_config(page_title="Password Strength Meter", page_icon="🔒", layout="centered")
    
    st.markdown(
        """
        <style>
        .main {text-align: center;}
        .stButton button {background-color: #4CAF50; color: white; font-size: 16px;}
        </style>
        """,
        unsafe_allow_html=True,
    )
    
    st.title("🔐 Password Strength Meter")
    st.subheader("Ensure Your Password is Secure and Strong")
    st.write(
        "Protect your online accounts by using a strong password. This tool analyzes your password's strength and provides suggestions to improve it."
    )
    
    password = st.text_input("Enter a password:", type="password")
    
    if password:
        score, strength, feedback = check_password_strength(password)
        st.markdown(f"**🔹 Password Strength:** `{strength}` (Score: {score}/5)")
        
        if strength == "Weak" or strength == "Moderate":
            st.warning("**Suggestions to improve your password:**")
            for tip in feedback:
                st.markdown(f"- {tip}")
        else:
            st.success("✅ Your password is strong! Great job!")
    
    if st.button("🔑 Generate a Strong Password"):
        new_password = generate_strong_password()
        st.markdown(f"**Suggested Password:** `{new_password}`")

if __name__ == "__main__":
    main()
