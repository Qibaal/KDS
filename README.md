<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8" />
</head>
<body>

  <!-- Judul Proyek -->
  <h1>Analisis Adaptasi Anti-Icing pada Bulu Beruang Kutub<br /><small>Animal Form and Function</small></h1>

  <!-- Preview Gambar Frontend -->
  <div style="display: flex; gap: 1rem; margin-bottom: 1rem;">
    <figure style="flex: 1;">
      <img src="frontend/first.jpg" alt="Preview Frontend 1" style="width: 100%; height: auto; border: 1px solid #ccc; border-radius: 4px;" />
      <figcaption style="text-align: center; font-size: 0.9rem; color: #555;">Preview 1: Halaman utama antarmuka 3D Viewer</figcaption>
    </figure>
    <figure style="flex: 1;">
      <img src="frontend/second.jpg" alt="Preview Frontend 2" style="width: 100%; height: auto; border: 1px solid #ccc; border-radius: 4px;" />
      <figcaption style="text-align: center; font-size: 0.9rem; color: #555;">Preview 2: Panel kontrol suhu dan grafik eksperimen</figcaption>
    </figure>
  </div>

  <!-- Cara Menjalankan Proyek Singkat -->
  <p style="background: #f0f8ff; padding: 0.75rem 1rem; border-left: 4px solid #2563eb; margin-bottom: 1rem;">
    <strong>Cara Menjalankan Proyek:</strong>  
    Pastikan <code>Python 3.8+</code> sudah terpasang, lalu pada direktori root jalankan:  
    <code>python start.py</code>.  
    Setelah itu, akses API di <code>http://127.0.0.1:5000</code> dan antarmuka di <code>http://127.0.0.1:8866</code>.
  </p>

  <hr />

  <h2>Table of Contents</h2>
  <ol>
    <li><a href="#deskripsi-proyek">Deskripsi Proyek</a></li>
    <li><a href="#latar-belakang--perumusan-masalah">Latar Belakang &amp; Perumusan Masalah</a></li>
    <li><a href="#tujuan-penelitian">Tujuan Penelitian</a></li>
    <li><a href="#metode--algoritma">Metode &amp; Algoritma</a>
      <ol type="a">
        <li><a href="#prediksi-struktur-3d-alphafold2">Prediksi Struktur 3D (AlphaFold2)</a></li>
        <li><a href="#persiapan-sistem-charmm-gui">Persiapan Sistem (CHARMM-GUI)</a></li>
        <li><a href="#simulasi-dinamika-molekuler-gromacs">Simulasi Dinamika Molekuler (GROMACS)</a></li>
        <li><a href="#alasan-pemilihan-metode">Alasan Pemilihan Metode</a></li>
      </ol>
    </li>
    <li><a href="#dataset">Dataset</a></li>
    <li><a href="#desain-antarmuka">Desain Antarmuka</a></li>
    <li><a href="#evaluasi--pengujian">Evaluasi &amp; Pengujian</a></li>
    <li><a href="#struktur-direktori">Struktur Direktori</a></li>
    <li><a href="#instalasi--persiapan-lingkungan">Instalasi &amp; Persiapan Lingkungan</a></li>
    <li><a href="#cara-menjalankan-proyek">Cara Menjalankan Proyek</a></li>
    <li><a href="#panduan-pemrograman">Panduan Pemrograman</a></li>
    <li><a href="#kontribusi">Kontribusi</a></li>
    <li><a href="#lisensi">Lisensi</a></li>
    <li><a href="#referensi--acknowledgments">Referensi &amp; Acknowledgments</a></li>
  </ol>

  <hr />

  <h2 id="deskripsi-proyek">Deskripsi Proyek</h2>
  <p>
    <strong>“Analisis Adaptasi Anti-Icing pada Bulu Beruang Kutub Menggunakan Teknik Simulasi Molekuler”</strong> adalah sebuah studi komputasional yang bertujuan mengeksplorasi mekanisme molekuler di balik kemampuan bulu beruang kutub (<em>Ursus maritimus</em>) untuk mencegah pembentukan es pada suhu ekstrem. Dengan memanfaatkan pipeline prediksi struktur protein (AlphaFold2), persiapan sistem lipid-protein (CHARMM-GUI), dan simulasi dinamika molekuler (GROMACS), kita akan:
  </p>
  <ul>
    <li>Memodelkan interaksi protein dan lipid bulu dengan molekul air/ice.</li>
    <li>Menganalisis stabilitas dan performa anti-icing berdasarkan metrik RMSD, &Delta;G, dan indikator hidrofobik.</li>
    <li>Memberikan dasar biologis untuk aplikasi biomimetik dan konservasi.</li>
  </ul>
  <p>
    Platform ini dilengkapi dengan antarmuka web interaktif yang memungkinkan pengguna:
  </p>
  <ol>
    <li>Mengunggah sekuens (<code>.fasta</code>, <code>.pep.gz</code>) untuk prediksi struktur.</li>
    <li>Menyesuaikan rentang suhu simulasi (−100 °C hingga 0 °C) melalui slider.</li>
    <li>Melihat visualisasi 3D hasil prediksi dan simulasi.</li>
    <li>Memperoleh grafik insight—seperti komposisi lipid, kuantifikasi NMR, dan heatmap—langsung dari browser.</li>
  </ol>

  <hr />

  <h2 id="latar-belakang--perumusan-masalah">Latar Belakang &amp; Perumusan Masalah</h2>
  <p>
    <strong>Konteks Ekologis &amp; Fisiologis</strong><br />
    Beruang kutub hidup di wilayah Arktik ekstrem dengan suhu turun di bawah −30 °C. Struktur bulu yang mampu mencegah pembentukan lapisan es (anti-icing) merupakan faktor kunci dalam menjaga isolasi termal dan mobilitas mereka.
  </p>
  <p>
    <strong>Komposisi Molekuler Bulunya</strong><br />
    Studi eksperimental (NMR, mikroskop elektron) menunjukkan adanya kandungan lipid spesifik (wax ester, sterol ester) dan protein struktural (keratin, aquaporin, antifreeze proteins/AFPs) yang berpotensi menghambat nucleation kristal es.
  </p>
  <p>
    <strong>Gap Penelitian</strong><br />
    Sebagian besar penelitian sebelumnya berfokus pada pendekatan eksperimental, yang memerlukan kondisi laboratorium khusus dan biaya tinggi. Belum banyak penelitian in silico yang memodelkan interaksi atomik antara komponen bulu dan air/ice pada rentang suhu Arktik.
  </p>
  <p>
    <strong>Pertanyaan Inti</strong>
  </p>
  <ul>
    <li>Bagaimana struktur 3D protein (misalnya aquaporin, AFP) dan lipid (wax ester, sterol ester) beruang kutub berkontribusi terhadap mekanisme anti-icing?</li>
    <li>Bagaimana simulasi dinamika molekuler pada suhu ekstrem dapat mengungkap stabilitas dan interaksi hidrofobik/energi bebas yang mendasari anti-icing?</li>
    <li>Dapatkah kita mengidentifikasi kandidat molekuler dominan yang menjadi target penelitian eksperimental atau aplikasi biomimetik?</li>
  </ul>

  <hr />

  <h2 id="tujuan-penelitian">Tujuan Penelitian</h2>
  <ol>
    <li>
      <strong>Identifikasi &amp; Isolasi Sekuens</strong><br />
      Mengompilasi sekuens gen dan protein terkait adaptasi dingin (misalnya AFPs, aquaporin) dari database GenBank (CDS &amp; pep data).
    </li>
    <li>
      <strong>Prediksi Struktur 3D</strong><br />
      Menggunakan AlphaFold2 untuk menghasilkan model atomik protein bulu beruang kutub yang menjadi kandidat anti-icing. Merakit model sistem lipid-protein berdasarkan data eksperimen (file <code>.mol</code>, PDB, GRO).
    </li>
    <li>
      <strong>Simulasi Dinamika Molekuler</strong><br />
      Menjalankan simulasi pada rentang suhu <strong>−100 °C hingga 0 °C</strong> menggunakan GROMACS (dengan input dari CHARMM-GUI). Menganalisis RMSD, energi bebas Gibbs (ΔG), dan fluiditas membran sebagai metrik anti-icing.
    </li>
    <li>
      <strong>Justifikasi Biologis &amp; Aplikasi</strong><br />
      Menginterpretasikan hasil simulasi secara biologis dan membandingkan dengan literatur (NMR, cryo-EM). Merumuskan rekomendasi untuk konservasi atau desain biomimetik.
    </li>
  </ol>

  <hr />

  <h2 id="metode--algoritma">Metode &amp; Algoritma</h2>

  <h3 id="prediksi-struktur-3d-alphafold2">1. Prediksi Struktur 3D (AlphaFold2)</h3>
  <p><strong>Tujuan:</strong><br />
    Mendapatkan struktur atomik protein kritis (AFP, aquaporin, dsb.) untuk memahami motif anti-icing.
  </p>
  <p><strong>Alur Kerja:</strong></p>
  <ol>
    <li><strong>Input:</strong> Sekuens protein (FASTA) – misalnya <code>AF-B1P0S1</code> (antifreeze protein).</li>
    <li><strong>Proses Prediksi:</strong> Jalankan AlphaFold2 (menggunakan model terlatih) &rarr; keluaran berupa file <code>.pdb</code> terprediksi (misalnya <code>AF-B1P0S1-F1-model_v4.pdb</code>).</li>
    <li><strong>Validasi Awal:</strong> Periksa Confidence Score (pLDDT) dan Ramachandran Plot untuk memverifikasi kualitas model.</li>
  </ol>
  <p><strong>Output:</strong> Struktur 3D protein (<code>.pdb</code>) siap untuk dirakit ke dalam sistem simulasi.</p>
  <div style="text-align: center; margin: 1rem 0;">
    <img src="https://i.imgur.com/jWzLmAe.png" alt="Diagram Alur AlphaFold2" style="max-width: 100%; height: auto;" />
    <p><em>Gambar 2.1: Diagram Alur Kerja AlphaFold2</em></p>
  </div>

  <h3 id="persiapan-sistem-charmm-gui">2. Persiapan Sistem (CHARMM-GUI)</h3>
  <p><strong>Tujuan:</strong><br />
    Membangun sistem lipid-protein yang realistis untuk simulasi pada suhu rendah (misalnya −20 °C hingga 0 °C).
  </p>
  <p><strong>Alur Kerja:</strong></p>
  <ol>
    <li><strong>Input Struktur:</strong>
      <ul>
        <li>File PDB protein (hasil AlphaFold2).</li>
        <li>File MOL2 lipid (misalnya <code>Cetyl Palmitate.mol</code>, <code>Cholesteryl Oleate.mol</code>).</li>
      </ul>
    </li>
    <li><strong>Pemilihan Komponen:</strong>
      <ul>
        <li>Pilih jenis lipid (wax ester, sterol ester, dsb.).</li>
        <li>Tambahkan molekul air atau es (mode “ice/water”).</li>
      </ul>
    </li>
    <li><strong>Parameter Simulasi:</strong>
      <ul>
        <li>Tempatkan pada suhu: −20 °C (253 K) hingga 0 °C (273 K).</li>
        <li>Tekanan &amp; Volume: Sesuai kondisi Arktik standar (1 atm, selisih volume untuk es).</li>
      </ul>
    </li>
    <li><strong>Optimasi Sistem:</strong>
      <ul>
        <li>Energy minimization &rarr; equilibration (NVT, NPT) &rarr; file output topologi &amp; koordinat (<code>.gro</code>, <code>.top</code>, <code>.itp</code>).</li>
      </ul>
    </li>
  </ol>
  <p><strong>Output:</strong> Kumpulan file topologi dan koordinat siap digunakan pada GROMACS.</p>
  <div style="text-align: center; margin: 1rem 0;">
    <img src="https://i.imgur.com/1BzNY6x.png" alt="Diagram Alur CHARMM-GUI" style="max-width: 100%; height: auto;" />
    <p><em>Gambar 2.2: Diagram Alur Kerja CHARMM-GUI</em></p>
  </div>

  <h3 id="simulasi-dinamika-molekuler-gromacs">3. Simulasi Dinamika Molekuler (GROMACS)</h3>
  <p><strong>Tujuan:</strong><br />
    Menilai interaksi atomik protein/lipid dengan molekul air/ice pada rentang suhu ekstrem (−100 °C hingga 0 °C).
  </p>
  <p><strong>Alur Kerja:</strong></p>
  <ol>
    <li><strong>Input:</strong>
      <ul>
        <li>File topologi &amp; koordinat (hasil CHARMM-GUI).</li>
        <li>Parameter force field (lipid, protein, water/ice).</li>
      </ul>
    </li>
    <li><strong>Tahapan Simulasi:</strong>
      <ol type="a">
        <li><strong>Energy Minimization:</strong> Menghilangkan tumpang tindih awal.</li>
        <li><strong>Equilibration (NVT &rarr; NPT):</strong>
          <ul>
            <li>NVT pada suhu target (misalnya 173 K untuk −100 °C, hingga 273 K untuk 0 °C).</li>
            <li>NPT pada tekanan 1 atm untuk menyesuaikan densitas.</li>
          </ul>
        </li>
        <li><strong>Production Run:</strong> Simulasi selama 50–100 ns (atau lebih) per kondisi suhu.</li>
      </ol>
    </li>
    <li><strong>Metrik Analisis:</strong>
      <ul>
        <li><strong>RMSD</strong> (Root Mean Square Deviation): Menunjukkan stabilitas konformasi.</li>
        <li><strong>&Delta;G</strong> (Gibbs Free Energy): Mengukur kekuatan interaksi antar molekul (protein-ice, lipid-ice).</li>
        <li><strong>Ice Nucleation Delay</strong>: Waktu penundaan terbentuknya nucleus es dekat permukaan molekul.</li>
        <li><strong>Hydrophobic Interaction Area</strong>: Luas area hidrofobik yang mempengaruhi pembentukan es.</li>
      </ul>
    </li>
    <li><strong>Analisis Output:</strong>
      <ul>
        <li>Plot RMSD vs. waktu, kurva &Delta;G, visualisasi trajektori (VMD/PyMOL).</li>
        <li>Perbandingan lintas suhu untuk mengekstrak kondisi optimal.</li>
      </ul>
    </li>
  </ol>
  <p><strong>Output:</strong> Berkas trajektori (<code>.xtc</code>), energi (<code>.edr</code>), log (<code>.log</code>), dan analisis metrik siap diekspor ke frontend.</p>
  <div style="text-align: center; margin: 1rem 0;">
    <img src="https://i.imgur.com/tpRJ6vV.png" alt="Diagram Alur GROMACS" style="max-width: 100%; height: auto;" />
    <p><em>Gambar 2.3: Diagram Alur Kerja GROMACS</em></p>
  </div>

  <h3 id="alasan-pemilihan-metode">4. Alasan Pemilihan Metode</h3>
  <ul>
    <li>
      <strong>AlphaFold2</strong>
      <ul>
        <li><em>Kelebihan:</em> Prediksi struktur protein paling akurat (pLDDT tinggi), sangat relevan untuk memahami motif anti-icing tanpa harus menunggu data eksperimental (cryo-EM/NMR).</li>
        <li><em>Kontribusi:</em> Membuka peluang analisis bagaimana situs aktif AFP/keratin memblokir nucleation es.</li>
      </ul>
    </li>
    <li>
      <strong>CHARMM-GUI</strong>
      <ul>
        <li><em>Kelebihan:</em> Antarmuka grafis yang intuitif untuk menyiapkan sistem lipid-protein, mudah diintegrasikan ke GROMACS.</li>
        <li><em>Kontribusi:</em> Mempercepat proses parameterisasi lipid dan setup initial box (air vs. es).</li>
      </ul>
    </li>
    <li>
      <strong>GROMACS</strong>
      <ul>
        <li><em>Kelebihan:</em> Perangkat lunak simulasi dinamika molekuler terdepan—ringan, sangat teroptimasi, komunitas luas.</li>
        <li><em>Kontribusi:</em> Memungkinkan simulasi panjang (~100 ns) pada berbagai suhu dengan metrik analitis terstandar (RMSD, &Delta;G).</li>
      </ul>
    </li>
  </ul>
  <p>
    Gabungan ketiganya menciptakan pipeline end-to-end:<br />
    <strong>Sekuens &rarr; Struktur (AlphaFold2) &rarr; Setup Sistem (CHARMM-GUI) &rarr; Simulasi (GROMACS) &rarr; Analisis.</strong>
  </p>

  <hr />

  <h2 id="dataset">Dataset</h2>
  <table border="1" cellpadding="6" cellspacing="0">
    <thead>
      <tr>
        <th><strong>File Data</strong></th>
        <th><strong>Format</strong></th>
        <th><strong>Ukuran</strong></th>
        <th><strong>Deskripsi &amp; Karakteristik</strong></th>
      </tr>
    </thead>
    <tbody>
      <tr>
        <td><code>polar_bear.gene.cds</code></td>
        <td>FASTA (.cds)</td>
        <td>31.1 MB</td>
        <td>Sekuens CDS protein antifreeze (<code>AF-B1P0S1</code>) sebagai input AlphaFold2.</td>
      </tr>
      <tr>
        <td><code>AF-B1P0S1-F1-model_v4.pdb</code></td>
        <td>PDB</td>
        <td>113 KB</td>
        <td>Struktur 3D terprediksi dari AlphaFold2 (antifreeze protein).</td>
      </tr>
      <tr>
        <td><code>Cetyl Palmitate.mol</code></td>
        <td>MOL</td>
        <td>4 KB</td>
        <td>Struktur kimia wax ester (komponen lipid anti-icing).</td>
      </tr>
      <tr>
        <td><code>Cholesteryl Oleate.mol</code></td>
        <td>MOL</td>
        <td>5 KB</td>
        <td>Struktur kimia sterol ester (komponen lipid anti-icing).</td>
      </tr>
      <tr>
        <td><code>NMR_quant.xlsx</code></td>
        <td>Excel</td>
        <td>10 KB</td>
        <td>Konsentrasi lipid absolut (μmol/g rambut) hasil kuantisasi NMR.</td>
      </tr>
      <tr>
        <td><code>Sample02.xlsx – Sample07.xlsx</code></td>
        <td>Excel</td>
        <td>9 KB per file</td>
        <td>Data integrasi mentah sinyal NMR per sampel rambut (Sample02 – Sample07).</td>
      </tr>
      <tr>
        <td><code>GC_mass.xlsx</code></td>
        <td>Excel</td>
        <td>30 KB</td>
        <td>Hasil kuantifikasi GC-MS untuk asam lemak &amp; ester (Total Count per kelas).</td>
      </tr>
      <tr>
        <td><code>WE_FA_Abundance.csv</code></td>
        <td>CSV</td>
        <td>2 KB</td>
        <td>Kuantifikasi lipid GC-MS per kelas (WE, DG, TG, dll.).</td>
      </tr>
      <tr>
        <td><code>Sample7_pos_IE2__MS2_identified.csv</code></td>
        <td>CSV</td>
        <td>41 KB</td>
        <td>Hasil identifikasi puncak MS2 (LC-MS/MS) dengan kolom utama <code>Lipid_headgroup</code>.</td>
      </tr>
      <tr>
        <td><code>DG_MS1_Area.csv</code>, <code>TG_MS1_Area.csv</code>, …</td>
        <td>CSV</td>
        <td>1 – 5 KB</td>
        <td>Intensitas puncak MS1 untuk lipid kelas DG, TG, PC, dsb.</td>
      </tr>
    </tbody>
  </table>
  <p><em>Catatan:</em> Semua data ditempatkan di folder <code>data/</code> pada root repository.</p>

  <hr />

  <h2 id="desain-antarmuka">Desain Antarmuka</h2>
  <p>
    Antarmuka berbasis web dirancang untuk memudahkan pengguna (peneliti/mahasiswa) dalam melakukan:
  </p>
  <ul>
    <li>
      <strong>Unggah Data:</strong> Pilih file sekuens (<code>.fasta</code>, <code>.pep.gz</code>) atau struktur (<code>.pdb</code>, <code>.mol</code>), disajikan dengan validasi format.
    </li>
    <li>
      <strong>Pengaturan Simulasi:</strong>
      <ul>
        <li>Slider interaktif untuk memilih suhu target (rentang −100 °C hingga 0 °C).</li>
        <li>Tombol <em>“Run Visualization”</em> untuk memulai pipeline prediksi &amp; simulasi.</li>
      </ul>
    </li>
    <li>
      <strong>Tampilan Visualisasi 3D:</strong>
      <ul>
        <li>Layar 3D menggunakan <strong>py3Dmol</strong> untuk menampilkan struktur protein/lipid dengan gaya “cartoon” berwarna spektrum, latar belakang biru pucat.</li>
        <li>Border animasi pada viewer menandakan state “Simulation Complete”.</li>
      </ul>
    </li>
    <li>
      <strong>Panel Informasi Molekul:</strong>
      <ul>
        <li>Deskripsi fungsi protein (misalnya Aquaporin-3) dengan judul, uraian biologis, dan caption ringkas.</li>
        <li>Tampilan siklus shimmering pada banner suhu (gradient dinamis) untuk menampilkan kondisi Arktik (Severe, Extreme, Moderate, Mild) sesuai nilai slider.</li>
      </ul>
    </li>
    <li>
      <strong>Insight Eksperimental (Charts):</strong>
      <ul>
        <li><strong>Lipid Class Abundance:</strong> Bar chart kelompok lipid (MG, DG, TG, WE, PC…).</li>
        <li><strong>Fatty Acid Abundance (Bar &amp; Pie):</strong> Chart distribusi rantai FA utama (≥10 %) vs. “Others”.</li>
        <li><strong>NMR Quantification:</strong>
          <ul>
            <li>Stacked Bar Chart (Glycerides, 1,2-Diglyceride, Wax esters, Sterol esters per sampel).</li>
            <li>Heatmap intensitas lipid per individu (colormap “Blues”).</li>
          </ul>
        </li>
        <li>Semua grafik di-embed sebagai <code>&lt;img&gt;</code> berbasis Base64 dari respons Flask <code>/api</code>.</li>
      </ul>
    </li>
    <li>
      <strong>Desain Responsif:</strong>
      <ul>
        <li>Layout fleksibel (flex-box) untuk chart: container akan menyusut dan membungkus otomatis saat lebar layar berkurang.</li>
        <li>Komponen antarmuka diberi efek “glassmorphism” (backdrop-filter, shadow, border-gradient) untuk estetika modern.</li>
      </ul>
    </li>
  </ul>

  <hr />

  <h2 id="evaluasi--pengujian">Evaluasi &amp; Pengujian</h2>

  <h3>Metrik Kuantitatif</h3>
  <table border="1" cellpadding="6" cellspacing="0">
    <thead>
      <tr>
        <th><strong>Metrik</strong></th>
        <th><strong>Definisi &amp; Tujuan</strong></th>
      </tr>
    </thead>
    <tbody>
      <tr>
        <td><strong>RMSD (Root Mean Square Deviation)</strong></td>
        <td>
          <ul>
            <li>Mengukur stabilitas struktur molekul selama simulasi dinamika molekuler.</li>
            <li><em>RMSD rendah</em> &rarr; struktur stabil, anti-icing efektif.</li>
          </ul>
        </td>
      </tr>
      <tr>
        <td><strong>&Delta;G (Gibbs Free Energy)</strong></td>
        <td>
          <ul>
            <li>Menilai kekuatan interaksi antar molekul (protein-ice, lipid-ice).</li>
            <li><em>&Delta;G negatif besar</em> &rarr; interaksi kuat mencegah nucleation.</li>
          </ul>
        </td>
      </tr>
      <tr>
        <td><strong>Ice Formation Rate</strong></td>
        <td>
          <ul>
            <li>Frekuensi agregasi molekul air menjadi es dekat permukaan.</li>
            <li><em>Waktu delay panjang</em> &rarr; proteksi anti-icing lebih kuat.</li>
          </ul>
        </td>
      </tr>
      <tr>
        <td><strong>Hydrophobic Interaction Area</strong></td>
        <td>
          <ul>
            <li>Luas permukaan hidrofobik (lipid/protein) yang menghambat pembentukan es.</li>
          </ul>
        </td>
      </tr>
      <tr>
        <td><strong>Hydration Shell Stability</strong></td>
        <td>
          <ul>
            <li>Distribusi molekul air di sekeliling molekul, untuk melihat potensi fungsi anti-freeze.</li>
            <li><em>Kelompok air terorganisir</em> &rarr; anti-icing optimal.</li>
          </ul>
        </td>
      </tr>
    </tbody>
  </table>

  <h3>Rencana Uji (Test Plan)</h3>
  <table border="1" cellpadding="6" cellspacing="0">
    <thead>
      <tr>
        <th><strong>No.</strong></th>
        <th><strong>Langkah Uji</strong></th>
        <th><strong>Deskripsi</strong></th>
      </tr>
    </thead>
    <tbody>
      <tr>
        <td>1</td>
        <td><strong>Input Data</strong></td>
        <td>Unggah file <code>.pep.gz</code> atau keluaran AlphaFold2 <code>.pdb</code>.</td>
      </tr>
      <tr>
        <td>2</td>
        <td><strong>Prediksi Struktur</strong></td>
        <td>Pastikan AlphaFold2 menghasilkan file PDB dengan pLDDT &gt; 80 (model valid).</td>
      </tr>
      <tr>
        <td>3</td>
        <td><strong>Persiapan Sistem</strong></td>
        <td>Gunakan CHARMM-GUI untuk merakit sistem lipid-protein, verifikasi keberhasilan generasi file <code>.gro</code>, <code>.top</code>, <code>.itp</code>.</td>
      </tr>
      <tr>
        <td>4</td>
        <td><strong>Simulasi Suhu Ekstrem</strong></td>
        <td>Jalankan simulasi GROMACS pada suhu: −100 °C (173 K), −50 °C (223 K), −30 °C (243 K), −10 °C (263 K), 0 °C (273 K). Pastikan run minimal 50 ns.</td>
      </tr>
      <tr>
        <td>5</td>
        <td><strong>Analisis Output</strong></td>
        <td>Hitung RMSD, &Delta;G, dan pantau pola nucleation es (visualisasi trajektori).</td>
      </tr>
      <tr>
        <td>6</td>
        <td><strong>Verifikasi Literatur</strong></td>
        <td>
          Bandingkan hasil simulasi dengan data eksperimental (NMR, cryo-EM) atau studi publikasi:
          <ul>
            <li>AQP3 expression di folikel rambut</li>
            <li>Komposisi lipid in vivo</li>
            <li>Struktur AFP crystal</li>
          </ul>
        </td>
      </tr>
      <tr>
        <td>7</td>
        <td><strong>Dokumentasi &amp; Interpretasi</strong></td>
        <td>Buat grafik (RMSD vs. waktu, tabel &Delta;G per suhu), heatmap intensitas es, serta ringkasan insight molekuler, lalu susun laporan berbasis data.</td>
      </tr>
    </tbody>
  </table>

  <hr />

  <h2 id="struktur-direktori">Struktur Direktori</h2>
  <pre>
