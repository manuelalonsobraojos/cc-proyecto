# cc-proyecto
Repositorio para el proyecto de la asignatura Cloud Computing

[![Build Status](https://travis-ci.org/manuelalonsobraojos/cc-proyecto.svg?branch=master)](https://travis-ci.org/manuelalonsobraojos/cc-proyecto) [![CircleCI](https://circleci.com/gh/manuelalonsobraojos/cc-proyecto.svg?style=svg)](https://circleci.com/gh/manuelalonsobraojos/cc-proyecto) 

En el siguiente enlace podemos consultar la documentación correspondiente a la primera entrega en la que se especifica la arquitectura:

![img](https://github.com/manuelalonsobraojos/cc-proyecto/blob/master/img/arquitectura.png)

[primera entrega](https://github.com/manuelalonsobraojos/cc-proyecto/blob/master/docs/Readme1.md)

En el siguiente enlace podemos consultar la documentación correspondiente a la segunda entrega:

[segunda entrega](https://github.com/manuelalonsobraojos/cc-proyecto/blob/master/docs/Readme2.md)

La herramienta de construcción utilizada y desarrollada en la segunda entrega fue la siguiente:
```
buildtool: Makefile
```

En el siguiente enlace podemos consultar la documentación correspondiente a la tercera entrega:

[tercera entrega](https://github.com/manuelalonsobraojos/cc-proyecto/blob/master/docs/Readme3.md)

Cada vez que se realice un push al repositorio de GitHub se realizará la construcción de la imagen en DockerHub.
```
Contenedor: https://hub.docker.com/r/manuelalonsobraojos/cc-proyecto
```

En el siguiente enlace podemos consultar la documentación correspondiente a la cuarta entrega:

```
Prestaciones: fichero_taurus.yml
```

### Provisionamiento de máquinas virtuales

Se ha realizado el despliegue de una máquina virtual en Google Cloud. En esta máquina virtual se ejecutan dos microservicios y un Gateway con **Nginx** que se encarga de recibir las peticiones y redireccionarlas a los dos microservicios.

**Creación de máquina virtual**
En primer lugar ha sido necesario instalar vagrant, el cual requiere la instalación de virtualbox, el cual instalamos con el siguiente comando:
```
apt install virtualbox
```
Una vez instalado virtualbox se ha procedido a instalar vagrant con los siguientes comandos:
```
curl -O https://releases.hashicorp.com/vagrant/2.2.6/vagrant_2.2.6_x86_64.deb

apt install ./vagrant_2.2.6_x86_64.deb
```

Una vez instalado vagrant,  se realizó la instalación del plugin de google mediante el siguiente comando:
```
vagrant pluging install vagrant-google
```

La configuración de la máquina virtual se ha especificado en el archivo [Vagrantfile](https://github.com/manuelalonsobraojos/cc-proyecto/blob/master/Vagrantfile), y se puede ver a continuación:
```
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
	# Configuración con ansible
	config.vm.provision "ansible" do |ansible|
	  ansible.playbook = "configuracion_ansible.yml"
	end	
end
```

De la configuración del archivo Vagrantfile cabe destacar las siguientes:

* ```google.google_json_key_location = "../ccproject1920-e4c012589b1d.json"``` en esta línea se especifica la ruta de nuestra máquina donde tenemos guardada la clave de google generada.

* ```google.image = "ubuntu-1804-bionic-v20200108"``` En esta línea se especifica la imagen de la máquina virtual. En este caso se ha escogido Ubuntu 18.04 porque ha sido la utilizda en el desarrollo y en la anterior práctica se vío que el microservicio testeado ofrecía buen rendimiento.

* ```override.ssh.username = "manuelalonso136"``` Usuario para el cual se ha generado una clave ssh
* ```override.ssh.private_key_path = "~/.ssh/my_gcp_keyname"``` Ruta donde se encuentra guardada la clave ssh para el usuario especificado. Esta clave ha sido guardada en **Google Cloud**. 

**Despliegue de la máquina**

Para el despliegue de la máquina se ejecuta la siguiente orden:
```
vagrant up
```
Al ejecutar esto automáticamente se desplegará la máquina virtulal y se realizará el aprovisionamiento mediante ansible, para el cual se ha creado el archivo [configuracion_ansible](https://github.com/manuelalonsobraojos/cc-proyecto/blob/master/configuracion_ansible.yml).
```
---
- hosts: all
  become: yes
  gather_facts: False
  vars:
    NAME_BD: "{{ lookup('env','NAME_BD') }}" 
    HOST_BD: "{{ lookup('env','HOST_BD') }}" 
    USER_BD: "{{ lookup('env', 'USER_BD') }}"
    PASS_BD: "{{ lookup('env', 'PASS_BD') }}"

  pre_tasks:
    - name: Instalar Python 2 para Ansible
      raw: test -e /usr/local/bin/python || (apt -y update && apt install -y python)
      changed_when: False

    - name: Instalar Python 3 para Ansible
      raw: test -e /usr/local/bin/python3 || (apt -y update && apt install -y python3)
      changed_when: False

  tasks:
  - name: Update
    command: apt-get update
  - name: essential
    command: apt-get install -y build-essential
  - name: Instalar pip
    apt: name=python3-pip state=present
  - name: Instalar setuotools
    apt: name=python3-setuptools state=present
  - name: Instalar python3-dev
    apt: name=python3-dev state=present
  - name: Instalar libgdbm-dev
    apt: name=libgdbm-dev state=present
  - name: Instalar libncurses5-dev
    apt: name=libncurses5-dev state=present
  - name: instalar postgresql
    apt: name=postgresql state=present
  - name: Instalar postgresql-contrib
    apt: name=postgresql-contrib state=present
  - name: Instalar libpq-dev
    apt: name=libpq-dev state=present
  - name: Instalar supervisor
    apt: name=supervisor state=present

  - name: Crear directorio
    command: mkdir -m 777 proyectocc

  - name: copy setup resultados
    copy:
      src: setup.py
      dest: proyectocc/setup.py

  - name: copy nginx configuracion
    copy:
      src: nginx.conf
      dest: proyectocc/nginx.conf

  - name: copy directorio resultados
    copy:
      src: bot
      dest: proyectocc/bot

  - name: copy directorio clasificacion
    copy:
      src: clasificacion
      dest: proyectocc/clasificacion

  - name: Instalar proyectocc/paquete resultados
    command: python3 setup.py install
    become: yes
    args:
      chdir: proyectocc/

  - name: Instalar nginx
    apt: name=nginx state=present  
    become: yes

  - name: Instalar proyectocc/paquete resultados
    command: mv -f proyectocc/nginx.conf /etc/nginx/nginx.conf
    become: yes	

  - name: mover configuracion nginx
    command: mv -f proyectocc/nginx.conf /etc/nginx/nginx.conf
    become: yes
    args:
      chdir: proyectocc/

  - name: iniciar nginx
    command: service nginx start
    become: yes

  - name: iniciar ms resultados
    command: make ejecutar_result
    args:
      chdir: proyectocc/

  - name: iniciar ms resultados
    command: make ejecutar_clasificacion
    args:
      chdir: proyectocc/
```
Como se puede observar se crean las variables de entorno necesarias, se instalan las dependencias para el correcto funcionamiento de la arquitectura, se sobreescribe la configuración nginx la cual ahora se verá y se pone en funcionamiento.

ara poder acceder mediante http al servidor Nginf se ejecutará la siguiente orden para la creación de reglas de Firewall en GCP, estas reglas han sido vistas en la documentación oficial de google cloud [Google_Cloud](https://cloud.google.com/vpc/docs/using-firewalls?hl=es-419).
```
gcloud compute firewall-rules create vm1-allow-ingress-tcp-port80-from-subnet1 \
    --network my-network \
    --action allow \
    --direction ingress \
    --rules tcp:80 \
    --source-ranges 10.240.10.0/24 \
```

La configuración de Nginx creada la podemos encontrar en el archivo [nginx.conf](https://github.com/manuelalonsobraojos/cc-proyecto/blob/master/nginx.conf).
```
worker_processes 1;

events { worker_connections 1024; }

http {

    sendfile on;

    gzip              on;
    gzip_http_version 1.0;
    gzip_proxied      any;
    gzip_min_length   500;
    gzip_disable      "MSIE [1-6]\.";
    gzip_types        text/plain text/xml text/css
                      text/comma-separated-values
                      text/javascript
                      application/x-javascript
                      application/atom+xml;

    # List of application servers
    upstream resultados_server {

        server 0.0.0.0:5000;

    }
	# List of application servers
    upstream clasificacion_server {

        server 0.0.0.0:8000;

    }

    # Configuration for the server
    server {

        # Running port
        listen 80;

        # Proxying the resultados API
        location /result {

            proxy_pass         http://resultados_server;
            proxy_redirect     off;
            proxy_set_header   Host $host;
            proxy_set_header   X-Real-IP $remote_addr;
            proxy_set_header   X-Forwarded-For $proxy_add_x_forwarded_for;
            proxy_set_header   X-Forwarded-Host $server_name;

        }

		# Proxying the Clasificacion API
        location /clasificacion {

            proxy_pass         http://clasificacion_server;
            proxy_redirect     off;
            proxy_set_header   Host $host;
            proxy_set_header   X-Real-IP $remote_addr;
            proxy_set_header   X-Forwarded-For $proxy_add_x_forwarded_for;
            proxy_set_header   X-Forwarded-Host $server_name;

        }

    }
}
```

En la siguiente imagen podemos ver como la máquina virtual está creada en la ventana de administración de Google Cloud:
![img](https://github.com/manuelalonsobraojos/cc-proyecto/blob/master/img/Captura_GC.PNG)

En la siguiente imagen se puede ver como desde el navegador es posible realizar una petición a la máquina virtual desplegada:
![img](https://github.com/manuelalonsobraojos/cc-proyecto/blob/master/img/Captura_4_1.PNG)


### Medición de prestaciones

Se ha realiazo una medición de prestaciones para la cual se ha utilizado la herramienta **Taurus**.
Tras la medición de prestaciones se ha comprobado que la máquina remota desplegada en **Google Cloud** no es capaz de soportar un número elevado de peticiones por segundo, obteniendo un número mucho menor que el obtenido en las mediciones realizadas en nuestra máquina local.

![img](https://github.com/manuelalonsobraojos/cc-proyecto/blob/master/img/prestaciones_GC.PNG)



