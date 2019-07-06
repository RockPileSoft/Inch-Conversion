#Inch conversion app. 7/6/19
from guizero import App, Text, PushButton, TextBox, Box, warn, ButtonGroup
from fractions import Fraction

#blanks all fields
def reset():
    input_box.value = ""
    fraction_answer.value = ""
    mm_answer.value = ""

#Converts to mm or inches depening on which button is selected
def convert():
    
    to_fraction = input_box.value
    
    if conversion_choice.value == "MM":
        try:
            to_fraction = Fraction(to_fraction)
            
            mm_answer.value = str(round((to_fraction / 25.4),2))
        except:
            reset()
            warn("Conversion Error!", "Please enter a valid value.")
    else:
        try:
            to_fraction = Fraction(to_fraction)
            fraction_answer.value = to_fraction
            mm_answer.value = str(to_fraction * 25.4)
        except:
            reset()
            warn("Conversion Error!", "Please enter a valid value.")


#updates display for inch or mm conversion
def inches_or_mm():
    if conversion_choice.value == "MM":
        input_label.value = "Enter Milimeters: "
        mm_label.value = " Inches: "
        fraction_label.visible = False
        fraction_answer.visible = False
    else:
        input_label.value = "Enter Decimal: "
        mm_label.value = "MM: "
        fraction_label.visible = True
        fraction_answer.visible = True
    reset()

#main app display
app = App(bg="gainsboro",layout="grid", title="Rockpile Conversion App", height=210,width=415)

#divider for text boxes and labels
info_box=Box(app, layout="grid", width=408,height=100,border=False, grid=[0,0])

#entry box and label
input_label = Text(info_box,size=24, color="black", text="Enter Decimal: ",grid=[0,0],align="right")
input_box = TextBox(info_box,width=15, grid=[1,0])
input_box.bg="white"

#to display fractions
fraction_label = Text(info_box,size=24,color="black", text="Fractional Inches: ",grid=[0,1],align="right")
fraction_answer = Text(info_box,color="black",size=24,grid=[1,1])

#radion buttons
conversion_choice = ButtonGroup(info_box, options=["Inches", "MM"],command=inches_or_mm, selected="Inches", grid=[0,2],align="left")

#to display mm
mm_label = Text(info_box, text="MM: ",color="black",size=24,grid=[0,2],align="right")
mm_answer = Text(info_box,color="black", size=24,grid=[1,2])

#divider for buttons
button_box=Box(app, layout="grid", width="fill",height=100,border=False, grid=[0,3])

#spacer for alignment purposes
spacer_1= Text(button_box,size=24,color="black", text="",grid=[0,0])

#buttons
convert_button = PushButton(button_box, text="Convert",width=15,command=convert,grid=[1,1],align="right")

#spacer for alignment purposes
spacer_2= Text(button_box,size=24,text="         ",grid=[2,1])
reset_button = PushButton(button_box, text="Reset",width=15,command=reset,grid=[3,1])

#updates display
app.display()
