class PhotoAlbum:
    def __init__(self, pages: int):
        self.pages = pages
        self.photos = [[] for _ in range(pages)]

    @classmethod
    def from_photos_count(cls, photos_count: int):
        if photos_count > 0:
            total_pages = 1
        else:
            total_pages = 0
        phts_tmp_cnt = 0
        photos_left = photos_count
        while photos_left > 0:
            if phts_tmp_cnt < 4:
                phts_tmp_cnt += 1
                photos_left -= 1
            elif phts_tmp_cnt == 4:
                total_pages += 1
                phts_tmp_cnt = 1
                photos_left -= 1
        return cls(total_pages)

    def add_photo(self, label: str):
        if len(self.photos) == self.pages and len(self.photos[-1]) == 4:
            return f"No more free slots"
        RO, cmxpr, cp = True, 0, 1
        while RO:
            if len(self.photos[cmxpr]) < 4:
                self.photos[cmxpr].append(label)
                RO = False
                return (f"{label} photo added successfully on page "
                        f"{cp} on slot {len(self.photos[cmxpr])}")
            else:
                cmxpr += 1
                cp += 1

    def display(self):
        to_display = ['-----------']
        for page_number, page in enumerate(self.photos, start=1):
            if not page:
                to_display.append('')
                to_display.append('-----------')
            else:
                photos_on_page = ' '.join('[]' for _ in page)
                to_display.append(f"{photos_on_page}")
                to_display.append('-----------')
        return '\n'.join(to_display)


''' test code'''
# album = PhotoAlbum(2)
#
# print(album.add_photo("baby"))
# print(album.add_photo("first grade"))
# print(album.add_photo("eight grade"))
# print(album.add_photo("party with friends"))
# print(album.photos)
# print(album.add_photo("prom"))
# print(album.add_photo("wedding"))
#
# print(album.display())


""" unittest"""
# import unittest
#
#
# class TestsPhotoAlbum(unittest.TestCase):
#     def test_init_creates_all_attributes(self):
#         album = PhotoAlbum(2)
#         self.assertEqual(album.pages, 2)
#         self.assertEqual(album.photos, [[], []])
#
#     def test_from_photos_should_create_instace(self):
#         album = PhotoAlbum.from_photos_count(12)
#         self.assertEqual(album.pages, 3)
#         self.assertEqual(album.photos, [[], [], []])
#
#     def test_add_photo_with_no_free_spots(self):
#         album = PhotoAlbum(1)
#         album.add_photo("baby")
#         album.add_photo("first grade")
#         album.add_photo("eight grade")
#         album.add_photo("party with friends")
#         result = album.add_photo("prom")
#         self.assertEqual(result, "No more free slots")
#
#     def test_add_photo_with_free_spots(self):
#         album = PhotoAlbum(1)
#         album.add_photo("baby")
#         album.add_photo("first grade")
#         album.add_photo("eight grade")
#         album.add_photo("party with friends")
#         self.assertEqual(album.photos, [['baby', 'first grade', 'eight grade', 'party with friends']])
#
#     def test_display_with_one_page(self):
#         album = PhotoAlbum(1)
#         album.add_photo("baby")
#         album.add_photo("first grade")
#         album.add_photo("eight grade")
#         album.add_photo("party with friends")
#         result = album.display().strip()
#         self.assertEqual(result, "-----------\n[] [] [] []\n-----------")
#
#     def test_display_with_three_pages(self):
#         album = PhotoAlbum(3)
#         for _ in range(8):
#             album.add_photo("asdf")
#         result = album.display().strip()
#         self.assertEqual(result, "-----------\n[] [] [] []\n-----------\n[] [] [] []\n-----------\n\n-----------")
#
#
# if __name__ == "__main__":
#     unittest.main()