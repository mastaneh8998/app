import customtkinter
from PIL import Image
import os

# //////////////////////////////////////////
app = customtkinter.CTk()
app.title("Calcualtor")
app.resizable(False,False)
icon = "img//icon.ico"
app.iconbitmap(icon)

app.geometry("395x500")
customtkinter.set_appearance_mode("light")
text_num = ""
equation = ""
result_num = ""
c_y= 0


# //////////////////////////////////////////

font_text = customtkinter.CTkFont(family = 'Arial' , size= 20 )
font_bold = customtkinter.CTkFont(family = 'Arial', size=27, weight="bold")
numbers = customtkinter.CTkLabel(app ,corner_radius=0 , text ="" ,font=font_text ,width = 400  ,text_color="#6898a8" , height = 100 , fg_color = "#f5f5f5")
numbers.place(x=0 , y=0)

result = customtkinter.CTkLabel(app , corner_radius=0  , text ="",font=font_bold ,width = 400 , height = 100 ,text_color="#6898a8" , fg_color = "#f5f5f5"  )
result.place(x=0 , y=80)

def write(num,num1):
    global equation
    global text_num
    if num1 != "=":
        equation += num1

        
    if c_y == 1 and num != "=":
        if text_num[-1] == "=":
            text_num = text_num[:-1]
            text_num += num
        else:
            text_num += num
    else:
        text_num += num
  
    numbers.configure(text=text_num)
    
    
def clear():
    global equation
    global text_num
    global c_y
    c_y=0
    text_num =""
    equation = ""
    result_num = " "
    numbers.configure(text=equation)
    result.configure(text=result_num)



def cdef():
    global equation
    global text_num
    global c_y
    
    if equation != "":
        equation = equation[:-1]
        if text_num[-1]== '=':
            text_num = text_num[:-2]
            numbers.configure(text=equation)
        else:
            text_num = text_num[:-1]
            numbers.configure(text=equation)
            
            
    

def calcuator():
    global equation
    global text_num
    global c_y
    write("=" , "=")
    if equation != "":
        try:
            result_num = eval(equation)
            c_y=1
        except:
            result_num = "Error!"
            
    result.configure(text=result_num)
    

current_path = os.path.dirname(os.path.realpath(__file__))                                          
click_btn= customtkinter.CTkImage(Image.open(current_path+"//img//result.png"),size=(50, 30))
btn_delete = customtkinter.CTkButton(app ,image=click_btn , command=cdef , width=90 , height=40 , fg_color = "#265073")
btn_delete.configure(text="", font= font_text ,corner_radius=6  , border_width=0 , border_color="#3887BE", border_spacing=0, anchor="center")
btn_delete.place(x=295 , y=210)
# # /////////////////////////////
button_c = customtkinter.CTkButton(app,command = clear ,corner_radius=6 ,text="C", font = font_text , width = 90   , height= 40 , fg_color ="#265073",border_color="#000000"  )
button_c.place(x=200, y=210)
# # /////////////////////////////
button_multiplied = customtkinter.CTkButton(app,command = lambda:write('x' ,"*") ,corner_radius=6 ,text="x", font = font_text, width = 90   , height= 40 , fg_color = "#265073" ,border_color="#000000"  )
button_multiplied.place(x=105, y=210)
# # /////////////////////////////
button_divided = customtkinter.CTkButton(app,command = lambda:write('÷' ,"/") ,corner_radius=6 ,text="÷", font = font_text, width =90   , height= 40 , fg_color = "#265073" ,border_color="#000000")
button_divided.place(x=10, y=210)
# /////////////////////////////////////////////////////////////////////////////////////////////////////////////

