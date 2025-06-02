import matplotlib
matplotlib.use('Agg')

import pandas as pd
import matplotlib.pyplot as plt
import io
from flask import send_file, abort
import os

def generate_lipid_chart():
    """
    - Membaca file CSV: data/Sample7_pos_IE2__MS2_identified.csv
    - Menghitung frekuensi Lipid_headgroup
    - Membuat bar chart (vertical) dengan:
        • Sumbu X: Lipid_headgroup (MG, DG, TG, WE, PC, dsb.)
        • Sumbu Y: count / frekuensi
    - Mengembalikan gambar PNG via Flask's send_file
    """

    # 1. Tentukan path absolut ke file CSV
    base_dir = os.path.abspath(os.path.dirname(__file__))       # .../controllers
    project_root = os.path.dirname(base_dir)                     # .../my-flask-app
    csv_path = os.path.join(project_root, 'data', 'Sample7_pos_IE2__MS2_identified.csv')

    if not os.path.isfile(csv_path):
        # Jika file CSV tidak ditemukan, kembalikan 404
        return abort(404, description=f"CSV not found at: {csv_path}")

    # 2. Baca CSV dengan Pandas
    df = pd.read_csv(csv_path)

    # 3. Hitung frekuensi per Lipid_headgroup
    #    Misal kolom header di CSV persis bernama "Lipid_headgroup"
    if 'Lipid_headgroup' not in df.columns:
        return abort(400, description="'Lipid_headgroup' column missing in CSV")

    counts = df['Lipid_headgroup'].value_counts().sort_index()  # sort_index agar label terurut

    # 4. Buat bar chart menggunakan Matplotlib
    fig, ax = plt.subplots(figsize=(8, 5))
    counts.plot(kind='bar', ax=ax)

    ax.set_xlabel('Lipid Headgroup')
    ax.set_ylabel('Count')
    ax.set_title('Lipid Composition by Headgroup')
    plt.xticks(rotation=45, ha='right')
    plt.tight_layout()

    # 5. Simpan plot ke BytesIO sebagai PNG
    img_io = io.BytesIO()
    fig.savefig(img_io, format='png')
    img_io.seek(0)
    plt.close(fig)

    # 6. Kembalikan response PNG
    return send_file(
        img_io,
        mimetype='image/png',
        as_attachment=False,
        download_name='lipid_composition.png'
    )