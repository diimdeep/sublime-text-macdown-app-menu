import os
import sys
import subprocess
import sublime_plugin


class MacdownCommand(sublime_plugin.WindowCommand):
    def run(self):
        filename = self.window.active_view().file_name()
        if filename is None:
            return

        proc_env = os.environ.copy()
        encoding = sys.getfilesystemencoding()
        for k, v in proc_env.items():
            proc_env[k] = os.path.expandvars(v).encode(encoding)

        for app in ('Macdown', 'MacDown'):
            try:
                subprocess.check_call(
                    ['open', '-a', app, filename],
                    env=proc_env
                )
                break
            except subprocess.CalledProcessError:
                pass

    def is_enabled(self):
        return True