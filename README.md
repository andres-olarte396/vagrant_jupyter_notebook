# Configuración de VM para Jupyter Notebook con Vagrant

Este proyecto configura una máquina virtual que ejecuta Ubuntu 20.04 (`ubuntu/focal64`) con Jupyter Notebook instalado, utilizando Vagrant. El script de configuración instala automáticamente las dependencias necesarias, configura el entorno y habilita el acceso remoto a Jupyter Notebook.

## Requisitos

Antes de comenzar, asegúrate de tener instalados en tu máquina local:

- [VirtualBox](https://www.virtualbox.org/) (o cualquier otro proveedor compatible con Vagrant)
- [Vagrant](https://www.vagrantup.com/)

## Comenzando

### 1. Clonar el repositorio

```bash
git clone <url_del_repositorio>
cd <directorio_del_repositorio>
```

### 2. Iniciar y levantar la máquina Vagrant

```bash
vagrant up
```

Esto descargará la imagen `ubuntu/focal64` si no está presente, aprovisionará la máquina virtual y ejecutará el script de configuración para instalar Python, pip y Jupyter Notebook.

### 3. Acceder a Jupyter Notebook

Una vez que la configuración esté completa, abre tu navegador y dirígete a:

```txt
  http://localhost:8888
```

Nota: El notebook está configurado para ser accesible desde cualquier dirección IP (`0.0.0.0`), y no abrirá automáticamente un navegador.

#### Acceso a Jupyter Notebook

Después de ejecutar el script de instalación y lanzar Jupyter Notebook, se te pedirá autenticación mediante un token. Puedes optar por usar el token actual o configurar una contraseña siguiendo los pasos a continuación.

##### Opción 1: Usar el Token Actual

3.1. **Obtener el token**: En la terminal donde lanzaste Jupyter Notebook, usa el siguiente comando para obtener el token:

  ```bash
  jupyter notebook list
  ```

  Esto mostrará una URL que incluye un token, similar a:

  ```txt
  http://localhost:8888/?token=<tu_token_aquí>
  ```

3.2. **Copia el token** desde la terminal y pégalo en el campo "Password or token" en la pantalla de autenticación de tu navegador web.

3.3. Haz clic en **"Log in"** para acceder a Jupyter Notebook.

##### Opción 2: Configurar una Contraseña Personalizada

Si prefieres usar una contraseña en lugar del token para futuras sesiones:

3.4. **Ingresa el token** en el campo "Token" de la pantalla de autenticación.

3.5. **Configura una nueva contraseña** escribiendo tu contraseña deseada en el campo "New Password".

3.6. Haz clic en **"Log in and set new password"**. Esto configurará la contraseña para que la uses en lugar del token en futuras sesiones.

### Nota

```txt
- A partir de este momento, podrás iniciar sesión en Jupyter Notebook utilizando solo tu contraseña personalizada.
- Si deseas restablecer la contraseña o volver a usar un token, puedes ejecutar nuevamente el comando `jupyter notebook --generate-config` y editar las configuraciones en el archivo de configuración generado.
```

### 4. Sincronización de Notebooks

La carpeta `/vagrant/notebooks` en la VM está sincronizada con una carpeta `notebooks` en el directorio raíz del proyecto. Cualquier archivo que agregues a esta carpeta estará disponible en el entorno de Jupyter dentro de la VM.

### 5. Detener la Máquina Virtual

Para detener la VM en ejecución, usa el siguiente comando:

```bash
vagrant halt
```

### 6. Destruir la Máquina Virtual

Si necesitas destruir la VM y eliminar todos los recursos asociados, ejecuta:

```bash
vagrant destroy
```

## Personalización de la Configuración

Si necesitas realizar ajustes en el script de aprovisionamiento, puedes modificar el `Vagrantfile` o el script de shell que maneja la instalación de Jupyter Notebook:

- `Vagrantfile` - Define la configuración de la VM.
- `provision.sh` - Script que instala y configura Jupyter Notebook.

## Resolución de Problemas

- **Jupyter Notebook no es accesible:** Asegúrate de que la VM está en ejecución (`vagrant up`) y que el puerto `8888` está disponible en tu máquina anfitriona. Si aún no es accesible, verifica que el servicio de Jupyter Notebook esté activo dentro de la VM usando `vagrant ssh` y `ps aux | grep jupyter`.

## Licencia

Este proyecto está licenciado bajo la Licencia MIT.
