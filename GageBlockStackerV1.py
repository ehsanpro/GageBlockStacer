import streamlit as st


# gage blcoks
gbs = [0.000, 0.050, 0.100, 0.200, 0.250, 0.300, 0.350, 0.400, 0.450, 0.500, 0.550, 0.600, 0.650, 0.700, 0.750, 0.800, 0.850, 0.900, 0.950, 1.000, 2.000, 3.000, 4.000, 0.101, 0.102, 0.103, 0.104, 0.105, 0.106, 0.107, 0.108, 0.109, 0.110, 0.111, 0.112, 0.113, 0.114, 0.115, 0.116, 0.117, 0.118, 0.119, 0.120, 0.121, 0.122, 0.123, 0.124, 0.125, 0.126, 0.127, 0.128, 0.129, 0.130, 0.131, 0.132, 0.133, 0.134, 0.135, 0.136, 0.137, 0.138, 0.139, 0.140, 0.141, 0.142, 0.143, 0.144, 0.145, 0.146, 0.147, 0.148, 0.149, 0.150, 0.1001, 0.1002, 0.1003, 0.1004, 0.1005, 0.1006, 0.1007, 0.1008, 0.1009]
gbs.sort(reverse=True)

results = []

with st.echo(code_location='below'):
    target = st.slider("Target (inch)", 0.25, 0, 4)


    # target = 0.2501 #inches
    target = round(target, 4) #inches
    print(target)
    
    
    
    print("START")
    for gb1 in gbs: 
        for gb2 in gbs:
            for gb3 in gbs:
                for gb4 in gbs:
                    if target == gb1 + gb2 + gb3 + gb4:
                        lst = [gb1, gb2, gb3, gb4]
                        nonzero_lst = [x for x in lst if x != 0]
                        if len(nonzero_lst) == len(set(nonzero_lst)):
                            print(lst)
                            results.append(lst)
    print("END")
    st.tables(results)
