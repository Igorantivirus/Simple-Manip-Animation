import os
if os.system("ffmpeg -version > nul"):
    print("Error: FFmpeg not found!")
    exit(1)

from manim import *

ANIMATION_FILE: str = "animation.txt"

class LaTexProcessor(Scene):

    header: Tex

    def getLines(self):
        
        f = "".join(open(ANIMATION_FILE).readlines()).replace("\\next\n", "")
        result: list = []
        for i in f.split('\n'):
            result.append(i.strip())
        return result

    def construct(self)->None:
        self.header = None

        lines = self.getLines()
        
        equation = None

        for line in lines:
            if(line == ""):
                self.printRectangle(equation[-1])
                continue
            if(line[0] == '#'):
                continue
            if(line[0:7] == "\header"):
                self.printHeader(line)
                continue
            equation = self.processLine(line, equation)
            self.wait()
        self.wait(2)

            
    def processLine(self, line : str, prev: Tex)->None:
        processed = ['$'+i+'$' if i != r"\\" else i for i in line.split()]

        new_equation = Tex(*processed)

        if prev is not None:
            self.play(TransformMatchingTex(prev, new_equation))
        else:
            self.play(Write(new_equation))
        return new_equation

    def printHeader(self, head: str)->str:
        new_header = Tex(head.replace("header", "text")).to_edge(UP)
        
        if self.header is None:
            self.play(FadeIn(new_header, shift=DOWN))
            self.header = new_header
        else:
            self.play(ReplacementTransform(self.header, new_header))
            self.header = new_header

    def printRectangle(self, last: Tex):
        box = SurroundingRectangle(last, color=GREEN)
        self.play(Create(box))
        self.wait(2)
        self.play(FadeOut(box))

if __name__ == "__main__":
    scene = LaTexProcessor()
    
    scene.render(preview=True)