root/
├── backend/                          
│   ├── controllers/
│   │   ├── lipid_chart.py           
│   │   ├── fa_bar_chart.py          
│   │   ├── fa_pie_chart.py          
│   │   ├── nmr_stacked_bar.py       
│   │   ├── nmr_heatmap.py           
│   │   └── …                        
│   ├── app.py                       
│   └── requirements.txt             
│
├── frontend/                         
│   ├── run.ipynb                    
│   ├── static/
│   │   ├── css/                     
│   │   └── js/                      
│   ├── templates/                   
│   └── requirements.txt             
│
├── data/                             
│   ├── polar_bear.gene.cds
│   ├── AF-B1P0S1-F1-model_v4.pdb
│   ├── Cetyl Palmitate.mol
│   ├── Cholesteryl Oleate.mol
│   ├── NMR_quant.xlsx
│   ├── Sample02.xlsx … Sample07.xlsx
│   ├── GC_mass.xlsx
│   ├── WE_FA_Abundance.csv
│   ├── Sample7_pos_IE2__MS2_identified.csv
│   └── DG_MS1_Area.csv, TG_MS1_Area.csv, …
│
├── protein_fold_model/               
│   ├── model_-100.cif
│   ├── model_-90.cif
│   ├── …                            
│   └── model_0.cif
│
├── start.py                          
├── README.md                         
└── LICENSE                           
  </pre>

  <hr />

  <h2 id="instalasi--persiapan-lingkungan">Instalasi &amp; Persiapan Lingkungan</h2>
  <p>Pastikan Anda memiliki:</p>
  <ul>
    <li><strong>Python 3.8+</strong> (direkomendasikan menggunakan <a href="https://github.com/pyenv/pyenv">pyenv</a> atau <a href="https://docs.conda.io/">conda</a>).</li>
    <li><strong>pip</strong> terbaru (<code>pip install --upgrade pip</code>).</li>
    <li><strong>C Compiler</strong> (misalnya <code>gcc</code>/<code>clang</code>) untuk instalasi paket yang memerlukan kompilasi (GROMACS diinstal secara terpisah).</li>
    <li><strong>GROMACS 2021+</strong> (pastikan <code>gmx</code> dapat diakses di PATH).</li>
    <li><strong>CHARMM-GUI Account</strong> (asal pengguna memiliki akses internet).</li>
    <li><strong>Koneksi Internet</strong> (untuk mengunduh pustaka Python).</li>
  </ul>

  <hr />

  <h2 id="cara-menjalankan-proyek">Cara Menjalankan Proyek</h2>
  <ol>
    <li>
      <strong>Clone Repository</strong><br />
      <code>git clone https://github.com/&lt;username&gt;/polarbear-antiicing-simulation.git</code><br />
      <code>cd polarbear-antiicing-simulation</code>
    </li>
    <li>
      <strong>Siapkan Virtual Environment</strong><br />
      <code>python -m venv venv</code><br />
      <code>source venv/bin/activate    # Linux/macOS</code><br />
      <code>venv\Scripts\activate      # Windows</code>
    </li>
    <li>
      <strong>Instalasi Dependencies Backend &amp; Frontend</strong>
      <ul>
        <li>
          <strong>Backend</strong><br />
          <code>cd backend</code><br />
          <code>pip install --upgrade pip</code><br />
          <code>pip install -r requirements.txt</code><br />
          <code>cd ..</code>
        </li>
        <li>
          <strong>Frontend</strong><br />
          <code>cd frontend</code><br />
          <code>pip install --upgrade pip</code><br />
          <code>pip install -r requirements.txt</code><br />
          <code>cd ..</code>
        </li>
      </ul>
    </li>
    <li>
      <strong>Jalankan Proyek (<code>python start.py</code>)</strong><br />
      Pada direktori root:<br />
      <code>python start.py</code><br />
      Skrip ini akan:
      <ul>
        <li>Melakukan instalasi ulang dependencies (jika belum terpasang).</li>
        <li>Menjalankan <code>app.py</code> (Flask backend) pada <code>http://127.0.0.1:5000</code>.</li>
        <li>Menjalankan <code>voila run.ipynb</code> (Voila frontend) pada <code>http://127.0.0.1:8866</code>.</li>
      </ul>
      Buka browser dan akses:
      <ul>
        <li><strong>API Backend:</strong> <code>http://127.0.0.1:5000/api/*</code> (misalnya <code>/api/lipid/lipid_chart</code>).</li>
        <li><strong>Frontend Dashboard:</strong> <code>http://127.0.0.1:8866</code></li>
      </ul>
    </li>
    <li>
      <strong>Menutup Proses</strong><br />
      Tekan <code>Ctrl + C</code> di terminal root untuk menghentikan <code>start.py</code>, yang kemudian akan menutup backend dan frontend secara otomatis.
    </li>
  </ol>

  <hr />

  <h2 id="panduan-pemrograman">Panduan Pemrograman</h2>
  <ol>
    <li>
      <strong>Menambahkan Fungsi API Baru</strong>
      <ul>
        <li>Buat file Python baru di <code>backend/controllers/</code> (misalnya <code>new_analysis.py</code>).</li>
        <li>Definisikan fungsi untuk membaca data, memproses, dan mengembalikan gambar PNG via <code>send_file</code>.</li>
        <li>Daftarkan endpoint di <code>backend/app.py</code>:</li>
      </ul>
      <pre><code>from controllers.new_analysis import generate_new_chart

