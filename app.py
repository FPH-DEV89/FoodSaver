import os
from datetime import datetime, timedelta
from dotenv import load_dotenv
from flask import Flask, render_template, jsonify, request
import requests
from dateutil import parser
import json
from supabase import create_client, Client
from routes.api import api

# Chargement des variables d'environnement
load_dotenv()

app = Flask(__name__)
app.secret_key = os.getenv('FLASK_SECRET_KEY', 'dev')

# Configuration de Supabase
supabase_url = os.getenv('SUPABASE_URL')
supabase_key = os.getenv('SUPABASE_KEY')
supabase: Client = create_client(supabase_url, supabase_key)

# Enregistrement des blueprints
app.register_blueprint(api)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/scan')
def scan():
    return render_template('scan.html')

@app.route('/inventory')
def inventory():
    return render_template('inventory.html')

@app.route('/add')
def add():
    return render_template('add_product.html')

@app.route('/api/product-info/<barcode>')
def get_product_info(barcode):
    # URL de l'API Open Food Facts
    url = f'https://world.openfoodfacts.org/api/v0/product/{barcode}.json'
    
    try:
        response = requests.get(url)
        data = response.json()
        
        if data['status'] == 1:
            product = data['product']
            return jsonify({
                'nom': product.get('product_name_fr', product.get('product_name', '')),
                'marque': product.get('brands', ''),
                'image': product.get('image_url', '')
            })
        else:
            return jsonify({'error': 'Produit non trouvé'}), 404
            
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/api/get-products')
def get_products():
    try:
        response = api.get_products()
        return response
    except Exception as e:
        return jsonify({'error': str(e)}), 500

def calculate_days_left(date_peremption):
    """Calcule le nombre de jours restants avant la date de péremption."""
    if isinstance(date_peremption, str):
        date_peremption = parser.parse(date_peremption).date()
    today = datetime.now().date()
    return (date_peremption - today).days

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
