MIN_PASS_LENGHT = 1
MIN_USERNAME_LENGHT = 1
#-------------------------------------------------------------------
DECIMAL_ROUND = 2
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
        'pages' : [ 'help'],
        'tabs': [],
    },
}



#-------------------------------------------------------------------
NAME_CODE_CHAR = '%'
NAME_CODE_SPACER = '_'
NAME_CODES = {
            'spacer':   '_',
            'year':     '%YEAR%',
            'month':    '%MONTH%',
            'day':      '%DAY%',
            'hour':    '%HOUR%',
            'minute':   '%MINUTE%',
            'standard': '%STANDARD%',
            'username': '%USERNAME%',
            'text1':    '%TEXT1%'

        }



#---------------------------------------------------------
SIDEBAR_MAX_WIDTH = 16772
SIDEBAR_MIN_WIDTH = 180
HIDE_SIDEBAR_PAGES = [
            'report', 
            'compare'
        ]



class IMAGES:
    STOP_SAMPLING = 'uiFiles\Assets\images\camera-finish.png'
    NO_IMAGE = 'uiFiles\Assets\images\\camera-error.png'