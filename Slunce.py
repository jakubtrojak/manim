from manimlib.imports import * 

class Uvod(Scene):
    def construct(self):
        text = TextMobject("Slunce")
        image1 = ImageMobject("sun")
        text.scale(3)
        image1.scale(2.5)
        image1.move_to(1*DOWN)
        self.play(GrowFromCenter(text),run_time=3)
        self.wait(10)
        self.play(text.to_edge, UP)
        self.play(FadeIn(image1),run_time=1)
        self.wait(10)
        self.play(FadeOut(text), FadeOut(image1), run_time=5)

#Sony vegas - pohyb planet kolem slunce


class info(GraphScene):
    def construct(self):
        
        text1 = TextMobject("Slunce je od Země 150 mil. km daleko, což je 1 AU.")
        image2 = ImageMobject("sun01")
        image3 = ImageMobject("earth")
        START = (0,0,0)
        END1 =  (4,0,0)
        END2 =  (-4,0,0)
        line1 = Line(START,END1)
        line2 = Line(START,END2)
        text2 = TextMobject("150 mil km = 1 AU (AU = astronomická jednotka)")
        text2.scale(0.7)
        text2.move_to(0.35*UP)
        text3 = TextMobject("Světlo doletí k Zemi za 8 minut a 18 sekund")
        text3.move_to(3*UP)
        text4 = TextMobject("8 minut a 18 sukund")
        text4.scale(0.7)
        text4.move_to(0.5*UP)
        sipka = TexMobject("\lhd",color = YELLOW)
        sipka.move_to(3.9*RIGHT+0.1*DOWN)

        CONFIG = {
        "y_axis_label": None, # Don't write y axis label
        "x_axis_label": None,
    }
        self.setup_axes()
        plotSin = self.get_graph(lambda x : np.sin(x), 
                                    color = YELLOW,
                                    x_min=-48,
                                    x_max=48,
                                )
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

        plotSin.scale(0.1)
        plotSin.move_to(0.02*RIGHT, 3*UP)
        plotSin.flip(UP)
        


        self.play(Write(text1))
        self.wait(10)
        self.play(text1.to_edge, 1.5*UP)
        self.wait(3)
        self.play(FadeIn(image2),image2.move_to, 5*RIGHT, FadeIn(image3), image3.move_to, 5*LEFT)
        self.wait(3)
        self.play(ShowCreation(line1),ShowCreation(line2))
        self.wait()
        self.play(Write(text2))
        self.wait(2)
        self.play(FadeOut(line1), FadeOut(line2))
        self.play(Transform(text1, text3), Transform(text2, text4))
        self.wait()
        self.play(Write(sipka))
        self.play(ShowCreation(plotSin),
                    sipka.move_to, 4*LEFT, run_time=2.5)
        self.play(FadeOut(sipka), run_time=0.2)
        self.wait(10)
        self.play(FadeOut(sipka), FadeOut(image3), FadeOut(text1), FadeOut(text2), FadeOut(plotSin))
        self.wait(5)

        
class info02(Scene):
    def construct(self):
        image2 = ImageMobject("sun01")
        image2.move_to(5*RIGHT)
        image2.scale(1.7)
        text1 = TextMobject("Hmotnost je jako 332 981 Zemí.")
        text2 = TextMobject("Průměr je 1,4 mil. km.")
        text3 = TextMobject("Objem je roven 1,3 mil. Zemí.")
        text4 = TextMobject("Gravitace je 28x větší než na Zemi.")
        text5 = TextMobject("Povrchová teplota stoupá na 5780 K.")
        text6 = TextMobject("Teplota jádra přesahuje 15,7 mil. K.")
        text7 = TextMobject("Vodík")
        text8 = TexMobject(r"73,5\%")
        text9 = TextMobject("Helium")
        text10 = TexMobject(r"24,9\%")
        text11 = TextMobject("Kyslík")
        text12 = TextMobject("Uhlík")
        text13 = TextMobject("Železo")
        text14 = TextMobject("Neon...")
        text1.to_edge(LEFT, buff=1)
        text2.to_edge(LEFT, buff=1)
        text3.to_edge(LEFT, buff=1)
        text4.to_edge(LEFT, buff=1)
        text5.to_edge(LEFT, buff=1)
        text6.to_edge(LEFT, buff=1)
        text7.move_to(3*LEFT + 0.5*DOWN)
        text8.move_to(3*LEFT + 1*DOWN)
        text9.move_to(0.5*DOWN)
        text10.move_to(1*DOWN)
        text11.move_to(3*RIGHT + 0.5*DOWN)
        text12.move_to(2.9*RIGHT + 1*DOWN)
        text13.move_to(3*RIGHT + 1.5*DOWN)
        text14.move_to(3.05*RIGHT + 2*DOWN)
        text1.scale(1.2)
        text2.scale(1.2)
        text3.scale(1.2)
        text4.scale(1.2)
        text5.scale(1.2)
        text6.scale(1.2)
        vector=np.array([0,2.2,0])
        START = (0,2,0)
        END1 =  (-2,0,0)
        END2 =  (0,0,0)
        END3 = (2,0,0)
        line1 = Line(START, END1)
        line2 = Line(START, END2)
        line3 = Line(START, END3)
        group1 = VGroup(text11, text12, text13, text14)
        brace1 = Brace(group1, RIGHT, buff = SMALL_BUFF)
        text15 = brace1.get_text(r"1,6\%")

        self.add(image2)
        self.wait(5)
        self.play(Write(text1))
        self.wait(5)
        self.play(Transform(text1, text2))
        self.wait(5)
        self.play(Transform(text1, text3))
        self.wait(5)
        self.play(Transform(text1, text4))
        self.wait(5)
        self.play(Transform(text1, text5))
        self.wait(5)
        self.play(Transform(text1, text6))
        self.wait(5)
        self.play(FadeOut(text1))
        self.play(image2.move_to, vector)
        self.wait(5)
        self.play(ShowCreation(line1))
        self.play(Write(text7))
        self.play(Write(text8))
        self.play(ShowCreation(line2))
        self.play(Write(text9))
        self.play(Write(text10))
        self.play(ShowCreation(line3))
        self.play(Write(text11))
        self.play(Write(text12))
        self.play(Write(text13))
        self.play(Write(text14))
        self.play(Write(brace1), Write(text15))
        self.wait(5)
        self.play(FadeOut(brace1), FadeOut(text15), FadeOut(text14), FadeOut(text13), FadeOut(text12), FadeOut(text11),
                FadeOut(line3), FadeOut(text10), FadeOut(text9), FadeOut(line2), FadeOut(text7), FadeOut(text8), FadeOut(line1),
                    FadeOut(image2))
        self.wait(5)

