"""
Project 5 - Pixel Magic, Part 2

Name:
Instructor: Mike Ryu
Section: 13
"""

import unittest
from blur_lib import *


class TestCases(unittest.TestCase):

    ### GIVEN UNIT TESTS ###########################################################
    # Run below as-is and DO NOT change them #######################################
    ################################################################################

    def test_process_command_line_arg_1(self):
        self.assertEqual({'file': 'image.ppm', 'row': 100, 'col': 100, 'radius': 30, 'reach': 4},
                         process_command_line_args('image.ppm 100 100 30'.split()))

    def test_process_command_line_arg_2(self):
        self.assertEqual({'file': 'image.ppm', 'row': 100, 'col': 100, 'radius': 30, 'reach': 10},
                         process_command_line_args('image.ppm 100 100 30 10'.split()))

    def test_process_command_line_arg_3(self):
        self.assertIsNone(process_command_line_args('good length but bad data'.split()))


    def test_build_output_file_path_1(self):
        self.assertEqual('image_blurred.ppm', build_output_file_path('image.ppm'))

    def test_build_output_file_path_2(self):
        self.assertIsNone(build_output_file_path('image'))

    def test_build_output_file_path_3(self):
        self.assertEqual('mason_blurred.ppm', build_output_file_path('mason.ppm'))

    def test_build_output_file_path_4(self):
        self.assertEqual('derek_kobi_sit2_blurred.ppm', build_output_file_path('derek_kobi_sit2.ppm'))

    def test_build_output_file_path_5(self):
        self.assertIsNone(build_output_file_path('jay.txt'))

    def test_cast_all_to_ints_1(self):
        valid_list = '20 30 122 1 23'.split()
        self.assertEqual([20, 30, 122, 1, 23],
                         cast_all_to_ints(valid_list))

    def test_cast_all_to_ints_2(self):
        invalid_list = 'some stuff that cannot be cast to ints, such as: 123.23'.split()
        self.assertIsNone(cast_all_to_ints(invalid_list))

    
    def test_get_pixels_from_groups_of_3_1(self):
        self.assertEqual(([Pixel(0, 0, 0)], []),
                         get_pixels_from_groups_of_3([[0, 0, 0]]))

    def test_get_pixels_from_groups_of_3_2(self):
        self.assertEqual(([Pixel(0, 0, 0), Pixel(1, 2, 3)], []),
                         get_pixels_from_groups_of_3([[0, 0, 0], [1, 2, 3]]))

    def test_get_pixels_from_groups_of_3_3(self):
        self.assertEqual(([Pixel(0, 0, 0), Pixel(1, 2, 3)], [4, 5]),
                         get_pixels_from_groups_of_3([[0, 0, 0], [1, 2, 3], [4, 5]]))

    def test_get_image_dimensions_from_header_lines_1(self):
        valid_header = ['P3',
                        '200 200',
                        '255']
        self.assertEqual((200, 200),
                         get_image_dimensions_from_header_lines(valid_header))

    def test_get_image_dimensions_from_header_lines_2(self):
        invalid_header = ['P3',
                          '2OO 2OO',
                          '255']
        self.assertIsNone(get_image_dimensions_from_header_lines(invalid_header))

    def test_get_image_dimensions_from_header_lines_3(self):
        invalid_header = ['P3',
                          '2OO',
                          '255']
        self.assertIsNone(get_image_dimensions_from_header_lines(invalid_header))


    ################################################################################
    # Run above as-is and DO NOT change them #######################################
    ########################################################################## END #

    # Write more unit tests down here!
    def test_process_command_line_arg_4(self):
        self.assertIsNone(process_command_line_args('too short'.split()))

    def test_process_command_line_arg_5(self):
        self.assertEqual({'file': 'merkin.ppm', 'row': 69, 'col': 69, 'radius': 10, 'reach': 4}, process_command_line_args('merkin.ppm 69 69 10'.split()))

    def test_cast_all_to_ints_3(self):
        valid_list = '1 2 3 4 5 6 7'.split()
        self.assertEqual([1, 2, 3, 4, 5, 6, 7],
                         cast_all_to_ints(valid_list))

    def test_cast_all_to_ints_4(self):
        invalid_list = 'I suck at coding 7'.split()
        self.assertIsNone(cast_all_to_ints(invalid_list))

    def test_cast_all_to_ints_5(self):
        valid_list = '100 5 69'.split()
        self.assertEqual(cast_all_to_ints(valid_list), [100, 5, 69])

    def test_get_pixels_from_groups_of_3_4(self):
        self.assertEqual(([Pixel(69, 420, 1738)], [858]), get_pixels_from_groups_of_3([[69, 420, 1738], [858]]))

    def test_get_pixels_from_groups_of_3_5(self):
        self.assertEqual(([], [255]), get_pixels_from_groups_of_3([[], [255]]))

    def test_get_image_dimensions_from_header_lines_4(self):
        valid_header = ['P3', '25 25', '255']
        self.assertEqual((25, 25), get_image_dimensions_from_header_lines(valid_header))

    def test_get_image_dimensions_from_header_lines_5(self):
        invalid_header = ['this', 'is an', 'invalid', 'header']
        self.assertIsNone(get_image_dimensions_from_header_lines(invalid_header))

    def test_groups_of_3_1(self):
        ints = [1, 2, 3, 4, 5]
        self.assertEqual([[1, 2, 3], [4, 5]], groups_of_3(ints))

    def test_groups_of_3_2(self):
        ints = [69, 5, 0, 1738, 420, 33]
        self.assertEqual([[69, 5, 0], [1738, 420, 33]], groups_of_3(ints))

    def test_groups_of_3_3(self):
        ints = [79, 666, 420, 69]
        self.assertEqual([[79, 666, 420], [69]], groups_of_3(ints))

    def test_get_reach_for_pixel_location_1(self):
        params = {'file': 'image.ppm', 'row': '60', 'col': '60', 'radius': '10', 'reach': '5'}
        self.assertEqual(None, get_reach_for_pixel_location(params, 100, 100))

    def test_get_reach_for_pixel_location_2(self):
        params = {'file': 'image.ppm', 'row': '5', 'col': '10', 'radius': '100', 'reach': '4'}
        self.assertEqual(4, get_reach_for_pixel_location(params, 5, 13))

    def test_get_reach_for_pixel_location_3(self):
        params = {'file': 'image.ppm', 'row': '10', 'col': '10', 'radius': '3', 'reach': '4'}
        self.assertEqual(1, get_reach_for_pixel_location(params, 13, 14))

    def test_get_blurred_pixel_1(self):
        p = Pixel(2, 4, 6)
        m = Pixel(8, 8, 8)
        pixels = [[m, m, m, m, m],
                  [m, p, p, p, m],
                  [m, p, p, p, m],
                  [m, p, p, p, m],
                  [m, m, m, m, m]]
        self.assertEqual(get_blurred_pixel(pixels, 2 ,2 ,1), p)

    def test_get_blurred_pixel_2(self):
        p = Pixel(1, 2, 2)
        pixels = [[Pixel(1, 1, 1), Pixel(1, 1, 1), Pixel(1, 1, 1), Pixel(1, 1, 1), Pixel(1, 1, 1)],
                  [Pixel(1, 1, 1), Pixel(1, 4, 3), Pixel(1, 3, 2), Pixel(2, 3, 1), Pixel(1, 1, 1)],
                  [Pixel(1, 1, 1), Pixel(2, 2, 2), Pixel(1, 3, 2), Pixel(2, 3, 3), Pixel(1, 1, 1)],
                  [Pixel(1, 1, 1), Pixel(1, 3, 3), Pixel(3, 1, 1), Pixel(1, 4, 3), Pixel(1, 1, 1)],
                  [Pixel(1, 1, 1), Pixel(1, 1, 1), Pixel(1, 1, 1), Pixel(1, 1, 1), Pixel(1, 1, 1)]]
        self.assertEqual(get_blurred_pixel(pixels, 2, 2, 1), p)

    def test_get_blurred_pixel_3(self):
        p = Pixel(2, 4, 6)
        m = Pixel(8, 8, 8)
        pixels = [[m, m, m, m, m],
                  [m, m, m, m, m],
                  [m, m, p, p, p],
                  [m, m, p, p, p],
                  [m, m, p, p, p]]
        self.assertEqual(get_blurred_pixel(pixels, 4, 4, 2), p)

    def test_distance_1(self):
        x1 = 0
        y1 = 0
        x2 = 3
        y2 = 4
        self.assertEqual(distance(x1, y1, x2, y2), 5)

    def test_distance_2(self):
        x1 = 0
        y1 = 0
        x2 = 9
        y2 = 12
        self.assertEqual(distance(x1, y1, x2, y2), 15)

    def test_distance_3(self):
        x1 = 0
        y1 = 0
        x2 = 12
        y2 = 16
        self.assertEqual(distance(x1, y1, x2, y2), 20)

if __name__ == '__main__':
    unittest.main()
