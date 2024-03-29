from manimlib.imports import *
import math

class uvod(Scene):
    def construct(self):

        text1 = TextMobject("Keplerovy zákony")
        
        text1.scale(3)

        image1 = ImageMobject("kepler")
        image1.scale(2.5)
        image1.move_to(0.5*UP)

        text2 = TextMobject("Johannes Kepler\\\\"
                                "1571-1630")
        text2.move_to(3*DOWN)

        image2 = ImageMobject("astronomia_nova")
        image2.scale(3)


        self.play(Write(text1))
        self.wait(3)
        self.play(FadeOut(text1))
        self.wait(2)
        self.play(FadeIn(image1))
        self.wait()
        self.play(Write(text2))
        self.wait(3)
        self.play(FadeOut(text2), FadeOut(image1))
        self.wait(2)
        self.play(FadeIn(image2))
        self.wait(2)
        self.play(FadeOut(image2))
        self.wait(2)

class elipsa(Scene):
    def construct(self):
        ellipse1 = Ellipse()
        ellipse1.scale(4)
        
        ellipse2 = Ellipse()
        ellipse2.scale(4)
        ellipse2.fade(0.6)

        image11 = ImageMobject("blue.circle")
        image11.scale(0.2)
        image11.move_to(4*RIGHT)

        image12 = ImageMobject("blue.circle")
        image12.scale(0.2)
        image12.move_to(4*RIGHT)
        image12.fade(0.6)


        image21 = ImageMobject("yellow.circle")
        image21.move_to(1.8*LEFT)
        image21.scale(0.7)

        image22 = ImageMobject("yellow.circle")
        image22.move_to(1.8*LEFT)
        image22.scale(0.7)
        image22.fade(0.6)

        text10 = TextMobject("1. zákon")
        text10.scale(3)

        text1 = TextMobject("Planety obíhají kolem Slunce\\\\"
                             "po eliptických drahách (přesněji trajektoriích),\\\\"
                             "v jejichž jednom společném ohnisku je Slunce.")
        text1.scale(1.2)

        arrow1 = Arrow(color=GREEN)
        arrow1.rotate(315*DEGREES)
        arrow1.move_to(1*UP+2.7*LEFT)

        text3 = TextMobject("Ohnisko")
        text3.move_to(2*UP+3*LEFT)

        arrow2 = Arrow(color=GREEN)
        arrow2.rotate(225*DEGREES)
        arrow2.move_to(1*UP+2.7*RIGHT)

        text4 = TextMobject("Ohnisko")
        text4.move_to(2*UP+3*RIGHT)

        dot1 = Dot(color=GREY)
        dot1.move_to(1.8*RIGHT)

        arrow3 = Arrow(color=GREEN)
        arrow3.rotate(250*DEGREES)
        arrow3.move_to(4.3*RIGHT+1*UP)
        arrow3.scale(0.85)

        text5 = TextMobject("Planeta\\\\"
                            "(Země)")
        text5.move_to(4.7*RIGHT+2.3*UP)

        text6 = TextMobject("Elipsa")
        text6.move_to(2.5*UP)
        text6.scale(1.5)

        text7 = TextMobject("Přísluní\\\\"
                            "Perihélium")
        text7.move_to(5.5*LEFT)


        text8 = TextMobject("Odsluní\\\\"
                            "Afélium")
        text8.move_to(5.5*RIGHT)

        image3 = ImageMobject("blue.circle")
        image3.scale(0.2)
        image3.move_to(4*LEFT)

        self.play(Write(ellipse1))
        self.wait(3)
        self.play(FadeIn(image11), FadeIn(image21))
        self.wait(3)
        self.play(FadeOut(image11), FadeOut(image21), FadeOut(ellipse1), FadeIn(image12), FadeIn(image22), FadeIn(ellipse2))
        self.play(Write(text10))
        self.wait(3)
        self.play(Transform(text10, text1))
        self.wait(5)
        self.play(FadeOut(text10), FadeOut(image12), FadeOut(image22), FadeOut(ellipse2), FadeIn(ellipse1), FadeIn(image11), FadeIn(image21))
        self.wait(3)
        self.play(GrowArrow(arrow1), GrowArrow(arrow2), Write(text3), Write(text4), FadeIn(dot1))
        self.wait(3)
        self.play(FadeOut(arrow1), FadeOut(arrow2), FadeOut(text3), FadeOut(text4), FadeOut(dot1))
        self.wait()
        self.play(GrowArrow(arrow3), Write(text5))
        self.wait(3)
        self.play(FadeOut(arrow3), FadeOut(text5))
        self.wait()
        self.play(FadeOut(image11), FadeIn(image12), FadeOut(image21), FadeIn(image22), Write(text6))
        self.wait(3)
        self.play(FadeOut(image12), FadeIn(image11), FadeOut(image22), FadeIn(image21), FadeOut(text6))
        self.wait(2)
        self.play(Write(text7), Write(text8), FadeIn(image3))
        self.wait(2)
        self.play(FadeOut(text7), FadeOut(text8), FadeOut(image3))
        self.wait()
        self.play(MoveAlongPath(image11, ellipse1), rate_func=smooth, run_time=10)
        self.wait(3)


