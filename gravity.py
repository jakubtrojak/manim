from manimlib.imports import *

class info(GraphScene):
    def construct(self):
        
        image6 = ImageMobject("apple")
        image6.scale(0.3)
        image6.move_to(2.55*RIGHT+1.35*DOWN)
        image6.rotate(20*DEGREES)
        
        text1 = TextMobject("Gravitace")
        text1.scale(2)

        image1 = ImageMobject("apple.tree")
        image1.scale(3.5)

        image2 = ImageMobject("newton")
        image2.move_to(2.5*DOWN+2.55*RIGHT)

        image3 = ImageMobject("apple")
        image3.move_to(0.85*UP+2.55*RIGHT)
        image3.scale(0.3)

        target1 = np.array(2.55*RIGHT+1.35*DOWN)

        image4 = ImageMobject("newton2")
        image4.move_to(2.5*DOWN+2.55*RIGHT)

        image5 = ImageMobject("angry.mouth")
        image5.scale(0.13)
        image5.move_to(2.8*DOWN+2.7*RIGHT)
        image5.rotate(340*DEGREES)
        
        image7 = ImageMobject("anger.symbol")
        image7.move_to(2.55*RIGHT+1.75*DOWN)
        image7.scale(0.2)
        
        
        text2 = TextMobject("Proč to na\\\\mě spadlo?")
        text2.move_to(1.9*LEFT+1.8*UP)

        image8 = ImageMobject("bubble")
        image8.move_to(2*LEFT+1.5*UP)
        image8.scale(1.5)
        
        target2 = np.array(5*LEFT+1*DOWN)

        CONFIG = {
        "y_axis_label": None, # Don't write y axis label
        "x_axis_label": None,
    }
        self.setup_axes()
        plotSin = self.get_graph(lambda x : -(x-6)*(x-3), 
                                    color = BLACK,
                                    x_min=4.5,
                                    x_max=2.75,
                                )
        plotSin.move_to(1.8*RIGHT+2.2*DOWN)
        plotSin.set_stroke(width=3) # width of line
        # Animation
        for plot in (plotSin):
            

            def setup_axes(self):
                GraphScene.setup_axes(self)
            # width of edges
            self.x_axis.set_stroke(width=0)
            self.y_axis.set_stroke(width=0)
            self.x_axis.set_color(BLACK)
            self.y_axis.set_color(BLACK)
            # Add x,y labels
        


        self.play(FadeIn(text1))
        self.wait(5)
        self.play(FadeOut(text1), run_time=3)
        self.wait(2)
        self.play(FadeIn(image1), FadeIn(image2), FadeIn(image3))
        self.wait(2)
        self.play(image3.move_to, target1,
                rate_func=rush_into)
        self.play(ShowCreation(plotSin), ShowCreation(image6), FadeOut(image3),MoveAlongPath(image6, plotSin),
                    FadeIn(image4), FadeOut(image2), FadeIn(image5),FadeOut(image3), FadeIn(image7))
        self.wait(5)
        self.play(FadeOut(image7), FadeOut(image5), FadeOut(image4), FadeOut(image6), FadeOut(image1), FadeIn(image2))
        self.wait(5)
        self.play(image2.move_to, target2,
                    image2.scale, 1.2)
        self.play(FadeIn(image8))
        self.play(FadeIn(text2))
        self.wait(2)

class gravity01(Scene):
    def construct(self):

        image1 = ImageMobject("earth1")
        image1.scale(2)
        image1.move_to(3*DOWN)
        image1.scale(0.8)
        

        image2 = ImageMobject("apple")
        image2.scale(0.4)

        arrow1 = Arrow(color=RED)
        arrow1.rotate(270*DEGREES)
        arrow1.move_to(0.65*DOWN)

        arrow2 = Arrow(color=BLUE)
        arrow2.rotate(90*DEGREES)
        arrow2.move_to(2.5*DOWN)

        image3 = ImageMobject("moon")
        image3.to_edge(UP)

        arrow3 = Arrow(color=RED)
        arrow3.scale(1.75)
        arrow3.move_to(UP)
        arrow3.rotate(270*DEGREES)

        text1 = TextMobject("Jablko působí stejnou silou na Zemi,\\\\jako Země na jablko.")
        text1.to_edge(LEFT+UP)
        




        self.play(FadeIn(image1), FadeIn(image2), Write(text1))
        self.wait(5)
        self.play(GrowArrow(arrow1), GrowArrow(arrow2))
        self.wait()
        self.play(FadeOut(image2), FadeOut(arrow1), FadeIn(image3),
                    image1.scale,0.75,
                    arrow2.scale, 1.75,
                    GrowArrow(arrow3), )
        self.wait(3)
        self.play(FadeOut(arrow3),FadeOut(arrow2),FadeOut(image3),FadeOut(image1))
        self.wait(2)


