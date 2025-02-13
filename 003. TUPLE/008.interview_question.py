QUE.1  since tuple is immutable, means u cannot add another element in already existing tuple,then
how u were able to add element in below code ???

t=(10,20,30,40)
t = t + (99,)
print(t)

o/p:
(10, 20, 30, 40, 99)

ANS.1 
the first tuple object named "t" is diffrent from the tuple "t" that was created after addition!!
see below code

t=(10,20,30,40)
print(id(t))            # 140207867563360
t = t + (99,)
print(id(t))            #  140207064605984
print(t)

u can see above that id of both "t" are diffrent, therfore they are two different object !!

__________________________________________________________________________________________________________________

QUE.2  since tuple is immutable, means u cannot INSERT another element in already existing tuple,then
how u were able to INSERT element in below code ???

t=(10,20,30,40)
t = t[:2] + (7, ) + t[2:]
print(t)

o/p:
(10, 20, 7, 30, 40)

ANS.1 
the first tuple object named "t" is diffrent from the tuple "t" that was created after INSERTION!!
see below code

t=(10,20,30,40)
print(id(t))                       #  140206749970528
t = t[:2] + (7, ) + t[2:]
print(id(t))                       #  140206749811072
print(t)

u can see above that id of both "t" are diffrent, therfore they are two different object !!
___________________________________________________________________________________________________________

que.3.

t=(5,(5,8,7),[2,7,6],"hello")
t[1]=34
print(t)

o/p: ERROR BECAUSE TUPLE IS IMMUTABLE

BUT WHEN I RUN THE BELOW CODE:-

t=(5,(5,8,7),[2,7,6],"hello")
t[2][1]=34
print(t)

o/p:
(5, (5, 8, 7), [2, 34, 6], 'hello')

in above code i was able to edit it , how??


ans.3.

beacuse in first code u were editing tuple elemnt and since tuple is immutable therefore u got error.
but in second code, notice that u are editing list's elemnt, and since is mutable therfore u got the output!!!



