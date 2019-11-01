import os
from shutil import copyfile


class CalibreUtils:
    CALIBRE_PATH = 'C:\\PROGRA~2\\Calibre2'

    def __init__(self, calibre_app_path=''):
        if calibre_app_path:
            CalibreUtils.CALIBRE_PATH = calibre_app_path

    @staticmethod
    def add_cover(cover_path, final_path):
        if os.path.isfile(cover_path):
            if os.path.exists(final_path):
                final_name = final_path + '\\' + 'cover.jpg'
                copyfile(cover_path, final_name)

    @staticmethod
    def generate_out_put_file_and_dir(input_file_name):
        if input_file_name:
            file_path = os.path.dirname(input_file_name)
            file_name = os.path.basename(input_file_name)[:-4]
            azw3_folder = os.path.join(file_path, file_name)
            output_file_name = os.path.join(azw3_folder, file_name + 'azw3')
            if not os.path.exists(azw3_folder):
                os.makedirs(azw3_folder)
            return azw3_folder, output_file_name

    def convert_book_to_azw3(self, input_file, cover_path):
        if os.path.exists(input_file):
            try:
                azw3_folder, output_file_name = self.generate_out_put_file_and_dir(input_file)
                calibre_path = '{0}\\ebook-convert.exe {1} {2}'.format(CalibreUtils.CALIBRE_PATH, input_file,
                                                                       output_file_name)
                self.add_cover(cover_path, azw3_folder)
                os.system(calibre_path)
            except Exception as e:
                print(e)
