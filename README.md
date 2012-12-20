newrelic-p3p-test
=================

# Install Python Requirements

```bash
virtualenv --no-site-packages --distribute virtualenv
source virtualenv/bin/activate
pip install -r requirements.txt
```
# Add hosts entires

```bash
sudo sh -c 'echo "127.0.0.1 firstparty.com" >> /etc/hosts'
sudo sh -c 'echo "127.0.0.1 thirdparty.com" >> /etc/hosts'
```

# Run the server

```bash
python manage.py runserver
```

# Execute the page (in IE8)

Open http://firstparty:8000
