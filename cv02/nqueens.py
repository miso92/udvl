import os

class NQueens:
    def q(self, r, s):
        return r * self.n + s + 1
    
    def zapis_problem(self, subor):
        for r in range(self.n):
            for i in range(self.n):
                subor.write("{} ".format(self.q(r,i)))
            subor.write("0 \n")
            
        for r in range(self.n):
            for i in range(self.n):
                for j in range(i+1, self.n):
                    subor.write("{} {} 0\n".format(-(self.q(r,i)), -(self.q(r, j))))

        for j in range(1, self.n + 1):
            for i in range(0, self.n):
                q_i_j = j + self.n * i;
                for l in range(1, self.n - i):
                    vystup = "-" + str(q_i_j) + " -" + str(q_i_j + self.n * l)+" 0\n";
                    subor.write(vystup);

        for i in range(0, self.n - 1):
            for j in range(i, self.n - 1):
                q_i_j = j + 1 + self.n * i;
                for l in range(1,self.n-j):
                    vystup = "-" + str(q_i_j) + " -" + str(q_i_j + l *(self.n + 1)) + " 0\n";
                    subor.write(vystup); 

        for i in range(0, self.n - 1):
            for j in range(0, i):
                q_i_j = j + 1 + self.n * i;
                for l in range(1, self.n - i):
                    vystup = "-" + str(q_i_j) + " -" + str(q_i_j + l *(self.n + 1)) + " 0\n";
                    subor.write(vystup); 

        for i in range(0, self.n):
            for j in range(0,self.n - i):
                q_i_j = j + 1 + self.n *i;
                for l in range(1, j + 1):
                    vystup = "-" + str(q_i_j) + " -" + str(q_i_j + l * (self.n - 1)) + " 0\n";
                    subor.write(vystup); 

        for i in range(0, self.n):
            for j in range(self.n-i, self.n):
                q_i_j = j + 1 + self.n * i;
                if (q_i_j != self.n * self.n):
                    for l in range(1, self.n - i):
                        vystup = "-" + str(q_i_j) + " -" + str(q_i_j + l * (self.n - 1)) + " 0\n";
                        subor.write(vystup); 
    
    def dekoduj_riesenie(self, ries):
        res = list()
        for i in [int(x) for x in ries.split()]:
            if i > 0:
                r = (i-1) // self.n
                s = (i-1) % self.n
                res.append((r,s))
        return res
    
    def solve(self, n):
        cesta_k_minisat = "minisat.exe"
        self.n = n
        with open('vstup.txt', 'w') as o:
            #zapisanie problem
            self.zapis_problem(o)
        os.system("{} vstup.txt vystup.txt".format(cesta_k_minisat))

        with open("vystup.txt", "r") as f:
            sat = f.readline()
            if sat == "SAT\n":
                print("Riesenie:")
                ries = f.readline()
                return self.dekoduj_riesenie(ries)
            else:
                print("Ziadne riesenie")
                return []
