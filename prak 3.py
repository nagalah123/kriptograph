def enkripsi_caesar(plaintext, kunci_geser):
    """Fungsi untuk melakukan enkripsi menggunakan Caesar Cipher."""
    ciphertext = ""
    # Pastikan kunci berada dalam rentang 0-25
    kunci = kunci_geser % 26 

    for karakter in plaintext:
        if 'a' <= karakter <= 'z':
            # Untuk huruf kecil
            # Ubah huruf menjadi nilai 0-25, geser, lalu kembali ke huruf
            nilai_ascii = ord(karakter) - ord('a')
            nilai_terenkripsi = (nilai_ascii + kunci) % 26
            karakter_terenkripsi = chr(nilai_terenkripsi + ord('a'))
            ciphertext += karakter_terenkripsi
            
        elif 'A' <= karakter <= 'Z':
            # Untuk huruf besar
            nilai_ascii = ord(karakter) - ord('A')
            nilai_terenkripsi = (nilai_ascii + kunci) % 26
            karakter_terenkripsi = chr(nilai_terenkripsi + ord('A'))
            ciphertext += karakter_terenkripsi
            
        else:
            # Karakter non-alfabet (spasi, tanda baca, dll.) tidak diubah
            ciphertext += karakter
            
    return ciphertext

def dekripsi_caesar(ciphertext, kunci_geser):
    """Fungsi untuk melakukan dekripsi menggunakan Caesar Cipher.
       Dekripsi sama dengan enkripsi dengan kunci geser negatif."""
    # Proses dekripsi sama dengan enkripsi, tetapi menggunakan kunci geser negatif
    kunci_dekripsi = -kunci_geser
    return enkripsi_caesar(ciphertext, kunci_dekripsi)

# --- Bagian Utama Program ---
if _name_ == "_main_":
    
    print("--- Caesar Cipher (Substitusi Sederhana) ---")
    
    # 1. Meminta input Plaintext
    plaintext_input = input("Masukkan Plaintext (teks asli): ")
    
    # 2. Meminta input Kunci (aturan substitusi)
    while True:
        try:
            kunci_input = int(input("Masukkan Kunci Geser (bilangan bulat, contoh: 3): "))
            if kunci_input < 0:
                print("Kunci harus bilangan bulat non-negatif. Coba lagi.")
            else:
                break
        except ValueError:
            print("Input kunci tidak valid. Masukkan bilangan bulat.")
            
    print("\n-------------------------------------------")
    
    # Proses Enkripsi
    ciphertext_hasil = enkripsi_caesar(plaintext_input, kunci_input)
    print(f"Plaintext Asli : {plaintext_input}")
    print(f"Kunci Geser    : {kunci_input}")
    print(f"Ciphertext (Terkunci): {ciphertext_hasil}")
    
    print("-------------------------------------------")
    
    # Proses Dekripsi
    plaintext_hasil = dekripsi_caesar(ciphertext_hasil, kunci_input)
    print(f"Ciphertext Masuk: {ciphertext_hasil}")
    print(f"Kunci Geser     : {kunci_input}")
    print(f"Plaintext (Terbuka) : {plaintext_hasil}")
    print("-------------------------------------------")