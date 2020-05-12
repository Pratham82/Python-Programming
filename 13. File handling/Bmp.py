# A module for dealing with BMP bitmap image files

def write_grayscale(filename,pixels):
      '''
      Creates and writes a grayscale BMP file 
      Args:
        filename: the name of the BMP file to me created
        
        pixels: A rectangular image sorted as a sequence of rows. 
        Each row must be an iterable series of integers in the range of 0-255

        Raises: 
            ValueErrorL If any of the integer values are out of range.
            OSError: If the file couldn't be written.
      '''

      height = len(pixels)
      width = len(pixels[0])

      with open(filename,'wb') as bmp:
          # BMP header
          bmp.write(b'BM')

          size_bookmark = bmp.tell()             # The next four bytes hold the filesize as a 32-bit
          bmp.write(b'\x00\x00\x00\x00')     # Little-endian integer. Zero placeholder for now
          
          bmp.write(b'\x00\x00')             # Unused 16-bit integer should be zero
          bmp.write(b'\x00\x00')             # Unused 16-bit integer should be zer
          
          pixel_offset_bookmark = bmp.tell()
          bmp.write(b'\x00\x00\x00\x00')     # pixel data 

          # Image header
          bmp.write(b'\x28\x00\x00\x00')     # Image header size in bytes - 40 decimal
          bmp.write(_int32_to_bytes(width))  # Image width in pixels 
          bmp.write(_int32_to_bytes(height)) # Image height in pixels 
          bmp.write(b'\x00\x00')             # Number of image planes
          bmp.write(b'\x00\x00')             # Bits per pixel 8 for grayscale
          bmp.write(b'\x00\x00\x00\x00')     # No compressed images
          bmp.write(b'\x00\x00\x00\x00')     # Zero compressed images
          bmp.write(b'\x00\x00\x00\x00')     # Unused pixesl per meter
          bmp.write(b'\x00\x00\x00\x00')     # Unused pixels per meter
          bmp.write(b'\x00\x00\x00\x00')     # Use whole color table
          bmp.write(b'\x00\x00\x00\x00')     # All colors are important 
          
          # Color palette - a linear grayscale 
          for c in range(256):
              bmp.write(bytes((c,c,c,0))) # Blue, Green , Red, Zero

          # Pixel date
          pixel_data_bookmark = bmp.tell()
          for row in reversed(pixels): # BMP files are bottom to top
              row_data= bytes(row)
              bmp.write(row_data)
              padding = b'\x00' *((4- (len(row)%4 ))% 4 ) # Pad row to multiple of four bytes
              bmp.write(padding)
          
          # End of file
          eof_bookmark = bmp.tell()

          # Fill in file size placeholder
          bmp.seek(size_bookmark)
          bmp.write(_int32_to_bytes(eof_bookmark))

          # Fill in the pixel offset placeholder 
          bmp.seek(pixel_offset_bookmark)
          bmp.write(_int32_to_bytes(pixel_data_bookmark))


          