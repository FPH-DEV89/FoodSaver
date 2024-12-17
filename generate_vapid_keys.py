from py_vapid import Vapid01
import json
import base64
from cryptography.hazmat.primitives import serialization

vapid = Vapid01()
vapid.generate_keys()

# Convertir les clés en format approprié
private_key = vapid._private_key.private_bytes(
    encoding=serialization.Encoding.PEM,
    format=serialization.PrivateFormat.PKCS8,
    encryption_algorithm=serialization.NoEncryption()
).decode('utf-8')

public_key = base64.urlsafe_b64encode(
    vapid._private_key.public_key().public_bytes(
        encoding=serialization.Encoding.X962,
        format=serialization.PublicFormat.UncompressedPoint
    )
).decode('utf-8')

# Sauvegarder les clés dans un fichier
vapid_keys = {
    "VAPID_PRIVATE_KEY": private_key,
    "VAPID_PUBLIC_KEY": public_key,
    "VAPID_CLAIMS": {
        "sub": "mailto:your@email.com"
    }
}

with open('vapid_keys.json', 'w') as f:
    json.dump(vapid_keys, f, indent=2)

print("Clés VAPID générées avec succès!")
print(f"Clé publique: {public_key}")
print("Clé privée sauvegardée dans vapid_keys.json")
