from flask import Flask, render_template, request
from cipher.caesar import CaesarCipher
from cipher.vigenere import VigenereCipher
from cipher.railfence import RailFenceCipher

app = Flask(__name__)

# Home page
@app.route("/")
def home():
    return render_template('index.html')

# Caesar Cipher page
@app.route("/caesar")
def caesar():
    return render_template('caesar.html')

# Vigenere Cipher page
@app.route("/vigenere")
def vigenere():
    return render_template('vigenere.html')

# Rail Fence Cipher page
@app.route("/railfence")
def railfence():
    return render_template('railfence.html')


# Caesar Cipher Encrypt & Decrypt
@app.route("/encrypt", methods=['POST'])
def caesar_encrypt():
    text = request.form['inputPlainText']
    key = int(request.form['inputKeyPlain'])

    Caesar = CaesarCipher()
    encrypted_text = Caesar.encrypt_text(text, key)

    return f"text: {text}<br/>key: {key}<br/>encrypted text: {encrypted_text}"

@app.route("/decrypt", methods=['POST'])
def caesar_decrypt():
    text = request.form['inputCipherText']
    key = int(request.form['inputKeyCipher'])

    Caesar = CaesarCipher()
    decrypted_text = Caesar.decrypt_text(text, key)

    return f"text: {text}<br/>key: {key}<br/>decrypted text: {decrypted_text}"


# Vigenere Cipher Encrypt & Decrypt
@app.route("/vigenere/encrypt", methods=['POST'])
def vigenere_encrypt():
    text = request.form['inputPlainText']
    key = request.form['inputKeyPlain']

    Vigenere = VigenereCipher()
    encrypted_text = Vigenere.vigenere_encrypt(text, key)

    return f"text: {text}<br/>key: {key}<br/>encrypted text: {encrypted_text}"

@app.route("/vigenere/decrypt", methods=['POST'])
def vigenere_decrypt():
    text = request.form['inputCipherText']
    key = request.form['inputKeyCipher']

    Vigenere = VigenereCipher()
    decrypted_text = Vigenere.vigenere_decrypt(text, key)

    return f"text: {text}<br/>key: {key}<br/>decrypted text: {decrypted_text}"


# Rail Fence Cipher Encrypt & Decrypt
@app.route("/railfence/encrypt", methods=['POST'])
def railfence_encrypt():
    text = request.form['inputPlainText']
    key = int(request.form['inputKeyPlain'])

    RailFence = RailFenceCipher()
    encrypted_text = RailFence.rail_fence_encrypt(text, key)

    return f"text: {text}<br/>key: {key}<br/>encrypted text: {encrypted_text}"

@app.route("/railfence/decrypt", methods=['POST'])
def railfence_decrypt():
    text = request.form['inputCipherText']
    key = int(request.form['inputKeyCipher'])

    RailFence = RailFenceCipher()
    decrypted_text = RailFence.rail_fence_decrypt(text, key)

    return f"text: {text}<br/>key: {key}<br/>decrypted text: {decrypted_text}"


# Main function
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5050, debug=True)
