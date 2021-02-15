# -*- coding: utf-8 -*-

# 需要记录出每一个基因型的占比
# 输入繁殖代数
# 突变机制
# 环境参数：某种表现型有利于生存
import random

class Conf:
    p_Aa = 0.0
    p_AA = 1.0
    p_aa = 0.0
    descend_gens = 50
    first_gen_counts = 100
    phenotype = "A"
    growth_rate = 2
    decay_p_positive = 0.1
    decay_p_negative = 0.9
    transgenation_rate = 0.01

    def check(self):
        sum_p_of_genes = self.p_Aa + self.p_AA + self.p_aa
        if not (sum_p_of_genes == 1 and self.decay_p_positive <= 1 and self.decay_p_negative <= 1):
            print ("proportion error!")
            return False
        else:
            return True

def generate_first_gen(conf):
    first_gen = list()
    for i in range(conf.first_gen_counts):
        seed = random.random()
        if seed < conf.p_Aa:
            first_gen.append("Aa")
        elif seed < conf.p_Aa + conf.p_AA:
            first_gen.append("AA")
        else:
            first_gen.append("aa")
    return first_gen

def decay(conf, cur_gen):
    for i, gene in enumerate(cur_gen):
        seed = random.random()
        if conf.phenotype == "A":
            if "A" in gene and seed < conf.decay_p_positive:
                cur_gen.pop(i)
            elif seed < conf.decay_p_negative:
                cur_gen.pop(i)
        elif conf.phenotype == "a":
            if gene == "aa" and seed < conf.decay_p_negative:
                cur_gen.pop(i)
            elif seed < conf.decay_p_positive:
                cur_gen.pop(i)
    return cur_gen

def copulation(conf, cur_gen):
    next_gen_count = len(cur_gen) * conf.growth_rate
    next_gen = list()
    for i in range(next_gen_count):
        parent_1 = random.choice(random.choice(cur_gen))
        parent_2 = random.choice(random.choice(cur_gen))
        child_gene = parent_1 + parent_2
        next_gen.append(child_gene)
    return next_gen

def transgenation_rate(conf, cur_gen):
    for i, gene in enumerate(cur_gen):
        for j, g in enumerate(gene):
            seed = random.random()
            if seed < conf.transgenation_rate:
                cur_gen[i] = list(cur_gen[i])
                if g == "a":
                    cur_gen[i][j] = 'A'
                elif g == "A":
                    cur_gen[i][j] = 'a'
                cur_gen[i] = "".join(cur_gen[i])
    return cur_gen

def descend_one_gen(conf, cur_gen):
    
    cur_gen = decay(conf, cur_gen)
    cur_gen = transgenation_rate(conf, cur_gen)
    cur_gen = copulation(conf, cur_gen)
    
    return cur_gen

def culculate_type(cur_gen):
    Aa = AA = aa = 0
    for gene in cur_gen:
        if gene == "AA":
            AA += 1
        elif gene == "aa":
            aa += 1
        else:
            Aa += 1
    total_count = float(len(cur_gen))
    print("ratio: AA:{}, Aa:{}, aa:{};").format(AA / total_count, Aa / total_count, aa / total_count)


def descend(conf):
    cur_gen = generate_first_gen(conf)
    for i in range(conf.descend_gens):
        cur_gen = descend_one_gen(conf, cur_gen)
        culculate_type(cur_gen)

if __name__ == "__main__":
    conf = Conf()
    if conf.check():
        descend(conf)