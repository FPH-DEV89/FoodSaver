-- Suppression des tables si elles existent déjà
DROP TABLE IF EXISTS products;
DROP TABLE IF EXISTS categories;

-- Création de la table categories
CREATE TABLE IF NOT EXISTS categories (
    id SERIAL PRIMARY KEY,
    nom VARCHAR(50) NOT NULL,
    description TEXT,
    couleur VARCHAR(7) DEFAULT '#000000'
);

-- Création de la table products
CREATE TABLE IF NOT EXISTS products (
    id SERIAL PRIMARY KEY,
    date_creation TIMESTAMPTZ DEFAULT CURRENT_TIMESTAMP,
    nom VARCHAR(255) NOT NULL,
    date_peremption DATE NOT NULL,
    code_barre VARCHAR(50),
    category_id INTEGER REFERENCES categories(id),
    quantite INTEGER DEFAULT 1,
    unite VARCHAR(20) DEFAULT 'unité'
);

-- Insertion des catégories par défaut
INSERT INTO categories (nom, description, couleur) VALUES
('Fruits', 'Fruits frais et secs', '#FF6B6B'),
('Légumes', 'Légumes frais et conserves', '#4ECDC4'),
('Produits laitiers', 'Lait, fromages, yaourts', '#45B7D1'),
('Viandes', 'Viandes, volailles, poissons', '#96CEB4'),
('Épicerie', 'Produits secs et conserves', '#FFEEAD'),
('Boissons', 'Boissons et liquides', '#D4A5A5'),
('Surgelés', 'Produits congelés', '#9DC8C8'),
('Snacks', 'Gâteaux, chips, confiseries', '#FF9999');