class rychlost(GraphScene):
    def construct(self):

        text10 = TextMobject("2. zákon")
        text10.scale(3)

        text1 = TextMobject("Obsahy ploch opsaných průvodičem planety\\\\"
                                "(spojnice planety a Slunce) za stejný\\\\"
                                    "čas jsou stejně velké.")
        text1.scale(1.2)

        ellipse1 = Ellipse()
        ellipse1.scale(4)

        image1 = ImageMobject("blue.circle")
        image1.scale(0.2)
        image1.move_to(4*RIGHT)

        image2 = ImageMobject("yellow.circle")
        image2.move_to(1.8*LEFT)
        image2.scale(0.7)

        START1 = (3.4,-0.8,0)
        END1 = (3.75,-0.9,0)
        line1 = Line(START1, END1)

        START2 = (3.4,0.8,0)
        END2 = (3.75,0.9,0)
        line2 = Line(START2, END2)

        line3 = Line(3.6*RIGHT+0.85*DOWN, 1.35*LEFT)
        line4 = Line(3.6*RIGHT+0.85*UP, 1.35*LEFT)
        
        image3 = ImageMobject("rlines")
        image3.scale(4.3)
        image3.move_to(1.5*DOWN+1.2*RIGHT)

        line5 = Line(1.4*UP+2.6*LEFT, 1.6*UP+2.7*LEFT)
        line6 = Line(1.4*DOWN+2.6*LEFT, 1.6*DOWN+2.7*LEFT)

        line7 = Line(1.5*UP+2.65*LEFT, 2.15*LEFT+0.35*UP)
        line8 = Line(1.5*DOWN+2.65*LEFT, 2.15*LEFT+0.35*DOWN)

        image4 = ImageMobject("rlines2")
        image4.move_to(0.45*UP+4.9*LEFT)
        image4.scale(3.1)
        image4.flip(UP)

        text2 = TextMobject("S2", color=GREEN)
        text2.move_to(3*RIGHT)
        
        text3 = TextMobject("S2", color=GREEN)
        text3.move_to(3*RIGHT)
        

        text4 = TextMobject("S1", color=GREEN)
        text4.move_to(3*LEFT)
        
        text5 = TextMobject("S1", color=GREEN)
        text5.move_to(3*LEFT)
        

        text6 = TextMobject("=")
        text6.move_to(3*UP)
        text6.scale(1.5)

        self.wait()
        self.play(Write(text10))
        self.wait(3)
        self.play(Transform(text10, text1))
        self.wait(5)
        self.play(FadeOut(text10))
        self.wait()
        self.play(FadeIn(ellipse1), FadeIn(image1), FadeIn(image2))
        self.play(MoveAlongPath(image1, ellipse1), rate_func=smooth, run_time=15)
        self.wait(5)
        self.play(FadeOut(image1))
        self.wait()
        self.play(ShowCreation(line1))
        self.wait()
        self.play(ShowCreation(line2))
        self.wait(2)
        self.play(FadeOut(line1))
        self.play(GrowArrow(line3))
        self.wait(2)
        self.play(FadeIn(image1), image1.move_to, 3.6*RIGHT+0.85*DOWN)
        self.wait(2)
        self.play(FadeOut(image1))
        self.wait(2)
        self.play(MoveAlongPath(image1, ellipse1), rate_func=linear, run_time=40)
        self.wait(5)
        self.play(FadeOut(image1))
        self.play(FadeOut(line2))
        self.play(GrowArrow(line4))
        self.wait(2)
        self.play(FadeIn(image1), image1.move_to, 3.6*RIGHT+0.85*UP)
        self.wait(5)
        self.play(FadeOut(image1))
        self.wait(2)
        self.play(FadeIn(image3))
        self.wait(2)
        self.play(GrowArrow(line5))
        self.play(GrowArrow(line6))
        self.wait(3)
        self.play(FadeOut(line5))
        self.wait(2)
        self.play(GrowArrow(line7))
        self.wait(2)
        self.play(FadeIn(image1), image1.move_to, 1.5*UP+2.65*LEFT)
        self.wait(2)
        self.play(MoveAlongPath(image1, ellipse1), rate_func=smooth, run_time=15)
        self.wait(2)
        self.play(FadeOut(line6))
        self.wait(2)
        self.play(GrowArrow(line8))
        self.wait(2)
        self.play(FadeOut(image1))
        self.wait(2)
        self.play(FadeIn(image1), image1.move_to, 1.5*DOWN+2.65*LEFT)
        self.wait(2)
        self.play(MoveAlongPath(image1, ellipse1), rate_func=smooth, run_time=15)
        self.wait(2)
        self.play(FadeIn(image4))
        self.wait(4)
        self.play(Write(text2), Write(text3), Write(text4), Write(text5), FadeOut(image3), FadeOut(image4))
        self.wait(10)
        self.play(text3.move_to, 1*RIGHT+3*UP, text5.move_to, 1*LEFT+3*UP, Write(text6))
        self.wait(5)
        self.play(FadeOut(text6), FadeOut(text5), FadeOut(text4), FadeOut(text3), FadeOut(text2), FadeOut(ellipse1), FadeOut(image1), FadeOut(image2), FadeOut(line8), FadeOut(line7), FadeOut(line4), FadeOut(line3))
        self.wait(5)

