document.addEventListener('DOMContentLoaded', () => {
    const startButton = document.getElementById('start-scan');
    const stopButton = document.getElementById('stop-scan');
    const video = document.getElementById('scanner-video');
    const resultDiv = document.getElementById('scan-result');
    const productForm = document.getElementById('product-form');
    
    let codeReader;

    async function startScanning() {
        try {
            codeReader = new ZXing.BrowserMultiFormatReader();
            const videoInputDevices = await ZXing.BrowserMultiFormatReader.listVideoInputDevices();
            
            if (videoInputDevices.length === 0) {
                throw new Error('Aucune caméra détectée');
            }

            // Utiliser la caméra arrière si disponible
            const selectedDeviceId = videoInputDevices.find(device => 
                device.label.toLowerCase().includes('back') || 
                device.label.toLowerCase().includes('arrière')
            )?.deviceId || videoInputDevices[0].deviceId;

            startButton.style.display = 'none';
            stopButton.style.display = 'block';

            codeReader.decodeFromVideoDevice(selectedDeviceId, video, (result, err) => {
                if (result) {
                    // Arrêter le scan une fois un code détecté
                    stopScanning();
                    
                    // Afficher le résultat
                    resultDiv.innerHTML = `Code-barres détecté : ${result.text}`;
                    
                    // Afficher le formulaire
                    productForm.style.display = 'block';
                    
                    // Rechercher les informations du produit
                    fetchProductInfo(result.text);
                }
                if (err && !(err instanceof ZXing.NotFoundException)) {
                    console.error(err);
                    resultDiv.innerHTML = 'Erreur lors du scan : ' + err;
                }
            });
        } catch (err) {
            console.error(err);
            resultDiv.innerHTML = 'Erreur lors de l\'initialisation du scanner : ' + err.message;
        }
    }

    function stopScanning() {
        if (codeReader) {
            codeReader.reset();
            startButton.style.display = 'block';
            stopButton.style.display = 'none';
        }
    }

    async function fetchProductInfo(codeBarre) {
        try {
            const response = await fetch(`/api/get-product-info/${codeBarre}`);
            const data = await response.json();
            
            if (response.ok) {
                // Pré-remplir le formulaire avec les données du produit
                document.getElementById('nom').value = data.nom || '';
                document.getElementById('code_barre').value = codeBarre;
            } else {
                console.error('Erreur lors de la récupération des informations du produit:', data.error);
            }
        } catch (err) {
            console.error('Erreur lors de la requête:', err);
        }
    }

    // Gestionnaire de soumission du formulaire
    productForm.addEventListener('submit', async (e) => {
        e.preventDefault();
        
        const formData = {
            nom: document.getElementById('nom').value,
            date_peremption: document.getElementById('date_peremption').value,
            code_barre: document.getElementById('code_barre').value
        };

        try {
            const response = await fetch('/api/add-product', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json'
                },
                body: JSON.stringify(formData)
            });

            const data = await response.json();

            if (response.ok) {
                alert('Produit ajouté avec succès !');
                window.location.href = '/inventory';
            } else {
                alert('Erreur : ' + (data.error || 'Erreur inconnue'));
            }
        } catch (err) {
            console.error('Erreur lors de l\'ajout du produit:', err);
            alert('Erreur lors de l\'ajout du produit');
        }
    });

    // Gestionnaires d'événements pour les boutons
    startButton.addEventListener('click', startScanning);
    stopButton.addEventListener('click', stopScanning);
});
