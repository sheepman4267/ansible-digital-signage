==============
Role Variables
==============
ansible-digital-signage is configured entirely through variables set in your ansible inventory. These can be set per group or per host, just like in any other ansible playbook.

----------------
signage_schedule
----------------
The Signage Schedule is defined as a list of dictionaries in YAML. Each line in the schedule is formatted as such::

    - { days: "Mon,Tue,Wed,Thu,Fri", start_time: "08:00", end_time: "17:00", url: "https://example.com" }

The above line will instruct the signage player to display https://example.com from 8:00 in the morning until 5:00 in the afternoon on every weekday. A few notes on this syntax:

#. The order of these elements doesn't matter. You can, for example, put the :code:`url:` directive first. I recommend putting it at the end, in case your url is long enough to make the rest of the schedule hard to read.
#. Days of the week to display a given URL *must* be specified as a comma-separated list (with no spaces) of capitalized 3-letter abbreviations.
#. All times *must* be specified in 24-hour time.
#. If there are overlapping times specified in the schedule, the signage player will load the first one it finds.
#. As long as times don't overlap, the schedule line shouldn't have to be in order of start and end time. For your own sanity, however, the author strongly recommends writing the schedule in order.
