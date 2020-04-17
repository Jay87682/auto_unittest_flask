#!/usr/bin/env python3
import os, signal, subprocess
import psutil

class ProcessT:
    def __init__(self, proc_arg):
        print(proc_arg)
        self._process = subprocess.Popen(proc_arg['cmd'], shell=True)
        self._name = proc_arg['name']

    def kill(self):
        self._process.kill()

    def name(self):
        return self._name

    def pid(self):
        return self._process.pid

def run_flask_app(proc):
    return ProcessT(proc)

def kill_process_tree(pid):
    try:
        parent = psutil.Process(pid)
        children = parent.children(recursive=True)
        for child in children:
            child.kill()
        gone, still_alive = psutil.wait_procs(children, timeout=5)

        parent.kill()
        parent.wait(5)
    except:
        pass

if __name__ == '__main__':
    commands = [
    {'cmd': "python3 ./web_8888.py",
     'name': "port 8888"},
    {'cmd': "python3 ./web_6666.py",
     'name': "port 6666"
    }]
     
    process_queue = [ run_flask_app(x) for x in commands]
    while True:
        cmd = input('please input command:\n')
        if cmd == 'q':
            for p in process_queue:
                #os.killpg(p.pid(), signal.SIGTERM)
                #os.kill(p.pid(), signal.SIGTERM)
                kill_process_tree(p.pid())
                print(p.name(), ' kill')
            if len(process_queue):
                process_queue.clear()
            break
        elif cmd == 'l':
            #print(process.name for process in process_queue)
            for p in process_queue:
                print(p.name(), p.pid(), os.getpgid(p.pid()))
        elif cmd == 'k':
            for p in process_queue:
                print(p.pid())
                #os.killpg(p.pid(), signal.SIGTERM)
                #os.kill(p.pid(), signal.SIGTERM)
                kill_process_tree(p.pid())
                print(p.name(), ' kill')
            process_queue.clear()
    print('end')
