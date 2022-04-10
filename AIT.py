from manim import *

class Introduction_One(Scene):
    def construct(self):
        spot1 = Circle(radius = 0.5, color = PURPLE_D).set_fill(PURPLE_D, opacity = 1)
        spot2 = Circle(radius = 0.5, color = GREEN_D).set_fill(GREEN_D, opacity = 1)
        spot3 = Circle(radius = 0.5, color = RED_D).set_fill(RED_D, opacity = 1)
        spot4 = Circle(radius = 0.5, color = GOLD_D).set_fill(GOLD_D, opacity = 1)
        spot1.shift(3*UP)
        spot2.shift(1*UP)
        spot3.shift(1*DOWN)
        spot4.shift(3*DOWN)
        allspots = VGroup(spot1, spot2, spot3, spot4)
        box = SurroundingRectangle(allspots, buff = .1, color = BLUE)   
        allspots_plus_box = VGroup(allspots, box)
        function_notation = Text("f", color = WHITE, slant = ITALIC)
        function_notation.shift(5*LEFT)        
        number1_purple = Text("1")
        number1_green = Text("2")
        number1_red = Text("3")
        number1_gold = Text("4")
        number1_purple.shift(3*UP)
        number1_green.shift(1*UP)
        number1_red.shift(1*DOWN)
        number1_gold.shift(3*DOWN)
        number2_purple = Text("13")
        number2_green = Text("15")
        number2_red = Text("21")
        number2_gold = Text("26")
        number2_purple.shift(3*UP)
        number2_green.shift(1*UP)
        number2_red.shift(1*DOWN)
        number2_gold.shift(3*DOWN)
        arrow = Arrow(start = LEFT, end = RIGHT, buff = 0.5)
        arrow.shift(2*LEFT)
        introduction_text = Text("Rankings over \nStates of Nature")
        introduction_text.scale(0.80)
        introduction_text.shift(4.5*RIGHT + 3*UP)
        point_1 = Text("Belief Systems", color = BLUE)
        point_1.scale(0.70)
        point_1.shift(4.5*RIGHT + 1*UP)
        point_2 = Text("Monetary Incentive", color = BLUE)
        point_2.scale(0.70)
        point_2.shift(4.5*RIGHT)
        point_3 = Text("Individual Aspiration", color = BLUE)
        point_3.scale(0.70)
        point_3.shift(4.5*RIGHT + 1*DOWN)
        point_4 = Text("But what about \nGroup Decisions?", color = RED_D)
        point_4.scale(1)
        point_4.shift(4.5*RIGHT)
        
    
        
        self.play(FadeIn(allspots), run_time = 2)
        self.wait(1)
        self.play(ReplacementTransform(allspots, allspots_plus_box))
        self.play(ApplyMethod(allspots_plus_box.shift, 4*LEFT))
        self.add(function_notation)
        self.play(FadeIn(arrow))
        self.play(FadeIn(number1_purple, number1_green, number1_red, number1_gold), run_time = 2)
        self.wait(2)
        self.play(Transform(number1_purple, number2_purple), run_time = 1)
        self.play(Transform(number1_green, number2_green), run_time = 1)
        self.play(Transform(number1_red, number2_red), run_time = 1)
        self.play(Transform(number1_gold, number2_gold), run_time = 1)
        self.wait(2)
        self.play(Write(introduction_text))
        self.wait(3.75)
        self.play(Write(point_1))
        self.wait(1)
        self.play(Write(point_2))
        self.wait(1)
        self.play(Write(point_3))
        self.wait(2)
        self.play(FadeOut(introduction_text, point_1, point_2, point_3), run_time = 1)
        self.play(Write(point_4))
        self.wait(5)
        self.play(FadeOut(function_notation, allspots_plus_box, arrow, number1_purple, number1_green, number1_red, number1_gold, point_4), run_time = 1)

        
