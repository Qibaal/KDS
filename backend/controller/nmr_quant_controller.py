import matplotlib
matplotlib.use('Agg')

import pandas as pd
import matplotlib.pyplot as plt
import io
import os
from flask import send_file, abort

def generate_nmr_stacked_bar():
    """
    - Membaca file Excel: data/NMR_quant.xlsx
    - Membuat Stacked Bar Chart: kolom Polar_bear di X, 
      dan empat lipid columns ('Glycerides', '1,2-Diglyceride', 'Wax_esters', 'Sterol_esters') sebagai stack segments.
    - Kembalikan PNG via send_file
    """
    # 1. Temukan path absolut ke NMR_quant.xlsx
    base_dir = os.path.abspath(os.path.dirname(__file__))     # .../controllers
    project_root = os.path.dirname(base_dir)                   # .../my-flask-app
    xlsx_path = os.path.join(project_root, 'data', 'NMR_quant.xlsx')

    if not os.path.isfile(xlsx_path):
        return abort(404, description=f"Excel file not found at: {xlsx_path}")

    # 2. Baca sheet pertama (atau sheet default) dari Excel
    try:
        df = pd.read_excel(xlsx_path)
    except Exception as e:
        return abort(500, description=f"Error reading Excel: {e}")

    # 3. Pastikan kolom yang diperlukan ada
    required_cols = {'Polar_bear', 'Glycerides', '1,2-Diglyceride', 'Wax_esters', 'Sterol_esters'}
    if not required_cols.issubset(df.columns):
        return abort(400, description=f"Excel must contain columns: {required_cols}")

    # 4. Susun DataFrame untuk plotting
    #    Kita gunakan Polar_bear sebagai index, dan ambil hanya keempat lipid columns
    df_plot = df[['Polar_bear', 'Glycerides', '1,2-Diglyceride', 'Wax_esters', 'Sterol_esters']].copy()
    df_plot.set_index('Polar_bear', inplace=True)

    # 5. Buat stacked bar chart
    fig, ax = plt.subplots(figsize=(10, 6))
    palette_blue = [
        "#03045e", "#0077b6", "#00b4d8", "#90e0ef"
    ]

    df_plot.plot(
        kind='bar',
        stacked=True,
        ax=ax,
        color=palette_blue
    )

    ax.set_xlabel('Polar Bear')
    ax.set_ylabel('Jumlah Lipid (nmol/g)')
    ax.set_title('Komposisi Lipid per Individu (Stacked)')
    plt.xticks(rotation=45, ha='right')
    plt.tight_layout()

    # 6. Simpan figure ke BytesIO sebagai PNG
    img_io = io.BytesIO()
    fig.savefig(img_io, format='png')
    img_io.seek(0)
    plt.close(fig)

    # 7. Kembalikan PNG sebagai response
    return send_file(
        img_io,
        mimetype='image/png',
        as_attachment=False,
        download_name='nmr_stacked_bar.png'
    )

def generate_nmr_heatmap():
    """
    - Membaca file Excel: data/NMR_quant.xlsx
    - Membuat Heatmap:
        • Baris: Polar_bear
        • Kolom: Glycerides, 1,2-Diglyceride, Wax_esters, Sterol_esters
        • Nilai: kuantitas lipid (Abundance)
    - Mengembalikan gambar PNG via send_file
    """
    # 1. Tentukan path absolut ke file Excel
    base_dir = os.path.abspath(os.path.dirname(__file__))     # .../controllers
    project_root = os.path.dirname(base_dir)                   # .../my-flask-app
    xlsx_path = os.path.join(project_root, 'data', 'NMR_quant.xlsx')

    if not os.path.isfile(xlsx_path):
        return abort(404, description=f"Excel file not found at: {xlsx_path}")

    # 2. Baca sheet default (sheet pertama) dari Excel menggunakan pandas
    try:
        df = pd.read_excel(xlsx_path)
    except Exception as e:
        return abort(500, description=f"Error reading Excel: {e}")

    # 3. Validasi kolom yang diperlukan
    required_cols = {'Polar_bear', 'Glycerides', '1,2-Diglyceride', 'Wax_esters', 'Sterol_esters'}
    if not required_cols.issubset(df.columns):
        return abort(400, description=f"Excel must contain columns: {required_cols}")

    # 4. Siapkan DataFrame untuk plotting heatmap
    #    • Gunakan Polar_bear sebagai index
    #    • Kolom: Glycerides, 1,2-Diglyceride, Wax_esters, Sterol_esters
    df_plot = df[['Polar_bear', 'Glycerides', '1,2-Diglyceride', 'Wax_esters', 'Sterol_esters']].copy()
    df_plot.set_index('Polar_bear', inplace=True)

    # 5. Konversi ke matrix (2D array) untuk imshow
    data_matrix = df_plot.values  # shape: (n_bears, 4)

    # 6. Buat heatmap menggunakan matplotlib
    fig, ax = plt.subplots(figsize=(8, 6))

    # Menggunakan colormap 'viridis' (atau sesuaikan sesuai selera)
    cax = ax.imshow(data_matrix, aspect='auto', cmap='Blues')

    # 7. Set label sumbu:
    #    • X-axis → nama-nama lipid (kolom)
    #    • Y-axis → nama-nama Polar_bear (index)
    ax.set_xticks(range(len(df_plot.columns)))
    ax.set_xticklabels(df_plot.columns, rotation=45, ha='right')

    ax.set_yticks(range(len(df_plot.index)))
    ax.set_yticklabels(df_plot.index)

    ax.set_xlabel('Jenis Lipid')
    ax.set_ylabel('Polar Bear')
    ax.set_title('Heatmap: Intensitas Lipid per Polar Bear')

    # 8. Tambahkan colorbar di samping
    fig.colorbar(cax, ax=ax, orientation='vertical', label='Jumlah (Abundance)')

    plt.tight_layout()

    # 9. Simpan figure ke objek BytesIO sebagai PNG
    img_io = io.BytesIO()
    fig.savefig(img_io, format='png')
    img_io.seek(0)
    plt.close(fig)

    # 10. Kembalikan response PNG
    return send_file(
        img_io,
        mimetype='image/png',
        as_attachment=False,
        download_name='nmr_heatmap.png'
    )