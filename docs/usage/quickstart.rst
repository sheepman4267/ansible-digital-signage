==========
Quickstart
==========

This guide should serve to get you up and running with a simple setup.

-------------
Prerequisites
-------------

You will need: 

#. Somewhere to run Ansible (if you have the ability, I suggest a virtual machine so you can just ssh in and manage it from anywhere).
#. At least one computer to be used as a signage player.

    * I recommend Ubuntu Server as the operating system on the player. That is the only Linux distribution I've tested. Theoretically, anything based on .deb and systemd should work, but I haven't tried it.

----------------------------
Prepare the signage player
----------------------------
This is fairly standard Ansible setup.

#. Install Ubuntu Server in minimized mode
#. Set your administrative user up for SSH key authentication
#. Set your administrative user up for passwordless sudo

---------------------------
Configure Ansible Inventory
---------------------------
#. Copy hosts.yml.example to hosts.yml
#. Change "ansible_user" to the administrative username you chose when setting up your operating system
#. Configure signage_schedule to display a page of your choice (example.com is traditional)
#. Add your signage player's hostname or IP address to the "hosts" list
#. Copy playbook.yml.example to playbook.yml 
