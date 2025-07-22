week 0


While working on this project, I struggled to configure my GitHub account properly in VS Code. It took some trial and error, but I eventually got it working by learning more about SSH keys and Git settings.

Another challenge was with the tip calculator program — I initially forgot that I needed to convert the percentage input into a decimal. This caused incorrect results, but I learned that dividing the percentage by 100 (e.g., float(percent) / 100) is essential for accurate calculations.

Both issues helped me better understand version control and basic Python logic. Mistakes became learning opportunities!



week 1
1. A program that checks the **type of file** based on the name you give it (like `.jpg`, `.pdf`).
2. A program that tells you what **meal time** it is (breakfast, lunch, or dinner) based on the time you enter.

#At first, I struggled to understand how endswith() works, especially when users enter filenames with extra spaces or capital letters.File names like "photo.JPG" or " myFile.PDF " wouldn’t 
match unless I used .lower() and .strip().
#I initially didn’t understand how the / 60 part worked. It took me a while to realize:

Time needs to be represented as a floating-point number of hours.

For example, "7:30" should become 7.5 hours, and "12:00" should be 12.0.

int(minutes) / 60 converts the minutes into a fraction of an hour.

Understanding that split(":") breaks the string at the colon and returns two separate values (hour and minute) was key to making this work.