class gravity02(Scene):
    def construct(self):

        tex1 = TexMobject(r"{ F }_{ G }=")
        tex1.move_to(DOWN+1.5*LEFT)

        tex13 = TexMobject(r"G")
        tex13.move_to(DOWN+0.5*LEFT)


        tex2 = TexMobject(r"{ m }_{ 1 }")
        tex2.move_to(0.75*DOWN+0.25*RIGHT)


        tex3 = TexMobject(r"\times ")
        tex3.move_to(0.75*DOWN+0.95*RIGHT)

        tex4 = TexMobject(r"{ m }_{ 2 }")
        tex4.move_to(0.75*DOWN+1.7*RIGHT)

        
        tex5 = TexMobject(r"\frac {}{ \quad \quad \quad \quad \quad  } ")
        tex5.move_to(DOWN+1*RIGHT)


        tex6 = TexMobject(r"r")
        tex6.move_to(1.5*DOWN+0.95*RIGHT)

        tex7 = TexMobject(r"{ \quad  }^{ 2 }")
        tex7.move_to(1.25*DOWN+1.15*RIGHT)

        START1 = (2.25*LEFT+2.5*UP)
        END1 = (2.25*LEFT+0.5*UP)

        START2 = (2.25*LEFT+0.5*UP)
        END2 = (2.25*RIGHT+0.5*UP)

        START3 = (2.25*RIGHT+0.5*UP)
        END3 = (2.25*RIGHT+2.5*UP)


        line1 = Line(START1,END1)
        line2 = Line(START2, END2)
        line3 = Line(START3, END3)

        circle1 = Circle(color=WHITE)
        circle1.scale(1.2)
        circle1.move_to(2.5*UP+2.25*LEFT)

        circle2 = Circle(color=WHITE)
        circle2.scale(0.8)
        circle2.move_to(2.5*UP+2.25*RIGHT)


        tex8 = TexMobject(r"r")
        tex8.move_to(0.8*UP+1*LEFT)

        text1 = TextMobject("-vzdálenost")
        text1.move_to(0.38*RIGHT+0.85*UP)

        tex9 = TexMobject(r"{ m }_{ 1 }")
        tex9.move_to(2.75*UP+2.25*LEFT)

        tex10 = TexMobject(r"{ m }_{ 2 }")
        tex10.move_to(2.75*UP+2.25*RIGHT)

        tex11 = TexMobject(r"G")
        tex11.move_to(6*LEFT+3*DOWN)

        tex12 = TexMobject(r"=6,67\times { 10 }^{ -11 }{ m }^{ 3 }\cdot { kg }^{ -1 }{ \cdot s }^{ -2 }")
        tex12.next_to(tex11)

        self.play(Write(tex1), Write(tex2), Write(tex3), Write(tex4), Write(tex5), Write(tex6), Write(tex7), Write(tex13))
        self.wait(5)
        self.play(Write(circle1), Write(circle2))
        self.wait(2)
        self.play(Write(line1), Write(line3), Write(line2))
        self.wait(2)
        self.play(Write(text1), Write(tex8))
        self.wait(2)
        self.play(Write(tex9), Write(tex10))
        self.wait(2)
        self.play(Write(tex11), Write(tex12))
        self.play(tex13.scale, 1.2, 
                    tex13.set_color,RED,
                    tex11.scale, 1.2,
                    tex11.set_color, RED
                    )
        self.wait(5)
        self.play(tex13.scale, 0.8, 
                    tex13.set_color,WHITE,
                    tex11.scale, 0.8,
                    tex11.set_color, WHITE)
        self.wait(5)
        self.play(tex2.set_color, RED,
                tex2.scale, 1.2,
                tex9.set_color, RED,
                tex9.scale, 1.2)
        self.wait(5)
        self.play(tex2.set_color, WHITE,
                tex2.scale,0.8,
                tex9.set_color, WHITE,
                tex9.scale, 0.8)
        self.wait(5)
        self.play(tex4.set_color, RED,
                tex4.scale, 1.2,
                tex10.set_color, RED,
                tex10.scale, 1.2)
        self.wait(5)
        self.play(tex4.set_color, WHITE,
                tex4.scale,0.8,
                tex10.set_color, WHITE,
                tex10.scale, 0.8)
        self.wait(5)
        self.play(tex8.set_color, RED,
                tex8.scale, 1.2,
                tex6.set_color, RED,
                tex6.scale, 1.2)
        self.play(tex8.set_color, WHITE,
                tex8.scale,0.8,
                tex6.set_color, WHITE,
                tex6.scale, 0.8)
        self.wait(5)
        self.play(FadeOut(tex1), FadeOut(tex2), FadeOut(tex3), FadeOut(tex4), FadeOut(tex5), FadeOut(tex6), FadeOut(tex7), FadeOut(tex8), FadeOut(tex9), FadeOut(tex10), 
        FadeOut(tex11), FadeOut(tex12), FadeOut(circle1), FadeOut(circle2), FadeOut(line1), FadeOut(line2), FadeOut(line3), FadeOut(text1), FadeOut(tex13))
        self.wait()


