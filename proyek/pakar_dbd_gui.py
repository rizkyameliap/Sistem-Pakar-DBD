from pyswip import Prolog
from tkinter import messagebox
import tkinter as tk
from tkinter import ttk

# Inisialisasi Prolog
prolog = Prolog()
prolog.consult("pakar_dbd_gui.pl")  # Ganti nama file Prolog

# Variabel global
penyakit = list()
gejala = dict()
index_penyakit = 0
index_gejala = 0
current_penyakit = ""
current_gejala = ""

# Fungsi untuk memulai diagnosa
def mulai_diagnosa():
    global penyakit, gejala, index_penyakit, index_gejala

    # Bersihkan fakta sebelumnya
    prolog.retractall("gejala_pos(_)")
    prolog.retractall("gejala_neg(_)")

    start_btn.configure(state=tk.DISABLED)
    yes_btn.configure(state=tk.NORMAL)
    no_btn.configure(state=tk.NORMAL)

    # Ambil daftar penyakit dan gejalanya
    penyakit = [p["X"].decode() for p in list(prolog.query("penyakit(X)"))]
    for p in penyakit:
        gejala[p] = [g["X"] for g in list(prolog.query(f'gejala(X, "{p}")'))]

    index_penyakit = 0
    index_gejala = -1
    pertanyaan_selanjutnya()

# Fungsi untuk menampilkan pertanyaan selanjutnya
def pertanyaan_selanjutnya(ganti_penyakit=False):
    global current_penyakit, current_gejala, index_penyakit, index_gejala

    if ganti_penyakit:
        index_penyakit += 1
        index_gejala = -1

    if index_penyakit >= len(penyakit):
        hasil_diagnosa()
        return

    current_penyakit = penyakit[index_penyakit]
    index_gejala += 1

    if index_gejala >= len(gejala[current_penyakit]):
        hasil_diagnosa(current_penyakit)
        return

    current_gejala = gejala[current_penyakit][index_gejala]

    if list(prolog.query(f"gejala_pos({current_gejala})")):
        pertanyaan_selanjutnya()
        return
    elif list(prolog.query(f"gejala_neg({current_gejala})")):
        pertanyaan_selanjutnya(ganti_penyakit=True)
        return

    pertanyaan = list(prolog.query(f"pertanyaan({current_gejala},Y)"))[0]["Y"].decode()
    tampilkan_pertanyaan(pertanyaan)

# Fungsi untuk menampilkan pertanyaan ke kotak teks
def tampilkan_pertanyaan(pertanyaan):
    kotak_pertanyaan.configure(state=tk.NORMAL)
    kotak_pertanyaan.delete(1.0, tk.END)
    kotak_pertanyaan.insert(tk.END, pertanyaan)
    kotak_pertanyaan.configure(state=tk.DISABLED)

# Fungsi untuk memproses jawaban pengguna
def jawaban(jwb):
    if jwb:
        prolog.assertz(f"gejala_pos({current_gejala})")
        pertanyaan_selanjutnya()
    else:
        prolog.assertz(f"gejala_neg({current_gejala})")
        pertanyaan_selanjutnya(ganti_penyakit=True)

# Fungsi untuk menampilkan hasil diagnosa
def hasil_diagnosa(penyakit=""):
    if penyakit:
        messagebox.showinfo("Hasil Diagnosa", f"Anda terdeteksi {penyakit}.")
    else:
        messagebox.showinfo("Hasil Diagnosa", "Tidak terdeteksi penyakit.")

    yes_btn.configure(state=tk.DISABLED)
    no_btn.configure(state=tk.DISABLED)
    start_btn.configure(state=tk.NORMAL)

# ------------------ GUI TKINTER ------------------

# Inisialisasi jendela utama
root = tk.Tk()
root.title("Sistem Pakar Diagnosis Penyakit DBD")
root.configure(bg="#f7f7f7")

# Frame utama
mainframe = tk.Frame(root, bg="#f7f7f7", padx=20, pady=20)
mainframe.pack(fill=tk.BOTH, expand=True)

# Judul
judul = tk.Label(mainframe, text="Aplikasi Diagnosa Penyakit DBD", font=("Helvetica", 18, "bold"), bg="#f7f7f7", fg="#2c3e50")
judul.grid(column=0, row=0, columnspan=3, pady=(0, 10))

# Label pertanyaan
label_pertanyaan = tk.Label(mainframe, text="Kolom Pertanyaan:", font=("Helvetica", 12), bg="#f7f7f7")
label_pertanyaan.grid(column=0, row=1, columnspan=3, sticky=tk.W)

# Kotak pertanyaan
kotak_pertanyaan = tk.Text(mainframe, height=4, width=50, font=("Helvetica", 11), state=tk.DISABLED, wrap=tk.WORD)
kotak_pertanyaan.grid(column=0, row=2, columnspan=3, pady=(0, 10))

# Tombol "Tidak"
no_btn = tk.Button(mainframe, text="Tidak", width=12, bg="#e74c3c", fg="white", font=("Helvetica", 10), state=tk.DISABLED, command=lambda: jawaban(False))
no_btn.grid(column=1, row=3, padx=5, pady=5)

# Tombol "Ya"
yes_btn = tk.Button(mainframe, text="Ya", width=12, bg="#2ecc71", fg="white", font=("Helvetica", 10), state=tk.DISABLED, command=lambda: jawaban(True))
yes_btn.grid(column=2, row=3, padx=5, pady=5)

# Tombol "Mulai Diagnosa"
start_btn = tk.Button(mainframe, text="Mulai Diagnosa", width=30, bg="#3498db", fg="white", font=("Helvetica", 11, "bold"), command=mulai_diagnosa)
start_btn.grid(column=0, row=4, columnspan=3, pady=15)

# Jalankan GUI
root.mainloop()
