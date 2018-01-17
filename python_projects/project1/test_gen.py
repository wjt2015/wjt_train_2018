##
def odd():
    n=1;
    while True:
        yield n;
        n += 2;


add_num=odd();
count=0;
for a  in add_num:
    ##if count >= 5:break;
    print("a=%d" %a);
    count += 1;
####