class Introduction_Two(Scene):
    def construct(self):
        swf_text = Text("Social Welfare Function")
        rankings_image = ImageMobject("C:\Manim\media\images\AIT/rank.png")
        rankings_image.scale(0.75)
        rankings_image.shift(3*RIGHT)
        question_one = Text("Would society reach \nan outcome?")
        question_two = Text("Would the outcome \nbe democratic?")
        question_one.scale(0.75)
        question_two.scale(0.75)
        question_one.shift(1*UP + 4*LEFT)
        question_two.shift(1*DOWN + 4*LEFT)
        box_two = SurroundingRectangle(question_one, buff = 0.1, color = RED_D)

        self.play(Write(swf_text), run_time = 5)
        self.wait(4)
        self.play(ApplyMethod(swf_text.shift, 3*UP))
        self.play(FadeIn(rankings_image))
        self.wait(5)
        self.play(Write(question_one), run_time = 5)
        self.wait(2)
        self.play(Write(question_two), run_time = 5)
        self.wait(4)
        self.play(FadeIn(box_two), run_time = 0.75)
        self.wait(7)

class Condorcet(Scene):
    def construct(self):
        table = Table(
            [["LoTR", "Dune", "Harry Potter"],
             ["Dune", "Harry Potter", "LoTR"],
             ["Harry Potter", "LoTR", "Dune"]],
             row_labels = [Text("1"), Text("2"), Text("3")],
             col_labels = [Text("Member 1"), Text("Member 2"), Text("Member 3")],
             top_left_entry = Text("Rank"), include_outer_lines = True)
        
        table.add(table.get_cell((2,2), color = GREEN))
        table.add(table.get_cell((3,4), color = GREEN))
        table.add(table.get_cell((4,2), color = GREEN))        
        table.scale(0.60)
        title = Text("The Condorcet Paradox", color = GREEN)
    

        self.play(Write(title), run_time=5)
        self.wait(3)
        self.play(ApplyMethod(title.shift, 3.5*UP), run_time = 3)
        self.wait(2)
        self.play(Write(table), run_time = 15)
        self.wait(1.5)


class Assumptions_One(Scene):
    def construct(self):
        arrow_image = ImageMobject("C:\Manim\media\images\AIT/arrow.jpg")
        arrow_image.scale(1.95)
        caption = Text("Kenneth Arrow")
        caption.scale(0.75)
        caption.shift(2.5*UP)
        text_one = Text("Voting Mechanism")
        text_two = Text("""
                        Properties of the
                          Voting Mechanism
                         """)
        text_one.scale(0.75)
        text_two.scale(0.75)
        text_one.shift(3.5*RIGHT + 2.5*UP)
        text_two.shift(3*RIGHT + 2.5*DOWN)
        arrow_one = Arrow([3.50, 2.0, 0.0], [3.50, -2.00, 0.0], buff = 0.1, color = RED_D)
        arrow_two = Arrow([3.50, -2.00, 0.0], [3.50, 2.0, 0.0], buff = 0.1, color = GREEN)

        self.play(FadeIn(arrow_image))
        self.add(caption)
        self.wait(2)
        self.remove(caption)
        self.play(ApplyMethod(arrow_image.shift, 4*LEFT), run_time = 1.5)
        
        self.play(Write(text_one), run_time = 0.75)
        self.wait(1)
        self.play(Write(text_two), run_time = 0.75)
        self.play(Write(arrow_one))
        self.wait(4)
        self.play(Transform(arrow_one, arrow_two), run_time = 3)
        self.wait(4)

class Transition(Scene):
    def construct(self):
        swf_text = Text("Social Welfare Function")
        swf_text.shift(3*UP)
        rankings_image = ImageMobject("C:\Manim\media\images\AIT/rank.png")
        rankings_image.scale(0.75)
        rankings_image.shift(3*RIGHT)
        question_one = Text("Would society reach \nan outcome?")
        question_two = Text("Would the outcome \nbe democratic?")
        question_one.scale(0.75)
        question_two.scale(0.75)
        question_one.shift(1*UP + 4*LEFT)
        question_two.shift(1*DOWN + 4*LEFT)
        box_two = SurroundingRectangle(question_one, buff = 0.1, color = RED_D)
        box_three = SurroundingRectangle(question_two, buff = 0.1, color = RED_D)
        
        self.add(swf_text, rankings_image, question_one, question_two, box_two)
        self.wait(1)
        self.play(Transform(box_two, box_three), run_time=3)
        self.wait(6)

