"""
Project 5 - Pixel Magic, Part 2

    blur.py Provided by Mike Ryu (doryu@calpoly.edu)

Name:
Instructor: Mike Ryu
Section: 13
"""

import sys
import blur_io
import blur_lib


def main(args_that_matter):
    # read the command line and store them as separate values of file name, row and col, radius and reach
    blur_params = blur_lib.process_command_line_args(args_that_matter)

    if not blur_params:
        # Print "Usage: python3 blur.py <image.ppm> <row> <col> <radius> <OPTIONAL:reach>"
        blur_io.print_usage_info()
        exit(1)

    # get the file name and create the output file by passing through build_output function
    input_file_path = blur_params['file']
    output_file_path = blur_lib.build_output_file_path(input_file_path)

    # store all the lines of the file into a variable
    lines_from_orig_image = blur_io.read_lines_from_image(input_file_path)

    # create and instance of the open output file
    output_file = blur_io.open_output_file(output_file_path)

    # File I/O validation.
    if not lines_from_orig_image:
        # print "Unable to open <input_file>"
        blur_io.print_file_io_error(input_file_path)
        exit(2)
    if not output_file:
        # print "Unable to open <output_file>"
        blur_io.print_file_io_error(output_file_path)
        exit(2)

    # write out the P3, row and col and color val to new file
    blur_io.write_header_to_output_file(output_file, lines_from_orig_image[:3])

    # store the height and width of the image
    dims = blur_lib.get_image_dimensions_from_header_lines(lines_from_orig_image[:3])

    # Header (dimensions line) validation.
    if not dims:
        # Print "Invalid formatting at line 2 in <input_file>"
        blur_io.print_file_format_error(2, input_file_path)
        exit(3)

    # set first value of dims to the width of the image
    width = dims[0]

    # List of pixels representing the original image.
    orig_image_pixels = []

    # Intermediate lists needed to build the 2D list of Pixels.
    row_of_pixels = []
    leftovers = []

    # store all of the color values as a big list of ints
    for line_num, line in enumerate(lines_from_orig_image[3:], start=4):
        list_of_ints = blur_lib.cast_all_to_ints(line.split())

        # PPM file format validation.
        if not list_of_ints:
            # Print "Invalid formatting at line <line_num> in <input_file>"
            blur_io.print_file_format_error(line_num, input_file_path)
            exit(3)

        # store the list of ints as the existing values plus any remaining color values that didn't get used
        list_of_ints = leftovers + list_of_ints

        # store the values of list of ints as groups of pixels
        groups = blur_lib.groups_of_3(list_of_ints)
        pixels, leftovers = blur_lib.get_pixels_from_groups_of_3(groups)

        # store the pixels in a list until it reaches width of the image, then write to output file
        for p in pixels:
            row_of_pixels.append(p)

            # ???
            if len(row_of_pixels) >= width:
                orig_image_pixels.append(row_of_pixels)
                row_of_pixels = []

    # run a for loop that goes through each pixel
    for row in range(len(orig_image_pixels)):
        for col in range(len(orig_image_pixels[0])):
            # find the reach for each pixel
            reach = blur_lib.get_reach_for_pixel_location(blur_params, row, col)

            if not reach:
                # if reach is none, set the pixel to its original value
                blurred_pixel = orig_image_pixels[row][col]
            else:
                # else blur the pixel according to its position relative to the blur origin
                blurred_pixel = blur_lib.get_blurred_pixel(orig_image_pixels, row, col, reach)

            # write out the pixel to the output file
            blur_io.write_pixel_to_output_file(output_file, blurred_pixel)

    # ALL DONE! Close the output file.
    output_file.close()


if __name__ == '__main__':
    # store all elements of the command line after "python"
    main(sys.argv[1:])