@app.route('/api/new/analysis', methods=['GET'])
def new_analysis():
    return generate_new_chart()</code></pre>
    </li>
    <li>
      <strong>Memperbarui Frontend (Voila Notebook)</strong>
      <ul>
        <li>Lokasi: <code>frontend/run.ipynb</code>.</li>
        <li>Tambahkan konfigurasi di bagian <code>chart_configs</code> untuk endpoint baru:</li>
      </ul>
      <pre><code>{
    "title": "New Analysis Chart",
    "endpoint": "/api/new/analysis",
    "insight": "Penjelasan singkat insight chart."
}</code></pre>
      <ul>
        <li>Jalankan ulang <code>voila run.ipynb</code> untuk melihat hasil.</li>
      </ul>
    </li>
    <li>
      <strong>Memperluas Dataset</strong>
      <ul>
        <li>Tambahkan file data baru ke folder <code>data/</code>.</li>
        <li>Perbarui kode di <code>backend/controllers/*</code> untuk membaca file baru sesuai format (CSV/Excel).</li>
        <li>Pastikan format kolom sesuai dengan logika plotting (misal: <code>FA_Chain</code>, <code>Abundance</code>, dsb.).</li>
      </ul>
    </li>
    <li>
      <strong>Menambah Model CIF untuk Visualisasi Suhu Tambahan</strong>
      <ul>
        <li>Simpan file <code>.cif</code> ke folder <code>protein_fold_model/</code> dengan penamaan <code>model_<temperature>.cif</code>.</li>
        <li>Fungsi <code>get_model_path_from_temperature(temp)</code> di notebook otomatis memetakan suhu ke indeks file.</li>
        <li>Untuk menambah rentang suhu lain (contoh: setiap 5 °C), tambahkan file <code>.cif</code> dan sesuaikan logika pembulatan.</li>
      </ul>
    </li>
  </ol>

  <hr />

  <h2 id="kontribusi">Kontribusi</h2>
  <p><strong>Panduan Kontribusi</strong></p>
  <ol>
    <li>Fork repository ini.</li>
    <li>Buat branch baru sesuai perubahan (<code>git checkout -b feature/&lt;deskripsi&gt;</code>).</li>
    <li>Lakukan perubahan kode (API, Notebook, dsb.) beserta dokumentasi.</li>
    <li>Tambahkan unit test (jika relevan) di <code>backend/tests/</code> (belum tersedia, bisa dibuat).</li>
    <li>Commit perubahan Anda dengan pesan yang jelas:
      <pre><code>git commit -m "Menambahkan endpoint analisis new_analysis"</code></pre>
    </li>
    <li>Push ke fork dan buat Pull Request ke <code>main</code> branch repository asli.</li>
  </ol>
  <p><em>Catatan:</em> Pastikan semua perubahan lulus uji dasar (jika ada test suite), dan dokumentasi (<code>README.md</code>) sudah diperbarui.</p>

  <hr />

  <h2 id="lisensi">Lisensi</h2>
  <p>
    Proyek ini dirilis di bawah lisensi <strong>MIT License</strong>.<br />
    Lihat file <code>LICENSE</code> untuk detail lengkap.<br />
    Silakan gunakan, modifikasi, dan distribusikan sesuai ketentuan MIT.
  </p>

  <hr />

  <h2 id="referensi--acknowledgments">Referensi &amp; Acknowledgments</h2>
  <ol>
    <li>
      <strong>AlphaFold2</strong><br />
      Jumper, J. et al. “Highly accurate protein structure prediction with AlphaFold.” <em>Nature</em> (2021).
    </li>
    <li>
      <strong>CHARMM-GUI</strong><br />
      Jo, S., Kim, T., Iyer, V. G., &amp; Im, W. “CHARMM-GUI: A web-based graphical user interface for CHARMM.” <em>J. Comput. Chem.</em> (2008).
    </li>
    <li>
      <strong>GROMACS</strong><br />
      Van Der Spoel, D. et al. “GROMACS: fast, flexible, and free.” <em>J. Comput. Chem.</em> (2005).
    </li>
    <li>
      <strong>Antifreeze Proteins &amp; Aquaporin in Polar Bear</strong><br />
      Yang, D. et al. “Molecular architecture of polar bear antifreeze protein.” <em>Proc. Natl. Acad. Sci. USA</em> (2015).<br />
      Koopman, M. et al. “Aquaporin-3 expression in polar bear hair follicles.” <em>J. Mammal. Biol.</em> (2017).
    </li>
    <li>
      <strong>NMR &amp; Lipidomics</strong><br />
      Zhang, X. et al. “Characterization of skin lipidome: Role in anti-icing mechanisms.” <em>Anal. Chem.</em> (2019).
    </li>
    <li>
      <strong>Perangkat Lunak &amp; Library</strong><br />
      <ul>
        <li><a href="https://github.com/voila-dashboards/voila">Voila (Jupyter to Web App)</a></li>
        <li><a href="https://github.com/avirshup/py3dmol">py3Dmol (Jupyter 3D Molecular Viewer)</a></li>
      </ul>
    </li>
  </ol>
  <h2>Tim G03_K5</h2>
    <table border="1" cellspacing="0" cellpadding="6">
    <thead>
        <tr>
        <th>Name</th>
        <th>NIM</th>
        <th>Role</th>
        </tr>
    </thead>
    <tbody>
        <tr>
        <td>Raizan Iqbal Resi</td>
        <td>18222068</td>
        <td>Back-End Developer</td>
        </tr>
        <tr>
        <td>Favian Izza Diasputra</td>
        <td>18222070</td>
        <td>Front-End Developer</td>
        </tr>
        <tr>
        <td>Athhar Mahendra Umar</td>
        <td>18222080</td>
        <td>Technical Writer (Documentation)</td>
        </tr>
    </tbody>
    </table>
  <p>
    Kami mengucapkan terima kasih kepada:<br />
    - Tim mata kuliah IF3211 Komputasi Domain Spesifik yang memberi arahan dan materi yang bermanfaat bagi projek ini.<br />
    - Komunitas open-source di balik <strong>AlphaFold2</strong>, <strong>CHARMM-GUI</strong>, <strong>GROMACS</strong>, <strong>GIMP</strong>, dan <strong>Inkscape</strong> (untuk ilustrasi).<br />
    - Penulis berbagai library Python yang mendukung analisis data (NumPy, Pandas, Matplotlib).
  </p>

  <blockquote>
    <p><em>“Dengan memanfaatkan kekuatan simulasi atomik, kita dapat menyingkap rahasia alam yang tersembunyi di balik adaptasi ekstrem beruang kutub—dengan harapan mentransformasikannya menjadi inovasi biomimetika yang bermanfaat bagi umat manusia.”</em><br />
    — Tim G03_K5, ITB, 2025</p>
  </blockquote>

  <p style="font-size: 0.9rem; color: #555;">
    *Dokumentasi ini disusun untuk keperluan publikasi kode sumber di GitHub (<a href="https://github.com/Qibaal/KDS">https://github.com/Qibaal/KDS</a>).*
  </p>

</body>
</html>
