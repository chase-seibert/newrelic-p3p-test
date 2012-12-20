newrelic-p3p-test
=================

This is a quick test suite that shows that P3P headers need to be rendered on the New Relic beacon in order to avoid the "evil eye" privacy report in IE7/8.

More on [P3P headers](http://stackoverflow.com/questions/389456/cookie-blocked-not-saved-in-iframe-in-internet-explorer).

# Install Python Requirements

```bash
virtualenv --no-site-packages --distribute virtualenv
source virtualenv/bin/activate
pip install -r requirements.txt
```

# Add hosts entires

If testing on a separate Windows machine, the IP address should be the IP of the server.

```bash
127.0.0.1 firstparty.com
127.0.0.1 d1ros97qkrwjf5.cloudfront.net
127.0.0.1 beacon-4.newrelic.com
```

# Run the server

```bash
sudo python manage.py runserver 0:80
```

# Execute the page (in IE8)

Open http://firstparty.com


You should see the following privacy report icon. Clicking on it will reveal the full report.

![screenshot](https://dl.dropbox.com/u/422013/Screenshots/p_annotated.png "Evil Eye")

You can refresh a few times, and the warning will remain.

# Test w/ P3P headers

Now go into `mysite/views.py` and edit the beacon view, uncommenting the p3p line. If you refresh the IE8 page, it will now not display the warning.

