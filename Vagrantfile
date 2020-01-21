# -*- mode: ruby -*-
# vi: set ft=ruby :

# All Vagrant configuration is done below. The "2" in Vagrant.configure
# configures the configuration version (we support older styles for
# backwards compatibility). Please don't change it unless you know what
# you're doing.
Vagrant.configure("2") do |config|
  	config.vm.synced_folder ".", "/vagrant", disabled: true
	config.vm.box = "google/gce"
	# Hacemos la primera configuración para la máquina
  	config.vm.define :ccproject1920 do |ccproject1920|

		# Creación de directorio
		# ccproject1920.vm.provision "shell", inline: "mkdir -m 777 proyectocc"
		# Transferir los archivos necesarios
		# ccproject1920.vm.provision "file", source: "setup.py", destination: "proyectocc/setup.py"
		# ccproject1920.vm.provision "file", source: "setup_clasificacion.py", destination: "proyectocc/setup_clasificacion.py"
		# ccproject1920.vm.provision "file", source: "nginx.conf", destination: "proyectocc/nginx.conf"
		# ccproject1920.vm.provision "file", source: "bot", destination: "proyectocc/bot"
		# ccproject1920.vm.provision "file", source: "clasificacion", destination: "proyectocc/clasificacion"
		# Transferir archivo de configuracion
		# ccproject1920.vm.provision "shell", inline: "mv -f proyectocc/nginx.conf /etc/nginx/nginx.conf"

		ccproject1920.vm.provider :google do |google, override|
			google.google_project_id = "ccproject1920"
			#google.google_client_email = "malonso@ccproject1920.iam.gserviceaccount.com"
			google.google_json_key_location = "../ccproject1920-e4c012589b1d.json"
			# Provide an instance name
			google.name = "ccproject"
			# Espeficiacion de donde se va a crear la máquina  virtual
			google.zone = "europe-west2-c"
			# Tipo de máquina
			google.machine_type = "n1-standard-2"
			# Especificacion de la imagen
			google.image = "ubuntu-1804-bionic-v20200108"
			override.ssh.username = "manuelalonso136"
			#provide the SSH key
			override.ssh.private_key_path = "~/.ssh/my_gcp_keyname"	  	
		end
	end
	# Configuración de ansible
	config.vm.provision "ansible" do |ansible|
	  ansible.playbook = "configuracion_ansible.yml"
	end	
end
