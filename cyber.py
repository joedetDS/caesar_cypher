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

# App title
st.title("Caesar Cipher: Encryption and Decryption Tool")
st.subheader("Encrypt or Decrypt your messages easily!")

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
st.text("Try out these example messages:")

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
