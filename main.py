import os
from manim import *
from stringUtils import *

ANIMATION_FILE: str = "animation.txt"

class LaTexProcessor(Scene):

    def construct(self)->None:
        self.header : Tex = None
        equation : Tex = None

        lines = getLines(ANIMATION_FILE)

        for line in lines:
            if(line == ""):
                continue
            elif(line[0:7] == r"\header"):
                self.printHeader(line)
            else:
                equation = self.processLine(line, equation)
                
        self.wait(2)

    def processLine(self, line : str, prev: Tex)->Tex:
        processed, toBorder = processString(line)
        new_equation = Tex(*processed)

        if prev is None:
            self.play(Write(new_equation))
        else:
            self.play(TransformMatchingTex(prev, new_equation))
        
        if(toBorder != ""):
            index = processed.index(toBorder)
            box = SurroundingRectangle(new_equation[index], color=GREEN)
            self.play(Create(box))
            self.wait(2)
            self.play(FadeOut(box))

        self.wait()

        return new_equation
    
    def printHeader(self, head: str)->str:
        new_header = Tex(head.replace("header", "text")).to_edge(UP)
        
        if self.header is None:
            self.play(FadeIn(new_header, shift=DOWN))
            self.header = new_header
        else:
            self.play(ReplacementTransform(self.header, new_header))
            self.header = new_header

if __name__ == "__main__":
    scene = LaTexProcessor()
    
    scene.render(preview=True)