class Assumptions_Two(Scene):
    def construct(self):
        circle_one = Circle(radius = 2, color = BLUE_A).set_fill(color = BLUE_A, opacity = 1)
        circle_two = Circle(radius = 2, color = BLUE_C).set_fill(color = BLUE_C, opacity = 1)
        circle_three = Circle(radius = 2, color = BLUE_E).set_fill(color = BLUE_E, opacity = 1)
        text_one = Text("Existence")
        text_two = Text("Paradoxes")
        text_three = Text("Democracy")
        circle_one.shift(5*LEFT)
        circle_three.shift(5*RIGHT)
        text_one.move_to(circle_one)
        text_two.move_to(circle_two)
        text_three.move_to(circle_three)
        axiom_one = Text("Unrestricted Domain: works for all \ncombinations of preferences").scale(0.60)
        axiom_three = Text("Well-Behaved: Social Preferences are \nComplete, Reflexive & Transitive").scale(0.60)
        axiom_two = Text("Pareto: if everyone likes LoTR over HP, \nsocial ranking reflects the same").scale(0.60)
        axiom_four = Text("IIA: Unrelated options don't cause preference \nreversion over current options").scale(0.55)
        axiom_five = Text("No Pivotal Voter: Everyone's preferences count \nin societal decisions").scale(0.50)
        rectangle_one = Rectangle(height = 1.5, width = 8, color = BLUE_A)
        rectangle_two = Rectangle(height = 1.5, width = 8, color = BLUE_A)
        rectangle_three = Rectangle(height = 1.5, width = 8, color = BLUE_C)
        rectangle_four = Rectangle(height = 1.5, width = 8, color = BLUE_C)
        rectangle_five = Rectangle(height = 1.5, width = 8, color = BLUE_E)
        rectangle_one.shift(3*RIGHT + 1.5*UP)
        rectangle_two.shift(3*RIGHT + 1.5*DOWN)
        rectangle_three.shift(3*RIGHT + 1.5*UP)
        rectangle_four.shift(3*RIGHT + 1.5*DOWN)
        rectangle_five.shift(3*RIGHT)
        axiom_one.move_to(rectangle_one)
        axiom_two.move_to(rectangle_two)
        axiom_three.move_to(rectangle_three)
        axiom_four.move_to(rectangle_four)
        axiom_five.move_to(rectangle_five)
        heading = Text("All of Arrow's Axioms").scale(0.70)
        heading.shift(3*UP)
        summary = Text('''
                        1. Unrestricted Domain
                        2. Complete, Reflexive and Transitive Social Preferences
                        3. The weak Pareto Criterion
                        4. Independence of Irrelevant Alternatives
                        5. No Dictator'''
                       ).scale(0.55)
        
        contradiction = SurroundingRectangle(summary, color = RED, buff = 0.5)
        line_1 = Line([-5, -1.5, 0], [5, 1.5, 0], color = RED)
        line_2 = Line([-5, 1.5, 0], [5, -1.5 ,0], color = RED)
        
        self.play(FadeIn(circle_one, text_one))
        self.wait(1)
        self.play(FadeIn(circle_two, text_two))
        self.wait(1)
        self.play(FadeIn(circle_three, text_three))
        self.wait(3)
        self.remove(circle_two, circle_three, text_two, text_three)
        self.add(rectangle_one, axiom_one, rectangle_two, axiom_two)
        self.wait(19)
        self.play(ReplacementTransform(circle_one, circle_two), ApplyMethod(circle_two.shift, 5*LEFT), ReplacementTransform(text_one, text_two), ApplyMethod(text_two.shift, 5*LEFT), ReplacementTransform(rectangle_one, rectangle_three), ReplacementTransform(axiom_one, axiom_three), ReplacementTransform(rectangle_two, rectangle_four), ReplacementTransform(axiom_two, axiom_four), run_time = 3)
        self.wait(38)
        self.remove(rectangle_four, axiom_four)
        self.play(ReplacementTransform(circle_two, circle_three), ApplyMethod(circle_three.shift, 10*LEFT), ReplacementTransform(text_two, text_three), ApplyMethod(text_three.shift, 10*LEFT), ReplacementTransform(rectangle_three, rectangle_five), ReplacementTransform(axiom_three, axiom_five), run_time = 3)
        self.wait(20)
        self.remove(circle_three, text_three, rectangle_five, axiom_five)
        self.play(Write(heading), Write(summary), run_time = 3)
        self.wait(1)
        self.add(contradiction)
        self.wait(5)
        self.play(GrowFromCenter(line_1), GrowFromCenter(line_2), run_time = 2)
        
        self.wait(8)
      

