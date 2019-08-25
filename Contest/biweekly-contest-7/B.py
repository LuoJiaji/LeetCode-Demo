class FileSystem(object):

    def __init__(self):

        self.file_sys = {}
        

    def create(self, path, value):
        """
        :type path: str
        :type value: int
        :rtype: bool
        """

        if path in self.file_sys:
            return  False

        i = 1
        while i < len(path):
            if path[i] == '/' and path[:i] not in self.file_sys:
                # print(path[:i])
                return False
            i += 1
            

        if not path in self.file_sys:
            self.file_sys[path] = value 
            return True

        

    def get(self, path):
        """
        :type path: str
        :rtype: int
        """
        if path in self.file_sys:
            return self.file_sys[path]
        else:
            return -1

fileSystem = FileSystem()
print(fileSystem.create("/a", 1))
print(fileSystem.get("/a"))
# print(fileSystem.file_sys)

fileSystem = FileSystem()
print(fileSystem.create("/leet", 1))
print(fileSystem.create("/leet/code", 2))
print(fileSystem.get("/leet/code"))
print(fileSystem.create("/c/d", 1))
print(fileSystem.get("/c"))

