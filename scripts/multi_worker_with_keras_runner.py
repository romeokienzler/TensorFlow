import sys
import os
import threading


node_str = sys.stdin.read().replace("\n","")
nodes = node_str.split(' ')
first = True
node_string = ""
for node in nodes:
    if not first:
        node_string += ','
    node_string += '"' + node + ':12345"'
    first = False

for i, node in enumerate(nodes):
    config = ('TF_CONFIG='+'\'"\'"\'{"cluster": {"worker": ['+node_string+']}, "task": {"index": '+str(i)+', "type": "worker"}}\'"\'"\'')
    print(node)
    command = 'ssh '+node+" 'conda activate wmlce-ea;"+config+";python multi_worker_with_keras_numpyArrays.py'"
    print(command)
    
    def thread_function(command):
        os.system(command)

    thread = threading.Thread(target=thread_function, args=(command,))


    thread.start()
thread.join()

