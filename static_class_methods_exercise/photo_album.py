class PhotoAlbum:
    MAX_PHOTOS_PER_PAGE = 4
    def __init__(self, pages):
        self.pages = pages
        self.photos = self.__init_photos(pages)


    def __init_photos(self, pages):
        result = []
        for _ in range(pages):
            result.append([])
        return result

    @classmethod
    def from_photos_count(cls, photos_count):
        pages_needed = photos_count //PhotoAlbum.MAX_PHOTOS_PER_PAGE
        if photos_count % PhotoAlbum.MAX_PHOTOS_PER_PAGE !=0:
            pages_needed +=1
        return cls(pages_needed)

    def add_photo(self, label):
        for row in range(self.pages):
            if len(self.photos[row]) == PhotoAlbum.MAX_PHOTOS_PER_PAGE:
                continue
            self.photos[row].append(label)
            return f"{label} photo added successfully on page {row + 1} slot {len(self.photos[row])}"
        return "No more free slots"

    def display(self):
        rows = [" ".join(["[]" for x in range(len(self.photos[row]))]) for row in range(len(self.photos))]
        res = '-----------\n' + '\n-----------\n'.join(rows) + '\n-----------'
        return res



album = PhotoAlbum(2)

print(album.add_photo("baby"))
print(album.add_photo("first grade"))
print(album.add_photo("eight grade"))
print(album.add_photo("party with friends"))
print(album.photos)
print(album.add_photo("prom"))
print(album.add_photo("wedding"))

print(album.display())
