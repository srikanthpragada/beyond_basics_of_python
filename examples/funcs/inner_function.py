def log(message, target='screen'):
    def log_to_screen(message):
        print('logging to screen')

    def log_to_file(message):
        print('logging to file')

    if target == 'screen':
        log_to_screen(message)
    else:
        log_to_file(message)

log('Testing')
log('Testing','file')