import os
from distutils.command.install_headers import install_headers


class InstallHeaders(install_headers):
    """
    The built-in install_headers installs all headers in the same directory
    This overrides that to walk a directory tree and copy the tree of headers

    """

    def run(self):
        headers = self.distribution.headers
        if not headers:
            return
        self.mkpath(self.install_dir)
        for header in headers:
            for dirpath, dirnames, filenames in os.walk(header):
                for file in filenames:
                    if file.endswith('.h'):
                        path = os.path.join(dirpath, file)
                        install_target = os.path.join(self.install_dir,
                                                      path.replace(header, ''))
                        self.mkpath(os.path.dirname(install_target))
                        (out, _) = self.copy_file(path, install_target)
                        self.outfiles.append(out)


__all__ = ['InstallHeaders']
