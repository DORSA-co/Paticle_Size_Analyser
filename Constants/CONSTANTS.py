import os


class meta:
    MASTER_PASSWORD = '1111'

class databaseConstant:
    KEY = b'hiyPabX4mQTPQZYW_iSueyTfhFWvf2EO3T_1uCGLTiw='
    META_PATH = 'dbmeta.json'

class screen:
    W = 0
    H = 0

class serialInfo:
    MAX_PORT_COM = 5
    BAUD_RATE = 9600


class Color:
    CHART_TRENDS_COLOR = [

        #dark color
        '#083782',
        '#c44b00',
        '#7a6800',
        '#2b7a00',
        '#31f0a6',
        '#09827e',
        '#50107d',

        #light color
        '#5780c2',
        '#820808',
        '#e0986c',
        '#dec63c',
        '#a9ff7a',
        '#66e8e4',
        '#b968f2',
        '#e673d6',
        

    ]

class Files:
    DEMO_IMGS_DIR = 'files//demo_imgs'
    DEMO_COUNT = os.listdir(DEMO_IMGS_DIR)

class TimeOut:
    TIMEOUT_CHECKING_DEVICE = 3


class CameraParms:
    SYNCHRONIZE = ['software', 'hardware']
    TRIGGER_DELAY = 0


class Calibration:
    PIXEL_SIZE_UM = 3.45
    LENZ_MAG = 0.095
    PX2MM = (3.45 / 1000) / 0.095
    THRESH = 30
    #CALIBRATOR_CIRCLES_COUNT = 32
    ITERATIONS = 20
    
    PARTICLES_DIAMETERS_MM = [
        1,
        1,
        1,
        1,
        2,
        2,
        2,
        2,
        3,
        3,
        4,
        4,
        4,
        5,
        5,
        6,
        6,
        7,
        7,
        8,
        8,
        9,
        10,
        12,
        13,
        14,
        15,
        16,
        18,
        20,
        21,
        25


    ]




MAX_CAMERA_TEMP = 65

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
    NO_IMAGE = 'uiFiles\Assets\images\\camera-error-500.png'