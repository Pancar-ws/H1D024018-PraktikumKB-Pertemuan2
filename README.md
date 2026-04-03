# H1D024018-PraktikumKB-Pertemuan2

## Penjelasan Program fuzzyLogic3.py

Program ini adalah implementasi **Logika Fuzzy** untuk mengontrol kecepatan kipas berdasarkan suhu dan kelembapan ruangan. Konsepnya sederhana: semakin panas dan lembap ruangan, semakin cepat kipas harus berputar.

### Cara Kerja:

1. **Input (Antecedent):**
   - **Suhu**: Dibagi menjadi 3 kategori → dingin (0-20°C), normal (15-35°C), panas (30-40°C)
   - **Kelembapan**: Dibagi menjadi 3 kategori → kering (0-45%), normal (35-75%), lembap (65-100%)

2. **Output (Consequent):**
   - **Kecepatan Kipas**: Dibagi menjadi 3 kategori → lambat (0-40%), sedang (30-70%), cepat (60-100%)

3. **Aturan Fuzzy (Rules):**
   - Dingin + Kering/Lembap → Kipas Lambat
   - Normal + Normal → Kipas Sedang
   - Panas + Kering → Kipas Sedang
   - Panas + Lembap → Kipas Cepat

4. **Contoh Kasus:**
   - Input: Suhu 32°C, Kelembapan 80%
   - Output: Program menghitung kecepatan kipas otomatis menggunakan inferensi fuzzy
   - Hasil ditampilkan dalam bentuk angka dan grafik visualisasi

### Library yang Digunakan:
- `numpy`: Untuk operasi array dan perhitungan numerik
- `scikit-fuzzy`: Library khusus untuk implementasi logika fuzzy
- `matplotlib`: Untuk visualisasi grafik membership function

Program ini cocok untuk memahami dasar-dasar fuzzy logic dalam sistem kontrol otomatis.
