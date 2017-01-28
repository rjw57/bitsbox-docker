#!/usr/bin/env python3
"""
Generate secrets used for deployment

Usage:
    gen_secrets.py [--nginx-user=USERNAME] [--force]

Options:
    --nginx-user, -u USERNAME   Specify username for htpasswd file
                                [default: bitsbox]
    --force                     Overwrite existing files

"""
import base64
import os
import textwrap

import docopt
import htpasswd

def main():
    opts = docopt.docopt(__doc__)
    this_dir = os.path.dirname(os.path.abspath(__file__))
    print('Working directory: {}'.format(this_dir))

    secrets_pn = os.path.join(this_dir, 'secrets-env')
    htpasswd_pn = os.path.join(this_dir, 'nginx', 'htpasswd')

    have_secrets = os.path.exists(secrets_pn)
    if have_secrets and opts['--force']:
        print('Overwriting {} since --force specified'.format(secrets_pn))
        have_secrets = False
    if have_secrets:
        print('Not overwriting existing file: {}'.format(secrets_pn))
    else:
        gen_secrets(secrets_pn)

    have_htpasswd = os.path.exists(htpasswd_pn)
    if have_htpasswd and opts['--force']:
        print('Overwriting {} since --force specified'.format(htpasswd_pn))
        have_htpasswd = False
    if have_htpasswd:
        print('Not overwriting existing file: {}'.format(htpasswd_pn))
    else:
        gen_htpasswd(htpasswd_pn, opts['--nginx-user'])

def _gen_token(entropy):
    token_bytes = os.urandom(entropy)
    return base64.urlsafe_b64encode(token_bytes).rstrip(b'=').decode('ascii')

def gen_secrets(pn):
    secret_key = _gen_token(64)
    db_pass = _gen_token(32)
    postgres_pass = _gen_token(32)

    print('Writing secrets to {}'.format(pn))
    with open(pn, 'w') as fobj:
        fobj.write(textwrap.dedent('''
        DB_PASS={db_pass}
        POSTGRES_PASSWORD={postgres_pass}
        SECRET_KEY={secret_key}
        ''').lstrip().format(
            db_pass=db_pass, secret_key=secret_key, postgres_pass=postgres_pass))

def gen_htpasswd(pn, user):
    passwd = _gen_token(8)
    print('Writing user to {}'.format(pn))
    if not os.path.exists(pn):
        with open(pn, 'w'):
            pass

    with htpasswd.Basic(pn) as passdb:
        try:
            passdb.add(user, passwd)
        except htpasswd.basic.UserExists:
            print('WARNING: changing existing password')
            passdb.change_password(user, passwd)
    print('Password for user {} is "{}"'.format(user, passwd))

if __name__ == '__main__':
    main()
