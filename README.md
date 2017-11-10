# Multithreaded Account Retrieval System

Multithreaded account retrieval system for Zero Hedge.

## About

This program exploits some major deficiencies in the user account protocol of Zero Hedge, a financial news web site, in order to retrieve account information.

Zero Hedge user accounts are given specific identification numbers when they are created. This number system is based on the number of accounts that have been created.

In addition to this, the login form has no form of protection against robots. This allows for retrieval of accounts in order of their creation using a password list.

This program sends login requests to user `0` and increments the user identification number, trying each password in `passwords.txt` as it goes.

Although the Zero Hedge front-end is wanting in some form of protection against robots, their back-end does have a limit for requests per time, probably for protection against denial-of-service attacks.

To combat this, the program includes a mere `pass` statement when it encounters a request limit error, giving enough time for the server to begin accepting new requests. This does have the effect of skipping that particular user and password combination, making the account retrieval imperfect. A function for repeating skipped combinations has yet to be implemented.

## Usage

Change the `passwords.txt` file to the desired configuration, and use:

`python mars.py`