class rovnost(Scene):
    def construct(self):

        text10 = TextMobject("3. zákon")
        text10.scale(3)

        text1 = TextMobject("Poměr druhých mocnin oběžných\\\\"
                            "dob dvou planet je stejný jako poměr \\\\"
                            "třetích mocnin délek jejich hlavních poloos.")
        text1.scale(1.2)                    
        
        tex1 = TexMobject(r"\frac{T^{2}}{a^{3}}")
        tex1.scale(2.8)

        text2 = TextMobject("Oběžná doba planety")
        text2.scale(1.3)
        text2.move_to(4*LEFT+2.5*UP)

        text3 = TextMobject("průměrná vzdálenost\\\\"
                                "planety od Slunce")
        text3.scale(1.3)
        text3.move_to(4*RIGHT+2.75*DOWN)

        line1 = Line(1.3*UP+1*LEFT, 2*LEFT+2*UP)

        line2 = Line(1.3*DOWN+0.5*RIGHT, 1.5*RIGHT+2*DOWN)

        tex2 = TexMobject(r"\frac{T\cdot T}{a\cdot a\cdot a}")
        tex2.scale(2.8)

        image1 = ImageMobject("merkur")

        tex3 = TexMobject(r"\frac{T^{2}}{a^{3}}")
        tex4 = TexMobject(r"\frac{T^{2}}{a^{3}}")
        tex4.scale(1.2)
        tex5 = TexMobject(r"\frac{T^{2}}{a^{3}}")
        tex5.move_to(1.75*RIGHT)
        tex5.scale(1.6)
        tex6 = TexMobject(r"\frac{T^{2}}{a^{3}}")
        tex6.scale(1.3)
        tex6.move_to(5.7*RIGHT)


        image2 = ImageMobject("venus")
        image2.scale(1.2)

        text4 = TextMobject("=")
        text4.move_to(3.825*LEFT)
        text4.scale(1.5)

        image3 = ImageMobject("earth")
        image3.scale(1.6)
        image3.move_to(1.75*RIGHT)

        text5 = TextMobject("=")
        text5.move_to(0.25*LEFT)
        text5.scale(1.5)

        text6 = TextMobject("=")
        text6.move_to(3.7*RIGHT)
        text6.scale(1.4)

        image4 = ImageMobject("mars")
        image4.scale(1.3)
        image4.move_to(5.7*RIGHT)


        self.wait(2)
        self.play(Write(text10))
        self.wait(2)
        self.play(Transform(text10, text1))
        self.wait(5)
        self.play(Transform(text10, tex1))
        self.wait(3)
        self.play(GrowArrow(line1))
        self.wait(2)
        self.play(Write(text2))
        self.wait(2)
        self.play(GrowArrow(line2))
        self.wait(2)
        self.play(Write(text3))        
        self.wait(5)
        self.play(FadeOut(text2), FadeOut(text3), FadeOut(line1), FadeOut(line2))
        self.wait(2)
        self.play(Transform(text10, tex2))
        self.wait(3)
        self.play(FadeOut(text10))
        self.wait(3)
        self.play(FadeIn(image1), FadeIn(tex3))
        self.wait(3)
        self.play(image1.move_to, 5.5*LEFT, tex3.move_to, 5.5*LEFT)
        self.wait(3)
        self.play(FadeIn(image2), FadeIn(tex4))
        self.wait(3)
        self.play(image2.move_to, 2*LEFT, tex4.move_to, 2*LEFT, Write(text4))
        self.wait(3)
        self.play(FadeIn(image3), FadeIn(tex5), Write(text5))
        self.wait()
        self.play(FadeIn(image4), FadeIn(tex6), Write(text6))
        self.wait(3)
        self.play(FadeOut(image4), FadeOut(image3), FadeOut(image2), FadeOut(image1), FadeOut(tex6), FadeOut(tex5), FadeOut(tex4), FadeOut(tex3), FadeOut(text6), FadeOut(text5), FadeOut(text4))
        self.wait(3)


