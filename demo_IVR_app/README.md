demo IVR app
=====================

This is a heroku hostable application.

Hosting on Heroku Tutorial
~~~~~~~~~~~~~~~~~~~~~~~~~~~~
`https://devcenter.heroku.com/articles/python`
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Using this app for IVR testing:


let say heroku app link :`<heroku_app>`

Use folowing xml in answer_url:
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
<Response>
  <Speak> Hi , welcome To Plivo. Please Press a digit to test the get digit application </Speak>Speak>
    <GetDigits action="<heroku_app>/getdigits" method="POST">
      </heroku_app>GetDigits>
      </GetDigits>Response>
      ~~~~~~~~~~~~~~~~~~~~~~~~~~~

method can be both `GET` and `POST`
