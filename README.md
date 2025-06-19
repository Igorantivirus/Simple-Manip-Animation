<h1 align="center">Simple Manip Animation</h1>

[![Русская версия](https://img.shields.io/badge/Русская%20версия-blue)](README_RU.md)

<h2>Description</h2>

Python code based on the manim library, which allows you to create animations without using a description of each screen with LaTex code in a txt file

<h2>Dependencies</h2>

* Python3+
* Manim
  * FFmpeg
  * MikTex


<h2>Key Features</h2>

* **The convenience of creating animations**
* **LaTex formatting**: added their own "LaTex" commands
* **Flexibility**

<h2>Installation</h2>

1. **Install all the dependencies**
   * Install MikTex from the <a href="https://miktex.org/download">official website</a>.
   * Install FFmpeg from the <a href="https://ffmpeg.org/download.html">official website</a>.
   * Install Manim
     ```ssh
     pip install manim
     ```
2. **Clone the Git repository**
   ```shh
   git clone "https://github.com/Igorantivirus/Simple-Manip-Animation"
   ```
3. **Create a file to describe the animation**
   Create a file where you will describe the animation and save the path to it to the `ANIMATION_FILE` variable in `main.py` the py file

<h2>Features of the LaTex syntax in the project</h2>

To improve the animation, the following features of the LaTex syntax used in the txt file have been created:
* **Space** - Separates animation objects. It cannot be used in the construction of `"\begin(name)...\end{name}"`.
* **\header{}** - (Separate line) The title on the screen before the new title appears
* **'#'** - (Separate line) Comments
* **'\\\\'** - Line break. The difference from Base LaTex: it should be surrounded by spaces only if the construction `"\begin(name)...\end{name}"` is not used.
* **Empty line** - Wraps the previous object in a frame until the next animation.

<h2>Examples</h2>

* **Example**: Solving a linear equation

``` txt
\header{Line equation}
ax + b = 0
ax = - b
ax = - b |\cdot \frac{1}{a}
\frac{ax}{a} = -\frac{b}{a}
x = -\frac{b}{a}
ax + b = 0 \\ x = -\frac{b}{a}

```
* **Run**

Run file `main.py`:
```ssh
./main.py
```

Or assemble the video with the command you need, for example:
```ssh
manim -pql main.py SolveEquation
```

<h2>License</h2>

**The MIT License**
