# -*- encoding: utf-8 -*-

from __future__ import unicode_literals, division, print_function,\
     absolute_import
from nizkctf.settings import Settings
from nizkctf.subrepo import SubRepo
from nizkctf.repohost import RepoHost
from nizkctf.proposal import consider_proposal
from nizkctf.six import to_bytes

from flask import abort

import os
import json
import base64
import tempfile
import traceback


def handle(request):
    merge_info = request.get_json()

    if not merge_info:
        # Message not of our interest (e.g. merge request closed)
        return abort(400)

    try:
        return run(merge_info)
    except Exception as e:
        print(e)
        print(traceback.format_exc())
        # Send tracking number to the user
        return send_cloudwatch_info(merge_info, e, request)


def run(merge_info):
    SubRepo.set_clone_into(tempfile.mkdtemp())

    # Prepare git and ssh for usage inside the container
    setup_environment()

    # Merge proposal if changes are valid
    consider_proposal(merge_info)

    return 'Great!'


def send_cloudwatch_info(merge_info, exception, request):
    proj = Settings.submissions_project
    mr_id = merge_info['mr_id']

    comment = 'Sorry. A failure has occurred when processing your proposal.\n' \
              '**Reason**: %s\n\n' \
              'Please contact support and present the following info:\n' \
              '**Request ID**: %s\n' % \
              (str(exception), request.headers.get('Function-Execution-Id'))

    repohost = RepoHost.instance()
    repohost.mr_comment(proj, mr_id, comment)
    repohost.mr_close(proj, mr_id)

    return comment


def setup_environment():
    root = os.path.dirname(os.path.realpath(__file__))
    ssh_dir = tempfile.mkdtemp()

    ssh_identity = os.path.join(ssh_dir, 'identity')
    with os.fdopen(os.open(ssh_identity, os.O_WRONLY | os.O_CREAT, 0o600), 'w') as f:
        f.write(base64.b64decode(os.getenv('SSH_IDENTITY')).decode('utf-8'))

    ssh_config = os.path.join(ssh_dir, 'config')
    with open(ssh_config, 'w') as f:
        f.write('CheckHostIP no\n'
                'StrictHostKeyChecking yes\n'
                'IdentityFile %s\n'
                'UserKnownHostsFile %s\n' %
                (ssh_identity, os.path.join(root, 'known_hosts')))

    os.environ['GIT_SSH_COMMAND'] = 'ssh -F %s' % ssh_config
