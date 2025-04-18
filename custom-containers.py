class TagCloud:
    def __init__(self):
        self.__tags = {}

    def add(self, tag):
        self.__tags[tag.lower()] = self.__tags.get(tag.lower(), 0) + 1

    # to support indexing - cloud["python"]
    def __getitem__(self, tag):
        return self.__tags.get(tag.lower(), 0)
    
    # to support set value by indexing - cloud["python"] = 5
    def __setitem__(self, tag, count):
        self.__tags[tag.lower()] = count

    # to support len - len(cloud)
    def __len__(self):
        return len(self.__tags)
    
    # to support iteration - for tag in cloud
    def __iter__(self):
        return iter(self.__tags)

cloud = TagCloud()
cloud.add("python")
cloud.add("Python")
cloud.add("python")
# print(cloud.__tags)

print(cloud["python"])

cloud["python"] = 5
# print(cloud.__tags)

cloud.add("javascript")
print(len(cloud))

for tag in cloud:
    print(tag, cloud[tag])
