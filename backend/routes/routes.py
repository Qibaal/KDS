from flask import Blueprint, request, jsonify
from controller.lipid_controller import generate_lipid_chart
from controller.abundance_controller import (
    generate_fa_bar_chart,
    generate_fa_pie_chart
)
from controller.nmr_quant_controller import (
    generate_nmr_stacked_bar,
    generate_nmr_heatmap  # <-- import baru
)

main_routes = Blueprint('main_routes', __name__)

@main_routes.route('/api/lipid/lipid_chart', methods=['GET'])
def lipid_chart():
    """
    GET /api/lipid_chart
    Menghasilkan bar chart PNG yang menampilkan jumlah lipid per Lipid_headgroup.
    """
    return generate_lipid_chart()

@main_routes.route('/api/abundance/fa_bar_chart', methods=['GET'])
def fa_bar_chart():
    """
    GET /api/fa_bar_chart
    Men-generate bar chart (FA_Chain vs Abundance)
    """
    return generate_fa_bar_chart()

@main_routes.route('/api/abundance/fa_pie_chart', methods=['GET'])
def fa_pie_chart():
    """
    GET /api/fa_pie_chart
    Men-generate pie chart (proportion Abundance per FA_Chain)
    """
    return generate_fa_pie_chart()


@main_routes.route('/api/nmr-quant/stacked-bar', methods=['GET'])
def nmr_stacked_bar():
    """
    GET /api/nmr-quant/stacked-bar
    Menghasilkan Stacked Bar Chart: Komposisi Lipid per Polar_bear
    """
    return generate_nmr_stacked_bar()


@main_routes.route('/api/nmr-quant/heatmap', methods=['GET'])
def nmr_heatmap():
    """
    GET /api/nmr-quant/heatmap
    Menghasilkan Heatmap: Intensitas lipid per Polar Bear
    """
    return generate_nmr_heatmap()