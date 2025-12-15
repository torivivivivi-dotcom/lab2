import urllib.request

class MyFile:
    def init(self, path_or_url, mode):
        self.path_or_url = path_or_url
        self.mode = mode
        self.content = None

    def read(self):
        if self.mode == "read":
            with open(self.path_or_url, 'r', encoding="utf-8") as f:
                return f.read()
        else:
            raise ValueError("Для чтения файла должен быть режим 'read'")

    def write(self, text):
        if self.mode == "write":
            with open(self.path_or_url, 'w', encoding="utf-8") as f:
                f.write(text)
        elif self.mode == "append":
            with open(self.path_or_url, 'a', encoding="utf-8") as f:
                f.write(text)
        else:
            raise ValueError("Режим должен быть 'write' или 'append'")

    def read_url(self):
        if self.mode == "url":
            with urllib.request.urlopen(self.path_or_url) as response:
                raw_data = response.read()
                self.content = raw_data.decode('utf-8')
                return self.content
        else:
            raise ValueError("Режим должен быть 'url'")

    def count_urls(self):
        if self.mode != "url":
            raise ValueError("Режим должен быть 'url'")

        if self.content is None:
            self.read_url()

        return self.content.count('href=') + self.content.count('src=')

    def write_url(self, filename):
        if self.mode != "url":
            raise ValueError("Режим должен быть 'url'")

        if self.content is None:
            self.read_url()

        with open(filename, 'w', encoding='utf-8') as f:
            f.write(self.content)