class Proof(Scene):
    def construct(self):
        
        voter = Circle(color = GOLD_D, radius = 0.1).set_fill(color = GOLD_D, opacity = 1)
        group = VGroup(*[voter.copy() for i in range(11)])
        group.arrange(RIGHT)
        group1 = VGroup(*[group.copy() for i in range(11)])
        group1.arrange(DOWN)
        heading = Text("N Voters", color = RED_E)
        heading.scale(0.75)
        heading.shift(UP*3)
        newvoter = Circle(color = GOLD_D, radius = 0.1).set_fill(color = GOLD_D, opacity = 1)
        dictator = Circle(color = RED_E, radius = 0.1).set_fill(color = RED_E, opacity = 1)
        decisive = ImageMobject("C:\Manim\media\images\AIT/decisive.png")
        decisive.scale(1.40)
        decisive.shift(2.5*LEFT)
        person1 = Text("I'd choose A over B.").scale(0.65)
        person1.shift(1.5*UP)
        person2 = Text("I like A over B too!").scale(0.65)
        person2.shift(0.5*UP)
        person3 = Text("B over A, any day!").scale(0.65)
        person3.shift(0.5*DOWN)
        person4 = Text("I like A better than B.").scale(0.65)
        person4.shift(1.5*DOWN)
        allpeople = VGroup(person1, person2, person3, person4)
        allpeople.shift(5*RIGHT)
        
        highlight = SurroundingRectangle(person3, color = RED_E)

        buttonone = Ellipse(width = 2, height = 1, color = BLUE_E).set_fill(color = BLUE_E, opacity = 1)
        buttonone.shift(3.2*UP + 4*LEFT)
        textone = Text("No Dictator").scale(0.40)
        textone.move_to(buttonone)
        buttontwo = Ellipse(width = 2, height = 1, color = BLUE_D).set_fill(color = BLUE_D, opacity = 1)
        buttontwo.shift(3.2*UP)
        texttwo = Text("Transitivity").scale(0.40)
        texttwo.move_to(buttontwo)
        buttonthree = Ellipse(width = 2, height = 1, color = BLUE_C).set_fill(color = BLUE_C, opacity = 1)
        buttonthree.shift(3.2*UP + 4*RIGHT)
        textthree = Text("IIA").scale(0.5)
        textthree.move_to(buttonthree)
        set_one = Circle(radius = 1.5, color = GOLD_D).set_fill(color = GOLD_D, opacity = 0.3)
        set_two = SurroundingRectangle(group1, color = GOLD_D).set_fill(color = GOLD_D, opacity = 0.3)
        group_on_left = group.arrange(DOWN)
        group_on_left.shift(6.85*LEFT)
        group_on_left.set_color_by_gradient(MAROON_E, GREEN_E)
        rectangle_S = Rectangle(height = 1.5, width = 10, color = MAROON_E).set_fill(color = MAROON_E, opacity = 0.8)
        rectangle_S.shift(1.68*LEFT + 1.62*UP)
        
        rectangle_S1 = Rectangle(height = 0.90, width = 10, color = MAROON_A).set_fill(color = MAROON_A, opacity = 0.8)
        rectangle_S1.shift(1.68*LEFT + 1.90*UP)
        rectangle_S2 = Rectangle(height = 0.90, width = 10, color = MAROON_B).set_fill(color = MAROON_B, opacity = 0.8)
        rectangle_S2.shift(1.68*LEFT + 0.70*UP)
        set_S = VGroup(rectangle_S1, rectangle_S2)
        rectangle_S3 = Rectangle(height = 2.2, width = 10, color = GREEN_E).set_fill(color = GREEN_E, opacity = 0.8)
        rectangle_S3.shift(1.68*LEFT + 1.2*DOWN)
        S1 = Text("one arbitrary member of set S").move_to(rectangle_S1)
        S1.scale(0.50)
        S2 = Text("everyone else from set S").move_to(rectangle_S2)
        S2.scale(0.50)
        S3 = Text("everyone else in society").move_to(rectangle_S3)
        S3.scale(0.50)

        brace = BraceBetweenPoints([3.2, 2, 0],[3.2, 0.4, 0], direction = [1, 0, 0 ])

        SPref = Text("LoTR > Dune", color = MAROON_E).scale(0.50)
        NminusSPref = Text("Dune > LoTR", color = GREEN_E).scale(0.50)
        SPref.next_to(brace, RIGHT)
        NminusSPref.next_to(rectangle_S3, RIGHT)

        IIA_Activation = Ellipse(width = 2, height = 1, color = RED_C).set_fill(color = RED_C, opacity = 1)
        IIA_Activation.shift(3.2*UP + 4*RIGHT)

        s11 = Text("LoTR > Dune > ", color = MAROON_A).scale(0.50)
        s12 = Text("HP", color = WHITE).scale(0.50)
        s12.next_to(s11, RIGHT)
        S1Pref = VGroup(s11, s12)
        S1Pref.next_to(rectangle_S1)

        s21 = Text("HP ", color = WHITE).scale(0.50)
        s22 = Text("> LoTR > Dune", color = MAROON_B).scale(0.50)
        s22.next_to(s21, RIGHT)
        S2Pref = VGroup(s21, s22)
        S2Pref.next_to(rectangle_S2)

        TotalS = VGroup(S1Pref, S2Pref)

        s31 = Text("Dune > ", color = GREEN_E).scale(0.50)
        s32 = Text("HP", color = WHITE).scale(0.50)
        s32.next_to(s31, RIGHT)
        s33 = Text(" > LoTR", color = GREEN_E).scale(0.50)
        s33.next_to(s32, RIGHT)
        S3Pref = VGroup(s31, s32, s33)
        S3Pref.next_to(rectangle_S3)

        DunetoHP = Text(" > ").scale(1.5)
        HPtoDune = Text(" < ").scale(1.5)
        HPinDune = Text(" ~ ").scale(1.5)

        DunetoHP.shift(4*LEFT + 3.2*DOWN)
        HPtoDune.shift(4*RIGHT + 3.2*DOWN)
        HPinDune.shift(3.2*DOWN)

        crossingHPtoDune = Cross(HPtoDune, stroke_color = RED_D, stroke_width = 6, scale_factor = 1.2)

        weakpreference = VGroup(DunetoHP, HPinDune)
        weakpreferencefinal = Text("Dune weakly preferred to HP").scale(0.65)
        weakpreferencefinal.shift(3.2*DOWN)

        Transitivity_Activation = Ellipse(width = 2, height = 1, color = RED_C).set_fill(color = RED_C, opacity = 1)
        Transitivity_Activation.shift(3.2*UP)

        part1 = Text("LoTR preferred to ", color = RED_D).scale(0.65)
        part2 = Text("Dune weakly preferred to HP", color = WHITE).scale(0.65)
        part2.next_to(part1, RIGHT)
        transitive_text = VGroup(part1, part2).shift(3.2*DOWN + 3*LEFT)

        
        dictator_highlight = SurroundingRectangle(S1Pref)
        dictator_activation = Ellipse(width = 2, height = 1, color = RED_C).set_fill(color = RED_C, opacity = 1).shift(3.2*UP + 4*LEFT)
    
            
    


        
        self.play(Write(group1), Write(heading), run_time = 10)
        self.wait(5)
        self.add(dictator)
        self.wait(15)
        self.remove(group1, heading, dictator)
        self.add(decisive)
        self.wait(10)
        self.play(Write(allpeople))
        self.wait(10)
        self.add(highlight)
        self.wait(33)
        self.play(FadeIn(buttonone, textone, buttontwo,texttwo, buttonthree, textthree), run_time = 2)
        self.wait(10)
        self.remove(allpeople, highlight, decisive)
        self.wait()
        self.play(FadeIn(group1))
        self.play(GrowFromCenter(set_one))
        self.wait(13)
        self.play(ReplacementTransform(set_one, set_two))
        self.wait(45)
        self.remove(set_two)
        self.play(Transform(group1, group_on_left), run_time = 4)
        self.add(rectangle_S)
        self.wait(60)
        self.play(ReplacementTransform(rectangle_S, set_S), run_time = 4)
        self.wait(8)
        self.play(FadeIn(rectangle_S3))
        self.wait(19)
        self.play(Write(S1), Write(S2), Write(S3))
        self.wait(19)
        self.play(Create(brace))
        self.play(Write(SPref), Write(NminusSPref))
        self.wait(16)
        self.play(Transform(buttonthree, IIA_Activation))
        self.wait()
        self.remove(brace)
        self.play(Transform(SPref, TotalS), Transform(NminusSPref, S3Pref), run_time = 3)
        self.wait(31)
        self.play(FadeIn(DunetoHP), FadeIn(HPtoDune), FadeIn(HPinDune), run_time = 3)
        self.wait(22)
        self.play(Create(crossingHPtoDune))
        self.wait(14)
        self.remove(crossingHPtoDune, HPtoDune)
        self.play(ReplacementTransform(weakpreference, weakpreferencefinal), run_time = 3)
        self.wait(7)
        self.play(Transform(buttontwo, Transitivity_Activation), ReplacementTransform(weakpreferencefinal, transitive_text), run_time = 2)
        self.wait(20)
        self.play(Write(dictator_highlight))
        self.play(Transform(buttonone, dictator_activation), run_time = 1)
        self.wait(18)