class scale(Scene):
    def construct(self):
        image1 = ImageMobject("moon")
        image1.scale(0.8)
        image1.move_to(2*UP+2*RIGHT)

        image2 = ImageMobject("earth")
        image2.move_to(2*UP+2*LEFT)

        tex1 = TexMobject(r"{ m }_{ 1 }=5,92\times { 10 }^{ 24 }kg")
        tex1.move_to(4.8*LEFT+2*UP)

        tex2 = TexMobject(r"{ m }_{ 2 }=7,35\times { 10 }^{ 22 }kg")
        tex2.move_to(4.8*RIGHT+2*UP)

        tex3 = TexMobject(r"r=384 400km")
        tex3.move_to(3*UP)

        tex4 = TexMobject(r"{ F }_{ G }=G\frac { { m }_{ 1 }\cdot { m }_{ 2 } }{ { r }^{ 2 } } ")

        tex5 = TexMobject(r"{ F }_{ G }=6,67\times { 10 }^{ -11 }\frac { 5,92\times { 10 }^{ 24 }\cdot 7,35\times { 10 }^{ 22 } }{ { \left( 384,4\times { 10 }^{ 6 } \right)  }^{ 2 } } ")

        tex6 = TexMobject(r"{ F }_{ G }=7,55\times { 10 }^{ 28 }")


        self.play(FadeIn(image1), FadeIn(image2))
        self.wait(2)
        self.play(image1.scale,0.5,
                    image1.to_edge, UP+RIGHT,
                    image2.scale, 0.5,
                    image2.to_edge, UP+LEFT)
        self.wait(5)
        self.play(Write(tex1))
        self.play(Write(tex2))
        self.wait(2)
        self.play(Write(tex3))
        self.wait(5)
        self.play(Write(tex4))
        self.wait(2)
        self.play(Transform(tex4, tex5))
        self.wait(2)
        self.play(Transform(tex4, tex6))
        self.wait(2)
        self.play(FadeOut(tex4), FadeOut(tex1),FadeOut(tex2),FadeOut(tex3),FadeOut(image1),FadeOut(image2))

class problem(Scene):
    def construct(self):
        tex1 = TexMobject(r"{ F }_{ G }=G\frac { { m }_{ 1 }\cdot { m }_{ 2 } }{ { r }^{ 2 } }")
        tex1.move_to(1.5*UP)

        text1 = TextMobject("Tato rovnice bohužel neplatí všude.")

        text2 = TextMobject("Rovnice selhává u velice hmotných objektů.\\\\Mezi takové patří např. černá díra.")
        text2.move_to(2*UP)

        image1 = ImageMobject("blackhole")
        image1.move_to(DOWN)

        text3 = TextMobject("Přesně se neví, zdali je to pravda,\\\\ale nejspíše neplatí u předmětu denního života.")
        text3.move_to(UP)

        text4 = TextMobject("U lehkých předmětů je síla mezi nimi\\\\velice malá, a skoro neměřitelná.\\\\U takových sil se využívají jiné rovnice")
        text4.move_to(1.5*DOWN)

        text5 = TextMobject("Rovnice vysvětluje objekty\\\\ podobné ve sluneční soustavě.")
        text5.move_to(UP)

        image2 = ImageMobject("solar.system")
        image2.move_to(DOWN)

        text6 = TextMobject("Co je ale gravitace za sílu?\\\\Odkud se ta síla bere?")
        text6.move_to(UP)

        image3 = ImageMobject("newton")
        image3.move_to(DOWN)

        image4 = ImageMobject("thinking.hand")
        image4.move_to(2*DOWN)

        image5 = ImageMobject("einstein")




        self.play(Write(tex1))
        self.wait()
        self.play(Write(text1))
        self.wait(2)
        self.play(FadeOut(tex1),Transform(text1, text2))
        self.wait(3)
        self.play(FadeIn(image1))
        self.wait(2)
        self.play(FadeOut(image1), FadeOut(text1), Write(text3), Write(text4))
        self.wait(3)
        self.play(FadeOut(text3), FadeOut(text4), Write(text5), FadeIn(image2))
        self.wait(3)
        self.play(FadeOut(text5), FadeOut(image2))
        self.play(FadeIn(image3), Write(text6), FadeIn(image4))
        self.wait()
        self.play(FadeOut(image3), FadeOut(image4), FadeOut(text6))
        self.wait()
        self.play(FadeIn(image5))
        self.wait(5)