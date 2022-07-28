

# Base Django Settings
secret_key='make a nice key'
allowed_hosts = [
    'api.screamfreely.org',
    'localhost',
    '0.0.0.0',
]

root_urlconf = 'server.urls'
wsgi_application = 'server.wsgi.application'

#Database Info
#dbname='mnapi'
dbname='postgres'
dbuser='postgres'
dbpasswd='postgres'

# Social Media Keys

fb_token="EAAShqFyQGf4BAED7B5OYAX31HzDUy0196BPvsOXo0NjeqOZCMaZBvZCnaZBbNhrC0LMojw5E8gqZANlcpU4YzOyB6JMZCYCEKZClVmOEorqmZCSZAmVGJIcOLkpAZCSsyvQVWFFWCI0J4HybZAaAZBSVg8BtSKKuGG3qZBBWZC5ZB6RUUYi04cF79OPThoLeQcumk5RNrgZD"
fb_id="1303644386367998"

#fb_token="EAAShqFyQGf4BADay1SltU6Nrgnr4JDYUbkBz1PrKdAv742rZCOgcr1LkTYJgHGcUiMo3pHYKi1pAKjlOPd1DamgF5NmrO8TfdrJSOPTwttfdeZBv5gnplrZBWKSNTVplJ5NKWWI4sEVHZCqzJdjQpnxG8FEWtPSeWFENlN5WAwZDZD"
#fb_id="643301685878275"

tw_ckey = '25Y0isr55G0u5ftSjoYXZEN6A'
tw_csecret = 'd8RhbWrajjE3IMv2EpwrmBMMXhMzVVnpfBScQNKDNDl0UuoJWl'
tw_tkey = '217566873-wq4li1pmDIaTPfUjOrxyQwYJfEZ9B32joCfJX0pO'
tw_tsecret = 'jjsH5op34Yw1LEIKnyfSGapw4jhwAjoYZkbmYQLvdzIPh'
