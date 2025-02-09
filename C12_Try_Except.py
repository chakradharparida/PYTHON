def main():
    try:
        a=int(input("Enter a number :"))
    except Exception as e:
        print("Print a valid number !")
        print(e)
    else:
        print(a)
    finally:
        print("Thank You !")
    #print("Thank You !")
main()