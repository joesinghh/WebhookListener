# WebhookListener

## A Webhook listener is a server that listens to a specific URL for incoming HTTP *Post* Message.

### Requirements 

User should have `python` installed on their system.

### Installation and working

- Open Project Directory `Server/` which has file named `manage.py`.

- Use the command :
``` pip install -r requirements.txt ``` for installing the required modules.

- Type `python manage.py runserver` to start the server with default port `8000`, to run server with custom post type `python manage.py runserver <port_number> `.
- Example : `python manage.py runserver 80`

Note : `/webhook/call/` is the endpoint for listening and `/admin` is for admin panel. 