class Discussion(Scene):
    def construct(self):

        question_1 = Text("But why so impossible?", color = BLUE_C).scale(0.80)
        left1 = Text("left", color = GREEN).scale(0.50)
        center1 = Text("center", color = RED).scale(0.50)
        center1.next_to(left1, RIGHT)
        first = VGroup(left1, center1)
        left2 = Text("left", color = RED).scale(0.50)
        center2 = Text("center", color = GREEN).scale(0.50)
        center2.next_to(left2, RIGHT)
        right = Text("right", color = RED).scale(0.50)
        right.next_to(center2, RIGHT)
        second = VGroup(left2, center2, right)
        arrow1 = Arrow([0,2.7,0], [-3.5, 1.3, 0], color = BLUE)
        text1 = Text("Assumptions").scale(0.70)
        text1.shift(3.5*LEFT + UP)
        first.next_to(text1, DOWN)
        second.next_to(text1, 2*DOWN)
        first_copy = first.copy().next_to(text1, DOWN)
        arrow2 = Arrow([0, 2.7, 0], [0, 0, 0], color = BLUE)
        text2 = Text('''
                       Relax
                    Transitivity
                    '''
                     ).scale(0.60)
        text2.shift(DOWN*0.35)
        arrow3 = Arrow([0,2.7,0], [3.5, 1.3, 0], color = BLUE)
        text3 = Text('''
                     Dictator in
                       S1 is ~
                     '''
                      ).scale(0.65)
        text3.shift(0.7*UP + 3.5*RIGHT)

        rectangle_S1 = Rectangle(height = 0.90, width = 10, color = MAROON_A).set_fill(color = MAROON_A, opacity = 0.8)
        rectangle_S1.shift(2.5*DOWN)
        S1 = Text("one arbitrary member of set S").move_to(rectangle_S1)
        S1.scale(0.50)
        question_mark = Text("?", stroke_width = 4, color = RED).scale(2.5)
        question_mark.move_to(rectangle_S1)
        question_2 = Text("Who is the dictator?", color = BLUE_C).scale(0.70)
        question_2.shift(1.5*DOWN)
        
        self.play(Write(question_1), run_time = 4)
        self.wait(15)
        self.play(ApplyMethod(question_1.shift, 3*UP))
        self.wait(10)
        self.play(Create(arrow1), Write(text1), Write(first), Write(first_copy), run_time = 5)
        self.wait(10)
        self.play(ReplacementTransform(first, second))
        self.wait(27)
        self.play(Create(arrow2), Write(text2), run_time = 5)
        self.wait(10)
        self.play(Create(arrow3), Write(text3), run_time = 5)
        self.wait(10)
        self.play(Write(question_2), run_time = 3)
        self.wait(2)
        self.play(FadeIn(rectangle_S1), Write(S1))
        self.play(FadeIn(question_mark))
        self.wait(42)
        
        
        
        
        

       


   
        




























        