class info03(Scene):
    def construct(self):
        image1 = ImageMobject("teplomer")
        image1.move_to(6.5*LEFT)
        image2 = ImageMobject("sun01")
        image2.move_to(5*RIGHT)
        image2.scale(1.2)
        image3 = ImageMobject("earth")
        image3.scale(1.1)
        image3.move_to(5*LEFT)
        image4 = ImageMobject("svetlo")
        image4.move_to(4*RIGHT)
        image5 = ImageMobject("stickman")
        image5.move_to(1.65*UP + 5.05*LEFT)
        image5.scale(0.7)
        image6 = ImageMobject("nuclearreactor")
        image6.scale(4)
        text1 = TextMobject("Velký třesk")
        text1.move_to([-5.5,-1,0])
        text2 = TextMobject("13,8 mld. let")
        text2.move_to([-5.5, -2.5,0])
        text3 = TextMobject("Zformovaní Slunce")
        text3.move_to([2, -1,0])
        text4 = TextMobject("4,6 mld. let")
        text4.move_to([2,-2.5,0])
        text5 = TextMobject("Současnost")
        text5.move_to([5.5,-1,0])
        text6 = TextMobject("05.07.2020")
        text6.move_to([5.5, -2.5, 0])
        vector = np.array([0,1.7,0])
        START1 = ([-5.5,-1.7,0])
        END1 = ([5.5,-1.7,0])
        START2 = ([-5.5,-1.42,0])
        END2 = ([-5.5,-2,0])
        START3 = ([2,-1.42,0])
        END3 = ([2,-2,0])
        START4 = ([5.5, -1.42,0])
        END4 = ([5.5, -2,0])
        line1 = Line(START1, END1)
        line2 = Line(START2, END2)
        line3 = Line(START3, END3)
        line4 = Line(START4, END4)
        
        



        self.play(FadeIn(image2), FadeIn(image3))
        self.wait(5)
        self.play(FadeIn(image4),run_time=2)
        self.play(image4.move_to, 4*LEFT)
        self.wait(3)
        self.play(FadeIn(image1))
        self.wait()
        self.play(FadeOut(image1), FadeOut(image4))
        self.wait(2)
        self.play(FadeIn(image5))
        self.wait(2)
        self.play(FadeOut(image3), FadeOut(image5))
        self.play(image2.move_to, vector)
        self.wait(2)
        self.play(ShowCreation(line1))
        self.wait(2)
        self.play(ShowCreation(line2))
        self.wait(2)
        self.play(Write(text1), Write(text2))
        self.wait()
        self.play(ShowCreation(line3))
        self.play(Write(text3), Write(text4))
        self.wait(4)
        self.play(text3.scale, 0.8, text4.scale, 0.8)
        self.play(ShowCreation(line4))
        self.wait()
        self.play(Write(text5), Write(text6))
        self.wait(3)
        self.play(FadeOut(line1),FadeOut(line2),FadeOut(text1),FadeOut(text2),FadeOut(line3),FadeOut(text3),FadeOut(text4),FadeOut(line4),FadeOut(text5),FadeOut(text6))
        self.wait(2)
        self.play(FadeOut(image2))
        self.wait(10)
        #wood burning
        self.play(FadeIn(image6))
        self.wait(2)
        self.play(FadeOut(image6))
        self.wait(8)


class casti(Scene):
    def construct(self):
        image1 = ImageMobject("sun03")
        image1.move_to(4*LEFT)
        image1.scale(2.5)
        text01 = TextMobject("Jádro - ")
        text02 = TextMobject("poloměru")
        text03 = TexMobject(r"20\%")
        text01.move_to([-3.7,3.5,0])
        text02.move_to([-0.5,3.5,0])
        text03.move_to([-2.25,3.5,0])

        text11 = TextMobject("Zářivá zóna - ")
        text12 = TextMobject("poloměru")
        text13 = TexMobject(r"50\%")
        text11.move_to([0.5, 1.5, 0])
        text12.move_to([4.35, 1.5, 0])
        text13.move_to([2.6, 1.5, 0])

        text21 = TextMobject("Konvektivní zóna - ")
        text22 = TextMobject("poloměru")
        text23 = TextMobject(r"30\%")
        text21.move_to([1.5,0.2,0])
        text22.move_to([5.95,0.2,0])
        text23.move_to([4.2,0.2,0])

        image2 = ImageMobject("sun04")
        image2.to_edge(DOWN)

        text001 = TextMobject("Fotosféra")
        text001.scale(1.5)
        text001.move_to(DOWN)
        text002 = TextMobject("Chromosféra")
        text002.scale(1.5)
        text002.move_to(UP)
        text003 = TextMobject("Koróna")
        text003.move_to(3*UP)
        text003.scale(1.5)

        start1 = ([-3.8, 0.2,0])
        end1 = ([-3.2,3 ,0])
        line1 = Line(start1, end1)
        
        start2 = ([-3.2, 0.8,0])
        end2 = ([-1,1.5,0])
        line2 = Line(start2, end2)
        
        start3 = ([-2.3, 0.2,0])
        end3 = ([-0.7,0.2,0])
        line3 = Line(start3, end3)
        

        self.play(FadeIn(image1))
        self.wait(5)
        self.play(ShowCreation(line1))
        self.play(Write(text01))
        self.play(Write(text03))
        self.play(Write(text02))
        self.wait(2)
        self.play(ShowCreation(line2))
        self.wait(2)
        self.play(Write(text11))
        self.play(Write(text13))
        self.play(Write(text12))
        self.wait(2)
        self.play(ShowCreation(line3))
        self.play(Write(text21))
        self.play(Write(text23))
        self.play(Write(text22))
        self.wait(2)
        self.play(FadeOut(line1), FadeOut(text01), FadeOut(text02), FadeOut(text03), FadeOut(line2), FadeOut(text11), FadeOut(text12), FadeOut(text13), FadeOut(line3), FadeOut(text21), FadeOut(text22), FadeOut(text23))
        self.wait()
        self.play(FadeOut(image1))
        self.play(FadeIn(image2))
        self.play(Write(text001))
        self.wait(2)
        self.play(Write(text002))
        self.wait(2)
        self.play(Write(text003))
        self.wait(5)
        self.play(FadeOut(image2), FadeOut(text001), FadeOut(text002), FadeOut(text003))
        self.wait(3)

