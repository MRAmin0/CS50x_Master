from fpdf import FPDF


class PDF(FPDF):
    def header(self):
        # image name, X , Y , W , H
        self.image("shirtificate.png", 10, 65, 190, 190)

        # setting font and style
        self.set_font("helvetica", "B", 45)

        # allignment
        self.text(45, 45, "CS50 Shirtificate")

    def footer(self):
        self.set_font("helvetica", "B", 25)
        self.set_text_color(255, 255, 255)
        self.text(72, 140, a + " took CS50")


# pdf output
a = input("what's your name ? ").strip().Title()
filepdf = PDF()
filepdf.add_page
filepdf.output("shirtificate.pdf")
