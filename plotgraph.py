def plotgraph():
    import matplotlib.pyplot as plt
    b=int(input("Enter the number of days over: "))
    c=int(input("Enter the total number of days required to achieve target weight: "))
    d=int(input("Enter your starting weight: "))
    e=int(input("Enter your current weight: "))
    f=int(input("Enter your target weight: "))
    g=int(input("Enter your starting fat percentage: "))
    h=int(input("Enter your current fat percentage: "))
    i=int(input("Enter your target fat percentage: "))
    x1 = [0,b,c]
    y1 = [d,e,f]
    x2=[0,b,c]
    y2=[g,h,i]
    plt.plot(x1, y1, label = "Weight Progress")
    plt.plot(x2, y2, label = "Fat percentage")
    plt.xlabel('Days')
    plt.ylabel('Weight')
    plt.title('PROGRESS TRACKER')
    plt.legend()
    plt.show()
plotgraph()
