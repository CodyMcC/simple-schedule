# schedule

```python
from simple_schedule import Schedule

s = Schedule()


while True:

    if s.run_action('5_s'):
        print('This runs every 5 seconds')
    if s.run_action('10_s'):
        print('This runs every 10 seconds')
    if s.run_action('1_m'):
        print('This runs every 1 minutes')
```
