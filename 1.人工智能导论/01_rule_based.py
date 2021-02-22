import random
# 用于便捷打印调试的库
from icecream import ic

rules = """
复合句子 = 句子 , 连词 句子
连词 = 而且 | 但是 | 不过
句子 = 主语 谓语 宾语
主语 = 你| 我 | 他 
谓语 = 吃| 玩 
宾语 = 桃子| 皮球
"""


# 处理规则
def get_grammar_by_description(description):
    # 将规则拆分成target和expend
    rules_pattern = [r.split('=') for r in description.split('\n') if r.strip()]
    # 将expend继续拆分
    target_with_expend = [(t, ex.split('|')) for t, ex in rules_pattern]
    # 将target和expend对应
    grammar = {t.strip(): [e.strip() for e in ex] for t, ex in target_with_expend}

    return grammar


def generate_by_grammar(grammar, target='句子'):
    if target not in grammar:
        return target
    # 不断分解expend作为新的target，组成完整的句子
    return ''.join([generate_by_grammar(grammar, t) for t in random.choice(grammar[target]).split()])


if __name__ == '__main__':
    grammar = get_grammar_by_description(rules)

    # 生成测试代码
    generated = [t for t in random.choice(grammar['句子']).split()]
    test_v = [t for t in random.choice(grammar['谓语']).split()]
    ic(generated)
    ic(test_v)
    ic(generate_by_grammar(grammar))
    ic(generate_by_grammar(grammar, target='复合句子'))
