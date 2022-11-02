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

--------------
signage-chrome
--------------
signage-chrome is a standard service. It is started by :ref:`signage_refresh`. 

The service runs as the user specified by :ref:`signage_user`. 

signage-chrome is responsible for 3 things:

#. Turning on the display output identified by :ref:`detect-primary-display.py` and setting the screen orientation per :ref:`signage_orientation`
#. Starting the browser selected by :ref:`signage_browser` with the URL selected by :ref:`signage-refresh`
#. Resizing the browser window to fill the screen

Objective #1 is fulfilled through an ExecStartPre directive which runs an :code:`xrandr` command. Said command reads the display output to configure from a file written by :ref:`detect-primary-display.py`.

Objective #2 is fulfilled by the ExecStart directive. This directive joins together the command specified by :ref:`signage_browser_command` and the contents of a file written by :ref:`signage-refresh.`

Objective #3 is fulfilled by an ExecStartPost directive which runs an xdotool command. This command searches *visible* windows (so, hopefully only the actual signage window) for anything matching the variable :ref:`signage_browser_window_name`.

-------------------
signage-display-off
-------------------
signage-display-off is a simple oneshot service which uses :code:`xrandr` to disable the video output specified by :ref:`detect-primary-display.py`.

---------------
signage-refresh
---------------
signage-refresh is the most complicated part of this entire system. It is a oneshot service, a timer, and a python script. 

The timer runs the service:

#. 60 seconds after the player boots
#. Every time a schedule item starts or ends

The service exists only to run the python script, which is run as root.

The python script:

#. Reads the schedule file populated by Ansible using :ref:`signage_schedule`
#. When it finds a schedule entry which is active on the current day and at the current time, it:
    a. Writes the :code:`url` parameter of that entry to :code:`/var/ansible-digital-signage/current`
    b. Uses :code:`subprocess.call()` to restart :ref:`signage-chrome` using :code:`systemctl`
#. If there is no entry which is determined to be currently active, the script:
    a. Writes the path to the :ref:`signage_placeholder` file to :code:`/var/ansible-digital-signage/current`
    b. Uses :code:`subprocess.call()` to stop :ref:`signage-chrome` using :code:`systemctl`
    c. Uses :code:`subprocess.call()` to run :ref:`signage-display-off` using :code:`systemctl`

To assist in this, the script also includes an incredibly simplistic :code:`strptime` function which only works for 24-hour time with no seconds.
    
