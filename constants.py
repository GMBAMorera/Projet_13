### DATABASE CONSTANTS ###

STATUS_DICT = {
    'Cu': 'customer',
    'Co': 'company',
    'Em': 'employee',
    'Ad': 'admin'
}
STATUS_CHOICE = [ (status, STATUS_DICT[status]) for status in STATUS_DICT]

ORDER_STATUS = [
    ('co', 'conception'),
    ('va', 'validation'),
    ('pr', 'production'),
    ('li', 'livraison'),
    ('ar', 'archivée')
]

HOME_COMPANY = 'homeco'