class Solution(object):
    def evalRPN(self, tokens):
        """
        :type tokens: List[str]
        :rtype: int
        """
        st = []
        # consider error -> starting with an operator
        for t in tokens:
            if len(t) > 1 or t.isdigit():
                st.append(int(t))
            else:
                if t =="+":
                    st[-2]+=st[-1]
                elif t== "-":
                    st[-2]-=st[-1]
                elif t =="*":
                    st[-2]*=st[-1]
                else:
                    st[-2]= int(float(st[-2])/st[-1])
                st.pop()
        return st[0]

