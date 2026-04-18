import tkinter as tk
from tkinter import ttk, messagebox

from core.encoding_utils import text_to_base64, base64_to_text
from core.hashing import generate_sha256_hash
from core.aes_cipher import encrypt_aes, decrypt_aes


class SecureCommApp:
    def __init__(self, root):
        self.root = root
        self.root.title("SecureComm v1.0")
        self.root.geometry("900x650")

        self.build_interface()

    def build_interface(self):
        title_label = ttk.Label(
            self.root,
            text="SecureComm 🔐",
            font=("Arial", 20, "bold")
        )
        title_label.pack(pady=10)

        subtitle_label = ttk.Label(
            self.root,
            text="Cryptography toolkit: Base64, SHA-256, AES",
            font=("Arial", 11)
        )
        subtitle_label.pack(pady=5)

        input_frame = ttk.LabelFrame(self.root, text="Input")
        input_frame.pack(fill="both", expand=True, padx=15, pady=10)

        self.input_text = tk.Text(input_frame, height=10, wrap="word")
        self.input_text.pack(fill="both", expand=True, padx=10, pady=10)

        password_frame = ttk.LabelFrame(self.root, text="AES Password")
        password_frame.pack(fill="x", padx=15, pady=5)

        self.password_entry = ttk.Entry(password_frame, show="*")
        self.password_entry.pack(fill="x", padx=10, pady=10)

        button_frame = ttk.LabelFrame(self.root, text="Actions")
        button_frame.pack(fill="x", padx=15, pady=10)

        ttk.Button(button_frame, text="Encode Base64", command=self.encode_base64).pack(side="left", padx=5, pady=10)
        ttk.Button(button_frame, text="Decode Base64", command=self.decode_base64).pack(side="left", padx=5, pady=10)
        ttk.Button(button_frame, text="Generate SHA-256", command=self.generate_hash).pack(side="left", padx=5, pady=10)
        ttk.Button(button_frame, text="Encrypt AES", command=self.encrypt_with_aes).pack(side="left", padx=5, pady=10)
        ttk.Button(button_frame, text="Decrypt AES", command=self.decrypt_with_aes).pack(side="left", padx=5, pady=10)
        ttk.Button(button_frame, text="Clear", command=self.clear_fields).pack(side="left", padx=5, pady=10)

        output_frame = ttk.LabelFrame(self.root, text="Output")
        output_frame.pack(fill="both", expand=True, padx=15, pady=10)

        self.output_text = tk.Text(output_frame, height=12, wrap="word")
        self.output_text.pack(fill="both", expand=True, padx=10, pady=10)

    def get_input_text(self):
        return self.input_text.get("1.0", tk.END).strip()

    def set_output_text(self, content):
        self.output_text.delete("1.0", tk.END)
        self.output_text.insert(tk.END, content)

    def encode_base64(self):
        text = self.get_input_text()
        if not text:
            messagebox.showwarning("Warning", "Please enter text to encode.")
            return
        result = text_to_base64(text)
        self.set_output_text(result)

    def decode_base64(self):
        text = self.get_input_text()
        if not text:
            messagebox.showwarning("Warning", "Please enter Base64 text to decode.")
            return
        try:
            result = base64_to_text(text)
            self.set_output_text(result)
        except Exception:
            messagebox.showerror("Error", "Invalid Base64 input.")

    def generate_hash(self):
        text = self.get_input_text()
        if not text:
            messagebox.showwarning("Warning", "Please enter text to hash.")
            return
        result = generate_sha256_hash(text)
        self.set_output_text(result)

    def encrypt_with_aes(self):
        text = self.get_input_text()
        password = self.password_entry.get()

        if not text:
            messagebox.showwarning("Warning", "Please enter text to encrypt.")
            return

        if not password:
            messagebox.showwarning("Warning", "Please enter an AES password.")
            return

        try:
            result = encrypt_aes(text, password)
            self.set_output_text(result)
        except Exception as e:
            messagebox.showerror("Error", f"AES encryption failed:\n{e}")

    def decrypt_with_aes(self):
        text = self.get_input_text()
        password = self.password_entry.get()

        if not text:
            messagebox.showwarning("Warning", "Please enter encrypted text to decrypt.")
            return

        if not password:
            messagebox.showwarning("Warning", "Please enter an AES password.")
            return

        try:
            result = decrypt_aes(text, password)
            self.set_output_text(result)
        except Exception:
            messagebox.showerror("Error", "AES decryption failed. Check the encrypted text or password.")

    def clear_fields(self):
        self.input_text.delete("1.0", tk.END)
        self.output_text.delete("1.0", tk.END)
        self.password_entry.delete(0, tk.END)


def run_app():
    root = tk.Tk()
    app = SecureCommApp(root)
    root.mainloop()


if __name__ == "__main__":
    run_app()