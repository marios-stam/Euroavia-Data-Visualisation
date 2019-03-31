file = open("test.txt", "r")
content=file.read()
split=content.split('==========================================')


class Log:
    def __init__(self, time,temp,height,orientation,acceleration):
        self.time = time
        self.temp = temp
        self.height=height
        self.orientation=orientation
        self.acceleration=acceleration
measurements=[]
for i in split:
    print(i)
    measurements.append(i.split('\n'))

measurements.pop(0)

Logs=[]
for i in range(len(measurements)):
    measurements[i].pop(0)
    x=measurements[i]
    Logs.append(Log(x[0],x[1],x[2],x[3].split(' '),x[4].split(' ')) )


        	
