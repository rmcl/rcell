#!/usr/bin/env python
import os
import sys
import env

if __name__ == "__main__":
    from django.core.management import execute_from_command_line
    
    env.setup_environ(__file__)
    execute_from_command_line(sys.argv)
