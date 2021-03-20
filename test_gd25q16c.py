from __future__ import print_function
from gd25q16c   import gd25q16c

spi_flash = gd25q16c(max_speed_hz=8000000) # 8MHz
print("Status Register Lower is 0x{:02x}".format(spi_flash.read_status_register_lower()))
print("Status Register Upper is 0x{:02x}".format(spi_flash.read_status_register_upper()))
print("Unique ID bytes are as follows:")
print(spi_flash.read_unique_id())
print("Identification bytes are as follows:")
print(spi_flash.read_identification())
print("Manufacturer Device ID bytes are as follows:")
print(spi_flash.manufacturer_device_id())
print("Erase entire device")
spi_flash.chip_erase(debug=True)
print("Read first and last pages")
print(spi_flash.read_data(address=(0 * spi_flash.PAGE_size_addr), num_bytes=256)) # first page
print(spi_flash.read_data(address=((spi_flash.NUM_PAGES - 1) * spi_flash.PAGE_size_addr), num_bytes=256)) # last page
print("Program all pages to have sequential values (this should take 8192 * 0.6ms = 5 seconds, but takes 8 seconds due to SPI frequency")
list_page_of_bytes = list(range(0, 256))
for pages in range(0,spi_flash.NUM_PAGES):
	spi_flash.program_page(address=(pages * spi_flash.PAGE_size_addr), page_bytes=list_page_of_bytes, debug=False)
print("Read first and last pages")
print(spi_flash.read_data(address=(0 * spi_flash.PAGE_size_addr), num_bytes=256)) # first page
print(spi_flash.read_data(address=((spi_flash.NUM_PAGES - 1) * spi_flash.PAGE_size_addr), num_bytes=256)) # last page
print("Erase first sector")
spi_flash.sector_erase(address=(0 * spi_flash.SECTOR_size_addr), debug=True) # sector 0
print("Read first and last pages")
print(spi_flash.read_data(address=(0 * spi_flash.PAGE_size_addr), num_bytes=256)) # first page
print(spi_flash.read_data(address=((spi_flash.NUM_PAGES - 1) * spi_flash.PAGE_size_addr), num_bytes=256)) # last page
print("Erase last 64k block")
spi_flash.block_erase_64k(address=((spi_flash.NUM_BLOCKS_size_64k - 1) * spi_flash.BLOCK_size_64k_addr)) # last 64k block
print("Read first and last pages")
print(spi_flash.read_data(address=(0 * spi_flash.PAGE_size_addr), num_bytes=256)) # first page
print(spi_flash.read_data(address=((spi_flash.NUM_PAGES - 1) * spi_flash.PAGE_size_addr), num_bytes=256)) # last page
