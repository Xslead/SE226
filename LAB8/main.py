class ArchiveItem:
    def __init__(self, title, uid, year):
        self.title = title
        self.uid = uid
        self.year = year

    def __str__(self):
        return f"{self.title} by {self.uid} ({self.year})"
    
    def __eq__(self, value):
        if isinstance(value, ArchiveItem):
            return self.uid == value.uid
        return False
    
    def is_recent(self,n):
        current_year = 2025
        return current_year - self.year <= n
    
class Book(ArchiveItem):
    def __init__(self, title, uid, year, author,pages):
        super().__init__(title, uid, year)
        self.author = author
        self.pages = pages

    def __str__(self):
        return f" {self.uid} {self.title} by {self.author} ({self.year} {self.pages} pages)"
    
class Article(ArchiveItem):
    def __init__(self, title, uid, year, journal, doi):
        super().__init__(title, uid, year)
        self.journal = journal
        self.doi = doi

    def __str__(self):
        return f" {self.uid} {self.title} in {self.journal} (Doi {self.doi}, {self.year})"
    
class Podcast(ArchiveItem):
    def __init__(self, title, uid, year, host, duration):
        super().__init__(title, uid, year)
        self.host = host
        self.duration = duration

    def __str__(self):
        return f" {self.uid} {self.title} by {self.host} ({self.year}, {self.duration} minutes)"
    
def save_to_file(items, filename):
    with open(filename, 'w') as file:
        for item in items:
            if item.__class__.__name__ == "Book":
                file.write(f"Book,{item.uid},{item.title},{item.year},{item.author},{item.pages}\n")
            elif item.__class__.__name__ == "Article":
                file.write(f"Article,{item.uid},{item.title},{item.year},{item.journal},{item.doi}\n")
            elif item.__class__.__name__ == "Podcast":
                file.write(f"Podcast,{item.uid},{item.title},{item.year},{item.host},{item.duration}\n")

def load_from_file(filename):
    items = []
    with open(filename, 'r') as file:
        lines = file.readlines()
        for line in lines:
            parts = line.strip().split(',')
            if len(parts) >= 5:
                item_type, uid, title, year, *extra = parts
                if item_type == 'Book':
                    author, pages = extra
                    items.append(Book(title, uid, int(year), author, int(pages)))
                elif item_type == 'Article':
                    journal, doi = extra
                    items.append(Article(title, uid, int(year), journal, doi))
                elif item_type == 'Podcast':
                    host, duration = extra
                    items.append(Podcast(title, uid, int(year), host, int(duration)))
    return items

def main():
    archive_items = [
        Book("B009", "Deep Learning", 2018, "Ian Goodfellow", 775),
        Book("B102", "Python Programming", 2021, "John Smith", 450),
        Article("A101", "Quantum Computing", 2022, "Nature", "10.1235/qc567"),
        Article("A102", "Machine Learning Advances", 2020, "Science", "10.1234/ml789"),
        Podcast("P301", "TechTalk AI", 2023, "Jane Doe", 45),
        Podcast("P302", "Programming 101", 2024, "Bob Johnson", 60)
    ]

    save_to_file(archive_items, "archive.txt")

    loaded_items = load_from_file("archive.txt")

    print("All Archive Items:")
    for item in loaded_items:
        print(item)

    print("\nRecent Items (last 5 years):")
    for item in loaded_items:
        if item.is_recent(5):
            print(item)

    print("\nArticles with DOI starting '10.1234':")
    for item in loaded_items:
        if item.__class__.__name__ == "Article" and item.doi.startswith("10.1234"):
            print(item)


if __name__ == '__main__':
    main()