#!/bin/bash

# Actualizar los paquetes del sistema
sudo apt-get update -y

# Instalar Python y pip
sudo apt-get install -y python3 python3-pip

# Instalar Jupyter Notebook
sudo pip3 install notebook

# Instalar herramientas adicionales
sudo pip3 install pandas numpy scipy matplotlib scikit-learn

# Crear una carpeta para los notebooks
mkdir -p /vagrant/notebooks

# Cambiar el propietario de la carpeta a vagrant
sudo chown -R vagrant:vagrant /vagrant/notebooks

# Generar el archivo de configuración de Jupyter para el usuario vagrant
sudo -u vagrant jupyter notebook --generate-config

# Configurar Jupyter para permitir acceso remoto y evitar que abra el navegador
echo "c.NotebookApp.ip = '0.0.0.0'" >> /vagrant/.jupyter/jupyter_notebook_config.py
echo "c.NotebookApp.open_browser = False" >> /vagrant/.jupyter/jupyter_notebook_config.py
echo "c.NotebookApp.port = 8888" >> /vagrant/.jupyter/jupyter_notebook_config.py

# Iniciar Jupyter Notebook en segundo plano y obtener el token de acceso
sudo -u vagrant jupyter notebook --no-browser --ip=0.0.0.0 --port=8888 &

# Mostrar el token de Jupyter Notebook al final de la ejecución
sleep 5  # Esperar unos segundos para asegurarse de que el servidor haya iniciado
TOKEN=$(sudo -u vagrant jupyter notebook list | grep -oP '(?<=token=)[a-z0-9]+')
echo "Jupyter Notebook ha sido instalado exitosamente."
echo "Accede a Jupyter Notebook en: http://localhost:8888/?token=$TOKEN"
echo "Utiliza este token para iniciar sesión: $TOKEN"