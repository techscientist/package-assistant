***********************
fTerm/package-assistant
***********************

=====
About
=====

package-assistant is an `fTerm <https://github.com/fterm/fterm>`_ package to provide useful assistant commands.

======
How-To
======

To run *command* with arguments *a1, a2,...*, simply run

.. code:: bash

   f command a1, a2,...


The fTerm interpreter will then attempt to interpret *command*.
First it will check if it was defined as a synonym of another, defined, command, and then do a string-based (typo-preventing) search. It will then prompt you with

.. code:: bash

   [f-i] interpreted_command a1, a2...


If you enter anything (except just pressing the return key), the command will not be run.

========
Commands
========

================
Installing (Mac)
================

Ensure you have `fTerm <https://github.com/fterm/fterm>`_ installed. Download the :code:`assistant.py` file from this repository, and put in in your :code:`~/.fterm` directory. 
  
=======
Authors
=======

- **Liam Schumm** - Developer - `@lschumm <https://github.com/lschumm>`_.

=======
License
=======

This project is licensed under the GNU GPL License, version 3.0 - see the `LICENSE <LICENSE>`_ file for details
