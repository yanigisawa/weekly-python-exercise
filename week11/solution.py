import os
import hashlib


class FileInfo:
    def __init__(self, filename, modifiedTime, sha1):
        self.filename = filename
        self.sha1 = sha1
        self.mtime = modifiedTime

    def __eq__(self, other):
        return self.filename == other.filename

    def __repr__(self):
        return f"FileInfo for {self.filename}, mtime {self.mtime}, sha1 {self.sha1}"

class FileList:
    def __init__(self, pathname):
        self.pathname = pathname
        self._all_files = self.scan()

    @property
    def all_file_infos(self):
        return self._all_files

    def scan(self):
        dir_files = []
        for root, _, files in os.walk(self.pathname, topdown=False):
            for name in files:
                full_path = os.path.join(root, name)

                file_info = FileInfo(
                    full_path,
                    os.stat(full_path).st_mtime,
                    hashlib.sha1(open(full_path, 'rb').read()).hexdigest()
                )
                dir_files.append(file_info)
        return dir_files


    def rescan(self):
        new_scan = self.scan()
        removed = []
        changed = []
        for f in self._all_files:
            if f not in new_scan:
                removed.append(f.filename)
            tmp = [nf for nf in new_scan if nf == f]
            if len(tmp) and tmp[0].sha1 != f.sha1:
                changed.append(f.filename)
        added = []
        for f in new_scan:
            if f not in self._all_files:
                added.append(f.filename)

        return {
            "added": added,
            "changed": changed,
            "removed": removed,
            "unchanged": [f.filename for f in self._all_files]
        }
