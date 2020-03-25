import simple_schedule

s = Schedule()

counter = 0
while True:
    # print(counter)
    counter += 1
    if s.run_action('5_s'):
        print('5 seconds ran!')
    if s.run_action('10_s'):
        print('10 seconds ran')

