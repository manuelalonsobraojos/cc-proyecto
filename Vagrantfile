# -*- mode: ruby -*-
# vi: set ft=ruby :

# All Vagrant configuration is done below. The "2" in Vagrant.configure
# configures the configuration version (we support older styles for
# backwards compatibility). Please don't change it unless you know what
# you're doing.
Vagrant.configure("2") do |config|
  	config.vm.synced_folder ".", "/vagrant", disabled: true
	config.vm.box = "gce"
	# Hacemos la primera configuración para la máquina
  	config.vm.define "mv" do |machine|

		# Transferir los archivos necesarios
		machine.vm.provision "file", source: "setup.py", destination: "/home/vagrant/proyectocc/setup.py"
		machine.vm.provision "file", source: "setup_clasificacion.py", destination: "/home/vagrant/proyectocc/setup_clasificacion.py"
		machine.vm.provision "file", source: "requirements.txt", destination: "/home/vagrant/proyectocc/requirements.txt"
		machine.vm.provision "file", source: "nginx.conf", destination: "/home/vagrant/proyectocc/nginx.conf"
		machine.vm.provision "file", source: "bot", destination: "/home/vagrant/proyectocc/bot"
		machine.vm.provision "file", source: "clasificacion", destination: "/home/vagrant/proyectocc/clasificacion"

		config.vm.provider :google do |google, override|
			google.google_project_id = "ccproject1920"
			# google.google_client_email = "malonso@ccproject1920.iam.gserviceaccount.com"
			google.google_json_key_location = "../ccproject1920-e4c012589b1d.json"
			# Provide an instance name
			google.name = "ccproject"
			# Espeficiacion de donde se va a crear la máquina  virtual
			google.zone = "europe-west2-c"
			# Tipo de máquina
			google.machine_type = "n1-standard-2"
			# Especificacion de la imagen
			google.image = "ubuntu-1804-bionic-v20200108"
			#provide the SSH key
			override.ssh.private_key_path = "~/.ssh/id_rsa"	  	
		end
		# Configuración de ansible
		machine.vm.provision "ansible" do |ansible|
		  ansible.playbook = "configuracion_ansible.yml"
		end	
	end
end
