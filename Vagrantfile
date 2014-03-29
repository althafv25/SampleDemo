# -*- mode: ruby -*-
# vi: set ft=ruby :

# Vagrantfile API/syntax version. Don't touch unless you know what you're doing!
VAGRANTFILE_API_VERSION = "2"

Vagrant.configure(VAGRANTFILE_API_VERSION) do |config|
  config.vm.box = "precise32"
  config.vm.network :forwarded_port, guest: 8000, host: 8000, auto_correct: true
  config.vm.network :forwarded_port, guest: 5432, host: 5431, auto_correct: true
end