class jadro01(Scene):
    def construct(self):
        text01 = TextMobject("Jádro")
        text01.move_to([0,2.5,0])
        text01.scale(2)

        text02 = TextMobject("Teplota je větší než 15 mil. K.")
        text03 = TextMobject("V jádru Slunce je gravitace natolik silná,")
        text03.move_to(0.5*UP)
        text04 = TextMobject("že je zde silný tlak, díky kterému dochází k termonuklearní fúzy.")
        text04.move_to(0.5*DOWN)
        text1 = TextMobject("Termonukleární fúze")
        text1.scale(2.5)
        
        text2 = TextMobject("Pohyb částic")
        text2.scale(1.5)
        text2.move_to([0,3,0])

        text3 = TextMobject("Odpudivé síly")
        text3.move_to([0,0.5,0])

        image1 = SVGMobject("circle", color=ORANGE)
        image1.move_to(4*LEFT)
        image2 = SVGMobject("circle", color=ORANGE)
        image2.move_to(4*RIGHT)

        arrow1 = Arrow(color=RED)
        arrow1.scale(2)
        arrow1.move_to(1.5*LEFT)

        arrow2 = Arrow(color=RED)
        arrow2.flip(UP)
        arrow2.scale(2)
        arrow2.move_to(1.5*RIGHT)

        self.play(Write(text01))
        self.wait()
        self.play(Write(text02))
        self.wait(3)
        self.play(FadeOut(text02))
        self.play(Write(text03))
        self.play(Write(text04))
        self.wait(2)
        self.play(FadeOut(text01), FadeOut(text03), FadeOut(text04))
        self.wait(2)
        self.play(Write(text1))
        self.wait(3)
        self.play(FadeOut(text1))
        self.wait(3)
        self.play(Write(text2))
        self.wait(2)
        self.play(DrawBorderThenFill(image1), DrawBorderThenFill(image2))
        self.wait(2)
        self.play(GrowArrow(arrow1), GrowArrow(arrow2), Write(text3))
        self.wait(2)
        self.play(FadeOut(text3),
                image1.move_to, 5*LEFT,
                image2.move_to, 5*RIGHT,
                arrow1.scale, 0.5,
                arrow1.move_to, 3.3*LEFT,
                arrow2.scale, 0.5,
                arrow2.move_to, 3.3*RIGHT,
                )
        self.wait(3)
        self.play(FadeOut(image1), FadeOut(image2), FadeOut(arrow1), FadeOut(arrow2), FadeOut(text2))
        self.wait(5)


class jadro02(Scene):
    CONFIG = {
        "amplitude": 0.4,
        "jiggles_per_second": 1,
    }
    def construct(self):
        text1 = TextMobject("Nad jádrem Slunce")
        text1.scale(1.5)
        text1.move_to(3.5*UP)
        
        text2 = TextMobject("Částice se")
        text2.to_edge(LEFT + UP)

        text3 = TextMobject("navzájem odpuzují")
        text3.to_edge(LEFT + 2.4*UP)

        text4 = TextMobject("kvůli odpudivé síle.")
        text4.to_edge(LEFT + 3.8*UP)

        text5 = TextMobject("Pohyb v jádru \\\\ "
                            "je naprostým chaosem.")
        text5.scale(2)

        points = VGroup(*[
            Dot(radius=0.1) for _ in range(25)
        ])
        points.arrange_in_grid(buff=0.8)
        for submob in points:
            submob.jiggling_direction = rotate_vector(
                RIGHT, np.random.random() * TAU *1.5,
            )
            submob.jiggling_phase = np.random.random() * TAU *1.5

        def update_mob(mob, dt):
            for submob in mob:
                submob.jiggling_phase += dt * self.jiggles_per_second * TAU
                submob.shift(
                    self.amplitude *
                    submob.jiggling_direction *
                    np.sin(submob.jiggling_phase) * dt
                )

        points.add_updater(update_mob)
        self.play(Write(text1))
        self.add(points)
        self.wait(5)
        self.play(Write(text2))
        self.play(Write(text3))
        self.play(Write(text4))
        self.wait(3)
        self.play(FadeOut(text1), FadeOut(text2), FadeOut(text3), FadeOut(text4), FadeOut(points))
        self.wait(2)
        self.play(Write(text5))
        self.wait()
        self.play(FadeOut(text5))
        self.wait(2)