btn_minus = customtkinter.CTkButton(app , width=90 , height=40 , fg_color = "#265073")
btn_minus.configure(text="-" ,command =  lambda:write('-' ,"-") , font= font_text ,corner_radius=6  , border_width=0 , border_color="#000000", border_spacing=0, anchor="center")
btn_minus.place(x=295 , y=270)
# # /////////////////////////////
button_9 = customtkinter.CTkButton(app,command = lambda:write("9" , "9") ,corner_radius=6 ,text="9", font = font_text , width = 90   , height= 40 , fg_color = "#6898a8",border_color="#000000"  )
button_9.place(x=200, y=270)
# # /////////////////////////////
button_8 = customtkinter.CTkButton(app,command =  lambda:write("8" , "8") ,corner_radius=6 ,text="8", font = font_text , width = 90   , height= 40 , fg_color = "#6898a8" ,border_color="#000000"  )
button_8.place(x=105, y=270)
# # /////////////////////////////
button_7 = customtkinter.CTkButton(app,command = lambda:write("7" , "7") ,corner_radius=6 ,text="7", font = font_text , width =90   , height= 40 , fg_color = "#6898a8" ,border_color="#000000")
button_7.place(x=10, y=270)

# /////////////////////////////////////////////////////////////////////////////////////////////////////////////


btn_plus = customtkinter.CTkButton(app , width=90 , height=40 , fg_color =  "#265073")
btn_plus.configure(text="+" ,command = lambda:write("+" , "+") , font= font_text ,corner_radius=6  , border_width=0 , border_color="#000000", border_spacing=0, anchor="center")
btn_plus.place(x=295 , y=330)
# # /////////////////////////////
button_6 = customtkinter.CTkButton(app,command =  lambda:write("6" , "6") ,corner_radius=6 ,text="6", font = font_text , width = 90   , height= 40 , fg_color = "#6898a8" ,border_color="#000000"  )
button_6.place(x=200, y=330)
# # /////////////////////////////
button_5 = customtkinter.CTkButton(app,command =  lambda:write("5" , "5") ,corner_radius=6 ,text="5", font = font_text , width = 90   , height= 40 , fg_color = "#6898a8" ,border_color="#000000"  )
button_5.place(x=105, y=330)
# # /////////////////////////////
button_4 = customtkinter.CTkButton(app,command = lambda:write("4" , "4") ,corner_radius=6 ,text="4", font = font_text , width =90   , height= 40 , fg_color = "#6898a8",border_color="#000000")
button_4.place(x=10, y=330)

# /////////////////////////////////////////////////////////////////////////////////////////////////////////////
btn3 = customtkinter.CTkButton(app , width=90 , height=40 , fg_color = "#265073")
btn3.configure(text="**" ,command =  lambda:write("**" , "**"), font= font_text ,corner_radius=6  , border_width=0 , border_color="#000000", border_spacing=0, anchor="center")
btn3.place(x=295 , y=390)


button_3 = customtkinter.CTkButton(app,command = lambda:write("3" , "3") ,corner_radius=6 ,text="3", font = font_text , width = 90   , height= 40 , fg_color = "#6898a8" ,border_color="#000000"  )
button_3.place(x=200, y=390)
# # /////////////////////////////
button_2 = customtkinter.CTkButton(app,command = lambda:write("2" , "2") ,corner_radius=6 ,text="2", font = font_text , width = 90   , height= 40 , fg_color = "#6898a8" ,border_color="#000000"  )
button_2.place(x=105, y=390)
# # /////////////////////////////
button_1 = customtkinter.CTkButton(app,command = lambda:write("1" , "1") ,corner_radius=6 ,text="1", font = font_text , width =90   , height= 40 , fg_color ="#6898a8"  ,border_color="#000000")
button_1.place(x=10, y=390)

# /////////////////////////////////////////////////////////////////////////////////////////////////////////////
btn1 = customtkinter.CTkButton(app , width=90 , height=40 , fg_color ="#365486" ,command = calcuator)
btn1.configure(text="=" , font= font_text,corner_radius=6  , border_width=0 , border_color="#000000", border_spacing=0, anchor="center")
btn1.place(x=295 , y=450)
# # /////////////////////////////

button = customtkinter.CTkButton(app,command =  lambda:write("." , ".") ,corner_radius=6 ,text=".", font = font_text , width = 90   , height= 40 , fg_color =  "#6898a8",border_color="#000000"  )
button.place(x=200, y=450)
# # /////////////////////////////
button0 = customtkinter.CTkButton(app,command =  lambda:write("0" , "0"),corner_radius=6 ,text="0", font = font_text , width =182   , height= 40 , fg_color = "#6898a8"  ,border_color="#000000")
button0.place(x=10, y=450)

# //////////////////////////////////////////


app.mainloop()