from kombu import Queue

broker_url = 'pyamqp://guest@localhost//'

task_queues = (
    Queue('default', routing_key='default'),
    Queue('high_priority', routing_key='high.priority'),
)

task_default_queue = 'default'
task_default_routing_key = 'default'

task_routes = {
    'tasks.add': {'queue': 'high_priority'},
}
