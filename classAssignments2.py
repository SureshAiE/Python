class multiAssignments():
    def subfields():
        print("Sub-fields in AI are:")
        print("Machine Learning")
        print("Neural Networks")
        print("Vision")
        print("Robotics")
        print("Speech Processing")
        print("Natural Language Processing")
        return

    def OddEven():
        num=int(input("Enter a Number"))
        if(num%2==1):
            print(num, "is Odd Number")
            OddEven="is Odd Number"
        else:
            print(num, "is Even Number")
            OddEven="is Even Number"
            return OddEven

    def Elegible():
        gender=input("Your Gender:")
        age=int(input("Your Age:"))
        if(age>20):
            print("ELIGIBLE")
            Message="ELIGIBLE"
        else:
            print("NOT ELIGIBLE")
            Message="NOT ELIGIBLE"
            return Message
            

    def Elegible():
        gender=input("Your Gender:")
        age=int(input("Your Age:"))
        if(age>17):
            print("ELIGIBLE")
            Message="ELIGIBLE"
        else:
            print("NOT ELIGIBLE")
            Message="NOT ELIGIBLE"
            return Message

    def percentage():
        subject1=int(input("Subject1="))
        subject2=int(input("Subject2="))
        subject3=int(input("Subject3="))
        subject4=int(input("Subject4="))
        subject5=int(input("Subject5="))
        subjects=(subject1,subject2,subject3,subject4,subject5)
        t=(subject1+subject2+subject3+subject4+subject5)
        print("Total : ",t)
        p=(t/5)
        print("Percentage : ",p)
        TOP="Percentage Value"
        return TOP

    def triangle():
        height=int(input("Height :"))
        breadth=int(input("Breadth :"))
        print("Area formula:Height*Breadth/2")
        aot=(height*breadth/2)
        print("Area of Traiangle:",aot)
        msg="Area of Triangle"
        height1=int(input("Height1:"))
        height2=int(input("Height2:"))
        breadth=int(input("Breadth:"))
        print("Perimeter forumula: Height1+Height2+Breadth")
        pot=(height1+height2+breadth)
        print("Perimeter of Triangle:",pot)
        msg="Perimeter of Triangle"
        return msg

    def BMI():
        weight=int(input("Enter your weight"))
        if(weight<18.5):
            print("Under Weight")
        elif(weight<24.9):
            print("Healthy Weight")
        elif(weight<29.9):
            print("Over Weight")
        else:
            print("Very Over Weight")
            return 

    def ageCategory():
        if age<18:
            print("Children")
            category="Children"
        elif age<35:
            print("Adult")
            category="Adult"
        elif age<59:
            print("Citizen")
            category="Citizen"
        elif age>59:
            print("Senior Citizen")
            category="Senior Citizen"
        return category

    
    def ageCategoryNoR():
        if age<18:
            print("Children")
            category="Children"
        elif age<35:
            print("Adult")
            category="Adult"
        elif age<59:
            print("Citizen")
            category="Citizen"
        elif age>59:
            print("Senior Citizen")
            category="Senior Citizen"
        return category