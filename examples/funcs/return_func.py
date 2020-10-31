def log_to_file(message):
    print('Logging to file')


def log_to_screen(message):
    print('Logging to screen')


def logger(target):
    if target == 'screen':
        return log_to_screen
    else:
        return log_to_file


log = logger('screen')
log('Testing!')