class tabulka(Scene):
    def construct(self):

        line1 = Line(0.8*LEFT, 0.8*RIGHT, stroke_width=5)
        line1.move_to(0.2*DOWN)

        tex1 = TexMobject(r"T")
        tex1.scale(2.8)
        tex1.move_to(0.85*UP+0.3*LEFT)

        tex2 = TextMobject(r"a")
        tex2.scale(2.8)
        tex2.move_to(1.2*DOWN+0.3*LEFT)

        tex3 = TextMobject(r"2")
        tex3.scale(2)
        tex3.move_to(1.225*UP+0.475*RIGHT)

        tex4 = TextMobject(r"3")
        tex4.scale(2)
        tex4.move_to(0.8*DOWN+0.35*RIGHT)

        tex5 = TexMobject(r"=")
        tex5.move_to(2.15*UP+0.5*LEFT)

        ################################################

        text1 = TextMobject("Merkur - ")
        text1.move_to(1*LEFT)

        tex201 = TextMobject("0,2408")
        tex201.scale(1.5)
        tex201.move_to(2.75*UP+2.5*LEFT)

        tex202 = TexMobject("0,3871")
        tex202.scale(1.5)
        tex202.move_to(1.1*UP+2.5*LEFT)

        tex203 = TexMobject("1,0000")
        tex203.scale(1.5)
        tex203.move_to(2.15*UP+1*RIGHT)

        tex204 = TexMobject("1,0000")
        tex204.scale(1.5)
        tex204.move_to(2.15*UP+1*RIGHT)

        image1 = ImageMobject("merkur")
        image1.move_to(2*DOWN)


        line2 = Line(3.75*LEFT+2.15*UP, 1*LEFT+2.15*UP)

        ################################################

        image2 = ImageMobject("venus")
        image2.move_to(2*DOWN)

        text2 = TextMobject("Venuše - ")
        text2.move_to(1*LEFT)

        tex301 = TextMobject("0,6152")
        tex301.scale(1.5)
        tex301.move_to(2.75*UP+2.5*LEFT)

        tex302 = TexMobject("0,7233")
        tex302.scale(1.5)
        tex302.move_to(1.1*UP+2.5*LEFT)

        tex205 = TexMobject("1,0000")
        tex205.scale(1.5)
        tex205.move_to(2.15*UP+1*RIGHT)

        ################################################

        image3 = ImageMobject("earth")
        image3.scale(1.4)
        image3.move_to(2*DOWN)

        text3 = TextMobject("Země - ")
        text3.move_to(1*LEFT)

        tex401 = TextMobject("1")
        tex401.scale(1.5)
        tex401.move_to(2.75*UP+1.5*LEFT)

        tex402 = TexMobject("1")
        tex402.scale(1.5)
        tex402.move_to(1.1*UP+1.5*LEFT)

        tex206 = TexMobject("1,0000")
        tex206.scale(1.5)
        tex206.move_to(2.15*UP+1*RIGHT)

        line3 = Line(0.8*LEFT, 0.8*RIGHT, stroke_width=5)
        line3.move_to(2.15*UP+1.5*LEFT)
        line3.scale(0.8)

        ################################################

        image4 = ImageMobject("mars")
        image4.scale(1.3)
        image4.move_to(2*DOWN)

        text4 = TextMobject("Mars - ")
        text4.move_to(1*LEFT)

        tex501 = TextMobject("1,8808")
        tex501.scale(1.5)
        tex501.move_to(2.75*UP+2.5*LEFT)

        tex502 = TexMobject("1,5236")
        tex502.scale(1.5)
        tex502.move_to(1.1*UP+2.5*LEFT)

        tex207 = TexMobject("1,0000")
        tex207.scale(1.5)
        tex207.move_to(2.15*UP+1*RIGHT)


        
        self.wait(3)
        self.play(Write(line1), Write(tex1), Write(tex2), Write(tex3), Write(tex4))
        self.wait(5)
        self.play(
                    tex1.move_to, 3*UP+0.25*LEFT, tex1.scale, 0.8,
                    tex2.move_to, 1.35*UP+0.25*LEFT, tex2.scale, 0.8,
                    tex3.move_to, 3.275*UP+0.375*RIGHT, tex3.scale, 0.8,
                    tex4.move_to, 1.65*UP+0.275*RIGHT, tex4.scale, 0.8,
                    line1.move_to, 2.15*UP, line1.scale, 0.8
                    )

        self.wait(3)
        self.play(Write(text1), tex1.move_to, 3*UP+1.75*LEFT,
                    tex2.move_to, 1.35*UP+1.75*LEFT,
                    tex3.move_to, 3.275*UP+1.125*LEFT,
                    tex4.move_to, 1.65*UP+1.225*LEFT, 
                    line1.move_to, 2.15*UP+1.5*LEFT,
                    FadeIn(image1)
                    )
        self.wait(2)
        self.play(Write(tex5))
        self.wait()
        self.play(Transform(tex1, tex201), Transform(tex2, tex202), Transform(line1, line2))
        self.wait(2)
        self.play(Write(tex203), Write(tex204))
        self.wait(2)
        self.play(tex204.move_to, 1*RIGHT+0.1*DOWN, tex204.scale, 0.8)
        self.wait(5)
        self.play(FadeOut(image1), FadeIn(image2), FadeOut(tex203), FadeOut(tex204), Transform(text1, text2), Transform(tex1,tex301), Transform(tex2,tex302))
        self.wait(3)
        self.play(Write(tex203), Write(tex205))
        self.wait(5)
        self.play(tex205.move_to, 1*RIGHT+0.1*DOWN, tex205.scale, 0.8)
        self.wait(5)
        self.play(FadeOut(image2), FadeIn(image3), FadeOut(tex203), FadeOut(tex205), Transform(text1, text3), Transform(tex1,tex401), Transform(tex2,tex402), Transform(line1, line3))
        self.wait(3)
        self.play(Write(tex203), Write(tex206))
        self.wait(2)
        self.play(tex206.move_to, 1*RIGHT+0.1*DOWN, tex206.scale, 0.8)
        self.wait(5)
        self.play(FadeOut(image3), FadeIn(image4), FadeOut(tex203), FadeOut(tex206), Transform(text1, text4), Transform(tex1,tex501), Transform(tex2,tex502), Transform(line3, line2), FadeOut(line1))
        self.wait(2)
        self.play(Write(tex203), Write(tex207))
        self.wait(2)
        self.play(tex207.move_to, 1*RIGHT+0.1*DOWN, tex207.scale, 0.8)
        self.wait(5)
        self.play(FadeOut(image4), FadeOut(text1), FadeOut(tex207), FadeOut(tex203),  FadeOut(tex1), FadeOut(tex2), FadeOut(line3), FadeOut(tex3), FadeOut(tex4), FadeOut(tex5))
        self.wait(3)

