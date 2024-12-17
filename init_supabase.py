import os
from supabase import create_client
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Initialize Supabase client
supabase = create_client(
    os.getenv("SUPABASE_URL"),
    os.getenv("SUPABASE_KEY")
)

def init_db():
    # Insert default categories
    try:
        # First check if categories exist
        response = supabase.table('categories').select("*").execute()
        if not response.data:  # Only insert if no categories exist
            supabase.table('categories').insert([
                {'nom': 'Fruits et Légumes', 'couleur': '#4CAF50'},
                {'nom': 'Viandes', 'couleur': '#F44336'},
                {'nom': 'Produits laitiers', 'couleur': '#2196F3'},
                {'nom': 'Épicerie', 'couleur': '#FF9800'},
                {'nom': 'Surgelés', 'couleur': '#9C27B0'},
                {'nom': 'Boissons', 'couleur': '#795548'},
                {'nom': 'Autre', 'couleur': '#607D8B'}
            ]).execute()
            print("Categories inserted successfully!")
        else:
            print("Categories already exist, skipping insertion.")
    except Exception as e:
        print(f"Error: {str(e)}")

if __name__ == '__main__':
    init_db()
