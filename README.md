# ThreadFix API

A Python API wrapper to facilitate interactions to and from [ThreadFix](https://github.com/denimgroup/threadfix).

## Quick Start

Several quick start options are available:

- [Download the latest release](https://github.com/aparsons/threadfix_api/releases/latest)
- Clone the repository: `git clone https://github.com/aparsons/threadfix_api.git`
- Install with pip (recommended): `pip install threadfix_api`

## How to Use

### Example

```python
# import the package
from threadfix_api import threadfix

# setup threadfix connection information
host = 'http://localhost:8080/threadfix/'
api_key = 'YourRandomAPIKeyFromThreadFix'

# instantiate this threadfix api wrapper
tf = threadfix.ThreadFixAPI(host, api_key)

# rock and roll
teams = tf.list_teams()
if teams.success:
  print(teams.data)
```

### Documentation

**Before you start**, its important to understand that all responses to api calls (even when errors occur) are wrapped in a response object. This object mimics the behavior of the ThreadFix API and allows you to simply check if the API call was successful and get the response message. Here is a simple example demonstrating this functionality.

```python
from threadfix_api import threadfix

tf = threadfix.ThreadFixAPI(host, api_key)

teams = tf.list_teams()

if teams.success:  # Was the request a success?
  # Everything worked fine, lets view the response data
  print(teams.data)
else:
  # Print the reason why the request was not a success
  print(teams.message)
```

If you are using a **self-signed certificate**, you can disable certificate verification when you instantiate the API wrapper. If disabled, API requests could be intercepted by third-parties -- use with caution.

```python
from threadfix_api import threadfix

tf = threadfix.ThreadFixAPI(host, api_key, verify_ssl=False)
```

#### Teams

##### List Teams: `list_teams`

Retrieves all the teams.

###### Parameters

_None_

###### Example 

```python
tf = threadfix.ThreadFixAPI(host, api_key)
response = tf.list_teams()
```

##### Create Team: `create_team`

Creates a team with the given name.

###### Parameters

| Parameter  | Required | Default | Description |
| ---------- | -------- | ------- | ----------- |
| name       | **Yes**  | N/A     | The name of the new team that is being created. |

###### Example 

```python
tf = threadfix.ThreadFixAPI(host, api_key)
response = tf.create_team('Example Team')
```

##### Get Team
##### Get Team By Name

#### Applications

##### Create Application
##### Get Application
##### Set Application Parameters
##### Set Application URL
##### Set Application WAF

#### Findings

##### Create Manual Finding
##### Create Static Finding
##### Upload Scan

#### WAFs

##### List WAFs
##### Create WAF
##### Get WAF
##### Get WAF Rules
##### Get WAF Rules By Application
##### Upload WAF Log

#### Vulnerabilities

##### Get Vulnerabilities

## Bugs and Feature Requests

Have a bug or a feature request? Please first search for existing and closed issues. If your problem or idea is not addressed yet, [please open a new issue](https://github.com/aparsons/threadfix_api/issues/new).

## Copyright and License

- Copyright 2015 [Adam Parsons](https://github.com/aparsons)
- [Licensed under MIT](https://github.com/aparsons/bootstrap-alignment/blob/master/README.md).
