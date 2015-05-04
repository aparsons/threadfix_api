ThreadFix API
=============

A Python API wrapper to facilitate interactions with `ThreadFix <https://github.com/denimgroup/threadfix>`_.

This package implements all API functionality available within ThreadFix 2.2.2 (Apr 30).

Quick Start
-----------

Several quick start options are available:

- Install with pip (recommended): :code:`pip install threadfix_api`
- `Download the latest release <https://github.com/aparsons/threadfix_api/releases/latest>`_
- Clone the repository: :code:`git clone https://github.com/aparsons/threadfix_api.git`

Example
-------

.. code-block:: python

    # import the package
    from threadfix_api import threadfix

    # setup threadfix connection information
    host = 'http://localhost:8080/threadfix/'
    api_key = 'your_api_key_from_threadfix'

    # instantiate the threadfix api wrapper
    tf = threadfix.ThreadFixAPI(host, api_key)

    # If you need to disable certificate verification, set verify_ssl to False.
    # tf = threadfix.ThreadFixAPI(host, api_key, verify_ssl=False)

    # You can also specify a local cert to use as client side certificate, as a
    # single file (containing the private key and the certificate) or as a tuple
    # of both file's path.
    # cert=('/path/server.crt', '/path/key')
    # tf = threadfix.ThreadFixAPI(host, api_key, cert=cert)

    # rock and roll
    teams = tf.list_teams()
    if teams.success:
        print(teams.data)  # Decoded JSON object

        for team in teams.data:
            print(team['name'])  # Print the name of each team
    else:
        print('Uh Oh! ' + teams.message)

Supporting information for each method available can be found in the `documentation <https://github.com/aparsons/threadfix_api/tree/master/docs>`_.

Bugs and Feature Requests
-------------------------

Have a bug or a feature request? Please first search for existing and closed issues. If your problem or idea is not addressed yet, `please open a new issue <https://github.com/aparsons/threadfix_api/issues/new>`_.

Copyright and License
---------------------

- Copyright 2015 `Adam Parsons <https://github.com/aparsons>`_
- `Licensed under MIT <https://github.com/aparsons/threadfix_api/blob/master/LICENSE.txt>`_.
