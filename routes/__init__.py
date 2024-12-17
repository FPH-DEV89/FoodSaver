from flask import Blueprint, jsonify, request, render_template
from datetime import datetime, timedelta
from apscheduler.schedulers.background import BackgroundScheduler
from pywebpush import webpush, WebPushException
import json
from dateutil.parser import parse

notifications = Blueprint('notifications', __name__)
scheduler = BackgroundScheduler()
scheduler.start()

# Configuration des notifications web push (à mettre dans votre fichier de configuration)
VAPID_PRIVATE_KEY = "your_private_key"  # À générer et à mettre dans .env
VAPID_PUBLIC_KEY = "your_public_key"    # À générer et à mettre dans .env
VAPID_CLAIMS = {
    "sub": "mailto:your@email.com"      # À configurer
}

@notifications.route('/notifications/subscribe', methods=['POST'])
def subscribe():
    subscription_info = request.get_json()
    # Stocker les informations d'abonnement dans la base de données
    return jsonify({'status': 'success'})

@notifications.route('/notifications/preferences')
def preferences():
    return render_template('notifications/preferences.html')

def check_expiring_products():
    # Récupérer tous les produits qui expirent dans les 3 prochains jours
    today = datetime.now().date()
    expiring_soon = []  # Requête à la base de données pour obtenir les produits

    for product in expiring_soon:
        try:
            # Envoyer une notification pour chaque produit
            webpush(
                subscription_info=subscription_info,  # À récupérer depuis la base de données
                data=json.dumps({
                    'title': 'Produit bientôt périmé !',
                    'body': f"Le produit {product['nom']} expire le {product['date_peremption']}"
                }),
                vapid_private_key=VAPID_PRIVATE_KEY,
                vapid_claims=VAPID_CLAIMS
            )
        except WebPushException as e:
            print(f"Erreur d'envoi de notification: {e}")

# Planifier la vérification quotidienne des produits
scheduler.add_job(
    check_expiring_products,
    'cron',
    hour=9,  # Exécuter tous les jours à 9h
    minute=0
)
