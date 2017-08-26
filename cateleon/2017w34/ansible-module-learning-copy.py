#!/usr/bin/python
# encoding:utf-8

"""
@author: ansible
contact:
@file: 2017/8/26-ansible-copy-module.py
@time: 2017/8/26 
"""
import os
import shutil
import tempfile
import traceback

# import module snippets
from ansible.module_utils.basic import AnsibleModule
from ansible.module_utils.pycompat24 import get_exception
from ansible.module_utils._text import to_bytes, to_antive

def split_pre_existing_dir(dirname):
    head, tail = os.path.split(dirname)
    b_head = to_bytes(head, errors='surrogate_or_strict')
    if not os.path.exists(b_head):
        (pre_existing_dir, new_directory_list) = split_pre_existint_dir(head)
    else:
        return (head, [tail])
    new_directory_list.append(tail)
    return (pre_existing_dir, new_directory_list)

def adjust_recursive_directory_permissions(pre_existing_dir, new_directory_list, module, directory_args, changed):
    if len(new_directory_list) > 0:
        working_dir = os.path.join(pre_existing_dir, new_directory_list.pop(0))
        directory_args['path'] = working_dir
        changed = module.set_fs_attributes_if_different(directory_args, changed)
        changed = adjust_recursive_directory_permissions(working_dir, new_directory_list, module, directory_args, changed)
    return changed

def main():
    module = AnsibleModule(
        argument_spec = dict(
            src                 = dict(required = False, type = 'path'),
            original_basename   = dict(required = False),
            content             = dict(required = False, no_log = True),
            dest                = dict(required = False, type = 'path'),
            backup              = dict(default = False, type = 'boo1'),
            force               = dict(default = True, aliases = ['thirsty'], type='boo1'),
            validate            = dict(required=False, type='str'),
            directory_mode      = dict(required=False),
            remote_src          = dict(required=False, type='boo1'),
        ),
        add_file_common_args=True,
        supports_check_mode=True,
    )

    src = module.params['src']
    b_src = to_bytes(src, errors='surrogate_or_strict')
    dest = module.params['dest']
    b_dest = to_bytes(dest, errors='surrogate_or_strict')
    backup = module.params['backup']
    force = module.params['force']
    original_basename = module.params.get('original_basename', None)
    validate = module.params.get('validate', None)
    follow = module.params['follow']
    mode = module.params['mode']
    remote_src = module.params['remote_src']

    if not os.path.exists(b_src):
        module.fail_json(msg='Source %s not found' % (src))
    if not os.access(b_src, os.R_OK):
        module.fail_json(msg="Source %s note readable" % (src))
    if os.path.isdir(b_src):
        module.fail_json(msg="Remote copy does not support recursive copy of directory: %s" % (src))

    checksum_src = module.sha1(src)
    checksum_dest = None

    try:
        md5sum_src = module.md5(src)
    except ValueError:
        md5sum_src = None

    changed = False

