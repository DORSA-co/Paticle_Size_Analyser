MIN_PASS_LENGHT = 1
MIN_USERNAME_LENGHT = 1


#-------------------------------------------------------------------
UNLOGIN_USER_ROLE = 'none'
USER_ROlES = ['admin', 'user']

USER_ROlES_ACCESS = {
    'admin': ['admin', 'user'],
    'user': ['user'],
    UNLOGIN_USER_ROLE: ['user'],
}

ACCESS = {
    'admin': {
        'pages': 'all',
        'tabs': 'all',
    },

    'user':{
        'pages': 'all',
        'tabs': ['grading_setting', 'register_user', 'edit_user' ],
    },

    UNLOGIN_USER_ROLE:{
        'pages' : ['user', 'help'],
        'tabs': ['register_user'],
    },
}



#-------------------------------------------------------------------