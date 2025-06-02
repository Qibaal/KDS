import matplotlib
matplotlib.use('Agg')

import pandas as pd
import matplotlib.pyplot as plt
import io
import os
from flask import send_file, abort

def generate_fa_bar_chart():
    """
    - Membaca file CSV: data/WE_FA_Abundance.csv
    - Membuat Bar Chart (FA_Chain vs Abundance), diurutkan berdasarkan Abundance descending
    - Mengembalikan PNG via send_file
    """
    base_dir = os.path.abspath(os.path.dirname(__file__))
    project_root = os.path.dirname(base_dir)                 
    csv_path = os.path.join(project_root, 'data', 'WE_FA_Abundance.csv')

    if not os.path.isfile(csv_path):
        return abort(404, description=f"CSV not found at: {csv_path}")

    try:
        df = pd.read_csv(csv_path)
    except Exception as e:
        return abort(500, description=f"Error reading CSV: {e}")

    required_cols = {'FA_Chain', 'Abundance'}
    if not required_cols.issubset(df.columns):
        return abort(400, description=f"CSV must contain columns: {required_cols}")

    df_sorted = df.sort_values(by='Abundance', ascending=False)

    fig, ax = plt.subplots(figsize=(10, 6))
    ax.bar(df_sorted['FA_Chain'].astype(str), df_sorted['Abundance'])
    ax.set_xlabel('FA Chain')
    ax.set_ylabel('Abundance')
    ax.set_title('FA Chain vs Abundance')
    plt.xticks(rotation=45, ha='right')
    plt.tight_layout()

    img_io = io.BytesIO()
    fig.savefig(img_io, format='png')
    img_io.seek(0)
    plt.close(fig)

    return send_file(
        img_io,
        mimetype='image/png',
        as_attachment=False,
        download_name='fa_bar_chart.png'
    )


def generate_fa_pie_chart():
    """
    - Membaca file CSV: data/WE_FA_Abundance.csv
    - Membuat Pie Chart berdasarkan proporsi Abundance per FA_Chain
    - Mengembalikan PNG via send_file
    """
    # 1. Path ke CSV
    base_dir = os.path.abspath(os.path.dirname(__file__))     
    project_root = os.path.dirname(base_dir)                  
    csv_path = os.path.join(project_root, 'data', 'WE_FA_Abundance.csv')

    if not os.path.isfile(csv_path):
        return abort(404, description=f"CSV not found at: {csv_path}")

    try:
        df = pd.read_csv(csv_path)
    except Exception as e:
        return abort(500, description=f"Error reading CSV: {e}")

    required_cols = {'FA_Chain', 'Abundance'}
    if not required_cols.issubset(df.columns):
        return abort(400, description=f"CSV must contain columns: {required_cols}")

    labels = df['FA_Chain'].astype(str)
    sizes = df['Abundance']

    fig, ax = plt.subplots(figsize=(8, 8))
    ax.pie(
        sizes,
        labels=labels,
        autopct='%1.1f%%',
        startangle=90
    )
    ax.set_title('Proportion of Abundance per FA Chain')
    ax.axis('equal') 

    plt.tight_layout()

    img_io = io.BytesIO()
    fig.savefig(img_io, format='png')
    img_io.seek(0)
    plt.close(fig)

    return send_file(
        img_io,
        mimetype='image/png',
        as_attachment=False,
        download_name='fa_pie_chart.png'
    )