st=[2,"cat",7,2,9,"cat",7,42]

def f(my_string):
    st0=[]
    for i in range(0,len(my_string)-1):
        if st.count(my_string[i])>1 and st0.count(my_string[i])==0:
            st0.append(my_string[i])
        elif st.count(my_string[i])==1:
            st0.append(my_string[i])
        else:
            pass
    return print(st0)

f(st)