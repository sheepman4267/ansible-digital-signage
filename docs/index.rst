.. toctree:: 
    :maxdepth: 2

    usage/usage

    technical/technical

=======================
Ansible Digital Signage
=======================
-----
What?
-----
A Digital Signage system primarily based on an Ansible playbook.

----
Why?
----
Because I couldn't find an open source signage solution which was:

* Simple
* Currently Maintained
* Able to be centrally managed

----
How?
----
Here's the simple version of what the Ansible role does:

#. Installs just enough to run Google Chrome in Kiosk mode
#. Creates a whole bunch of systemd units to handle all the standard actions (start Chrome, reload the page every so often, etc.)
#. Writes a schedule file to allow the system to decide what to display and when
#. Installs a python script to read that schedule file and take action (this script does not stay running)

This system is based entirely on the premise that it is better to let someone else write the long-running code. This frees me entirely from having to worry about such things as memory leaks, and greatly reduces the chance of finding some edge-case crash that takes 3 weeks to occur. 

Enough of a simple digital signage system existed on every (systemd-based) Linux system already that all I had to do was configure it right. Hence, Ansible!