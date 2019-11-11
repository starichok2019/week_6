from filemanager import author_info, filenames
import os


def test_author_info():
    assert author_info() == 'Boris Shustrov'


def test_filenames():
    for item in filenames():
        assert not os.path.isdir(item)
        assert os.path.exists(item)
        assert os.path.isfile(item)
        assert item in filenames()
        assert os.path.exists(item) and os.path.isfile(item) and item in filenames() and not os.path.isdir(item)
    assert filenames() == [i for i in filenames() if os.path.isfile(i) and os.path.exists(i) and not os.path.isdir(i)]


