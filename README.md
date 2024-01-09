# Food_Recomendation

# **Sistem Rekomendasi Makanan menggunakan Algoritma TF-IDF dan Cosine Similarity**

## Muhammad Rizky Naufal (A11.2022.14859) - Sistem Temu Kembali Informasi

---

## ~ Dataset

Dataset diambil dari kaggle → [![Kaggle Badge](https://img.shields.io/badge/Kaggle-blue?style=flat&logo=kaggle&logoColor=white)](https://www.kaggle.com/code/gracehephzibahm/food-recommendation-system-easy-comprehensive)

Pada dataset terdapat 4 Kolom:

- Name
- C_Type
- Veg_Non
- Describe

Dari 4 kolom diatas yang akan digunakan untuk membuat sistem Rekomendasi ini.

## ~ Tujuan

Sistem rekomendasi berdasarkan deskripsi makanan dapat menjadi solusi yang berguna bagi pengguna yang ingin menemukan menu makanan yang sesuai dengan selera mereka. Dengan menggunakan dataset yang telah disebutkan, penulis dapat mengembangkangkan sebuah sistem rekomendasi dengan pendekatan content-based.

## ~ Metode dan Tahapan

- Data Collection : Pada tahapan ini dilakukan pencarian dataset yang cocok untuk menyelesaikan penelitian rekomendasi makanan ini. Ditemukan dataset public dari kaggle yang merupakan menu makanan dari berbagai negara.
- Preprocessing :
  - Memproses file ratings.csv yang berisikan rating menu makanan yang sudah dinilai oleh foodie dari berbagai negara, serta menunjukkan rating makanan yang lebih disukai, lalu disimpan pada function "rating_matrix".
  - Sorting secara descending berdasarkan kolom "rating_matrix".
  - Drop baris yang memiliki jumlah review 0.
- Method :
  - SKLearn digunakan untuk melakukan vektorisasi TF-IDF.
  - SKLearn digunakan untuk menghitung similaritas (cosine similarity) berdasarkan matrix TF-IDF dari vektorisasi.
  - Outputnya adalah 5 nama makanan yang memiliki deskripsi yang serupa dari input menu makanan yang dimasukkan pengguna.

## ~ Performa Uji

Performa Uji dilakukan menggunakan K-Fold Cross-Validation yang sebelumnya penulis perlu membuat beberapa sampel rekomendasi pada menu makanan tertentu untuk mendapatkan hasil dari pengujian ini.
Setelah dilakukan pengujian hasil Average Hit Ratio yang didapat: 0.224.

## ~ Deployment

Sistem Rekomendasi Makanan dapat dicoba di → [![Streamlit Badge](https://img.shields.io/badge/Streamlit-red?style=flat&logo=streamlit&logoColor=white)](https://naufalrz-food-rec.streamlit.app/)

Jika Kebingunan untuk pengetesan awal, Anda dapat menginput menu makanan berikut:

- chicken minced salad
- sweet chilli almonds
- christmas cake
- japanese curry arancini with barley salsa
- almond and cranberry poha

Jika ingin menguji daftar menu makanan yang tidak memiliki rekomendasi, Anda dapat memasukkan judul apapun.

Anda perlu menekan tombol "Submit" untuk mengirim menu makanan yang ingin direkomendasi