class jadro03(Scene):
    CONFIG = {
            "amplitude": 25,
            "jiggles_per_second": 0.5,
                }
    def construct(self):
        
        text1 = TextMobject("V jádru Slunce")
        text1.scale(1.5)
        text1.move_to(3.5*UP)
        
        text2 = TextMobject("V jádru Slunce je vysoký tlak,\\\\"
                            "kvůli tomu zde částice do sebe narážejí.")
        text2.scale(1.5)
        text2.move_to(1*UP)

        text3 = TextMobject("Většina částic se od sebe jen odrazí,\\\\"
                            "ale některé překonají odpor a spojí se.")
        text3.scale(1.5)
        text3.move_to(1*DOWN)

        points = VGroup(*[
            Dot(radius=0.1) for _ in range(25)
        ])
        points.arrange_in_grid(buff=0.8)
        for submob in points:
            submob.jiggling_direction = rotate_vector(
                RIGHT, np.random.random() * TAU *1.5,
            )
            submob.jiggling_phase = np.random.random() * TAU *1.5

        def update_mob(mob, dt):
            for submob in mob:
                submob.jiggling_phase += dt * self.jiggles_per_second * TAU
                submob.shift(
                    self.amplitude *
                    submob.jiggling_direction *
                    np.sin(submob.jiggling_phase) * dt
                )

        points.add_updater(update_mob)
        self.play(Write(text1))
        self.wait(2)
        self.add(points)
        self.wait(10)
        self.play(points.scale, 0.2)
        self.play(Write(text2))
        self.wait(5)
        self.play(Write(text3))
        self.wait(5)
        self.play(FadeOut(text1), FadeOut(text2), FadeOut(text3), FadeOut(points))
        self.wait()


class fuze(Scene):
    def construct(self):
        text1 = TextMobject("Termonukleární fúze")
        text1.scale(2.5)
        
        text2 = TextMobject("1. Spojení protonů")
        text2.scale(1.5)
        text2.to_edge(UP)

        text3 = TextMobject("- proton H")
        text3.scale(0.75)
        text3.move_to(5.55*RIGHT+3.3*UP)

        image1 = ImageMobject("red.circle")
        image1.move_to(3*LEFT)
        target1 = np.array([-0.6,0,0])

        image2 = ImageMobject("red.circle")
        image2.move_to(3*RIGHT)
        target2 = np.array([0.6,0,0])

        
        image3 = ImageMobject("red.circle")
        image3.scale(0.3)
        image3.move_to(4.2*RIGHT + 3.3*UP)

        image4 = ImageMobject("grey.circle")
        image4.move_to(3*LEFT)
        image4.scale(1.1)

        image5 = ImageMobject("grey.circle")
        image5.scale(0.31)
        image5.move_to(4.2*RIGHT + 2.6*UP)
        
        text4 = TextMobject("- netron")
        text4.move_to(5.36*RIGHT+2.6*UP)
        text4.scale(0.75)

        circle1 = Circle()
        circle1.move_to(3*RIGHT)

        circle2 = Circle()
        circle2.move_to(3*LEFT)

        text5 = TextMobject("Deuterium \\\\ "
             "1 proton + 1 neutron")
        text5.move_to(2*DOWN+3.8*LEFT)

        arrow1 = Arrow(color=RED)
        arrow1.move_to(2.3*LEFT + 1*DOWN)
        arrow1.rotate(26*DEGREES)
            
        text6 = TextMobject("Při srážce se uvolnila energie \\\\ "
                            "a dala tak vzniknout positronu a neutrinu.")
        text6.to_edge(DOWN)

        text7 = TexMobject(r"\nu")
        text7.move_to(4.2*RIGHT + 2*UP)

        text8 = TextMobject("- neutrino")
        text8.scale(0.75)
        text8.move_to(5.5*RIGHT+2*UP)

        text9 = TexMobject(r"\nu")
        text9.scale(2)

        text10 = ImageMobject("white.circle")
        text10.scale(0.4)

        text11 = ImageMobject("white.circle")
        text11.move_to(4.2*RIGHT + 1.4*UP)
        text11.scale(0.3)

        text12 = TextMobject("- positron")
        text12.scale(0.75)
        text12.move_to(5.48*RIGHT+1.4*UP)


        self.play(Write(text1))
        self.wait(3)
        self.play(FadeOut(text1))
        self.wait()
        self.play(Write(text2))
        self.wait()
        self.play(FadeIn(image1), FadeIn(image2))
        self.add(text3, image3, circle1, circle2)
        self.wait(5)
        self.play(FadeOut(circle2), FadeOut(circle1))
        self.play(FadeOut(image1),
                FadeIn(image4),
                image4.move_to, target1,
                image1.move_to, target1,
                image2.move_to, target2,
                run_time=3)
        self.play(FadeIn(text9),
                     text9.move_to, 4.5*LEFT,
                     FadeIn(text10),
                     text10.move_to, 4.5*RIGHT)
        self.add(image5, text4, text7,text8, text11, text12)
        self.wait(3)
        self.play(GrowArrow(arrow1))
        self.play(Write(text5))
        self.wait(2)
        self.play(FadeOut(text5), FadeOut(arrow1))
        self.wait()
        self.play(Write(text6))
        self.wait(2)
        self.wait(2)
        self.play(FadeOut(text6))
        self.wait(2)
        self.play(FadeOut(text2),FadeOut(image5), FadeOut(text4), FadeOut(text7), FadeOut(text8), FadeOut(text11), FadeOut(text12), FadeOut(text9), FadeOut(text10), FadeOut(image4), FadeOut(text2), FadeOut(text3), FadeOut(image2), FadeOut(image3))
        self.wait(2)

