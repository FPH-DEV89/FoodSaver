# FoodSaver

FoodSaver est une application web conçue pour lutter contre le gaspillage alimentaire en permettant aux utilisateurs de gérer efficacement leur inventaire alimentaire. L'application utilise un scanner de codes-barres pour faciliter l'ajout de produits et intègre un système d'alertes intelligent pour prévenir de la péremption des aliments.

## Fonctionnalités principales

- **Scanner de codes-barres** : Ajoutez rapidement des produits en scannant leur code-barres
- **Gestion d'inventaire** : Suivez facilement vos stocks alimentaires
- **Système d'alertes** : Recevez des notifications avant la péremption de vos produits
- **Interface intuitive** : Navigation simple et efficace
- **Base de données produits** : Accès à une large base de données de produits alimentaires
- **Stockage cloud** : Vos données sont stockées en sécurité sur Supabase

## Prérequis

- Python 3.8 ou supérieur
- Navigateur web moderne
- Caméra (pour le scan des codes-barres)
- Compte Supabase (gratuit)

## Installation

1. Clonez le dépôt :
```bash
git clone https://github.com/votre-username/foodsaver.git
cd foodsaver
```

2. Installez les dépendances :
```bash
pip install -r requirements.txt
```

3. Configurez les variables d'environnement :
- Créez un fichier `.env` à la racine du projet avec les variables suivantes :
```
FLASK_SECRET_KEY=votre_clé_secrète
SUPABASE_URL=votre_url_supabase
SUPABASE_KEY=votre_clé_supabase
```

4. Lancez l'application :
```bash
python app.py
```

L'application sera accessible à :
- http://127.0.0.1:5000 (localhost)
- http://[votre-ip]:5000 (réseau local)

## Utilisation mobile

Pour utiliser l'application sur votre téléphone :
1. Connectez votre téléphone au même réseau WiFi que l'ordinateur
2. Ouvrez le navigateur sur votre téléphone
3. Entrez l'adresse : http://[ip-de-votre-ordinateur]:5000

## Technologies utilisées

- **Backend** : Flask (Python)
- **Base de données** : Supabase (PostgreSQL)
- **Frontend** : HTML, CSS, JavaScript
- **UI Framework** : Bootstrap 5
- **API externe** : Open Food Facts (données produits)

## Structure du projet

```
foodsaver/
├── app.py              # Application principale Flask
├── schema.sql          # Structure de la base de données
├── requirements.txt    # Dépendances Python
├── static/            # Fichiers statiques
│   ├── css/          # Styles CSS
│   └── js/           # Scripts JavaScript
└── templates/         # Templates HTML
```

## Contribution

Les contributions sont les bienvenues ! N'hésitez pas à :
1. Fork le projet
2. Créer une branche pour votre fonctionnalité
3. Commiter vos changements
4. Pousser vers la branche
5. Ouvrir une Pull Request

## Licence

Ce projet est sous licence MIT. Voir le fichier `LICENSE` pour plus de détails.

## Support

Pour toute question ou problème, veuillez ouvrir une issue sur le dépôt GitHub.
