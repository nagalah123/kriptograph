# vigenere_cipher_final.py
# Implementasi Vigenere Cipher berbasis OOP (langsung tampil hasil)
# Key = "renaldo sinag"
# Pesan = "bang naga"

class VigenereCipher:
    def __init__(self, key: str):
        self.key = self._normalize(key)

    def _normalize(self, text):
        """Mengubah teks menjadi huruf besar dan hanya menyisakan alfabet."""
        return "".join([c.upper() for c in text if c.isalpha()])

    def _generate_keystream(self, text):
        """Membuat keystream berdasarkan panjang pesan (hanya huruf)."""
        letters = [c for c in text if c.isalpha()]
        keystream = []
        j = 0
        for _ in letters:
            keystream.append(self.key[j % len(self.key)])
            j += 1
        return "".join(keystream)

    def _num(self, c):
        return ord(c.upper()) - 65

    def _chr(self, n):
        return chr((n % 26) + 65)

    def encrypt(self, plaintext):
        """Melakukan enkripsi Vigenere Cipher."""
        keystream = self._generate_keystream(plaintext)
        cipher = ""
        steps = []
        j = 0
        for i, ch in enumerate(plaintext):
            if ch.isalpha():
                k = keystream[j]
                pnum, knum = self._num(ch), self._num(k)
                cnum = (pnum + knum) % 26
                c = self._chr(cnum)
                cipher += c
                steps.append(f"[{i}] '{ch}' (P={pnum}) + '{k}' (K={knum}) = '{c}' (C={cnum})")
                j += 1
            else:
                cipher += ch
                steps.append(f"[{i}] '{ch}' bukan huruf → tetap.")
        summary = (
            "Proses enkripsi Vigenère Cipher mengubah setiap huruf dari plaintext menjadi angka antara 0 hingga 25 "
            "(A=0, B=1, ..., Z=25). Huruf kunci yang telah dinormalisasi diulang sepanjang pesan untuk membentuk "
            "keystream. Setiap huruf pesan dijumlahkan dengan huruf kunci yang sesuai menggunakan operasi modulo 26, "
            "lalu dikonversi kembali menjadi huruf. Karakter non-alfabet seperti spasi atau tanda baca tidak diubah "
            "agar struktur kalimat tetap sama. Teknik ini membuat pola huruf berubah secara dinamis, menjadikannya "
            "lebih aman dibandingkan sandi Caesar yang hanya memakai satu pergeseran tetap."
        )
        return cipher, steps, summary

    def decrypt(self, ciphertext):
        """Melakukan dekripsi Vigenere Cipher."""
        keystream = self._generate_keystream(ciphertext)
        plain = ""
        steps = []
        j = 0
        for i, ch in enumerate(ciphertext):
            if ch.isalpha():
                k = keystream[j]
                cnum, knum = self._num(ch), self._num(k)
                pnum = (cnum - knum + 26) % 26
                p = self._chr(pnum)
                plain += p
                steps.append(f"[{i}] '{ch}' (C={cnum}) - '{k}' (K={knum}) = '{p}' (P={pnum})")
                j += 1
            else:
                plain += ch
                steps.append(f"[{i}] '{ch}' bukan huruf → tetap.")
        summary = (
            "Dekripsi Vigenère merupakan kebalikan dari proses enkripsi. Setiap huruf sandi diubah ke angka 0–25, "
            "kemudian dikurangi dengan nilai huruf kunci yang bersesuaian menggunakan operasi modulo 26. Hasilnya "
            "dikembalikan menjadi huruf asli plaintext. Huruf non-alfabet tetap dibiarkan tanpa perubahan, sehingga "
            "pesan asli dapat dipulihkan sepenuhnya jika menggunakan kunci yang sama. Dengan cara ini, metode Vigenère "
            "mampu menjaga keamanan data teks dengan baik karena pola huruf sandinya tidak bersifat statis."
        )
        return plain, steps, summary


# ==== PROGRAM UTAMA ====
if __name__ == "__main__":
    print("=== PROGRAM VIGENERE CIPHER BERBASIS OOP ===\n")

    # Data otomatis (sesuai permintaan)
    key = "renaldo sinag"
    pesan = "bang naga"

    print(f"Kata Kunci : {key}")
    print(f"Plaintext  : {pesan}\n")

    cipher = VigenereCipher(key)

    # Proses Enkripsi
    ciphertext, enc_steps, enc_summary = cipher.encrypt(pesan)
    print("=== HASIL ENKRIPSI ===")
    print("Ciphertext :", ciphertext)
    print("\n--- Detail Proses Enkripsi ---")
    for s in enc_steps:
        print(s)
    print("\nRingkasan Proses Enkripsi (≥80 kata):")
    print(enc_summary)
    print("\n=============================================\n")

    # Proses Dekripsi
    plaintext, dec_steps, dec_summary = cipher.decrypt(ciphertext)
    print("=== HASIL DEKRIPSI ===")
    print("Plaintext :", plaintext)
    print("\n--- Detail Proses Dekripsi ---")
    for s in dec_steps:
        print(s)
    print("\nRingkasan Proses Dekripsi (≥80 kata):")
    print(dec_summary)
    print("\n=== SELESAI ===")
