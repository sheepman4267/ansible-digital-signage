===============
Installed Files
===============
This page contains a detailed description of the files installed by ansible-digital-signage.

-----------------------------
chrome-firstrun-workaround.sh
-----------------------------
This is a shell script installed to :code:`/opt/ansible-digital-signage/chrome-firstrun-workaround.sh`.
The script is run as the specified :ref:`signage_user` during the initial run of the ansible role. It uses a bunch of :code:`xdotool` commmands to dismiss Chrome's firstrun dialog.

-------------------------
detect-primary-display.py
-------------------------
This is a python script which parses the output of :code:`xrandr` to determine the currently connected display output, then writes that to a file. It takes one argument, which should be the path to said file.

This script is executed by :ref:`xinitrc`.

.. tip:: This script currently does not support having multiple outputs connected. In such a case, the output listed first alphabetically will be written to the specified file.

.. warning:: Currently, this script will write an empty file if no connected output is found. This could happen if X11 is started before certain DisplayPort and HDMI monitors are turned on. In such a case, :ref:`signage-chrome` would fail. This will be fixed in a future version. This can be worked around by rebooting the computer after a display is connected.

--------
schedule
--------
The schedule file is written by a jinja2 template to :code:`/var/ansible-digital-signage/schedule`.
The template iterates over :ref:`signage_schedule` and writes lines formatted as::
    
    Mon,Tue,Wed,Thu,Fri,Sat,Sun|08:00|17:00|example.com
    days|start-time|end-time|example.com

.. note:: This will likely be replaced with JSON in a future version.

-------------------
signage-placeholder
-------------------
This is a placeholder HTML file which will be loaded by :ref:`signage-chrome` if :ref:`signage-refresh`'s last run found nothing in the schedule. This should only happen on first run, or if :ref:`signage-chrome` is started manually.

------------------
signage-refresh.py
------------------
signage-refresh.py is a python script which:

#. Reads the :ref:`schedule` file populated by Ansible using :ref:`signage_schedule`
#. When it finds a schedule entry which is active on the current day and at the current time, it:
    a. Writes the :code:`url` parameter of that entry to :code:`/var/ansible-digital-signage/current`
    b. Uses :code:`subprocess.call()` to restart :ref:`signage-chrome` using :code:`systemctl`
#. If there is no entry which is determined to be currently active, the script:
    a. Writes the path to the :ref:`signage_placeholder` file to :code:`/var/ansible-digital-signage/current`
    b. Uses :code:`subprocess.call()` to stop :ref:`signage-chrome` using :code:`systemctl`
    c. Uses :code:`subprocess.call()` to run :ref:`signage-display-off` using :code:`systemctl`

To assist in this, the script also includes an incredibly simplistic :code:`strptime` function which only works for 24-hour time with no seconds.

--------
timezone
--------
ansible-digital-signage writes :ref:`signage_timezone` to :code:`/etc/timezone` to keep Ubuntu from "helpfully" resetting the timezone after every tzdata update.

-------
xinitrc
-------
ansible-digital-signage writes a :code:`.xinitrc` file to :ref:`signage_user`'s home directory. This is so that X11 (as started by :ref:`signage-startx`) will run :ref:`detect-primary-display.py` and :code:`xeyes` rather than just starting :code:`xeyes`.
  

