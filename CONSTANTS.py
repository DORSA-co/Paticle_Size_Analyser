MIN_PASS_LENGHT = 1
MIN_USERNAME_LENGHT = 1


#-------------------------------------------------------------------
USER_ROlES = ['admin', 'user']
USER_ROlES_ACCESS = {
    'admin': ['admin', 'user'],
    'user': ['user'],
    'none': ['user'],
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

    'none':{
        'pages' : ['user', 'help'],
        'tabs': ['register_user'],
    },
}



#-------------------------------------------------------------------