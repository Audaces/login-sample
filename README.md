# Login with AudacesID

This project has a very simple example that shows how to authenticate a user and obtain an access token, that can be used to consume a couple of different APIs from Audaces.

Our Identity Server is an implementation of OpenID Connect (https://openid.net/specs/openid-connect-core-1_0.html#Authentication).

In order to make use of the login system, you first need to register your application within our Identity Server. Once you have done that, you will receive a `client_id` and we'll also setup an authetication endpoint, that must be a valid endpoint in your application (this endpoint is where you will get an access token in response to a successful authentication).

The current example illustrates the **implicit flow**, and you can learn more about it by reading the OpenID Connect documentation.

#### URL

Authentication URL: `https://login.audaces.com/core/connect/authorize`

#### Lauching the Example

This sample code is written in Python and requires the **Bottle** library.

Install it by calling: `pip install bottle` or `pip install -r requirements.txt`

After the install is complete, you may run the application by typing: `python app.py`