class newton(MovingCameraScene):
    def construct(self):
        
        image1 = ImageMobject("yellow.circle")
        image1.scale(0.2)
        image1.move_to(0.4*RIGHT)

        circle1 = Circle(color=WHITE)
        circle1.scale(0.4)

        circle2 = Circle(color=WHITE)
        circle2.scale(4)

        dot1 = Dot(color=GREY)

        line1 = Line(0.05*UP+0.05*LEFT, 0.05*DOWN+0.05*RIGHT)
        line2 = Line(0.05*UP+0.05*RIGHT, 0.05*DOWN+0.05*LEFT)

        text1 = TextMobject("T")
        text1.scale(0.5)
        text1.move_to(0.15*DOWN+0.15*RIGHT)

        image2 = ImageMobject("newton")
        image2.scale(2.5)
        image2.move_to(0.5*UP)

        text2 = TextMobject("Isaac Newton\\\\"
                                "1642-1727")
        text2.move_to(3*DOWN)
        
        text3 = TextMobject("Autor: Jakub Troják")
        text3.scale(1.3)

        image3 = ImageMobject("night_sky")
        image3.scale(4)

        self.camera_frame.save_state()
        self.wait(2)
        self.play(FadeIn(image1))
        self.wait()
        self.play(self.camera_frame.set_height,circle1.get_width()*5, self.camera_frame.move_to,circle1)
        self.wait(2)
        self.play(ShowCreation(circle1, rate_func=linear, run_time=10), MoveAlongPath(image1, circle1, rate_func=linear), Write(line1), Write(line2), Write(text1))
        self.wait()
        self.play(FadeOut(line1), FadeOut(line2), FadeOut(text1), Restore(self.camera_frame, run_time=2.5), ShowCreation(circle1, rate_func=linear, run_time=20), MoveAlongPath(image1, circle1, rate_func=linear), ShowCreation(circle2, rate_func=linear, run_time=30), MoveAlongPath(dot1, circle2, rate_func=linear))
        self.wait(5)
        self.play(FadeOut(circle1), FadeOut(circle2), FadeOut(dot1), FadeOut(image1))
        self.wait(2)
        self.play(FadeIn(image2), Write(text2))
        self.wait(3)
        self.play(FadeOut(image2), FadeOut(text2))
        self.wait(3)
        self.play(FadeIn(image3))
        self.wait(3)
        self.play(image3.fade, 0.8)
        self.wait()
        self.play(Write(text3))
        self.wait(10)