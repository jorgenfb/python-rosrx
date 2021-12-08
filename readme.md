# ROS rx

Helpers used to convert to/from ROS topics and observables.

## Helpers

### Subscribe to a topic as an observable
The method `observabletopic()` supports the same signature as `rospy.Subscriber`.

Example:

```
from rosrx import observabletopic
from std_msgs.msg import String

source = observabletopic('/chatter', String)

source.subscribe(lambda msg: rospy.loginfo(msg.data))
```

### Publish observable values to a topic

```
from rosrx import TopicObserver
from std_msgs.msg import String

from rx import interval
from rx.operators import map

source = interval(1.0)
source.pipe(map(lambda value: 'hello world {}'.format(value))).subscribe(
            observer=TopicObserver('/chatter', String, queue_size=1))
```

## Development

### Publish new version

```
# Create a source archive in dist/
python setup.py sdist bdist_wheel

# Upload to pypi
twine upload dist/*
```