class fuze02(Scene):
    def construct(self):
        text1 = TextMobject("2. Přidání protonu")
        text1.scale(1.5)
        text1.to_edge(UP)

        image1 = ImageMobject("red.circle")
        image1.move_to([-3,-0.6,0])

        image2 = ImageMobject("grey.circle")
        image2.move_to([-3, 0.6,0])

        image3 = ImageMobject("red.circle")
        image3.move_to(3*RIGHT)

        image4 = ImageMobject("red.circle")
        image4.scale(0.3)
        image4.move_to(4.2*RIGHT + 3.3*UP)

        text2 = TextMobject("- proton H")
        text2.scale(0.75)
        text2.move_to(5.55*RIGHT+3.3*UP)

        target1 = np.array([-0.6,-0.6,0])
        target2 = np.array([-0.6,0.6,0])
        target3 = np.array([0.6,0,0])

        image5 = ImageMobject("grey.circle")
        image5.scale(0.31)
        image5.move_to(4.2*RIGHT + 2.6*UP)
        
        text3 = TextMobject("- netron")
        text3.move_to(5.36*RIGHT+2.6*UP)
        text3.scale(0.75)

        text4 = TexMobject(r"\gamma")
        text4.move_to(4.2*RIGHT + 2*UP)

        text5 = TextMobject("- gamma\\\\"
                             "záření")
        text5.scale(0.75)
        text5.move_to(5.4*RIGHT+1.8*UP)

        text6 = TexMobject(r"\gamma")
        text6.scale(2)

        arrow1 = Arrow(color=RED)
        arrow1.move_to(2.3*LEFT + 1*DOWN)
        arrow1.rotate(26*DEGREES)

        text7 = TextMobject("Helium-3")
        text7.move_to(3.1*LEFT + 1.9*DOWN)

        image6 = ImageMobject("svetlo")
        image6.move_to(4*RIGHT)

        circle1 = Circle()
        circle1.move_to(3*RIGHT)

        self.play(Write(text1))
        self.wait()
        self.play(FadeIn(image1), FadeIn(image2), FadeIn(image3), FadeIn(circle1))
        self.add(text2, image4, text3, image5)
        self.wait(2)
        self.play(image1.move_to, target1,
                    image2.move_to, target2,
                    image3.move_to, target3,
                    circle1.move_to, target3)
        self.wait()
        self.play(FadeIn(text6), text6.move_to, 4*RIGHT)
        self.add(text5, text4)
        self.wait(2)
        self.play(GrowArrow(arrow1))
        self.play(Write(text7))
        self.wait(2)
        self.play(FadeOut(text7), FadeOut(arrow1))
        self.play(FadeOut(text6), FadeIn(image6))
        self.play(image6.move_to, 10*RIGHT, run_time=3)
        self.wait(5)
        self.play(FadeOut(text1),FadeOut(circle1), FadeOut(image2), FadeOut(image3), FadeOut(image1), FadeOut(image4), FadeOut(text2), FadeOut(text3), FadeOut(image5), FadeOut(text4), FadeOut(text5))
        self.wait()


