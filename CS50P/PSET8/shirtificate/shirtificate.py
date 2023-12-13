from fpdf import FPDF
class PDF(FPDF):
    def header(self):
        # image name, X , Y , W , H
        self.image("shirtificate.png", 10, 65 , 190 , 190)

        # setting font and style
        self.set_font("helvetica","B",45)

        # allignment
        self.text(45,45,"CS50 Shirtificate")

        
