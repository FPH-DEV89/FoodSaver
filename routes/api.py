from flask import Blueprint, jsonify, request
from datetime import datetime
import os
from supabase import create_client
from dotenv import load_dotenv

# Chargement des variables d'environnement
load_dotenv()

api = Blueprint('api', __name__)

# Initialize Supabase client
supabase = create_client(
    os.getenv("SUPABASE_URL"),
    os.getenv("SUPABASE_KEY")
)

@api.route('/api/categories', methods=['GET'])
def get_categories():
    response = supabase.table('categories').select("*").order('nom').execute()
    return jsonify(response.data)

@api.route('/api/products', methods=['GET'])
def get_products():
    response = supabase.table('products').select(
        "*",
        count="exact"
    ).execute()
    return jsonify(response.data)

@api.route('/api/products', methods=['POST'])
def add_product():
    data = request.json
    try:
        response = supabase.table('products').insert({
            'nom': data['nom'],
            'date_peremption': data['date_peremption'],
            'code_barre': data.get('code_barre'),
            'category_id': data.get('category_id'),
            'quantite': data.get('quantite', 1),
            'unite': data.get('unite', 'unité')
        }).execute()
        return jsonify(response.data[0]), 201
    except Exception as e:
        return jsonify({'error': str(e)}), 400

@api.route('/api/products/<int:product_id>', methods=['DELETE'])
def delete_product(product_id):
    try:
        supabase.table('products').delete().eq('id', product_id).execute()
        return '', 204
    except Exception as e:
        return jsonify({'error': str(e)}), 400