class fuze03(Scene):
    def construct(self):
        image11 = ImageMobject("red.circle")
        image11.scale(0.3)
        image11.move_to(4.2*RIGHT + 3.3*UP)

        image12 = ImageMobject("grey.circle")
        image12.scale(0.31)
        image12.move_to(4.2*RIGHT + 2.6*UP)

        text2 = TextMobject("- netron")
        text2.move_to(5.36*RIGHT+2.6*UP)
        text2.scale(0.75)

        text3 = TextMobject("- proton H")
        text3.scale(0.75)
        text3.move_to(5.59*RIGHT+3.3*UP)

        text1 = TextMobject("3. Spojení s heliem")
        text1.scale(1.5)
        text1.to_edge(UP)

        image1 = ImageMobject("red.circle")
        image1.move_to(5.8*RIGHT+3*UP)
        image1.scale(0.4)

        image2 = ImageMobject("red.circle")
        image2.move_to(4*RIGHT+3*UP)
        image2.scale(0.4)

        image3 = ImageMobject("red.circle")
        image3.move_to(5.8*LEFT+3*UP)
        image3.scale(0.4)

        image4 = ImageMobject("red.circle")
        image4.move_to(4*LEFT+3*UP)
        image4.scale(0.4)

        circle1 = Circle()
        circle1.move_to(5.8*RIGHT+3*UP)
        circle1.scale(0.4)

        circle2 = Circle()
        circle2.move_to(5.8*LEFT+3*UP)
        circle2.scale(0.4)

        target1 = np.array(4.4*RIGHT+3*UP)
        target2 = np.array(4.4*LEFT+3*UP)

        arrow1 = Arrow(color = RED)
        arrow1.scale(0.7)
        arrow1.rotate(300*DEGREES)
        arrow1.move_to(4*LEFT+2*UP)

        arrow2 = Arrow(color = RED)
        arrow2.scale(0.7)
        arrow2.rotate(240*DEGREES)
        arrow2.move_to(4*RIGHT+2*UP)

        image5 = ImageMobject("grey.circle")
        image5.scale(0.4)
        image5.move_to(target1)

        image6 = ImageMobject("grey.circle")
        image6.scale(0.4)
        image6.move_to(target2)

        target3 = np.array(3.5*RIGHT+1*UP)
        target4 = np.array(3.5*LEFT+1*UP)

        image7 = ImageMobject("red.circle")
        image7.scale(0.4)
        image7.move_to(4*LEFT+3*UP)

        image8 = ImageMobject("red.circle")
        image8.scale(0.4)
        image8.move_to(4*RIGHT+3*UP)

        target5 = np.array(3.2*LEFT+1.1*UP)
        target6 = np.array(3.2*RIGHT+1.1*UP)

        image9 = ImageMobject("red.circle")
        image9.scale(0.4)
        image9.move_to(1.1*UP+5*LEFT)

        image10 = ImageMobject("red.circle")
        image10.scale(0.4)
        image10.move_to(1.1*UP+5*RIGHT)

        target7 = np.array(3.9*RIGHT+1.1*UP)
        target8 = np.array(3.9*LEFT+1.1*UP)

        target9 = np.array(3*RIGHT)
        target10 = np.array(3*LEFT)
        target11 = np.array(3.8*LEFT+1*UP)
        target12 = np.array(2.5*LEFT+1*UP)
        target13 = np.array(3.8*RIGHT+1*UP)
        target14 = np.array(2.5*RIGHT+1*UP)
        target15 = np.array(0.5*RIGHT+0.5*UP)
        target16 = np.array(0.5*RIGHT+0.5*DOWN)
        target17 = np.array(0.5*LEFT+0.5*UP)
        target18 = np.array(0.5*LEFT+0.5*DOWN)

        arrow3 = Arrow()
        arrow3.rotate(45*DEGREES)
        arrow3.scale(1.2)
        arrow3.move_to(2*LEFT+1.5*DOWN)

        text4 = TextMobject("Helium-4")
        text4.move_to(3*LEFT + 2.5*DOWN)

        text5 = TextMobject("Vzniklo helium-4\\\\ a odtrhly se 2 protony.")
        text5.to_edge(LEFT+UP)

        text6 = TextMobject("Poslední atom Helium-4 má menší hmotnost\\\\"
             "než původní 4 protony, které se spojily.\\\\ ")
        text6.move_to(0.75*UP)
        text7 = TextMobject("Zbytek se přeměnil na energii\\\\ a ta byla zforvovaná do tepla a světla.")
        text7.move_to(0.75*DOWN)

        text8 = TextMobject("Spojení protonů")
        text8.to_edge(UP)
        text8.scale(1.6)

        text9 = TextMobject("Zformování helia\\\\ a přidání protunu")
        text9.to_edge(UP)
        text9.scale(1.6)

        self.play(Write(text1))
        self.wait()
        self.play(FadeOut(text1))
        self.play(FadeIn(image1), FadeIn(image3))
        self.wait()
        self.play(FadeIn(image2), FadeIn(image4), FadeIn(circle1), FadeIn(circle2),
                    image1.move_to,target1,
                    circle1.move_to, target1,
                    image3.move_to, target2,
                    circle2.move_to, target2)
        self.play(Write(text8))
        self.wait()
        
        self.play(GrowArrow(arrow1), GrowArrow(arrow2))
        self.play(Transform(text8, text9))
        self.wait(2)
        self.play(
                    FadeIn(image7), FadeIn(image8), 
                    image7.move_to, target5, image8.move_to, target6,
                    FadeIn(image5), FadeIn(image6),
                    image5.move_to, target3,
                    image6.move_to, target4,)

        self.wait()

        self.play(FadeIn(image9), FadeIn(image10),
                    image9.move_to, target8,
                    image10.move_to, target7
                    )
        self.wait(5)
        self.play(FadeOut(text8), FadeOut(image1), FadeOut(image2), FadeOut(image3), FadeOut(image4), FadeOut(arrow1), FadeOut(arrow2), FadeOut(circle1), FadeOut(circle2))
        self.play(image5.scale,2,
        image6.scale,2,
        image7.scale,2,
        image8.scale,2,
        image9.scale,2,
        image10.scale,2)
        self.add(image11, image12, text2, text3)
        self.play(
                    image5.move_to, target9,
                    image6.move_to, target10,
                    image7.move_to,target12,
                    image8.move_to,target14,
                    image9.move_to,target11,
                    image10.move_to, target13,
                    )
        self.wait(2)
        self.play(
                image5.move_to, target15,
                image6.move_to, target16,
                image7.move_to, target17,
                image8.move_to, target18,
                image9.move_to, target18,
                image10.move_to, target17,
                )
        self.play(image9.move_to, 4*RIGHT,
                    image10.move_to, 4*LEFT,)
        self.wait(5)
        self.play(GrowArrow(arrow3))
        self.play(Write(text4))
        self.wait(2)
        self.play(Write(text5))
        self.wait(5)
        self.play(FadeOut(text5), FadeOut(text4), FadeOut(arrow3), FadeOut(image9), 
                    FadeOut(image10), FadeOut(image5), FadeOut(image6),
                    FadeOut(image7), FadeOut(image8), FadeOut(image11), FadeOut(image12), FadeOut(text2), FadeOut(text3))
        self.wait(5)
        self.play(Write(text6))
        self.wait(3)
        self.play(Write(text7))
        self.wait(5)
        self.play(FadeOut(text7), FadeOut(text6), run_time=3)


class zzona(Scene):
    CONFIG = {
            "amplitude": 0.6,
            "jiggles_per_second": 1.5,
                }
    def construct(self):
        
        points = VGroup(*[
            Dot(radius=0.3) for _ in range(1)
        ])
        points.arrange_in_grid(buff=0.8)
        for submob in points:
            submob.jiggling_direction = rotate_vector(
                RIGHT, np.random.random() * TAU *1.5,
            )
            submob.jiggling_phase = np.random.random() * TAU *1.5

        def update_mob(mob, dt):
            for submob in mob:
                submob.jiggling_phase += dt * self.jiggles_per_second * TAU
                submob.shift(
                    self.amplitude *
                    submob.jiggling_direction *
                    np.sin(submob.jiggling_phase) * dt
                )

        text1 = TextMobject("Vrstva v zářivé rovnováze\\\\neboli zářivá zóna")
        text1.scale(2)
        image1 = ImageMobject("sun03")
        image1.move_to(4*LEFT)
        image1.scale(2.5)

        text2 = TextMobject("Zářivá zóna - ")
        text3 = TextMobject("poloměru")
        text4 = TexMobject(r"50\%")
        text2.move_to([0.5, 1.5, 0])
        text3.move_to([4.35, 1.5, 0])
        text4.move_to([2.6, 1.5, 0])

        start1 = ([-3.2, 0.8,0])
        end1 = ([-1,1.5,0])
        line2 = Line(start1, end1)

        circle1 = Circle(color=RED)
        circle1.scale(8)
        circle1.move_to(12*LEFT)

        circle2 = Circle(color=RED)
        circle2.scale(8)
        circle2.move_to(3*LEFT)

        text5 = TextMobject("Jádro")
        text5.move_to(6*LEFT)
        text5.scale(1.8)

        image2 = ImageMobject("white.circle")
        image2.scale(0.35)
        image2.move_to(10*LEFT)

        target1 = np.array([0,0,0])

        text6 = TextMobject("Předpokládá se, že fotony touto vrstvou\\\\ projdou přibližně za 100 000 let.")
        text6.to_edge(UP)

        points.add_updater(update_mob)
        self.play(Write(text1))
        self.wait(5)
        self.play(FadeOut(text1))
        self.play(FadeIn(image1))
        self.wait(5)
        self.play(ShowCreation(line2))
        self.wait(2)
        self.play(Write(text2))
        self.play(Write(text4))
        self.play(Write(text3))
        self.wait(2)
        self.play(FadeOut(image1), FadeOut(line2), FadeOut(text2), FadeOut(text3), FadeOut(text4))
        self.wait(2)
        self.play(FadeIn(circle1), FadeIn(text5), FadeIn(image2), FadeIn(circle2))
        self.wait(5)
        self.play(image2.move_to, target1, run_time=2)
        self.add(points)
        self.play(FadeOut(image2), run_time=0.000000001)
        self.wait(10)
        self.play(Write(text6))
        self.wait(3)
        self.play(FadeIn(image2))
        self.play(FadeOut(points), run_time=0.000000001)
        self.play(image2.move_to, 8*RIGHT)
        self.wait(2)

