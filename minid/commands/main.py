"""
Copyright 2016 University of Chicago, University of Southern California

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

   http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.
"""
import logging

from minid.commands.cli import cli, execute_command
# Importing the commands loads them into argparse.
from minid.commands import auth, minid_ops, misc  # noqa

log = logging.getLogger(__name__)


def main():
    logger = logging.getLogger('minid')
    logger.addHandler(logging.StreamHandler())
    logger.setLevel(logging.INFO)

    args = cli.parse_args()
    execute_command(cli, args, logger)
