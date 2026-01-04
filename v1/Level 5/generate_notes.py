"""
Docstring for generate_notes
generate notes for sample use

"""


import os

ABS_PATH = os.path.abspath(__file__)
NOTES_DIR = os.path.join(os.path.dirname(ABS_PATH),"Notes")

notes = [
    (
        "Hari ini saya belajar lebih dalam tentang cara membaca dan menulis file teks dengan Python.\n"
        "Ternyata konsepnya sederhana: buka file dengan open(), baca atau tulis isi, lalu tutup kembali.\n"
        "Dengan memahami dasar file I/O ini, saya bisa mulai membuat program yang menyimpan catatan dan hasil latihan ke dalam file."
    ),
    (
        "Target minggu ini adalah menyelesaikan seluruh latihan Level 1 dan mulai menyentuh materi Level 2 tentang algoritma dasar.\n"
        "Supaya tidak terlalu berat, saya membagi waktu belajar menjadi sesi pendek 1–2 jam per hari.\n"
        "Fokus utama saya adalah konsisten latihan, bukan langsung memahami semua hal sekaligus."
    ),
    (
        "Project to do list di terminal sudah hampir selesai dan mulai terasa manfaatnya.\n"
        "Saya bisa menambah, melihat, dan menghapus tugas langsung dari command line tanpa perlu aplikasi lain.\n"
        "Langkah berikutnya adalah merapikan kode dengan memecahnya menjadi beberapa fungsi agar lebih mudah dibaca dan dirawat."
    ),
    (
        "Integrasi dengan API AI awalnya terasa menakutkan, tetapi ketika dipecah menjadi langkah-langkah kecil, ternyata jauh lebih masuk akal.\n"
        "Pertama saya perlu paham cara membuat HTTP request dengan library requests di Python.\n"
        "Setelah itu baru belajar bagaimana mengirim teks ke layanan AI dan memproses respons ringkasan yang dikembalikan."
    ),
    (
        "Besok saya berencana fokus latihan file I/O dan menyelesaikan script ringkas_file.py.\n"
        "Script ini akan membaca isi input.txt, mengecek apakah file kosong, lalu mengirim teks ke API untuk diringkas secara otomatis.\n"
        "Hasil ringkasan kemudian akan disimpan ke summary.txt sehingga saya bisa membaca versi singkat catatan kapan saja."
    ),
    (
        "Hari ini saya mencoba menulis fungsi kecil untuk membaca file dan mengembalikan isinya sebagai string.\n"
        "Awalnya sempat lupa menutup file, tapi setelah belajar tentang keyword with, kode jadi lebih rapi dan aman.\n"
        "Sekarang saya merasa lebih paham kenapa context manager itu penting di Python."
    ),
    (
        "Saat mengerjakan latihan, saya sadar bahwa memberi nama variabel yang jelas sangat membantu ketika membaca ulang kode.\n"
        "Nama seperti content, file_path, dan notes_dir jauh lebih mudah dipahami dibanding a, b, c.\n"
        "Ke depan, saya ingin membiasakan diri menulis kode yang tidak hanya jalan, tapi juga enak dibaca."
    ),
    (
        "Hari ini saya latihan membuat pengecekan error sederhana menggunakan raise.\n"
        "Saya membuat kondisi yang akan melempar ValueError ketika konten file kosong.\n"
        "Dengan begitu, program berhenti dengan pesan yang jelas daripada diam-diam menghasilkan output aneh."
    ),
    (
        "Saya mulai membangun kebiasaan menulis docstring untuk setiap fungsi yang saya buat.\n"
        "Dengan docstring, saya bisa melihat penjelasan fungsi hanya dengan hover di editor.\n"
        "Ini membuat project terasa lebih profesional walaupun masih skala latihan."
    ),
    (
        "Latihan berikutnya adalah membuat script yang bisa merangkum banyak file catatan sekaligus.\n"
        "Saya akan membuat folder notes yang berisi beberapa file teks berbeda.\n"
        "Lalu, script akan membaca semuanya, mengirim ke API, dan menyimpan hasil ringkasan ke folder lain."
    ),
    (
        "Saat mencoba os.listdir, saya baru paham bahwa fungsi ini mengembalikan nama semua entri di dalam folder.\n"
        "Karena itu, saya perlu memfilter sendiri hanya yang berakhiran .txt.\n"
        "Latihan kecil ini membantu saya lebih nyaman bekerja dengan sistem file."
    ),
    (
        "Hari ini saya eksperimen membuat nama file dinamis menggunakan f-string.\n"
        "Saya membuat pola seperti catatan-1.txt, catatan-2.txt, dan seterusnya.\n"
        "Ternyata cara ini jauh lebih simpel dibanding menggabungkan string dengan plus berkali-kali."
    ),
    (
        "Saya menyadari pentingnya memecah masalah besar menjadi langkah-langkah kecil.\n"
        "Daripada langsung memikirkan integrasi AI, saya fokus dulu pada baca file, cek error, dan simpan hasil.\n"
        "Setelah semua bagian kecil itu jalan, barulah bagian AI terasa lebih mudah disentuh."
    ),
    (
        "Saat debugging, saya mulai terbiasa menambahkan print sederhana untuk melihat nilai variabel penting.\n"
        "Misalnya, saya cek file_path, isi konten, dan status apakah file kosong atau tidak.\n"
        "Dengan cara ini, mencari sumber bug jadi lebih terarah dan tidak sekadar menebak-nebak."
    ),
    (
        "Hari ini saya menuliskan rencana belajar minggu depan di dalam beberapa file catatan.\n"
        "Tiap file berisi fokus latihan, seperti file I/O, error handling, atau penggunaan API.\n"
        "Rencananya, semua catatan ini akan saya rangkum otomatis menggunakan script yang sedang saya kembangkan."
    )
]

for index , konten in enumerate(notes):
    nomor = index+1
    file_name = "catatan-"+str(nomor)+".txt"

    file_path = os.path.join(NOTES_DIR,file_name)
    
    f = open(file_path ,"w",encoding="UTF-8")
    f.write(konten)
    f.close()