class kzona02(Scene):
    def construct(self):
        text1 = TextMobject("Konvektivní zóna")
        text1.scale(2)

        image1 = ImageMobject("sun03")
        image1.move_to(4*LEFT)
        image1.scale(2.5)

        text2 = TextMobject("Konvektivní zóna - ")
        text3 = TextMobject("poloměru")
        text4 = TextMobject(r"30\%")
        text2.move_to([1.5,0.2,0])
        text3.move_to([5.95,0.2,0])
        text4.move_to([4.2,0.2,0])

        start1 = ([-2.3, 0.2,0])
        end1 = ([-0.7,0.2,0])
        line1 = Line(start1, end1)

        circle1 = Circle(color=RED)
        circle1.scale(8)
        circle1.move_to(12.5*LEFT)

        circle2 = Circle(color=RED)
        circle2.scale(8)
        circle2.move_to(6*LEFT)

        circle3 = Circle(color=RED)
        circle3.scale(8)
        circle3.move_to(1.8*LEFT)

        text5 = TextMobject("Jádro")
        text5.to_edge(LEFT)
        text5.scale(1.8)

        text6 = TextMobject("Zářivá zóna")
        text6.move_to(1.5*LEFT)
        text6.scale(1.8)

        image2 = ImageMobject("white.circle")
        image2.scale(0.35)
        image2.move_to(6*LEFT)

        image3 = ImageMobject("red.circle")
        image3.scale(0.35)
        image3.move_to(4.3*RIGHT)

        target1 = np.array(6.25*RIGHT)

        image4 = ImageMobject("blue.circle")
        image4.scale(0.35)
        image4.move_to(4.3*RIGHT)

        target2 = np.array(6*LEFT)


        self.play(Write(text1))
        self.wait()
        self.play(FadeOut(text1))
        self.wait(2)
        self.play(FadeIn(image1))
        self.wait(5)
        self.play(ShowCreation(line1))
        self.play(Write(text2))
        self.play(Write(text4))
        self.play(Write(text3))
        self.wait(5)
        self.play(FadeOut(image1), FadeOut(line1), FadeOut(text2), FadeOut(text3), FadeOut(text4))
        self.wait(2)
        self.play(FadeIn(circle1), FadeIn(circle2), FadeIn(circle3), FadeIn(text5), FadeIn(text6))
        self.wait(3)
        self.play(FadeIn(image2))
        self.play(image2.move_to, 8*RIGHT)
        self.wait()
        self.play(FadeIn(image3))
        self.wait(3)
        self.play(image3.move_to, target1, run_time=4)
        self.wait()
        self.play(FadeIn(image4))
        self.wait(3)
        self.play(image4.move_to, target2, run_time=4)
        self.wait(2)
        self.play(FadeOut(image4), FadeOut(image3), FadeOut(image2), FadeOut(circle1), FadeOut(circle2),
                FadeOut(circle3), FadeOut(text5), FadeOut(text6))
        self.wait(5)


