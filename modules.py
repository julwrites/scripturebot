# coding=utf-8

# Local modules
from .bible import bible_actions, bible_hooks
from .tms import tms_actions, tms_hooks
from .common.admin import admin_actions
from .user import user_actions
from .dailydevo import dailydevo_actions, dailydevo_hooks
from .subscribe import subscribe_actions


def get_actions():
    return  admin_actions.get() + \
            tms_actions.get() + \
            user_actions.get() + \
            dailydevo_actions.get() + \
            subscribe_actions.get() + \
            bible_actions.get()


def get_hooks():
    return tms_hooks.get() + \
            bible_hooks.get() + \
            dailydevo_hooks.get()
