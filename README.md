# schedule

```
from simple_schedule import Schedule

s = Schedule()


while True:

    if s.run_action('5_s'):
        print('5 seconds ran!')
    if s.run_action('10_s'):
        print('10 seconds ran')
```