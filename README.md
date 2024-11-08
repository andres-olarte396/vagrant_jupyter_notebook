# Jupyter Notebook VM Setup with Vagrant

This project sets up a virtual machine running Ubuntu 20.04 (`ubuntu/focal64`) with Jupyter Notebook installed using Vagrant. The configuration script automatically installs the necessary dependencies, sets up the environment, and configures Jupyter Notebook to be accessible remotely.

## Requirements

Before starting, ensure you have the following installed on your local machine:

- [VirtualBox](https://www.virtualbox.org/) (or any other provider supported by Vagrant)
- [Vagrant](https://www.vagrantup.com/)

## Getting Started

### 1. Clone the repository

```bash
git clone <repository_url>
cd <repository_directory>
```

### 2. Initialize and start the Vagrant machine

```bash
vagrant up
```

This will download the `ubuntu/focal64` image if not already present, provision the virtual machine, and execute the setup script to install Python, pip, and Jupyter Notebook.

### 3. Access Jupyter Notebook

Once the setup is complete, open your browser and navigate to:

```txt
  http://localhost:8888
```

Note: The notebook is configured to be accessible from any IP address (`0.0.0.0`), and it won't automatically open a browser.

#### Acceso a Jupyter Notebook

Después de ejecutar el script de instalación y ejecutar Jupyter Notebook, se te pedirá autenticación mediante token. Puedes optar por usar el token actual o configurar una contraseña siguiendo los pasos a continuación.

##### Opción 1: Usar el token actual

3.1. **Obtener el token**: En la terminal donde ejecutaste Jupyter Notebook, usa el siguiente comando para obtener el token:
  
  ```bash
  jupyter notebook list
  ```

  Esto mostrará una URL que incluye un token, algo similar a:

  ```txt
  http://localhost:8888/?token=<tu_token_aquí>
  ```

3.2. **Copia el token** desde la terminal y pégalo en el campo de autenticación "Password or token" en el navegador web.

3.3. Haz clic en **"Log in"** para acceder a Jupyter Notebook.

##### Opción 2: Configurar una contraseña personalizada

Si prefieres usar una contraseña en lugar del token para futuras sesiones:

3.4. **Ingresa el token** en el campo "Token" de la pantalla de autenticación.

3.5. **Configura una nueva contraseña** escribiendo tu nueva contraseña en el campo "New Password".

3.6. Haz clic en **"Log in and set new password"**. Esto configurará la contraseña para que la uses en lugar del token en futuras sesiones.

### Nota

```txt
- A partir de este momento, podrás iniciar sesión en Jupyter Notebook utilizando solo tu contraseña personalizada.
- Si deseas resetear la contraseña o volver a usar un token, puedes ejecutar nuevamente el comando `jupyter notebook --generate-config` y editar las configuraciones en el archivo de configuración generado.
```

Este texto puede ser agregado a la sección de **Uso y Configuración** en tu archivo `README` para que los usuarios sepan cómo acceder a Jupyter Notebook.

### 4. Syncing Notebooks

The `/vagrant/notebooks` folder in the VM is synced with a local `notebooks` folder in the root directory of the project. Any files you add to this folder will be available within the VM's Jupyter environment.

### 5. Stopping the Virtual Machine

To stop the running VM, use the following command:

```bash
vagrant halt
```

### 6. Destroying the Virtual Machine

If you need to destroy the VM and remove all associated resources, run:

```bash
vagrant destroy
```

## Customizing the Setup

If you need to make adjustments to the provisioning script, you can modify the `Vagrantfile` or the shell script that handles Jupyter Notebook installation:

- `Vagrantfile` - Defines the VM's configuration.
- `provision.sh` - Script that installs and configures Jupyter Notebook.

## Troubleshooting

- **Jupyter Notebook not accessible:** Ensure that the VM is running (`vagrant up`) and that port `8888` is available on your host machine. If it's still not accessible, verify that the Jupyter Notebook service is running within the VM using `vagrant ssh` and `ps aux | grep jupyter`.

## License

This project is licensed under the MIT License.
