# Python Calculator - With PySide6 GUI
This lovely project was made possible by the wonderful Professor Otávio Miranda, and his Python Course "Curso de Python 3 do básico ao avançado - com projetos reais", available at: www.udemy.com/course/python-3-do-zero-ao-avancado/.

For starters, make sure to import the following modules on your virtual enviroments, if you're not downloading the packed-up version below:

### For the script -----------> PySide6==6.7.2
### For packing --------------> pyinstaller==6.10.0

I would share my "requirements.txt" here, but unfortunately I made the mistake of NOT creating another venv when initiating this project, it is basically unusable.

![Captura de tela 2024-10-11 205018](https://github.com/user-attachments/assets/73cc5227-4c40-4ff7-864c-43bb42fc0746)

## The Backstory

Now, this project was made with the library PySide6 in mind, said library is a Qt based module, brought to our world from the C++ language, and it brings with itself high-end resources for Guided User Interface development entirely in Python.

But why a calculator, you say...?

Honestly, it seemed like something simple to do, just to get started with the library, oh how wrong I was. The documentation is extensive and leaves no room for doubts, the problem was with my shabby attempts to integrate my code with the GUI, while not losing access to keyboard funcionalities. With every fix, something else broke, until nothing worked anymore, it was a pain, but I LOVED IT! The hardest part wasn't even the window, the layouts or the various widgets, it was trying to make the negative numbers work with with what I had done.

Anyway, as fun and heart wrenching as this project was, it is far, FAAAAAAAR from optimized, it is simply too bare bones a calculator to even be called that, it does the bare minimum, which I'm still proud of.

To finish the project, I tried to pack it up using something else I'm not familiar with, PyInstaller, and it went relatively well. No fatal errors, no bricking PC's or even turning off the internet, but again, it IS unoptimized. The packed archive ended up with over 42 Megabytes of size, which is terrible, considering the simplicity of the app. This was just my inexperience speaking, as what it had to be done was carefully import only the piece of the modules I wanted to use, not the entire thing, and then pack everything up.

#### Packed-up Executable --------> https://drive.google.com/drive/folders/13LphjCdZEQOf7aSV9NjJP_79QKZ9iwAA?usp=sharing

Keep in mind the following:
- PyInstaller takes account of what Operational System the code was being packed in;
- This particular calculator was packed-up in Windows 11 Pro, Version 23H2, so take that in mind if downloading the archive;
- Elaborating on the previous point, it might work on some machines running Linux, but it definitely wont't on Mac; 
- The app was made in Python Version 3.12.6, I'm not sure if this is relevant, but keep in mind anyway.

## Wrap-up
If you're still here, even if you're bored out of you mind, thank you for reading my ramblings, for even taking the time of your schedules to see what I developed, it means the world to me.

At this point in time, the time I made this, I am still an amateur just trying to learn, to get better, bit by bit. This line of work can be hard and treacherous, but I know I can persevere and achieve great things.

Again, thank you for being here, any feedback is very much apreciated.

Signing out.