class atmo(Scene):
    def construct(self):


        image1 = ImageMobject("sun04")
        image1.to_edge(DOWN)

        text1 = TextMobject("Fotosféra")
        text1.scale(1.5)
        text1.move_to(DOWN)
        text2 = TextMobject("Chromosféra")
        text2.scale(1.5)
        text2.move_to(UP)
        text3 = TextMobject("Koróna")
        text3.move_to(3*UP)
        text3.scale(1.5)

        text4 = TextMobject("\"povrch Slunce\"")
        text4.move_to(2.2*UP)

        text5 = TextMobject("Šířka:")
        text5.move_to(1.5*UP+2*LEFT)

        text7 = TextMobject("200-300 km")
        text7.move_to(1.43*UP+0.9*RIGHT)

        text6 = TextMobject("Teplota:")
        text6.move_to(0.5*UP+1.75*LEFT)

        text8 = TextMobject("6000 K")
        text8.move_to(0.5*UP+0.42*RIGHT)

        text9 = TextMobject("Chromosféra")
        text9.to_edge(UP)
        text9.scale(1.5)

        target1 = np.array(2.2*UP+2*LEFT)
        target2 = np.array(1.2*UP+1.75*LEFT)

        text10 = TextMobject("2000 km")
        text10.move_to(2.2*UP+0.7*RIGHT)

        text11 = TextMobject("4500-10000 K")
        text11.move_to(1.2*UP+1.2*RIGHT)

        text12 = TextMobject("Koróna")
        text12.to_edge(UP)
        text12.scale(1.5)

        text13 = TextMobject("miliony km")
        text13.move_to(2.1*UP+1.1*RIGHT)

        text14 = TextMobject("2 mil. K")
        text14.move_to(1.2*UP+0.8*RIGHT)

        image2 = ImageMobject("korona")
        image2.scale(3)

        self.play(FadeIn(image1))
        self.play(Write(text1))
        self.wait(2)
        self.play(Write(text2))
        self.wait(2)
        self.play(Write(text3))
        self.wait(5)
        self.play(FadeOut(text2), FadeOut(text3),
                text1.to_edge, UP)
        self.wait()
        self.play(Write(text4))
        self.wait()
        self.play(Write(text5))
        self.play(Write(text7))
        self.wait(2)
        self.play(Write(text6))
        self.play(Write(text8))
        self.wait(2)
        self.play(Transform(text1, text9), FadeOut(text4), FadeOut(text7), FadeOut(text8),
                    text5.move_to, target1,
                    text6.move_to, target2)
        self.wait(3)
        self.play(Write(text10))
        self.wait()
        self.play(Write(text11))
        self.wait(2)
        self.play(Transform(text1, text12), FadeOut(text10), FadeOut(text11))
        self.wait(3)
        self.play(Write(text13))
        self.wait()
        self.play(Write(text14))
        self.wait(2)
        self.play(FadeOut(text1), FadeOut(text14), FadeOut(text13), FadeOut(image1), FadeOut(text5), FadeOut(text6))
        self.wait(2)
        self.play(FadeIn(image2))
        self.wait(2)

class future(Scene):
    def construct(self):
        text1 = TextMobject("Slunce existuje přes 4,5 mld. let.")
        text1.scale(1.5)

        text2 = TextMobject("Za svou dobu existence\\\\ se zvětšilo o 6 procent.")
        text2.scale(1.5)

        text3 = TextMobject("Zásoby vodíku vystačí na 5 mld. let.")
        text3.scale(1.5)

        text4 = TextMobject("Když jádru dojde vodík, začne se smršťovat\\\\pod tíhou gravitace.\\\\Některé reakce ještě proběhnou\\\\ve vnějších vrstvách.")
        text4.scale(1.5)

        text5 = TextMobject("Jak se jádro smršťuje, zahřívá se\\\\a to ohřeje vnější vrstvy,\\\\které kvůli tomu začnou expandovat.")
        text5.scale(1.5)

        image1 = ImageMobject("red.circle")
        image1.scale(0.3)

        circle1 = Circle(color=RED)

        tex1 = TexMobject(r"{ F }_{ G }")
        tex1.move_to(1.5*RIGHT+0.4*UP)

        arrow1 = Arrow(color=BLUE)
        arrow1.move_to(1.35*RIGHT)
        arrow1.rotate(180*DEGREES)
        arrow1.scale(0.5)

        arrow2 = Arrow(color=ORANGE)
        arrow2.scale(0.5)
        arrow2.move_to(0.65*RIGHT)

        target1 = np.array(3.3*RIGHT+0.35*UP)
        
        text6 = TextMobject("Ze Slunce se stane rudý obr, \\\\jehož velikost bude sahat za orbitu Země.")
        text6.scale(1.5)

        text7 = TextMobject("Nakonec dojde i hélium, jádro se ochladí, \\\\horní vrstvy expandují\\\\ a budou se zbavovat materiálu.")
        text7.scale(1.5)

        text8 = TextMobject("Slunce se zchladí do bílého trpaslíka.")
        text8.scale(1.5)

        image2 = ImageMobject("sky")
        image2.scale(6)

        image3 = ImageMobject("white.dwarf")
        image3.scale(1.3)

        text9 = TextMobject("Z bílého trpaslíka se stane\\\\ nakonec stane černý trpaslík.")
        text9.to_edge(UP)

        text10 = TextMobject("Autor: Jakub Troják")
        text10.scale(1.3)

        self.play(Write(text1))
        self.wait(2)
        self.play(FadeOut(text1))
        self.play(Write(text2))
        self.wait(2)
        self.play(FadeOut(text2))
        self.play(Write(text3))
        self.wait(2)
        self.play(FadeOut(text3))
        self.play(Write(text4), run_time=2.5)
        self.wait(3)
        self.play(FadeOut(text4))
        self.play(Write(text5))
        self.wait(3)
        self.play(FadeOut(text5))
        self.wait()
        self.play(FadeIn(image1), FadeIn(circle1), FadeIn(arrow1), FadeIn(tex1), FadeIn(arrow2))
        self.wait(2)
        self.play(image1.scale, 0.3,
                circle1.scale, 3,
                arrow1.move_to, 3.3*RIGHT,
                arrow1.scale,0.8,
                arrow2.scale, 3,
                arrow2.move_to, 1.9*RIGHT,
                tex1.move_to, target1,
                tex1.scale,0.8,  run_time=5)
        self.wait(3)
        self.play(FadeOut(image1),FadeOut(circle1), FadeOut(arrow1), FadeOut(tex1), FadeOut(arrow2))
        self.wait(2)
        self.play(Write(text6))
        self.wait(3)
        self.play(FadeOut(text6))
        self.play(Write(text7))
        self.wait(2)
        self.play(FadeOut(text7))
        self.play(Write(text8))
        self.wait(2)
        self.play(FadeOut(text8))
        self.play(FadeIn(image2), run_time=3)
        self.wait(3)
        self.play(FadeIn(image3))
        self.wait(3)
        self.play(Write(text9), image2.fade, 0.75)
        self.wait(5)
        self.play(FadeOut(text9))
        self.play(FadeOut(image3), run_time=5)
        self.wait(5)
        self.play(Write(text10))
        self.wait(5)
        self.play(FadeOut(text10), run_time=4)
        self.wait(25)