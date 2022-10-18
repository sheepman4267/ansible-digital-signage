=============
Systemd Units
=============
This page contains a detailed description of the function of all systemd units deployed by ansible-digital-signage.

------------------
signage-autoreload
------------------
signage-autoreload is both a timer and a oneshot service. The timer fires the service at an interval specified by :ref:`signage_reload_every`.

The service runs as the user specified by :ref:`signage_user`. 

The service sends :code:`ctrl+r` to X11 display :code:`:0` using :code:`xdotool` to reload the webpage.

