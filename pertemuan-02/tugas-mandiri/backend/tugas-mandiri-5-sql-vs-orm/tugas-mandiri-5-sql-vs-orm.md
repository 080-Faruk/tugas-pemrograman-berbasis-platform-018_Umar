
# Laporan Tugas Mandiri 5: Membandingkan SQL Mentah dan ORM

**Nama:** Moh Faruq  
**NIM / Kelas:** 018 / Pemrograman Berbasis Platform  
**Pertemuan:** 02  

---

## Perbandingan Contoh Kode (Operasi Ambil Data Berdasarkan ID)

Berikut adalah perbandingan penulisan kode untuk mengambil data dari tabel `jadwal` berdasarkan kolom `id`:

### A. SQL Mentah (Raw SQL dengan Node.js / `mysql2`)
```javascript
// Menggunakan query SQL langsung secara manual
const [rows] = await db.execute('SELECT * FROM jadwal WHERE id = ?;', [id]);
const jadwal = rows[0];