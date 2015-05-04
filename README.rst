ThreadFix API
=============

A Python API wrapper to facilitate interactions with `ThreadFix <https://github.com/denimgroup/threadfix>`_.

Quick Start
-----------

Several quick start options are available:

- Install with pip (recommended): :samp:`pip install threadfix_api`
- `Download the latest release <https://github.com/aparsons/threadfix_api/releases/latest>`_
- Clone the repository: :samp:`git clone https://github.com/aparsons/threadfix_api.git`

Example
-------

.. code-block:: python

    # import the package
    from threadfix_api import threadfix

    # setup threadfix connection information
    host = 'http://localhost:8080/threadfix/'
    api_key = 'YourAPIKeyFromThreadFix'

    # instantiate this threadfix api wrapper
    tf = threadfix.ThreadFixAPI(host, api_key)

    # rock and roll
    teams = tf.list_teams()
    if teams.success:
      print(teams.data)

Bugs and Feature Requests
-------------------------

Have a bug or a feature request? Please first search for existing and closed issues. If your problem or idea is not addressed yet, [please open a new issue](https://github.com/aparsons/threadfix_api/issues/new).

Copyright and License
---------------------

- Copyright 2015 `Adam Parsons <https://github.com/aparsons>`_
- `Licensed under MIT <https://github.com/aparsons/threadfix_api/blob/master/LICENSE.txt>`_.