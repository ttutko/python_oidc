===========
python_oidc
===========


Add a short description here!


Description
===========

A longer description of your project goes here...


Note
====

This project has been set up using PyScaffold 3.2.3. For details and usage
information on PyScaffold see https://pyscaffold.org/.


Setup Commands
===============

.. code-block::

    docker run --name keycloak -e KEYCLOAK_USER=admin -e KEYCLOAK_PASSWORD=admin -p 8180:8080 -p 8181:8443 -d -v "/home/ttutko/Downloads/localhost.crt:/etc/x509/https/localhost.crt" -v "/home/ttutko/Downloads/localhost.key:/etc/x509/https/localhost.key" jboss/keycloak

.. code-block::

    step certificate create localhost localhost.crt localhost.key --profile self-signed --subtle
