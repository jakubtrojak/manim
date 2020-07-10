from manimlib.imports import *

class Test(GraphScene):
    def construct(self):
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