# Vagrantfile para Jupyter Notebook
Vagrant.configure("2") do |config|
  # Usamos Ubuntu como sistema base
  config.vm.box = "ubuntu/focal64"
  # Nombre de la máquina virtual
  config.vm.hostname = "jupyter-nb"
  # Configurar la red privada con IP fija
  config.vm.network "private_network", ip: "192.168.36.39"
  # Configurar la red para acceder al Jupyter Notebook desde el host
  config.vm.network "forwarded_port", guest: 8888, host: 8888
  # Provisión para instalar Jupyter y dependencias
  config.vm.provision "shell", path: "scripts/provision.sh"
  # Configuración de recursos
  config.vm.provider "virtualbox" do |vb|
    # Nombre de la máquina virtual
    vb.name = "jupyter-nb"
    # Configuración de recursos
    vb.memory = 2*1024
    vb.cpus = 2
  end
  # Sync folder from host to guest
  config.vm.synced_folder "./shared", "/vagrant"
end