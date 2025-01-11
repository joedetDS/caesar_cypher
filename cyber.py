import streamlit as st
import pyperclip
import time

# Caesar Cipher function for encryption and decryption
def caesar_cipher(text, shift, mode="encrypt"):
    result = ""
    for char in text:
        if char.isalpha():  # Check if character is a letter
            start = ord('A') if char.isupper() else ord('a')
            if mode == "encrypt":
                result += chr((ord(char) - start + shift) % 26 + start)
            elif mode == "decrypt":
                result += chr((ord(char) - start - shift) % 26 + start)
        else:
            result += char  # Non-alphabetic characters remain unchanged
    return result

# Set the background color and styling
st.markdown("""
    <style>
    body {
        background-color: #f0f4f8;
    }
    .title {
        font-size: 40px;
        font-weight: bold;
        color: #4CAF50;
    }
    .subtitle {
        font-size: 20px;
        font-style: italic;
        color: #888;
    }
    .info-text {
        font-size: 16px;
        color: #333;
    }
    .result-text {
        font-size: 20px;
        font-weight: bold;
        color: #1E88E5;
    }
    .button {
        background-color: #2196F3;
        color: white;
        font-size: 16px;
        border-radius: 5px;
    }
    </style>
""", unsafe_allow_html=True)

# App title with custom styles
st.markdown('<p class="title">Caesar Cipher: Encryption and Decryption Tool</p>', unsafe_allow_html=True)
st.markdown('<p class="subtitle">Encrypt or Decrypt your messages easily!</p>', unsafe_allow_html=True)

# Input fields
text = st.text_area("Enter your message:")
shift = st.slider("Select Shift Value (Key):", min_value=1, max_value=25, value=3)
mode = st.radio("Choose an option:", ("Encrypt", "Decrypt"))

# Button to process the cipher
if st.button("Process"):
    if text:
        # Show loading spinner during processing
        with st.spinner('Processing your message...'):
            time.sleep(2)  # Simulate processing time
            processed_text = caesar_cipher(text, shift, mode.lower())
            st.write(f"### Result: {processed_text}")
            if st.button("Copy Result"):
                pyperclip.copy(processed_text)  # Copy the result to clipboard
                st.success("Result copied to clipboard!")
    else:
        st.warning("Please enter a message to process.")
    
# Additional notes
st.markdown("---")
st.info("""
### Notes:
- Shift value determines how many positions each letter is shifted in the alphabet.
- Non-alphabetic characters (e.g., numbers, symbols) remain unchanged.
- Use the same shift value to decrypt an encrypted message.
""")

# Interactive Example Buttons
st.markdown("---")
st.markdown('<p class="info-text">Try out these example messages:</p>', unsafe_allow_html=True)

# Example Buttons for pre-set messages
if st.button("Try Example: Encrypt 'HELLO' with Shift 3"):
    text = "HELLO"
    shift = 3
    mode = "Encrypt"
    processed_text = caesar_cipher(text, shift, mode.lower())
    st.write(f"### Result: {processed_text}")
    
if st.button("Try Example: Decrypt 'KHOOR' with Shift 3"):
    text = "KHOOR"
    shift = 3
    mode = "Decrypt"
    processed_text = caesar_cipher(text, shift, mode.lower())
    st.write(f"### Result: {processed_text}")
